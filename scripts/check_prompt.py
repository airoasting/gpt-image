#!/usr/bin/env python3
"""Validate gpt-image seven-block prompts.

Usage:
    python3 scripts/check_prompt.py <file> [<file> ...]
    echo "...prompt..." | python3 scripts/check_prompt.py
    python3 scripts/check_prompt.py --strict-warnings <file>
    python3 scripts/check_prompt.py --test

Output:
    JSON. A single input returns one result object. Multiple files return
    {"ok": bool, "results": [...]}.

Exit codes:
    0  no errors
    1  validation errors, or warnings with --strict-warnings
    2  input/output or usage failure

Rule sources:
    SKILL.md
    references/gpt-image-prompt-craft.md
    references/gpt-image-variation-recipes.md
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


VERSION = "2.0.0"

KR_BLOCKS = [
    "결과물 유형",
    "주 피사체",
    "구도와 비율",
    "맥락과 배경",
    "스타일과 매체",
    "빛과 디테일",
    "정확성 조건",
]

EN_BLOCKS = [
    "Output type",
    "Main subject",
    "Composition and ratio",
    "Context and background",
    "Style and medium",
    "Light and detail",
    "Accuracy conditions",
]

VAGUE_TERMS = [
    "예쁘게",
    "예쁜",
    "고급스럽게",
    "감성적으로",
    "감성적인",
    "멋지게",
    "멋진",
    "세련되게",
    "세련된",
    "분위기 있게",
    "beautiful",
    "stunning",
    "gorgeous",
    "premium",
    "modern",
    "clean",
]

VAGUE_ALLOWED_CONTEXT = {
    "premium": ["premium product photography", "premium commercial", "premium toy photography"],
    "modern": ["modern sans-serif", "modern sans serif"],
    "clean": ["clean typography", "clean spacing", "clean white background", "clean layout"],
}

DEAD_QUALITY_TOKENS = [
    "8k",
    "4k",
    "uhd",
    "masterpiece",
    "best quality",
    "ultra-detailed",
    "ultra detailed",
    "highly detailed",
    "sharp focus",
    "trending on artstation",
]

STAGE_DIRECTIONS = [
    "어워드 수준",
    "전문가처럼",
    "최고급으로",
    "award-winning",
    "professional grade",
]

CANON_AR = {"3:4", "16:9", "1:1", "9:16", "21:9"}
AR_PATTERN = re.compile(r"\b(\d{1,2}:\d{1,2})\b")
SIZE_PATTERN = re.compile(r"\b(\d{3,4})x(\d{3,4})\b")

SIZE_TO_AR = {
    "1024x1024": "1:1",
    "1536x2048": "3:4",
    "1920x1080": "16:9",
    "1080x1920": "9:16",
    "2520x1080": "21:9",
}

ALLOWED_LATIN_TERMS = {
    "arabica",
    "bokeh",
    "close",
    "crisp",
    "editorial",
    "film",
    "grain",
    "hex",
    "kelvin",
    "light",
    "rim",
    "sans",
    "serif",
    "smooth",
    "vector",
    "wide",
}

TEXT_GUARD_PATTERN = re.compile(
    r"(또렷|가독|한 번씩|선명|crisp|legible|readable|no garbled|no duplicate)",
    re.IGNORECASE,
)

NEGATIVE_LABEL_PATTERN = re.compile(r"(?mi)^\s*(negative|avoid|do not include|exclude)\s*:")
AVOID_SENTENCE_PATTERN = re.compile(r"(?i)\bavoid\b\s+[a-z]")
KO_NEG_PATTERN = re.compile(r"([^\s\"]{0,12}\s*(?:없이|피하기|피합니다|피해주세요|금지))")


@dataclass(frozen=True)
class Issue:
    code: str
    msg: str
    line: int | None = None
    column: int | None = None

    def to_json(self) -> dict:
        data = {"code": self.code, "msg": self.msg}
        if self.line is not None:
            data["line"] = self.line
        if self.column is not None:
            data["column"] = self.column
        return data


def line_col(text: str, index: int) -> tuple[int, int]:
    line = text.count("\n", 0, index) + 1
    line_start = text.rfind("\n", 0, index) + 1
    return line, index - line_start + 1


def issue(code: str, msg: str, text: str | None = None, index: int | None = None) -> Issue:
    if text is not None and index is not None:
        line, col = line_col(text, index)
        return Issue(code, msg, line, col)
    return Issue(code, msg)


def find_block_positions(text: str, blocks: list[str]) -> list[tuple[str, int]]:
    positions: list[tuple[str, int]] = []
    for block in blocks:
        pattern = re.compile(rf"(?m)^\s*{re.escape(block)}\s*:")
        matches = list(pattern.finditer(text))
        for match in matches:
            positions.append((block, match.start()))
    return positions


def choose_block_schema(text: str) -> tuple[str, list[str], list[tuple[str, int]]]:
    kr_positions = find_block_positions(text, KR_BLOCKS)
    en_positions = find_block_positions(text, EN_BLOCKS)
    if len(en_positions) > len(kr_positions):
        return "en", EN_BLOCKS, en_positions
    return "ko", KR_BLOCKS, kr_positions


def quoted_strings(text: str) -> list[str]:
    """Return double-quoted strings likely intended as rendered text."""
    strings: list[str] = []
    for match in re.finditer(r'"([^"\n]{2,})"', text):
        value = match.group(1).strip()
        if re.fullmatch(r"#[0-9A-Fa-f]{6}", value):
            continue
        if value.endswith(".md") or "/" in value and "." in value:
            continue
        strings.append(value)
    return strings


def term_allowed(term: str, lower_text: str) -> bool:
    allowed_contexts = VAGUE_ALLOWED_CONTEXT.get(term.lower(), [])
    return any(context in lower_text for context in allowed_contexts)


def normalize_messages(items: Iterable[Issue]) -> list[dict]:
    return [item.to_json() for item in items]


def check_blocks(text: str) -> tuple[str, list[Issue], list[Issue]]:
    errors: list[Issue] = []
    warnings: list[Issue] = []
    mode, blocks, positions = choose_block_schema(text)

    seen = {}
    for block, pos in positions:
        seen.setdefault(block, []).append(pos)

    for block in blocks:
        if block not in seen:
            errors.append(issue("E-BLOCK-MISSING", f"Missing block: '{block}:'"))
        elif len(seen[block]) > 1:
            errors.append(issue("E-BLOCK-DUPLICATE", f"Duplicate block: '{block}:'", text, seen[block][1]))

    if all(block in seen for block in blocks):
        first_positions = [(block, seen[block][0]) for block in blocks]
        order = [block for block, _ in sorted(first_positions, key=lambda item: item[1])]
        if order != blocks:
            errors.append(
                issue(
                    "E-BLOCK-ORDER",
                    "Block order differs from the canonical sequence: " + " > ".join(order),
                )
            )

        sorted_positions = sorted(first_positions, key=lambda item: item[1])
        for idx, (block, pos) in enumerate(sorted_positions):
            block_start = text.find(":", pos) + 1
            block_end = sorted_positions[idx + 1][1] if idx + 1 < len(sorted_positions) else len(text)
            body = text[block_start:block_end].strip()
            if len(body) < 12:
                warnings.append(issue("W-BLOCK-THIN", f"Block is very thin: '{block}:'", text, pos))

    return mode, errors, warnings


def check(text: str, source: str | None = None) -> dict:
    errors: list[Issue] = []
    warnings: list[Issue] = []
    lower_text = text.lower()

    mode, block_errors, block_warnings = check_blocks(text)
    errors.extend(block_errors)
    warnings.extend(block_warnings)

    for term in VAGUE_TERMS:
        pattern = re.compile(rf"(?<![A-Za-z0-9가-힣]){re.escape(term)}(?![A-Za-z0-9가-힣])", re.IGNORECASE)
        for match in pattern.finditer(text):
            if term_allowed(term, lower_text):
                continue
            errors.append(
                issue(
                    "E-VAGUE",
                    f"Vague descriptor '{term}'. Replace it with objects, layout, material, lighting, or numbers.",
                    text,
                    match.start(),
                )
            )

    for term in STAGE_DIRECTIONS:
        pattern = re.compile(rf"(?<![A-Za-z0-9가-힣]){re.escape(term)}(?![A-Za-z0-9가-힣])", re.IGNORECASE)
        for match in pattern.finditer(text):
            warnings.append(
                issue(
                    "W-STAGE",
                    f"External taste cue '{term}'. Replace with concrete visual criteria.",
                    text,
                    match.start(),
                )
            )

    ars = AR_PATTERN.findall(text)
    if not ars:
        errors.append(issue("E-AR-MISSING", "Missing aspect-ratio token such as 3:4, 16:9, 1:1, 9:16, or 21:9."))
    else:
        noncanonical = sorted({ar for ar in ars if ar not in CANON_AR})
        if noncanonical:
            warnings.append(
                issue(
                    "W-AR-NONCANON",
                    f"Non-canonical aspect ratio {noncanonical}. Recommended set: 3:4, 16:9, 1:1, 9:16, 21:9.",
                )
            )

    sizes = [f"{width}x{height}" for width, height in SIZE_PATTERN.findall(text)]
    for size in sizes:
        expected_ar = SIZE_TO_AR.get(size)
        if expected_ar and ars and expected_ar not in ars:
            warnings.append(
                issue(
                    "W-SIZE-AR-MISMATCH",
                    f"Size {size} usually maps to {expected_ar}, but that ratio is not stated.",
                )
            )

    for term in DEAD_QUALITY_TOKENS:
        pattern = re.compile(rf"(?<![a-z0-9]){re.escape(term)}(?![a-z0-9])", re.IGNORECASE)
        for match in pattern.finditer(text):
            errors.append(
                issue(
                    "E-DEAD-WORD",
                    f"Dead quality token '{term}'. Replace it with concrete visual instructions.",
                    text,
                    match.start(),
                )
            )

    label_match = NEGATIVE_LABEL_PATTERN.search(text)
    if label_match:
        errors.append(
            issue(
                "E-NEG-LABEL",
                "Negative/Avoid/Exclude label detected. Restate the desired visible state positively.",
                text,
                label_match.start(),
            )
        )
    for match in AVOID_SENTENCE_PATTERN.finditer(text):
        errors.append(
            issue(
                "E-NEG-AVOID",
                "Avoid-sentence detected. Restate the desired visible state positively.",
                text,
                match.start(),
            )
        )

    ko_negative = KO_NEG_PATTERN.findall(text)
    if ko_negative:
        warnings.append(
            issue(
                "W-NEG-KO",
                f"Korean exclusion phrasing detected {len(ko_negative)} time(s). Positive restatement is recommended.",
            )
        )

    body_without_quotes = re.sub(r'"[^"]*"', "", text)
    hangul_count = len(re.findall(r"[가-힣]", body_without_quotes))
    latin_words = [
        word
        for word in re.findall(r"[A-Za-z]{4,}", body_without_quotes)
        if word.lower() not in ALLOWED_LATIN_TERMS
    ]
    if hangul_count > 30 and len(latin_words) > 12:
        warnings.append(
            issue(
                "W-LANG-MIX",
                f"Possible mixed prompt language: {hangul_count} Korean chars plus {len(latin_words)} Latin words. Prefer one prompt language.",
            )
        )

    rendered_text = quoted_strings(text)
    if rendered_text and not TEXT_GUARD_PATTERN.search(text):
        warnings.append(
            issue(
                "W-TEXT-GUARD",
                f"{len(rendered_text)} quoted text string(s) found, but no readability guard. Add a short crisp/legible text guard.",
            )
        )

    result = {
        "ok": not errors,
        "version": VERSION,
        "source": source or "<stdin>",
        "block_language": mode,
        "errors": normalize_messages(errors),
        "warnings": normalize_messages(warnings),
    }
    return result


GOOD_KO = """결과물 유형:
브랜드 출시용 3:4 세로형 제품 포스터. 주제는 "봄맞이 텀블러".

