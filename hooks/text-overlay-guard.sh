#!/usr/bin/env bash
# Block post-generation text overlays on image/video outputs.
#
# Rule:
#   Text that must appear in an image should be rendered by the image model from
#   the prompt. If the text is wrong, revise the prompt and regenerate. Do not
#   patch generated images by drawing text on top with Pillow, ImageMagick,
#   ffmpeg drawtext, SVG text, HTML canvas text, or similar tooling.
#
# Register:
#   PreToolUse hook, matcher "Bash".
#
# Self-test:
#   hooks/text-overlay-guard.sh --test

set -u

if [ "${1:-}" = "--test" ]; then
  hook_payload=""
else
  hook_payload="$(cat)"
fi
export BLOCK_TEXT_OVERLAY_HOOK_PAYLOAD="$hook_payload"

python3 - "$@" <<'PY'
import json
import os
import re
import sys
from typing import Optional, Tuple

VERSION = "2.0.0"

DENY_REASON = (
    "Text must be rendered inside the image from the prompt. "
    "Post-generation text overlays are blocked. Revise the prompt, reduce copy, "
    "increase canvas size if needed, and regenerate. See SKILL.md and "
    "references/gpt-image-prompt-craft.md."
)

SIGNATURES = [
    ("pillow-imagedraw", re.compile(r"\bImageDraw\b|\bImageFont\b|\.textbbox\s*\(|\.textlength\s*\(|\.text\s*\(")),
    ("ffmpeg-drawtext", re.compile(r"(?i)(?:-vf|-filter_complex)\s+[^'\"]*drawtext\s*=|drawtext\s*=")),
    ("imagemagick-annotate", re.compile(r"(?i)\b(?:convert|magick|mogrify)\b.*\s-annotate\b")),
    ("imagemagick-label", re.compile(r"(?i)\b(?:convert|magick|mogrify)\b.*\b(?:label:|caption:|pango:)")),
    ("imagemagick-draw-text", re.compile(r"(?i)\b(?:convert|magick|mogrify)\b.*\s-draw\s+['\"]?text\b")),
    ("svg-text", re.compile(r"(?is)<text\b|<tspan\b")),
    ("canvas-filltext", re.compile(r"\b(?:fillText|strokeText)\s*\(")),
    ("canvas-font", re.compile(r"\bctx\.font\s*=|\bcontext\.font\s*=")),
    ("css-text-overlay", re.compile(r"(?is)<[^>]+style\s*=\s*['\"][^'\"]*position\s*:\s*absolute[^'\"]*(?:font-size|font-family)|<[^>]+style\s*=\s*['\"][^'\"]*(?:font-size|font-family)[^'\"]*position\s*:\s*absolute")),
]

ALLOW_PATTERNS = [
    re.compile(r"\bscripts/check_prompt\.py\b"),
    re.compile(r"\breferences/gpt-image-prompt-craft\.md\b"),
    re.compile(r"\breferences/gpt-image-variation-recipes\.md\b"),
    re.compile(r"\bgrep\b.*(?:ImageDraw|drawtext|fillText|<text)"),
    re.compile(r"\brg\b.*(?:ImageDraw|drawtext|fillText|<text)"),
]


def hook_response(deny: bool, reason: Optional[str] = None) -> str:
    if not deny:
        return ""
    payload = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason or DENY_REASON,
        }
    }
    return json.dumps(payload, ensure_ascii=False, separators=(",", ":"))


def extract_command(payload: str) -> str:
    """Extract a likely shell command from Codex/Claude hook JSON.

    Falls back to scanning the full payload so the hook still works if the
    wrapper schema changes.
    """
    try:
        data = json.loads(payload)
    except json.JSONDecodeError:
        return payload

    candidates = []

    def walk(value):
        if isinstance(value, dict):
            for key, item in value.items():
                lowered = str(key).lower()
                if lowered in {"command", "cmd", "script", "input"} and isinstance(item, str):
                    candidates.append(item)
                walk(item)
        elif isinstance(value, list):
            for item in value:
                walk(item)

    walk(data)
    if candidates:
        return "\n".join(candidates)
    return payload


def is_allowed_context(command: str) -> bool:
    return any(pattern.search(command) for pattern in ALLOW_PATTERNS)


def detect_overlay(command: str) -> Tuple[bool, Optional[str]]:
    if is_allowed_context(command):
        return False, None
    for name, pattern in SIGNATURES:
        if pattern.search(command):
            return True, name
    return False, None


def run_tests() -> int:
    deny_cases = {
        "pillow": 'python -c "from PIL import Image, ImageDraw; d=ImageDraw.Draw(im); d.text((10,10), \\"SALE\\")"',
        "font": 'python -c "from PIL import ImageFont; ImageFont.truetype(\\"NotoSans.ttf\\", 40)"',
        "ffmpeg": "ffmpeg -i in.png -vf \"drawtext=text='50% OFF':x=10:y=10\" out.png",
        "imagemagick_annotate": 'magick in.png -annotate +10+10 "신제품" out.png',
        "imagemagick_label": 'convert label:"오늘의 행사" out.png',
        "imagemagick_draw": "convert in.png -draw \"text 10,10 'Hi'\" out.png",
        "svg_text": "python - <<'EOF'\nprint('<svg><text x=\"10\" y=\"10\">SALE</text></svg>')\nEOF",
        "canvas_text": "node -e \"ctx.font='40px sans-serif'; ctx.fillText('SALE', 10, 10)\"",
        "css_overlay": "cat <<'EOF'\n<div style=\"position:absolute; font-size:40px\">SALE</div>\nEOF",
    }
    allow_cases = {
        "validator": "python3 scripts/check_prompt.py draft.txt",
        "craft_ref": "cat references/gpt-image-prompt-craft.md",
        "variation_ref": "cat references/gpt-image-variation-recipes.md",
        "ffmpeg_scale": "ffmpeg -i a.mp4 -vf scale=1280:720 out.mp4",
        "imagemagick_resize": "convert in.png -resize 50% out.png",
        "search_signature": "rg 'drawtext|ImageDraw|fillText' hooks scripts",
        "plain_echo": "echo 'draw text as part of the prompt, not as overlay'",
    }

    failures = []
    for name, command in deny_cases.items():
        detected, signature = detect_overlay(command)
        if not detected:
            failures.append({"case": name, "expected": "deny", "actual": "allow"})
        elif not signature:
            failures.append({"case": name, "expected": "signature", "actual": None})

    for name, command in allow_cases.items():
        detected, signature = detect_overlay(command)
        if detected:
            failures.append({"case": name, "expected": "allow", "actual": f"deny:{signature}"})

    json_payload = json.dumps({"tool_input": {"command": deny_cases["ffmpeg"]}})
    detected, signature = detect_overlay(extract_command(json_payload))
    if not detected or signature != "ffmpeg-drawtext":
        failures.append({"case": "json_extract", "expected": "deny:ffmpeg-drawtext", "actual": signature})

    report = {
        "ok": not failures,
        "version": VERSION,
        "deny_cases": len(deny_cases),
        "allow_cases": len(allow_cases),
        "failures": failures,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not failures else 1


def main() -> int:
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        return run_tests()

    payload = os.environ.get("BLOCK_TEXT_OVERLAY_HOOK_PAYLOAD", "")
    command = extract_command(payload)
    detected, signature = detect_overlay(command)
    if detected:
        reason = f"{DENY_REASON} Detected overlay signature: {signature}."
        print(hook_response(True, reason))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
PY
