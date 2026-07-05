#!/usr/bin/env python3
"""gpt-image 7블록 프롬프트 규칙 검증기.

사용:
    python3 scripts/check_prompt.py <파일>
    echo "...프롬프트..." | python3 scripts/check_prompt.py
    python3 scripts/check_prompt.py --test        # 내장 픽스처 셀프테스트

출력: JSON {ok, errors:[{code,msg}], warnings:[{code,msg}]}
errors가 0이면 exit 0, 하나라도 있으면 exit 1.

규칙 근거는 SKILL.md·references/craft.md. 핵심:
- 7블록 존재·순서
- 모호 형용사 환원 (E-VAGUE)
- 화면비 토큰 + 5종 정본 (E-AR-MISSING / W-AR-NONCANON)
- 낡은 품질 토큰(8k·masterpiece 등) 금지 (E-DEAD-WORD)
- 네거티브 최소화: 라벨형 금지(E-NEG-LABEL), 한국어 배제형은 경고(W-NEG-KO)
- 언어 혼용 경고 (W-LANG-MIX)
- 따옴표 텍스트에 가독성 가드 (W-TEXT-GUARD)
"""
import sys, re, json

BLOCKS = ["결과물 유형", "주 피사체", "구도와 비율", "맥락과 배경",
          "스타일과 매체", "빛과 디테일", "정확성 조건"]

VAGUE = ["예쁘게", "예쁜", "고급스럽게", "감성적으로", "감성적인", "멋지게", "멋진",
         "세련되게", "세련된", "분위기 있게", "beautiful", "stunning", "gorgeous"]

DEAD = ["8k", "4k", "uhd", "masterpiece", "best quality", "ultra-detailed",
        "ultra detailed", "highly detailed", "sharp focus", "trending on artstation"]

# 5종 정본 화면비
CANON_AR = {"3:4", "16:9", "1:1", "9:16", "21:9"}
AR_ANY = re.compile(r"\b(\d{1,2}:\d{1,2})\b")

STAGE_DIRECTIONS = ["어워드 수준", "전문가처럼", "최고급으로", "award-winning", "professional grade"]


def quoted_strings(text):
    # 렌더 텍스트로 간주할 따옴표 문자열 (한글/영문 카피). 2자 이상만.
    out = []
    for m in re.finditer(r'"([^"]{2,})"', text):
        out.append(m.group(1))
    return out


def check(text):
    errors, warnings = [], []
    low = text.lower()

    # 1) 7블록 존재 + 순서
    positions = []
    for b in BLOCKS:
        m = re.search(rf"(?m)^\s*{re.escape(b)}\s*:", text)
        if not m:
            errors.append({"code": "E-BLOCK-MISSING", "msg": f"블록 누락: '{b}:'"})
        else:
            positions.append((b, m.start()))
    if len(positions) == len(BLOCKS):
        order = [b for b, _ in sorted(positions, key=lambda x: x[1])]
        if order != BLOCKS:
            errors.append({"code": "E-BLOCK-ORDER",
                           "msg": f"블록 순서가 정본과 다름: {' > '.join(order)}"})

    # 2) 모호 형용사 (영어는 대소문자 무시)
    for w in VAGUE:
        if w.lower() in low:
            errors.append({"code": "E-VAGUE",
                           "msg": f"모호 형용사 '{w}'. 명사·수치·배치로 환원할 것"})
    for w in STAGE_DIRECTIONS:
        if w.lower() in low:
            warnings.append({"code": "W-STAGE",
                             "msg": f"무대 지정 '{w}'. 기준이 프롬프트 밖. 구체 명세로 대체"})

    # 3) 화면비 (5종 정본)
    ars = AR_ANY.findall(text)
    if not ars:
        errors.append({"code": "E-AR-MISSING", "msg": "화면비 토큰 없음 (예: 3:4 세로형)"})
    else:
        noncanon = [a for a in ars if a not in CANON_AR]
        if noncanon and not (set(ars) & CANON_AR):
            warnings.append({"code": "W-AR-NONCANON",
                             "msg": f"비정본 화면비 {noncanon}. 5종(3:4·16:9·1:1·9:16·21:9) 권장"})

    # 4) 낡은 품질 토큰
    for w in DEAD:
        if re.search(rf"(?<![a-z0-9]){re.escape(w)}(?![a-z0-9])", low):
            errors.append({"code": "E-DEAD-WORD",
                           "msg": f"낡은 품질 토큰 '{w}'. 결과를 구체 명세로 대체"})

    # 5) 네거티브
    if re.search(r"(?mi)^\s*(negative|avoid)\s*:", text) or re.search(r"(?i)\bavoid\b\s+[a-z]", text):
        errors.append({"code": "E-NEG-LABEL",
                       "msg": "라벨형 네거티브(Negative:/Avoid ...). 긍정형으로 재서술"})
    ko_neg = re.findall(r"([^\s\"]{0,10}\s*(?:없이|피하기|피합니다|피해주세요|금지))", text)
    if ko_neg:
        warnings.append({"code": "W-NEG-KO",
                         "msg": f"한국어 배제형 {len(ko_neg)}건(없이/피하기 등). 원하는 상태를 긍정형으로 재서술 권장"})

    # 6) 언어 혼용 (프롬프트 본문에 한글 서사 + 영문 문장이 동시에 많으면)
    body = re.sub(r'"[^"]*"', "", text)  # 따옴표 카피 제외
    hangul = len(re.findall(r"[가-힣]", body))
    latin_words = re.findall(r"[A-Za-z]{4,}", body)
    # 허용 기술 토큰은 제외
    allow = {"shallow", "rim", "light", "grain", "film", "bokeh", "editorial", "vector",
             "close", "wide", "hex", "kelvin", "worm"}
    latin_words = [w for w in latin_words if w.lower() not in allow]
    if hangul > 30 and len(latin_words) > 12:
        warnings.append({"code": "W-LANG-MIX",
                         "msg": f"언어 혼용 의심(한글 {hangul}자 + 영문 단어 {len(latin_words)}개). 한 프롬프트 한 언어"})

    # 7) 따옴표 텍스트 가독성 가드
    qs = quoted_strings(text)
    if qs:
        guard = re.search(r"(또렷|가독|legible|한 번씩|선명|crisp)", text)
        if not guard:
            warnings.append({"code": "W-TEXT-GUARD",
                             "msg": f"렌더 텍스트 {len(qs)}개 있으나 가독성 가드 없음. \"각 글자 한 번씩 또렷하게\" 1줄 추가"})

    return {"ok": len(errors) == 0, "errors": errors, "warnings": warnings}


