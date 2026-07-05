#!/usr/bin/env bash
# 이미지에 넣을 글자는 프롬프트로 이미지 안에서 렌더한다.
# 생성된 그림 위에 코드로 글자를 덧그리는 후처리는 폰트·톤이 원본과 겉돌아 막는다.
# PreToolUse(Bash) 훅으로 등록하면 그런 명령을 차단한다.
# 등록: .claude/settings.json → hooks.PreToolUse, matcher "Bash".
#
# 훅 입력(JSON)에서 command 필드를 따로 파싱하지 않는다. 덧그리기 도구의
# 고유 토큰은 payload 원문에 그대로 담기므로, 원문을 바로 스캔한다.

payload="$(cat)"

# 글자 덧그리기 신호 (도구별). 하나라도 걸리면 차단.
overlay_signals=(
  'ImageDraw'                                       # Pillow 텍스트 드로잉
  'ImageFont'                                       # Pillow 폰트 로딩
  'drawtext'                                        # ffmpeg 자막 필터
  '-annotate'                                       # ImageMagick 주석
  '(convert|magick|mogrify)[^"]*(label:|caption:|pango:)'  # ImageMagick 텍스트 이미지
  '-draw[[:space:]][^"]{0,80}text'                  # ImageMagick draw text
)

for sig in "${overlay_signals[@]}"; do
  if printf '%s' "$payload" | grep -Eq -e "$sig"; then
    printf '%s\n' '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"글자는 프롬프트로 이미지 안에서 렌더한다. 생성물 위 글자 덧그리기(후처리)는 막는다 — 틀리면 프롬프트를 고쳐 재생성할 것(SKILL.md 하지 말 것, craft.md 1)."}}'
    exit 0
  fi
done
exit 0
