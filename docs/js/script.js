const promptBlueprints = {
  "game": {
    artifact: "게임 콘셉트 이미지 또는 게임 화면",
    structure: "플레이어가 보는 공간, 캐릭터 또는 유닛의 위치, 지형, 인터페이스 요소, 장르의 규칙이 분명하게 보이는 화면 구성",
    style: "게임 키아트 또는 인게임 화면처럼 강한 실루엣, 명확한 플레이 상황, 깊이 있는 배경, 장르에 맞는 시각 언어를 사용합니다.",
  },
  "cinematic-storyboard": {
    artifact: "시네마틱 장면 또는 스토리보드 컷",
    structure: "영화의 한 장면처럼 주 피사체, 배경, 빛, 카메라 시점, 사건의 긴장점이 분명한 화면 구성",
    style: "시네마틱 컬러, 장면 중심 연출, 자연스러운 질감, 감정이 드러나는 조명, 이야기의 단서가 보이는 화면으로 만듭니다.",
  },
  "posters-typography": {
    artifact: "포스터 또는 타이포그래피 중심 그래픽",
    structure: "제목, 부제, 대표 이미지, 여백, 정보 영역의 위계가 분명하고 멀리서도 핵심 문구가 읽히는 화면 구성",
    style: "편집 디자인과 인쇄 포스터의 완성도를 우선합니다. 글자 크기, 자간, 행간, 색 대비, 종이 질감이 정돈되어야 합니다.",
  },
  "illustration-character": {
    artifact: "일러스트 또는 캐릭터 중심 이미지",
    structure: "주 피사체, 캐릭터성, 배경, 장식 요소, 색상, 질감이 하나의 작품처럼 균형 있게 배치된 화면 구성",
    style: "선화, 채색, 회화, 수채화, 픽셀 아트, 스티커, 문신 도안처럼 선택한 매체의 질감과 개성을 분명히 보여줍니다.",
  },
  "space-architecture": {
    artifact: "건물 사진 또는 공간 이미지",
    structure: "건물의 규모, 입구, 중심 구역, 이동 경로, 가구나 안내 요소의 위치가 실제 사용성을 갖는 화면 구성",
    style: "건축 사진, 건축 시각화, 실내 렌더, 전시 공간처럼 재료와 구조가 읽히는 실무형 표현을 사용합니다.",
  },
  "product-brand": {
    artifact: "제품 이미지 또는 브랜드 비주얼",
    structure: "제품의 형태, 소재, 라벨, 패키지, 사용 장면, 보조 소품이 제품을 중심으로 정리된 화면 구성",
    style: "상업 광고 사진, 제품 렌더, 브랜드 무드 이미지처럼 재질, 반사, 그림자, 라벨의 위치가 정확한 마감을 사용합니다.",
  },
  "photo-fashion": {
    artifact: "인물 사진 또는 패션 화보",
    structure: "인물, 의상, 소품, 장소, 카메라 거리, 배경 초점이 실제 촬영처럼 자연스럽게 정리된 화면 구성",
    style: "패션 에디토리얼, 거리 사진, 스튜디오 초상, 라이프스타일 사진처럼 카메라 질감과 현실적인 빛을 우선합니다.",
  },
  "infographic-education": {
    artifact: "인포그래픽 또는 설명형 시각 자료",
    structure: "제목, 대표 이미지, 번호 단계, 라벨, 아이콘, 그래프, 화살표, 설명 박스가 읽기 쉬운 순서로 정리된 화면 구성",
    style: "필드 가이드, 안내 포스터, 기술 다이어그램, 데이터 비교표처럼 정보 위계가 선명하고 장식보다 이해가 먼저 보이는 디자인을 사용합니다.",
  },
  "research-technical-diagram": {
    artifact: "논문 그림 또는 기술 도표",
    structure: "블록, 화살표, 라벨, 범례, 그래프, 부품, 단계가 논리적으로 연결된 설명형 화면 구성",
    style: "학술 논문용 벡터 도표, 기술 일러스트, 구조도처럼 선 두께와 색상 의미가 일정하고 복잡한 정보도 분리되어 보여야 합니다.",
  },
  "interface-data": {
    artifact: "UI 화면 또는 데이터 대시보드",
    structure: "상단 바, 메뉴, 카드, 그래프, 표, 버튼, 범례, 데이터 영역이 실제 제품 화면처럼 정렬된 화면 구성",
    style: "실무형 UI와 데이터 대시보드처럼 가독성, 정렬, 간격, 색상 의미, 조작 가능한 화면의 현실감을 우선합니다.",
  },
};