GOOD = """결과물 유형:
브랜드 출시용 3:4 세로형 제품 포스터. 주제는 "봄맞이 텀블러".

주 피사체:
선샤인 옐로우 세라믹 텀블러를 화면 중앙에 크게 배치.

구도와 비율:
3:4 세로형. 제품은 중앙, 상단에 제목 영역.

맥락과 배경:
일요일 아침 주방 창가, 부드러운 아침 햇살.

스타일과 매체:
무광 세라믹 질감의 고급 제품 렌더. 팔레트 #F2B84B / #1B2566 / #FAF1E2.

빛과 디테일:
부드러운 스튜디오 조명.
낮은 3/4 시점.

정확성 조건:
제목 "Morning Solar"는 각 글자 한 번씩 또렷하게. 브랜드 표기 없는 클린 마감."""

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


USAGE = """gpt-image 7블록 프롬프트 규칙 검증기

  python3 scripts/check_prompt.py <파일>      파일을 검증
  echo "...프롬프트..." | python3 scripts/check_prompt.py   표준입력을 검증
  python3 scripts/check_prompt.py --test      내장 픽스처 셀프테스트
  python3 scripts/check_prompt.py --help      이 도움말

종료 코드: errors 0이면 0, errors 있으면 1, 파일 입출력 실패면 2."""


def selftest():
    """GOOD은 통과하고 BAD는 대표 오류 코드를 전부 잡는지 확인한다."""
    g = check(GOOD)
    b = check(BAD)
    bad_codes = {e["code"] for e in b["errors"]}
    expected = {"E-VAGUE", "E-DEAD-WORD", "E-NEG-LABEL", "E-BLOCK-ORDER", "E-AR-MISSING"}
    okg = g["ok"] is True
    okb = b["ok"] is False and expected <= bad_codes
    print(json.dumps({
        "good_pass": okg,
        "bad_caught": okb,
        "missing_codes": sorted(expected - bad_codes),
        "good": g,
        "bad": b,
    }, ensure_ascii=False, indent=2))
    return 0 if (okg and okb) else 1


def main():
    argv = sys.argv[1:]
    if "-h" in argv or "--help" in argv:
        print(USAGE)
        return 0
    if "--test" in argv:
        return selftest()

    paths = [a for a in argv if not a.startswith("-")]
    if paths:
        try:
            with open(paths[0], encoding="utf-8") as f:
                text = f.read()
        except OSError as e:
            print(json.dumps(
                {"ok": False,
                 "errors": [{"code": "E-IO", "msg": f"파일을 읽을 수 없음: {e}"}],
                 "warnings": []},
                ensure_ascii=False, indent=2))
            return 2
    else:
        text = sys.stdin.read()

    res = check(text)
    print(json.dumps(res, ensure_ascii=False, indent=2))
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
