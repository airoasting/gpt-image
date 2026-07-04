<p align="center">
  <img src="docs/assets/gptimage2skill-banner.png" alt="GPT 이미지 생성 프롬프트로 만든 결과물 예시 모음" width="100%" />
</p>

# GPT 이미지 생성 프롬프트 가이드

한국어로 구상한 장면을 GPT 이미지 모델에 바로 넣을 수 있는 프롬프트로 바꾸는 실전 가이드입니다. **7가지 품질 원칙**, **프롬프트 도움창**, **선별 레퍼런스 갤러리**를 한곳에서 제공합니다.

사이트(`docs/`)와 번들 스킬(`SKILL.md`, `references/`, `scripts/`)은 분리되어 있습니다. GitHub Pages는 `docs/`만 배포 소스로 서빙하고, 스킬은 프로젝트 루트에서 바로 로드됩니다.

- 정적 웹사이트(`docs/index.html`): 원칙 학습 → 프롬프트 조립 → 레퍼런스 탐색
- 번들 스킬(`SKILL.md`): AI 에이전트가 같은 7원칙으로 프롬프트를 설계하게 하는 실행 규칙
- 레퍼런스 라이브러리(`references/`): 31개 카테고리 파일, 160여 개의 큐레이션 프롬프트

## 담긴 것

| 구성 | 수량 | 위치 |
|---|---|---|
| 품질 원칙 | 7가지 | `docs/index.html` 섹션 01 |
| 결과물 카테고리 | 10개 | 갤러리 필터 |
| 선별 레퍼런스 | 160여 개 | `references/gallery-*.md` |

## 7가지 원칙

이미지 모델의 실패는 대부분 "예쁘게", "고급스럽게", "감성적으로" 같은 모호한 형용사에서 나옵니다. 모델이 형용사를 상상으로 채우기 때문입니다. 7원칙은 그 빈칸을 결정 가능한 항목으로 바꿉니다.

1. **결과물 유형을 정하기** — 포스터·인물 사진·UI·인포그래픽처럼 종류를 첫 줄에 고정
2. **주 피사체를 고정하기** — 중심이 되는 대상·인물·제품을 하나로
3. **구도와 비율을 지정하기** — 화면 비율, 피사체 위치, 여백, 시점
4. **맥락과 배경을 설명하기** — 어디에서, 어떤 상황에서, 어떤 분위기로
5. **스타일과 매체를 선택하기** — 사진·3D 렌더·수채화·포스터·편집 디자인
6. **빛과 디테일을 구체화하기** — 조명·질감·재료·표면·카메라 렌즈
7. **정확성 조건을 덧붙이기** — 텍스트, 금지 요소, 유지 요소, 왜곡 방지

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

10개 카테고리마다 레퍼런스 갤러리의 대표 프롬프트를 하나씩 골랐습니다. 각 카테고리의 전체 목록과 이미지, 전체 프롬프트는 링크된 파일에서 볼 수 있습니다.

### 웹툰
액션·감정·컷 흐름 중심. 애니메이션 스틸과 만화 연출.
> **MAPPA 스타일 애니 액션 스틸** (16:9): "An anime action still in the visual style of MAPPA's Jujutsu Kaisen … a mid-fight stance, one palm extended outward releasing a swirling energy …"
> 전체: [`references/gallery-anime-and-manga.md`](references/gallery-anime-and-manga.md)

### 일러스트
선·색면·질감·장식이 하나의 작품처럼 균형 잡힌 화면.
> **빈티지 아말피 해안 여행 포스터** (@WolfRiccardo): "Modern pencil illustration of a vintage travel poster of the Amalfi Coast … 1960s white car on a curved seaside road, deep blue Mediterranean, pastel hillside village …"
> 전체: [`references/gallery-illustration.md`](references/gallery-illustration.md)

### 게임
플레이 공간·유닛 위치·지형·장르 규칙이 보이는 화면.
> **Hitman 게임 화면 — OpenAI 본사** (@flowersslop): "A Hitman level where you are in the OpenAI HQ and your mission is to steal GPT-6 without getting caught."
> 전체: [`references/gallery-gaming.md`](references/gallery-gaming.md)

### 시네마틱
피사체·배경·빛·카메라·긴장점이 분명한 영화 한 장면.
> **픽사 스타일 3D 애니 스틸** (16:9): "A Pixar-quality 3D animation still … a cozy apartment kitchen at dawn, a small orange tabby kitten reaching a paw toward a rising soufflé, oven glow lighting the scene …"
> 전체: [`references/gallery-cinematic-and-animation.md`](references/gallery-cinematic-and-animation.md)

### 포스터
제목·부제·대표 이미지·여백의 위계가 멀리서도 읽히는 편집 디자인.
> **중국풍 차 브랜드 출시 포스터** (3:4): "Design a 3:4 vertical poster for a new Chinese tea launch … dark green, off-white and gold palette, rice-paper texture, elegant negative space, modern layout …"
> 전체: [`references/gallery-typography-and-posters.md`](references/gallery-typography-and-posters.md)

### 제품 · 브랜드
형태·소재·라벨·패키지가 제품을 중심으로 정리된 광고 마감.
> **다이라인에서 만든 3D 제품 박스** (@Salmaaboukarr): "Assemble the dieline into a flawless 3D box with accurate panels, clean folds, undistorted type … minimal premium studio, diffused light, matte paperboard texture … front reads \"AURAE / COLD-BREW MATCHA / 12 fl oz\"."
> 전체: [`references/gallery-product-and-food.md`](references/gallery-product-and-food.md)