const detailGuides = {
  final:
    "최종 결과물로 사용할 이미지처럼 완성도를 높여주세요. 글자 가독성, 구도, 색감, 디테일의 일관성을 우선합니다.",
  exploration:
    "아이디어 탐색용 이미지처럼 콘셉트를 분명하게 보여주세요. 완벽한 마감보다 다양한 시각적 가능성과 분위기 실험을 허용합니다.",
  "text-heavy":
    "이미지 안의 문구가 중요합니다. 따옴표 안의 텍스트를 정확하고 선명하게, 충분히 큰 크기로 표현해주세요. 깨진 글자나 의미 없는 문자를 피합니다.",
  "reference-edit":
    "레퍼런스 이미지를 함께 사용할 경우, 따로 바꾸라고 한 부분을 제외하고 인물/제품의 정체성, 구도, 조명 방향, 중요한 디테일을 유지해주세요.",
};

const styleGuides = {
  "category-default": null,
  photoreal:
    "실사 사진 매체로 표현합니다. 실제 카메라로 촬영한 듯한 질감, 자연스러운 그림자, 현실적인 배경 깊이를 우선합니다.",
  "product-render":
    "3D 제품 렌더 매체로 표현합니다. 표면 재질, 반사, 형태의 정확성, 광고 이미지처럼 정돈된 마감을 우선합니다.",
  "editorial-poster":
    "포스터/편집 디자인 매체로 표현합니다. 명확한 시각 위계, 넉넉한 여백, 인쇄물 같은 완성도를 우선합니다.",
  illustrated:
    "일러스트레이션 매체로 표현합니다. 선, 색면, 질감, 장식 요소가 주제와 조화되도록 구성합니다.",
  "watercolor-style":
    "수채화 매체로 표현합니다. 종이 질감, 투명한 색감, 자연스러운 번짐, 부드러운 붓터치를 우선합니다.",
  "pixel-style":
    "픽셀 아트 매체로 표현합니다. 제한된 팔레트, 또렷한 실루엣, 작은 해상도에서도 읽히는 형태를 우선합니다.",
  "cinematic-style":
    "시네마틱 장면 매체로 표현합니다. 영화의 한 프레임처럼 빛, 색, 공간감, 인물 또는 피사체의 존재감을 구성합니다.",
};

const lightingGuides = {
  "soft-studio":
    "부드러운 스튜디오 조명. 그림자는 너무 강하지 않게 처리하고, 피사체의 질감과 형태가 고르게 보이도록 합니다.",
  "golden-hour":
    "골든아워 자연광. 따뜻한 햇빛, 긴 그림자, 부드러운 역광을 활용해 감성적이고 생동감 있는 분위기를 만듭니다.",
  "dramatic-rim":
    "극적인 림 라이트. 피사체 가장자리에 선명한 빛의 윤곽을 만들고, 배경과 주 피사체가 강하게 분리되도록 합니다.",
  "neon-night":
    "네온 야간 조명. 색이 있는 간판빛, 반사광, 젖은 표면의 빛 번짐을 활용해 도시적이고 선명한 분위기를 만듭니다.",
  overcast:
    "흐린 날의 확산광. 그림자를 부드럽게 줄이고 색과 형태가 차분하게 보이도록 합니다.",
  "low-key":
    "로우키 조명. 어두운 배경과 제한된 하이라이트를 사용해 깊이감 있고 긴장감 있는 장면을 만듭니다.",
};

