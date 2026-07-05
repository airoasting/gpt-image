<p align="center">
  <img src="docs/assets/gptimage2skill-banner.png" alt="GPT 이미지 생성 프롬프트로 만든 결과물 예시 모음" width="100%" />
</p>

# GPT 이미지 프롬프트 랩

한국어로 구상한 장면을 GPT 이미지 모델에 바로 넣을 수 있는 프롬프트로 바꾸는 실전 가이드입니다. **7가지 품질 원칙**, **프롬프트 도움창**, **선별 레퍼런스 갤러리**를 한곳에서 제공합니다.

**▶ 라이브 사이트: [airoasting-image.vercel.app](https://airoasting-image.vercel.app)** · 버전 1.0 (2026-07-05, [변경 이력](CHANGELOG.md))

사이트(`docs/`)와 번들 스킬(`SKILL.md`, `references/`, `scripts/`)은 분리되어 있습니다. Vercel은 `docs/`를 배포 소스로 서빙하고, 스킬은 프로젝트 루트에서 바로 로드됩니다.

- **정적 웹사이트**(`docs/index.html`): 원칙을 익히고, 프롬프트를 조립하고, 레퍼런스를 탐색합니다.
- **번들 스킬**(`SKILL.md`): AI 에이전트가 같은 7원칙으로 프롬프트를 설계하도록 안내하는 실행 규칙입니다.
- **레퍼런스 라이브러리**(`references/`): 10개 카테고리 파일에 각 10개씩, 사이트 갤러리(100개)의 실제 프롬프트를 담았습니다. 작성 규칙(`craft.md`)과 변주 레시피(`variation-recipes.md`)도 함께 있습니다.

## 담긴 것

| 구성 | 수량 | 위치 |
|---|---|---|
| 품질 원칙 | 7가지 | `docs/index.html` 섹션 01 |
| 결과물 카테고리 | 10개 | 갤러리 필터 |
| 선별 레퍼런스 | 100개 | `references/gallery-*.md` |

## 7가지 원칙

이미지 모델의 실패는 대부분 "예쁘게", "고급스럽게", "감성적으로" 같은 모호한 형용사에서 나옵니다. 모델이 형용사를 상상으로 채우기 때문입니다. 7원칙은 그 빈칸을 결정 가능한 항목으로 바꿉니다.

각 원칙을 같은 소재(노란 텀블러)로 **안 좋은 예(모호한 지시)**와 **좋은 예(구체적 지시)** 두 장씩 나란히 놓았습니다. 왼쪽이 모호할 때와 오른쪽이 결정 가능한 항목으로 바뀔 때 결과가 어떻게 달라지는지 비교해 보세요.

### 1. 결과물 유형을 정하기
포스터, 인물 사진, UI, 인포그래픽처럼 결과물의 종류를 첫 줄에 고정합니다.

<p>
  <img src="docs/assets/principles/principle-01-weak.png" height="200" alt="원칙 1 안 좋은 예: 노란 텀블러가 있는 멋진 카페 느낌" />
  <img src="docs/assets/principles/principle-01-strong.png" height="200" alt="원칙 1 좋은 예: 브랜드 출시용 3:4 세로형 제품 포스터" />
</p>

`안 좋은 예` 노란 텀블러가 있는 멋진 카페 느낌 · `좋은 예` 선샤인 옐로우 세라믹 텀블러의 브랜드 출시용 3:4 세로형 제품 포스터, 제품이 중앙에 크게 보이는 인쇄물 스타일

### 2. 주 피사체를 고정하기
이미지의 중심이 되는 대상, 인물, 제품, 장면을 분명히 씁니다.

<p>
  <img src="docs/assets/principles/principle-02-weak.png" height="200" alt="원칙 2 안 좋은 예: 봄 카페 분위기, 꽃, 디저트, 음료" />
  <img src="docs/assets/principles/principle-02-strong.png" height="200" alt="원칙 2 좋은 예: 텀블러를 화면 중앙에 크게 배치" />
</p>

`안 좋은 예` 봄 카페 분위기, 꽃, 디저트, 음료, 따뜻한 햇살 · `좋은 예` 선샤인 옐로우 세라믹 텀블러를 화면 중앙에 크게 배치, 뒤에는 봄꽃과 카페 배경을 부드럽게 흐리게 처리

### 3. 구도와 비율을 지정하기
화면 비율, 피사체 위치, 여백, 시점의 큰 틀을 정합니다.

<p>
  <img src="docs/assets/principles/principle-03-weak.png" height="200" alt="원칙 3 안 좋은 예: 여행 간 느낌의 적당히 예쁜 사진" />
  <img src="docs/assets/principles/principle-03-strong.png" height="200" alt="원칙 3 좋은 예: 16:9 와이드, 텀블러는 오른쪽 1/3 지점" />
</p>

`안 좋은 예` 노란 텀블러를 들고 여행 간 느낌, 적당히 예쁜 사진 · `좋은 예` 16:9 가로형 와이드 제품 여행 사진, 노란 텀블러는 오른쪽 1/3 지점, 왼쪽에는 호수와 산맥의 넓은 여백

### 4. 맥락과 배경을 설명하기
어디에서, 어떤 상황에서, 어떤 분위기로 보일지 정합니다.

<p>
  <img src="docs/assets/principles/principle-04-weak.png" height="200" alt="원칙 4 안 좋은 예: 좋은 분위기에서 보여주기" />
  <img src="docs/assets/principles/principle-04-strong.png" height="200" alt="원칙 4 좋은 예: 일요일 아침 주방 창가 루틴" />
</p>

`안 좋은 예` 노란 텀블러를 좋은 분위기에서 보여주기 · `좋은 예` 일요일 아침 주방 창가에서 쓰는 노란 텀블러, 반쯤 열린 노트와 커피 원두, 부드러운 아침 햇살로 차분한 루틴을 표현

### 5. 스타일과 매체를 선택하기
사진, 3D 렌더, 수채화, 포스터, 편집 디자인처럼 표현 방식을 정합니다.

<p>
  <img src="docs/assets/principles/principle-05-weak.png" height="200" alt="원칙 5 안 좋은 예: 고급스럽게, 예쁘고 세련된 느낌" />
  <img src="docs/assets/principles/principle-05-strong.png" height="200" alt="원칙 5 좋은 예: 무광 세라믹 질감의 고급 제품 렌더" />
</p>

`안 좋은 예` 노란 텀블러를 고급스럽게, 예쁘고 세련된 느낌 · `좋은 예` 무광 세라믹 질감이 보이는 노란 텀블러의 고급 제품 렌더, 부드러운 스튜디오 조명, 석회석 받침대, 인디고 포인트

### 6. 빛과 디테일을 구체화하기
조명, 질감, 재료, 표면, 카메라 렌즈처럼 완성도를 좌우하는 요소를 씁니다.

<p>
  <img src="docs/assets/principles/principle-06-weak.png" height="200" alt="원칙 6 안 좋은 예: 극적으로 찍기, 분위기 있게" />
  <img src="docs/assets/principles/principle-06-strong.png" height="200" alt="원칙 6 좋은 예: 낮은 앵글, 강한 림 라이트" />
</p>

`안 좋은 예` 노란 텀블러를 극적으로 찍기, 분위기 있게 · `좋은 예` 노란 텀블러를 바닥 가까운 낮은 앵글로 촬영, 강한 림 라이트와 젖은 돌 바닥의 노란빛 반사를 사용

### 7. 정확성 조건을 덧붙이기
텍스트, 금지 요소, 유지해야 할 요소, 왜곡 방지 조건을 마지막에 씁니다.

<p>
  <img src="docs/assets/principles/principle-07-weak.png" height="200" alt="원칙 7 안 좋은 예: 깔끔하게, 제목도 적당히" />
  <img src="docs/assets/principles/principle-07-strong.png" height="200" alt="원칙 7 좋은 예: 제목 Morning Solar 정확히 표시" />
</p>

`안 좋은 예` 노란 텀블러 포스터를 깔끔하게, 제목도 적당히 넣기 · `좋은 예` 노란 텀블러 포스터, 제목은 "Morning Solar"로 정확히 표시, 로고와 깨진 글자와 뒤틀린 뚜껑은 넣지 않기

핵심 규칙은 하나입니다. **모든 형용사를 명사·수치·배치로 환원합니다.** "고급스럽게"는 "무광 세라믹 + 석회석 받침대 + 스튜디오 조명"으로, "극적으로"는 "낮은 앵글 + 림 라이트"로 바꿉니다.

## 7블록 프롬프트 템플릿

원칙을 순서대로 채우면 아래 형식이 됩니다. 이 순서를 정본으로 삼습니다.

```
결과물 유형:
선샤인 옐로우 세라믹 텀블러의 브랜드 출시용 3:4 세로형 제품 포스터. 제품이 중앙에 크게 보이는 인쇄물 스타일.

주 피사체:
선샤인 옐로우 세라믹 텀블러를 화면 중앙에 크게 배치. 뚜껑까지 닫힌 완성된 형태를 유지하고, 뒤에는 봄꽃과 카페 배경을 부드럽게 흐리게 처리.

구도와 비율:
3:4 세로형. 텀블러를 정중앙에 두고 위쪽에 제목 영역, 아래쪽에 브랜드 정보 영역을 위한 여백을 남긴다.

맥락과 배경:
일요일 아침 주방 창가의 차분한 루틴. 반쯤 열린 노트와 커피 원두를 곁들이고 부드러운 아침 햇살로 따뜻한 분위기를 만든다.

스타일과 매체:
무광 세라믹 질감이 보이는 고급 제품 렌더. 부드러운 스튜디오 조명, 석회석 받침대, 인디고 포인트.

빛과 디테일:
부드러운 스튜디오 조명에 은은한 골든아워 느낌을 더한다.
정면에 가까운 미디엄 샷.

정확성 조건:
최종 결과물: 글자 가독성·구도·색감·디테일 일관성 우선. 제목은 "Morning Solar"로 정확히 표시하고, 로고·깨진 글자·뒤틀린 뚜껑은 피한다.
따옴표 안의 문구는 철자와 띄어쓰기를 그대로 유지해주세요. 모호한 일반 표현, 왜곡된 타이포그래피, 불필요한 장식은 피해주세요.
```

## 카테고리별 샘플

10개 카테고리마다 사이트 갤러리의 대표 이미지 2장을 골랐습니다. 각 카테고리의 전체 목록과 프롬프트는 링크된 파일에서 볼 수 있습니다.

### 웹툰
액션과 감정, 컷 흐름을 중심으로 웹툰·만화 연출을 다룹니다.

<p>
  <img src="docs/assets/generated-gallery/gallery-001.png" height="220" alt="웹툰 샘플: 용을 깨운 신입 기사 (세로 히어로컷)" />
  <img src="docs/assets/generated-gallery/gallery-010.png" height="220" alt="웹툰 샘플: 바다 마을의 기계 심장 (와이드 파노라마)" />
</p>

전체: [`references/gallery-webtoon.md`](references/gallery-webtoon.md)

### 일러스트
선과 색면, 질감, 장식이 하나의 작품처럼 균형을 이루는 화면입니다.

<p>
  <img src="docs/assets/generated-gallery/gallery-012.png" height="220" alt="일러스트 샘플: 엘프 궁수 설정 시트 (세로 선화)" />
  <img src="docs/assets/generated-gallery/gallery-020.png" height="220" alt="일러스트 샘플: 해질녘 강가 인상주의 회화 (와이드)" />
</p>

전체: [`references/gallery-illustration.md`](references/gallery-illustration.md)

### 게임
플레이 공간과 유닛 위치, 지형, 장르 규칙이 한눈에 드러나는 화면입니다.

<p>
  <img src="docs/assets/generated-gallery/gallery-022.png" height="220" alt="게임 샘플: 해변 오픈월드 게임 화면 (밝은 와이드)" />
  <img src="docs/assets/generated-gallery/gallery-027.png" height="220" alt="게임 샘플: 어두운 판타지 세계관 아홉 장면 (정사각 그리드)" />
</p>

전체: [`references/gallery-gaming.md`](references/gallery-gaming.md)

### 시네마틱
피사체와 배경, 빛, 카메라, 긴장점이 분명한 영화 한 장면입니다.

<p>
  <img src="docs/assets/generated-gallery/gallery-033.png" height="220" alt="시네마틱 샘플: 여섯 컷 영화 스토리보드 (정사각 그리드)" />
  <img src="docs/assets/generated-gallery/gallery-036.png" height="220" alt="시네마틱 샘플: 검은 기념비와 사막 공상과학 장면 (시네마스코프 와이드)" />
</p>

전체: [`references/gallery-cinematic.md`](references/gallery-cinematic.md)

### 포스터
제목과 부제, 대표 이미지, 여백의 위계가 멀리서도 읽히는 편집 디자인입니다.

<p>
  <img src="docs/assets/generated-gallery/gallery-041.png" height="220" alt="포스터 샘플: 미니멀 스릴러 영화 포스터 (여백 중심)" />
  <img src="docs/assets/generated-gallery/gallery-048.png" height="220" alt="포스터 샘플: 도시 재즈 페스티벌 포스터 (고밀도 컬러)" />
</p>

전체: [`references/gallery-typography-and-posters.md`](references/gallery-typography-and-posters.md)

### 제품 · 브랜드
형태와 소재, 라벨, 패키지가 제품을 중심으로 정리된 광고 마감입니다.

<p>
  <img src="docs/assets/generated-gallery/gallery-053.png" height="220" alt="제품 · 브랜드 샘플: 샐러드 재료가 흩어지는 음식 사진 (동적 촬영)" />
  <img src="docs/assets/generated-gallery/gallery-055.png" height="220" alt="제품 · 브랜드 샘플: 휴대용 라디오 브랜드 아이덴티티 보드 (정렬형)" />
</p>

전체: [`references/gallery-product-and-brand.md`](references/gallery-product-and-brand.md)

### 인물 사진
인물과 의상, 소품, 카메라 거리가 실제 촬영처럼 정리된 화면입니다.

<p>
  <img src="docs/assets/generated-gallery/gallery-064.png" height="220" alt="인물 사진 샘플: 숲속 탐험가 (와이드 다큐멘터리)" />
  <img src="docs/assets/generated-gallery/gallery-068.png" height="220" alt="인물 사진 샘플: 초현실주의 하이패션 화보 (세로 스튜디오)" />
</p>

전체: [`references/gallery-photography.md`](references/gallery-photography.md)

### 건물 사진
규모와 입구, 동선, 재료에서 실제 사용성이 드러나는 건축 시각화입니다.

<p>
  <img src="docs/assets/generated-gallery/gallery-071.png" height="220" alt="건물 사진 샘플: 아이소메트릭 미니 카페 거리 (정사각 조감)" />
  <img src="docs/assets/generated-gallery/gallery-076.png" height="220" alt="건물 사진 샘플: 고딕 대성당 내부 (세로형 실내)" />
</p>

전체: [`references/gallery-architecture-and-interior.md`](references/gallery-architecture-and-interior.md)

### 인포그래픽
제목과 번호 단계, 라벨, 아이콘, 그래프가 읽기 쉬운 순서로 정리된 설명 자료입니다.

<p>
  <img src="docs/assets/generated-gallery/gallery-082.png" height="220" alt="인포그래픽 샘플: 서울 지하철 환승 안내 (세로 노선도)" />
  <img src="docs/assets/generated-gallery/gallery-085.png" height="220" alt="인포그래픽 샘플: 국민건강검진 절차 안내도 (와이드 플로우)" />
</p>

전체: [`references/gallery-infographics-and-field-guides.md`](references/gallery-infographics-and-field-guides.md)

### UI·대시보드
상단 바와 카드, 그래프, 버튼이 실제 제품 화면처럼 정렬된 목업입니다.

<p>
  <img src="docs/assets/generated-gallery/gallery-091.png" height="220" alt="UI·대시보드 샘플: 월급 관리 가계부 앱 (모바일 세로)" />
  <img src="docs/assets/generated-gallery/gallery-100.png" height="220" alt="UI·대시보드 샘플: 지역 농산물 수확량 지도 (와이드 대시보드)" />
</p>

전체: [`references/gallery-ui-ux-mockups.md`](references/gallery-ui-ux-mockups.md)

전체 카테고리 인덱스는 [`references/gallery.md`](references/gallery.md)에 있습니다.

## 설치하고 사용하기 (비개발자용)

**이 도구가 하는 일.** 평소 말로 "카페 신메뉴 홍보용 세로 포스터 만들어줘"라고 하면, AI가 이 가이드의 7원칙에 맞춰 GPT 이미지 모델용 전문 프롬프트로 바꿔 줍니다. 프롬프트를 직접 배우지 않아도 됩니다.

**준비물.** 컴퓨터에 **Codex**(터미널에서 쓰는 AI 도우미)가 설치되어 있으면 됩니다. Codex가 없다면 먼저 그것부터 설치합니다.

**설치 방법 (택 1)**

**방법 A (가장 쉬움).** 이 폴더를 열어 둔 상태에서 Codex(또는 Claude Code 같은 터미널 AI)에게 이렇게 부탁하면 알아서 설치합니다.

> 이 폴더를 `gpt-image`라는 이름의 Codex 스킬로 설치해 줘.

**방법 B (직접 하기).** 터미널을 열고 이 폴더 안에서 아래 세 줄을 그대로 복사해 붙여넣고 실행합니다. 스킬 파일을 Codex가 찾는 폴더로 복사하는 명령이며, 한 번만 실행하면 됩니다.

```bash
mkdir -p ~/.codex/skills/gpt-image/docs/js
cp -r SKILL.md references scripts hooks ~/.codex/skills/gpt-image/
cp docs/js/gallery-data.js ~/.codex/skills/gpt-image/docs/js/
```

**사용 방법.** 설치 후에는 Codex에게 평소 말로 요청하면 됩니다. 예: "분기 실적 발표용 표지 이미지가 필요해", "제품 상세페이지 상단 배너 만들어줘". AI가 요청을 10개 카테고리 중 하나로 알아보고, 이 저장소의 실제 예시 100개를 참고해, 바로 복사해 쓸 수 있는 프롬프트를 만들어 줍니다.

**만든 프롬프트로 실제 이미지 뽑기.** 프롬프트를 ChatGPT의 이미지 생성이나 다른 이미지 도구에 붙여넣으면 됩니다. 프롬프트를 만드는 것 자체에는 추가 비용이 없고, 실제 이미지 생성은 선택입니다. (이미지 생성 API를 직접 호출하면 사용량에 따라 요금이 부과될 수 있습니다.)

<details>
<summary>개발자·고급 사용자용 참고</summary>

스킬에는 품질 도구가 함께 들어 있습니다. 규칙 검증기(`scripts/check_prompt.py`, `python3 scripts/check_prompt.py <파일>`로 `ok: true` 확인), 생성물 위 글자 후처리를 막는 훅(`hooks/block-text-overlay.sh`), 규칙의 근거가 된 실측 채점(`experiments/`, 10개 카테고리 각 1컷씩 총 10컷 비전 채점, 상세 결과는 `experiments/REPORT.md`). AI는 요청을 분류한 뒤 1차로 `docs/js/gallery-data.js`의 한국어 예시 100개를 참고하고, 세부 기법이 필요하면 `references/gallery.md`가 가리키는 카테고리 파일과 `references/craft.md`·`references/variation-recipes.md`를 추가로 읽습니다. 실제 이미지 생성은 ChatGPT 등 호스트의 이미지 생성 도구에 완성 프롬프트를 붙여넣어 실행합니다.

</details>

## 로컬에서 보기

정적 사이트라 빌드가 필요 없습니다.

```bash
cd docs && python3 -m http.server 8000
# 브라우저에서 http://localhost:8000
```

갤러리 데이터(`docs/js/gallery-data.js`)가 사이트의 정본입니다. 레퍼런스 `references/gallery-*.md`는 이 정본에서 생성된 사본입니다.

## 프로젝트 구조

사이트(`docs/`)와 번들 스킬(`SKILL.md`, `references/`, `scripts/`, `hooks/`, `experiments/`)이 분리되어 있습니다. Vercel 등으로 `docs/` 폴더를 배포하면 사이트만 서빙되고([airoasting-image.vercel.app](https://airoasting-image.vercel.app)), 스킬은 프로젝트 루트에서 그대로 로드됩니다. 사이트의 "MD 다운로드" 링크는 GitHub 원본 URL(`raw.githubusercontent.com`)을 가리켜, 레퍼런스가 사이트 배포본 밖에 있어도 항상 접근됩니다.

```
.
├── README.md
├── SKILL.md                       # 번들 스킬 (7원칙 프롬프트 설계 규칙)
├── references/                    # 레퍼런스 (gallery-*.md, craft.md, variation-recipes.md, openai-cookbook.md)
├── scripts/check_prompt.py        # 프롬프트 규칙 검증기 (--test 셀프테스트)
├── hooks/block-text-overlay.sh    # 생성물 위 글자 후처리 차단 훅
├── experiments/                   # 실측 채점 (RUBRIC · REPORT · scores · select_sample)
└── docs/                          # 정적 사이트 배포 소스 (Vercel)
    ├── index.html                 # 가이드 사이트 (원칙 · 빌더 · 갤러리)
    ├── css/styles.css
    ├── js/
    │   ├── script.js              # 7원칙 데이터, 빌더, 갤러리 렌더링
    │   └── gallery-data.js        # 갤러리 데이터 (사이트 정본)
    └── assets/                    # 로고, 원칙 예시 이미지, 갤러리 이미지
```

## 라이선스

이 프로젝트는 **Apache License 2.0**으로 배포됩니다. 자유롭게 사용, 수정, 재배포, 상업적 이용이 가능하며, 수정한 파일에는 변경 사실을 표시하고 원저작권·라이선스 고지를 유지하면 됩니다. 전문은 [`LICENSE`](LICENSE)를 참고하세요.

Copyright 2026 AIROASTING