### 인물 사진
인물·의상·소품·카메라 거리가 실제 촬영처럼 정리된 화면.
> **RAW 아이폰 촬영 — 42번가 지하철** (@WolfRiccardo): "A completely RAW, unprocessed image with full iPhone camera quality. A subway station, the subway in motion with a momentary blur, an elderly woman and man in front …"
> 전체: [`references/gallery-photography.md`](references/gallery-photography.md)

### 건물 사진
규모·입구·동선·재료가 실제 사용성을 갖는 건축 시각화.
> **일본식 미니멀 거실** (28mm 시점): "Render a serene Japanese minimalist living room in photorealistic architectural visualization … light oak flooring, shoji-inspired sliding panels, low modular seating, a recessed tokonoma niche …"
> 전체: [`references/gallery-architecture-and-interior.md`](references/gallery-architecture-and-interior.md)

### 인포그래픽
제목·번호 단계·라벨·아이콘·그래프가 읽기 쉬운 순서로 정리된 설명 자료.
> **송나라 SNS 피드** (@Panda20230902): "\"SONG DYNASTY SOCIAL MEDIA FEED\" … a mobile social media interface, but the content is entirely Song Dynasty scenes, the avatar a Song-era portrait …"
> 전체: [`references/gallery-infographics-and-field-guides.md`](references/gallery-infographics-and-field-guides.md)

### UI·대시보드
상단 바·카드·그래프·버튼이 실제 제품 화면처럼 정렬된 목업.
> **모바일 가계부 앱 목업** (1290×2796): "Design a polished mobile finance app UI for a fictional neobank called AURAE … calm palette of deep navy, mint green, warm gray and white, a complete home screen …"
> 전체: [`references/gallery-ui-ux-mockups.md`](references/gallery-ui-ux-mockups.md)

전체 카테고리 라우팅 인덱스는 [`references/gallery.md`](references/gallery.md)에 있습니다.

## 번들 스킬로 프롬프트 설계하기

`SKILL.md`는 AI 에이전트(Claude Code 등)가 위 7원칙으로 프롬프트를 설계하게 하는 실행 규칙입니다. 스킬을 지원하는 환경에서 이미지 프롬프트 요청이 들어오면, 에이전트가 다음을 수행합니다.

1. 요청을 10개 카테고리 중 하나로 분류
2. 1차로 `docs/js/gallery-data.js`의 사이트 실제 갤러리 예시(한국어 100개)를 찾아 참고하고, 세부 기법이 더 필요하면 2차로 `references/gallery.md`가 가리키는 해당 카테고리 파일을 로딩
3. 7블록으로 프롬프트를 조립하고 정본 필드 어휘로 정밀화
4. 이미지 속 글자·다이어그램·UI는 `references/craft.md` 규칙으로 보정
5. 품질 체크리스트를 통과할 때까지 다듬어 복사용 프롬프트로 전달

프롬프트 작성 자체에는 외부 도구가 필요 없습니다. 실제 이미지 생성은 선택 사항이며, 호스트의 이미지 생성 도구나 `scripts/generate.py`(+ `OPENAI_API_KEY`)로 실행할 수 있습니다. API 호출은 과금될 수 있습니다.

## 로컬에서 보기

정적 사이트라 빌드가 필요 없습니다.

```bash
cd docs && python3 -m http.server 8000
# 브라우저에서 http://localhost:8000
```

갤러리 데이터를 다시 생성하려면(레퍼런스를 추가·수정한 경우):

```bash
cd docs && node js/build-gallery-data.mjs   # ../references/gallery-*.md → js/gallery-data.js
```

## 프로젝트 구조

사이트(`docs/`)와 번들 스킬(`SKILL.md`, `references/`, `scripts/`)이 분리되어 있습니다. GitHub Pages를 `docs/` 폴더에서 배포하도록 설정하면 사이트만 서빙되고, 스킬은 프로젝트 루트에서 그대로 로드됩니다. 사이트의 "MD 다운로드" 링크는 GitHub 원본 URL(`raw.githubusercontent.com`)을 가리켜, 레퍼런스가 사이트 배포본 밖에 있어도 항상 접근됩니다.

```
.
├── README.md
├── SKILL.md                       # 번들 스킬 (7원칙 프롬프트 설계 규칙)
├── references/                    # 레퍼런스 라이브러리 (gallery-*.md, craft.md, openai-cookbook.md)
├── scripts/generate.py            # (선택) 이미지 생성 CLI 런처
└── docs/                          # GitHub Pages 배포 소스
    ├── index.html                 # 가이드 사이트 (원칙 · 빌더 · 갤러리)
    ├── css/styles.css
    ├── js/
    │   ├── script.js              # 7원칙 데이터, 빌더, 갤러리 렌더링
    │   ├── gallery-data.js        # 빌드 산출물 (갤러리 데이터)
    │   └── build-gallery-data.mjs # ../references → gallery-data.js 빌더
    └── assets/                    # 로고, 원칙 예시 이미지, 갤러리 이미지
```

## 크레딧

레퍼런스 갤러리의 각 프롬프트에는 원저자와 출처(X 등)가 `references/gallery-*.md`에 표기되어 있습니다. `Curated` 표기는 가이드용으로 정리한 예시입니다.

© 2026 AIROASTING. All rights reserved.