const cameraGuides = {
  "front-view":
    "정면 보기. 피사체를 카메라 정면에 두고 안정적이고 명확한 구도로 구성합니다.",
  "extreme-close-up":
    "극단적 클로즈업. 눈, 질감, 로고, 재료처럼 아주 작은 디테일이 화면 대부분을 차지하도록 가까이 잡습니다.",
  fisheye:
    "어안 렌즈. 둥글게 왜곡되는 광각 렌즈 느낌을 사용해 공간감과 독특한 원형 프레임을 강조합니다.",
  "extreme-wide":
    "극단적 와이드. 피사체보다 주변 환경과 스케일이 크게 보이도록 아주 넓은 장면으로 구성합니다.",
  "face-close-up":
    "얼굴 클로즈업. 얼굴이 화면의 중심이 되도록 가까이 잡고 표정, 피부 질감, 눈빛이 잘 보이게 합니다.",
  "high-angle":
    "높은 앵글. 카메라를 위쪽에 두고 아래를 내려다보는 시점으로, 피사체의 형태와 주변 배치가 잘 보이게 합니다.",
  "low-angle":
    "낮은 앵글. 카메라를 아래쪽에 두고 피사체를 올려다보게 구성해 더 크고 인상적으로 보이게 합니다.",
  "medium-shot":
    "미디엄 샷. 피사체의 상반신 또는 전신 일부와 주변 배경이 함께 보이도록 균형 있게 잡습니다.",
  "rear-view":
    "후면 보기. 피사체의 뒷모습을 중심으로 구성해 시선의 방향, 실루엣, 배경과의 관계를 강조합니다.",
  "side-view":
    "측면 보기. 피사체를 옆에서 바라보는 구도로 윤곽, 자세, 방향성을 분명하게 보여줍니다.",
  "dramatic-low-angle":
    "극단적 낮은 앵글. 영어로는 worm's-eye view에 가까운 시점입니다. 바닥 가까이에서 위를 올려다보며 피사체를 압도적이고 극적으로 표현합니다.",
};

const purposeLabels = {
  "game": "게임",
  "illustration-character": "일러스트",
  "cinematic-storyboard": "시네마틱",
  "posters-typography": "포스터",
  "product-brand": "제품 · 브랜드",
  "photo-fashion": "인물 사진",
  "space-architecture": "건물 사진",
  "infographic-education": "인포그래픽",
  "interface-data": "UI·대시보드",
};

const corePrinciples = [
  {
    title: "결과물 유형을 정하기",
    summary: "포스터, 인물 사진, UI, 인포그래픽처럼 결과물의 종류를 첫 줄에 고정합니다.",
    weak: "노란 텀블러가 있는 멋진 카페 느낌",
    strong: "선샤인 옐로우 세라믹 텀블러의 브랜드 출시용 3:4 세로형 제품 포스터. 제품이 중앙에 크게 보이는 인쇄물 스타일",
  },
  {
    title: "주 피사체를 고정하기",
    summary: "이미지의 중심이 되는 대상, 인물, 제품, 장면을 분명히 씁니다.",
    weak: "봄 카페 분위기, 꽃, 디저트, 음료, 따뜻한 햇살",
    strong: "선샤인 옐로우 세라믹 텀블러를 화면 중앙에 크게 배치. 뒤에는 봄꽃과 카페 배경을 부드럽게 흐리게 처리",
  },
  {
    title: "구도와 비율을 지정하기",
    summary: "화면 비율, 피사체 위치, 여백, 시점의 큰 틀을 정합니다.",
    weak: "노란 텀블러를 들고 여행 간 느낌. 적당히 예쁜 사진",
    strong: "16:9 가로형 와이드 제품 여행 사진. 노란 텀블러는 오른쪽 1/3 지점, 왼쪽에는 호수와 산맥의 넓은 여백",
  },
  {
    title: "맥락과 배경을 설명하기",
    summary: "어디에서, 어떤 상황에서, 어떤 분위기로 보일지 정합니다.",
    weak: "노란 텀블러를 좋은 분위기에서 보여주기",
    strong: "일요일 아침 주방 창가에서 쓰는 노란 텀블러. 반쯤 열린 노트, 커피 원두, 부드러운 아침 햇살로 차분한 루틴을 표현",
  },
  {
    title: "스타일과 매체를 선택하기",
    summary: "사진, 3D 렌더, 수채화, 포스터, 편집 디자인처럼 표현 방식을 정합니다.",
    weak: "노란 텀블러를 고급스럽게. 예쁘고 세련된 느낌",
    strong: "무광 세라믹 질감이 보이는 노란 텀블러의 고급 제품 렌더. 부드러운 스튜디오 조명, 석회석 받침대, 인디고 포인트",
  },
  {
    title: "빛과 디테일을 구체화하기",
    summary: "조명, 질감, 재료, 표면, 카메라 렌즈처럼 완성도를 좌우하는 요소를 씁니다.",
    weak: "노란 텀블러를 극적으로 찍기. 분위기 있게",
    strong: "노란 텀블러를 바닥 가까운 낮은 앵글로 촬영. 강한 림 라이트와 젖은 돌 바닥의 노란빛 반사를 사용",
  },
  {
    title: "정확성 조건을 덧붙이기",
    summary: "텍스트, 금지 요소, 유지해야 할 요소, 왜곡 방지 조건을 마지막에 씁니다.",
    weak: "노란 텀블러 포스터를 깔끔하게. 제목도 적당히 넣기",
    strong: "노란 텀블러 포스터. 제목은 \"Morning Solar\"로 정확히 표시. 로고, 깨진 글자, 뒤틀린 뚜껑은 피하기",
  },
];