주 피사체:
선샤인 옐로우 세라믹 텀블러를 화면 중앙에 크게 배치한다.

구도와 비율:
3:4 세로형. 제품은 중앙, 상단에는 제목 영역, 하단에는 짧은 제품 설명 영역을 둔다.

맥락과 배경:
일요일 아침 주방 창가, 흰 타일, 연한 나무 선반, 작은 봄꽃이 제품 사용 맥락을 만든다.

스타일과 매체:
무광 세라믹 질감의 제품 렌더. 팔레트는 #F2B84B / #1B2566 / #FAF1E2.

빛과 디테일:
부드러운 스튜디오 조명과 낮은 3/4 시점. 컵의 림, 손잡이, 세라믹 입자, 받침 그림자를 선명하게 표현한다.

정확성 조건:
제목 "Morning Solar"는 각 글자 한 번씩 또렷하게. 표면은 공급된 문구 외에 매끈하게 유지한다."""

GOOD_EN = """Output type:
3:4 vertical product launch poster for a ceramic tumbler with exact headline text "Morning Solar".

Main subject:
A sunshine-yellow ceramic tumbler centered as the hero product, with a small spring flower stem as scale context.

Composition and ratio:
3:4 vertical layout. Product centered, headline at the top, short product note at the bottom, generous margins.

