#!/usr/bin/env bash
# 이미지에 넣을 글자는 프롬프트로 이미지 "안에서" 렌더한다.
# 생성된 그림 위에 코드로 글자를 덧그리는 후처리는 폰트·톤이 원본과 겉돌아 막는다.
# 틀린 글자는 후보정이 아니라 프롬프트를 고쳐 재생성으로 잡는다(SKILL.md, craft.md §1).
#
# 등록: .claude/settings.json → hooks.PreToolUse, matcher "Bash".
# PreToolUse 훅으로 등록하면 아래 도구 호출을 차단한다.
# 자체 점검: `bash hooks/block-text-overlay.sh --test` (차단/통과 표본을 검증).
#
# 설계 노트
# - 훅 입력(JSON)에서 command 필드를 따로 파싱하지 않는다. 덧그리기 도구의 고유
#   토큰은 payload 원문에 그대로 담기므로 원문을 바로 스캔한다(인자 구조에 안 흔들림).
# - 판정은 "덜 막기보다 더 막기". 가드레일이라 오탐(선의의 명령 차단)이 미탐(오버레이
#   통과)보다 안전하다. 오탐이 나면 해당 시그니처를 좁히거나 명령을 바꿔 재시도한다.
# - 아래 시그니처는 각 도구의 "텍스트" 오버레이 문법에만 걸리도록 좁혔다(도형 그리기,
#   리사이즈 등 글자와 무관한 호출은 통과).

# 글자 덧그리기 신호 (도구별). 하나라도 걸리면 차단.
overlay_signals=(
  'ImageDraw'                                       # Pillow 텍스트 드로잉 객체
  'ImageFont'                                       # Pillow 폰트 로딩
  'drawtext='                                       # ffmpeg drawtext 필터 (항상 = 뒤에 인자)
  '-annotate'                                        # ImageMagick 주석(텍스트)
  '(convert|magick|mogrify)[^"]*(label:|caption:|pango:)'  # ImageMagick 텍스트→이미지
  '-draw[[:space:]"]*text'                           # ImageMagick draw text "..."
)

# payload 문자열에 오버레이 신호가 있으면 0(차단), 없으면 1(통과)을 반환.
is_overlay() {
  local text="$1" sig
  for sig in "${overlay_signals[@]}"; do
    if printf '%s' "$text" | grep -Eq -e "$sig"; then
      return 0
    fi
  done
  return 1
}

deny_json='{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"글자는 프롬프트로 이미지 안에서 렌더한다. 생성물 위 글자 덧그리기(후처리)는 막는다. 틀리면 프롬프트를 고쳐 재생성할 것(SKILL.md 하지 말 것, craft.md §1)."}}'

# ---- 셀프테스트: bash block-text-overlay.sh --test ----
run_tests() {
  local fail=0 c
  # 차단돼야 하는 명령
  local deny=(
    'python -c "from PIL import Image, ImageDraw; d=ImageDraw.Draw(im); d.text((10,10),\"Sale\")"'
    'ImageFont.truetype("NanumGothic.ttf", 40)'
    "ffmpeg -i a.png -vf \"drawtext=text='50% OFF'\" out.png"
    'convert in.png -annotate +10+10 "신제품" out.png'
    'magick label:"오늘의 행사" out.png'
    "convert in.png -draw \"text 10,10 'Hi'\" out.png"
  )
  # 통과돼야 하는 명령 (오버레이와 무관)
  local allow=(
    'python3 scripts/check_prompt.py draft.txt'
    'cat references/craft.md'
    'ffmpeg -i a.mp4 -vf scale=1280:720 out.mp4'
    'echo "drawing board notes"'
    'convert in.png -resize 50% out.png'
  )
  for c in "${deny[@]}"; do
    if is_overlay "$c"; then echo "PASS 차단: $c"; else echo "FAIL 차단 기대인데 통과: $c"; fail=1; fi
  done
  for c in "${allow[@]}"; do
    if is_overlay "$c"; then echo "FAIL 통과 기대인데 차단: $c"; fail=1; else echo "PASS 통과: $c"; fi
  done
  if [ "$fail" -eq 0 ]; then echo "ok: 셀프테스트 전부 통과 (차단 ${#deny[@]} / 통과 ${#allow[@]})"; else echo "fail: 셀프테스트 실패"; fi
  return "$fail"
}

if [ "${1:-}" = "--test" ]; then
  run_tests
  exit $?
fi

# ---- 실제 훅 동작: stdin payload를 스캔 ----
payload="$(cat)"
if is_overlay "$payload"; then
  printf '%s\n' "$deny_json"
fi
exit 0