const references = Array.isArray(window.GALLERY_REFERENCES) ? window.GALLERY_REFERENCES : [];
const galleryCategoryOrder = [
  "웹툰",
  "일러스트",
  "게임",
  "시네마틱",
  "포스터",
  "제품 · 브랜드",
  "인물 사진",
  "건물 사진",
  "인포그래픽",
  "UI·대시보드",
];
const galleryGrid = document.querySelector("#galleryGrid");
const galleryCategoryList = document.querySelector("#galleryCategoryList");
const galleryCount = document.querySelector("#galleryCount");
const galleryMore = document.querySelector("#galleryMore");
const galleryMoreButton = document.querySelector("#galleryMoreButton");
const GALLERY_PAGE_SIZE = 20;
const principleGrid = document.querySelector("#principleGrid");
const modal = document.querySelector("#promptModal");
const modalImage = document.querySelector("#modalImage");
const referenceDetail = document.querySelector("#referenceDetail");
const detailBackButton = document.querySelector("#detailBackButton");
const detailCategoryButton = document.querySelector("#detailCategoryButton");
const detailNumber = document.querySelector("#detailNumber");
const detailCategory = document.querySelector("#detailCategory");
const detailCategoryName = document.querySelector("#detailCategoryName");
const detailTitle = document.querySelector("#detailTitle");
const detailMeta = document.querySelector("#detailMeta");
const detailPrompt = document.querySelector("#detailPrompt");
const detailSourceLink = document.querySelector("#detailSourceLink");
const detailCopyButton = document.querySelector("#detailCopyButton");
const detailImage = document.querySelector("#detailImage");
const detailImageButton = document.querySelector("#detailImageButton");
let activePrompt = "";
let activeGalleryCategory = "all";
let activeReference = null;
let galleryScrollSpyFrame = null;
let galleryVisibleCount = GALLERY_PAGE_SIZE;