Context and background:
Sunday morning kitchen window, white tile, pale wood shelf, folded linen, and a quiet breakfast setting.

Style and medium:
Commercial product render with matte ceramic material, controlled reflections, and a restrained editorial layout.

Light and detail:
Soft studio side light, low three-quarter camera view, visible rim thickness, handle curve, ceramic grain, and contact shadow.

Accuracy conditions:
Render "Morning Solar" once, crisp and legible, with no garbled characters or duplicate letters."""

BAD = """결과물 유형:
멋진 카페 느낌의 포스터, 8K UHD, masterpiece.

주 피사체:
노란 텀블러.

구도와 비율:
적당히 예쁜 사진.

스타일과 매체:
고급스럽게.

맥락과 배경:
좋은 분위기.

빛과 디테일:
분위기 있게.

정확성 조건:
Negative: crowd, logo. 깨진 글자는 피하기."""


def selftest() -> int:
    good_ko = check(GOOD_KO, "GOOD_KO")
    good_en = check(GOOD_EN, "GOOD_EN")
    bad = check(BAD, "BAD")
    bad_codes = {item["code"] for item in bad["errors"]}
    expected = {"E-VAGUE", "E-DEAD-WORD", "E-NEG-LABEL", "E-BLOCK-ORDER"}
    payload = {
        "ok": good_ko["ok"] and good_en["ok"] and not bad["ok"] and expected <= bad_codes,
        "version": VERSION,
        "good_ko": good_ko,
        "good_en": good_en,
        "bad": bad,
        "missing_bad_codes": sorted(expected - bad_codes),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if payload["ok"] else 1


def read_inputs(paths: list[str]) -> tuple[list[tuple[str, str]], list[Issue]]:
    inputs: list[tuple[str, str]] = []
    errors: list[Issue] = []
    if not paths:
        inputs.append(("<stdin>", sys.stdin.read()))
        return inputs, errors

    for path_text in paths:
        path = Path(path_text)
        try:
            inputs.append((path_text, path.read_text(encoding="utf-8")))
        except OSError as exc:
            errors.append(Issue("E-IO", f"Cannot read file '{path_text}': {exc}"))
    return inputs, errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate gpt-image seven-block prompts.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("paths", nargs="*", help="Prompt files to validate. Reads stdin when omitted.")
    parser.add_argument("--strict-warnings", action="store_true", help="Exit 1 when warnings are present.")
    parser.add_argument("--test", action="store_true", help="Run built-in self tests.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.test:
        return selftest()

    inputs, io_errors = read_inputs(args.paths)
    if io_errors:
        print(
            json.dumps(
                {"ok": False, "version": VERSION, "errors": normalize_messages(io_errors), "warnings": []},
                ensure_ascii=False,
                indent=2,
            )
        )
        return 2

    results = [check(text, source) for source, text in inputs]
    if len(results) == 1:
        output = results[0]
    else:
        output = {
            "ok": all(result["ok"] for result in results),
            "version": VERSION,
            "results": results,
        }

    print(json.dumps(output, ensure_ascii=False, indent=2))

    has_errors = not output["ok"]
    has_warnings = any(result["warnings"] for result in results)
    if has_errors or (args.strict_warnings and has_warnings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