function buildCommand() {
  const purpose = document.querySelector("#purpose").value;
  const ratio = document.querySelector("#ratio").value;
  const detail = document.querySelector("#detail").value;
  const style = document.querySelector("#style").value;
  const lighting = document.querySelector("#lighting").value;
  const camera = document.querySelector("#camera").value;
  const subject = document.querySelector("#subject").value.trim();
  const context = document.querySelector("#context").value.trim();
  const blueprint = promptBlueprints[purpose];
  const detailGuide = detailGuides[detail];
  const styleGuide = styleGuides[style] || blueprint.style;
  const lightingGuide = lightingGuides[lighting];
  const cameraGuide = cameraGuides[camera];

  document.querySelector("#builtCode").textContent = `결과물 유형:
${blueprint.artifact}

주 피사체:
${subject}

구도와 비율:
${ratio}. ${blueprint.structure}

맥락과 배경:
${context}

스타일과 매체:
${styleGuide}

빛과 디테일:
${lightingGuide}
${cameraGuide}

정확성 조건:
${detailGuide}
따옴표 안의 문구는 철자와 띄어쓰기를 그대로 유지해주세요. 전체 이미지는 하나의 완성된 장면처럼 자연스럽고 구체적으로 보여야 합니다. 모호한 일반 표현, 왜곡된 타이포그래피, 불필요한 장식, 맞지 않는 조명은 피해주세요.`;
  syncBuilderHeight();
}

function syncBuilderHeight() {
  const form = document.querySelector(".builder-form");
  const output = document.querySelector(".generated-command");
  if (!form || !output) return;

  if (window.matchMedia("(max-width: 980px)").matches) {
    output.style.height = "";
    return;
  }

  output.style.height = `${form.offsetHeight}px`;
}

function renderPrinciples() {
  if (!principleGrid) return;

  principleGrid.replaceChildren();
  corePrinciples.forEach((principle, index) => {
    const card = document.createElement("article");
    card.className = "principle-card";

    const number = document.createElement("span");
    number.className = "number-pill";
    number.textContent = String(index + 1).padStart(2, "0");

    const title = document.createElement("h3");
    title.textContent = principle.title;

    const summary = document.createElement("p");
    summary.textContent = principle.summary;

    const examples = document.createElement("div");
    examples.className = "example-pair";

    const weak = createExampleFigure("weak", index, "안 좋은 예", principle.weak);
    const strong = createExampleFigure("strong", index, "좋은 프롬프트 예시", principle.strong);

    examples.append(weak, strong);
    card.append(number, title, summary, examples);
    principleGrid.append(card);
  });
}

function createExampleFigure(kind, index, label, text) {
  const figure = document.createElement("figure");
  figure.className = `example-figure ${kind}`;

  const image = document.createElement("img");
  image.src = `./assets/principles/principle-${String(index + 1).padStart(2, "0")}-${kind}.png`;
  image.alt = `${label}: ${text}`;
  image.loading = "lazy";

  const caption = document.createElement("figcaption");
  const captionLabel = document.createElement("strong");
  captionLabel.textContent = label;
  const captionText = document.createElement("span");
  captionText.textContent = text;
  caption.append(captionLabel, captionText);

  figure.append(image, caption);
  return figure;
}

document.querySelectorAll("#promptForm select, #promptForm input, #promptForm textarea").forEach((input) => {
  input.addEventListener("input", buildCommand);
});

function formatMetadata(text, item = null) {
  const itemCategoryParts = new Set(
    (item?.category || "")
      .split("·")
      .map((part) => part.trim())
      .filter(Boolean)
  );
  const categoryLabels = new Set([
    "Anime & Manga",
    "Gaming",
    "Retro & Cyberpunk",
    "Cinematic & Animation",
    "Cinematic Animation",
    "Character Design",
    "Typography & Posters",
    "Illustration",
    "Watercolor",
    "Pixel Art",
    "Isometric",
    "Product & Food",
    "Brand Systems & Identity",
    "Photography",
    "Infographics & Field Guides",
    "Research Paper Figures",
    "Official OpenAI Cookbook",
    "Edit Endpoint Showcase",
    "UI/UX Mockups",
    "Data Visualization",
    "Technical Illustration",
    "Architecture & Interior",
    "Scientific & Educational",
    "Fashion Editorial",
    "Fine Art Painting",
    "More Illustration Styles",
    "Cinematic Film References",
    "Beauty & Lifestyle",
    "Events & Experience",
    "Tattoo Design",
    "Screen Photography"
  ]);
  const termMap = {
    landscape: "가로형",
    portrait: "세로형",
    square: "정사각형",
    tall: "긴 세로형",
    panoramic: "파노라마형",
    wide: "와이드",
  };
  return text
    .replaceAll("`", "")
    .split("·")
    .map((part) => part.trim())
    .filter((part) => part && !categoryLabels.has(part) && part !== item?.category && !itemCategoryParts.has(part))
    .map((part) => termMap[part] || part)
    .join(" · ");
}

function populateCategories() {
  if (!galleryCategoryList) return;

  galleryCategoryList.replaceChildren();
  const categorySet = new Set(references.map((item) => item.category));
  const orderedCategories = [
    ...galleryCategoryOrder.filter((category) => categorySet.has(category)),
    ...[...categorySet].filter((category) => !galleryCategoryOrder.includes(category)),
  ];
  const categories = ["all", ...orderedCategories];
  galleryCategoryList.style.gridTemplateColumns = `repeat(${categories.length}, minmax(0, 1fr))`;
  const counts = new Map();
  references.forEach((item) => {
    counts.set(item.category, (counts.get(item.category) || 0) + 1);
  });
  counts.set("all", references.length);

  categories.forEach((category) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "category-chip";
    button.dataset.category = category;
    button.setAttribute("aria-pressed", category === activeGalleryCategory ? "true" : "false");

    const label = document.createElement("span");
    label.textContent = category === "all" ? "전체" : category;

    const count = document.createElement("span");
    count.className = "count-pill";
    count.textContent = counts.get(category).toLocaleString("ko-KR");

    button.append(label, count);
    button.addEventListener("click", () => {
      activeGalleryCategory = category;
      galleryVisibleCount = GALLERY_PAGE_SIZE;
      renderGallery();
      scrollToGalleryCategoryTop("instant");
      window.requestAnimationFrame(() => scrollToGalleryCategoryTop("instant"));
    });
    galleryCategoryList.append(button);
  });
}

function updateGalleryCategorySelection(category) {
  galleryCategoryList?.querySelectorAll(".category-chip").forEach((button) => {
    const isActive = button.dataset.category === category;
    button.setAttribute("aria-pressed", isActive ? "true" : "false");
  });
}

function scrollToGalleryCategoryTop(behavior = "smooth") {
  const target = galleryGrid || document.querySelector("#gallery");
  if (!target) return;

  const topbarHeight = document.querySelector(".topbar")?.offsetHeight || 0;
  const toolsHeight = document.querySelector(".gallery-tools")?.offsetHeight || 0;
  const offset = topbarHeight + toolsHeight + 14;
  const top = target.getBoundingClientRect().top + window.scrollY - offset;

  if (behavior === "instant") {
    const originalScrollBehavior = document.documentElement.style.scrollBehavior;
    document.documentElement.style.scrollBehavior = "auto";
    window.scrollTo(0, Math.max(0, top));
    document.documentElement.style.scrollBehavior = originalScrollBehavior;
    return;
  }

  window.scrollTo({ top: Math.max(0, top), behavior });
}

function scrollToGallerySection(behavior = "smooth") {
  const target = document.querySelector("#gallery");
  if (!target) return;

  const topbarHeight = document.querySelector(".topbar")?.offsetHeight || 0;
  const top = target.getBoundingClientRect().top + window.scrollY - topbarHeight - 12;

  if (behavior === "instant") {
    const originalScrollBehavior = document.documentElement.style.scrollBehavior;
    document.documentElement.style.scrollBehavior = "auto";
    window.scrollTo(0, Math.max(0, top));
    document.documentElement.style.scrollBehavior = originalScrollBehavior;
    return;
  }

  window.scrollTo({ top: Math.max(0, top), behavior });
}

function getDisplayNumber(item) {
  const index = references.indexOf(item);
  return index >= 0 ? index + 1 : item.number;
}

function formatDisplayNumber(item) {
  return String(getDisplayNumber(item)).padStart(2, "0");
}

function createGalleryCard(item) {
  const card = document.createElement("button");
  card.type = "button";
  card.className = "gallery-card";
  card.dataset.referenceId = item.id;
  card.dataset.category = item.category;

  const image = document.createElement("img");
  image.src = item.image;
  image.alt = item.alt || item.title;
  image.loading = "lazy";

  const content = document.createElement("div");
  const number = document.createElement("span");
  number.className = "number-pill ref-number";
  number.textContent = formatDisplayNumber(item);

  const title = document.createElement("h3");
  title.textContent = item.title;

  const meta = document.createElement("p");
  meta.textContent = formatMetadata(item.metadata || item.category, item);

  content.append(number, title, meta);
  card.append(image, content);
  card.addEventListener("click", () => openReferencePage(item, true));
  return card;
}

function renderGallery() {
  if (!galleryGrid) return;

  const category = activeGalleryCategory;
  const filtered = references.filter((item) => {
    return category === "all" || item.category === category;
  });

  const visibleCount = Math.min(galleryVisibleCount, filtered.length);
  const visible = filtered.slice(0, visibleCount);

  galleryGrid.replaceChildren();
  visible.forEach((item) => galleryGrid.append(createGalleryCard(item)));

  if (filtered.length === 0) {
    const empty = document.createElement("div");
    empty.className = "empty-gallery";
    empty.textContent = "표시할 레퍼런스가 없습니다.";
    galleryGrid.append(empty);
  }

  if (galleryCount) {
    galleryCount.textContent = `${filtered.length.toLocaleString("ko-KR")}개 레퍼런스`;
  }

  updateGalleryMore(filtered.length, visibleCount);
  updateGalleryCategorySelection(activeGalleryCategory);
}

function updateGalleryMore(total, shown) {
  if (!galleryMore || !galleryMoreButton) return;
  const remaining = total - shown;
  if (remaining > 0) {
    const nextBatch = Math.min(GALLERY_PAGE_SIZE, remaining);
    galleryMoreButton.textContent = `더 보기 (${nextBatch}개 더, 남은 ${remaining.toLocaleString("ko-KR")}개)`;
    galleryMore.hidden = false;
  } else {
    galleryMore.hidden = true;
  }
}

function showMoreGallery() {
  const category = activeGalleryCategory;
  const total = references.filter(
    (item) => category === "all" || item.category === category,
  ).length;
  galleryVisibleCount = Math.min(galleryVisibleCount + GALLERY_PAGE_SIZE, total);
  renderGallery();
}

function updateGallerySelectionByScroll() {
  galleryScrollSpyFrame = null;
  if (!galleryGrid || !galleryCategoryList || activeGalleryCategory !== "all") return;
  if (document.body.classList.contains("reference-detail-open")) return;

  const cards = [...galleryGrid.querySelectorAll(".gallery-card")];
  if (!cards.length) {
    updateGalleryCategorySelection("all");
    return;
  }

  const topbarHeight = document.querySelector(".topbar")?.offsetHeight || 0;
  const toolsHeight = document.querySelector(".gallery-tools")?.offsetHeight || 0;
  const markerY = window.scrollY + topbarHeight + toolsHeight + 36;
  let currentCategory = cards[0].getBoundingClientRect().top < window.innerHeight
    ? cards[0].dataset.category || "all"
    : "all";
  const seenCategories = new Set();

  for (const card of cards) {
    const category = card.dataset.category || "all";
    if (seenCategories.has(category)) continue;
    seenCategories.add(category);

    const cardTop = card.getBoundingClientRect().top + window.scrollY;
    if (cardTop <= markerY) {
      currentCategory = category;
    } else {
      break;
    }
  }

  updateGalleryCategorySelection(currentCategory);
}

function scheduleGalleryScrollSpy() {
  if (galleryScrollSpyFrame !== null) return;
  galleryScrollSpyFrame = window.requestAnimationFrame(updateGallerySelectionByScroll);
}

function openReferencePage(item, updateHash = false) {
  if (!referenceDetail || !item) return;

  activeReference = item;
  activePrompt = item.prompt || "";

  detailNumber.textContent = formatDisplayNumber(item);
  detailCategory.textContent = item.category;
  detailCategoryButton.textContent = item.category;
  detailCategoryName.textContent = item.category;
  detailTitle.textContent = item.title;
  detailMeta.textContent = formatMetadata(item.metadata || "", item);
  detailPrompt.textContent = activePrompt;
  detailImage.src = item.image;
  detailImage.alt = item.alt || item.title;

  if (item.categoryFile) {
    detailSourceLink.hidden = false;
    detailSourceLink.href = `./references/${item.categoryFile}`;
  } else {
    detailSourceLink.hidden = true;
    detailSourceLink.removeAttribute("href");
  }

  referenceDetail.hidden = false;
  document.body.classList.add("reference-detail-open");
  detailCopyButton.textContent = "프롬프트 복사";
  if (updateHash) {
    history.pushState(null, "", `#reference-${item.id}`);
  }
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function closeReferencePage({ scroll = true, behavior = "smooth" } = {}) {
  if (!referenceDetail) return;
  referenceDetail.hidden = true;
  document.body.classList.remove("reference-detail-open");
  activeReference = null;
  activePrompt = "";
  if (location.hash.startsWith("#reference-")) {
    history.pushState(null, "", "#gallery");
  }
  if (scroll) {
    scrollToGallerySection(behavior);
  }
}

function closeReferenceToCategory() {
  if (!activeReference) return;
  activeGalleryCategory = activeReference.category;
  galleryVisibleCount = GALLERY_PAGE_SIZE;
  renderGallery();
  closeReferencePage({ scroll: false });
  scrollToGalleryCategoryTop("instant");
}

function openImageModal() {
  if (!modal || !modalImage || !activeReference) return;
  modalImage.src = activeReference.image;
  modalImage.alt = activeReference.alt || activeReference.title;
  modal.classList.add("open");
  modal.setAttribute("aria-hidden", "false");
  document.body.classList.add("modal-locked");
}

function hideReferencePage() {
  if (!referenceDetail) return;
  referenceDetail.hidden = true;
  document.body.classList.remove("reference-detail-open");
  activeReference = null;
  activePrompt = "";
}

function closeModal() {
  if (!modal) return;
  modal.classList.remove("open");
  modal.setAttribute("aria-hidden", "true");
  document.body.classList.remove("modal-locked");
}

document.querySelectorAll("[data-close-modal]").forEach((button) => {
  button.addEventListener("click", closeModal);
});

detailBackButton?.addEventListener("click", () => closeReferencePage({ behavior: "instant" }));
detailCategoryButton?.addEventListener("click", closeReferenceToCategory);
detailImageButton?.addEventListener("click", openImageModal);

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && modal?.classList.contains("open")) {
    closeModal();
  }
});

detailCopyButton?.addEventListener("click", async () => {
  await navigator.clipboard.writeText(activePrompt);
  detailCopyButton.textContent = "복사 완료";
  detailCopyButton.classList.add("copied");
  window.setTimeout(() => {
    detailCopyButton.textContent = "프롬프트 복사";
    detailCopyButton.classList.remove("copied");
  }, 1200);
});

function openReferenceFromHash() {
  if (!location.hash.startsWith("#reference-")) {
    hideReferencePage();
    return;
  }

  const referenceId = location.hash.replace("#reference-", "");
  const item = references.find((reference) => reference.id === referenceId);
  if (item) {
    openReferencePage(item, false);
  }
}

document.querySelectorAll(".copy-button").forEach((button) => {
  button.addEventListener("click", async () => {
    const target = document.querySelector(`#${button.dataset.copyTarget}`);
    if (!target) return;

    await navigator.clipboard.writeText(target.textContent);
    const original = button.textContent;
    button.textContent = "완료";
    button.classList.add("copied");
    window.setTimeout(() => {
      button.textContent = original;
      button.classList.remove("copied");
    }, 1200);
  });
});

if (galleryMoreButton) {
  galleryMoreButton.addEventListener("click", showMoreGallery);
}

buildCommand();
renderPrinciples();
populateCategories();
renderGallery();
scheduleGalleryScrollSpy();
openReferenceFromHash();
syncBuilderHeight();

window.addEventListener("scroll", scheduleGalleryScrollSpy, { passive: true });
window.addEventListener("resize", syncBuilderHeight);
window.addEventListener("hashchange", openReferenceFromHash);
