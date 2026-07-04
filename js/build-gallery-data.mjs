import { readFileSync, writeFileSync, readdirSync } from "node:fs";
import { basename, join } from "node:path";

// 갤러리 데이터 생성기.
//
// 번호(number)와 id 규칙 (사이트와 통일):
//   - number : 전역 순번 1..N. 파일 정렬 순서 + 파일 내 문서 순서를 따라 매긴다.
//   - id     : `ref-<number>`. 카드에 보이는 번호와 URL 해시(#reference-ref-<number>)가
//              항상 일치하도록 number에서 직접 파생한다.
// 소스 마크다운의 `### No. N`(파일별 번호)은 순서 판단에만 쓰고, 최종 number/id에는 쓰지 않는다.
// 과거 버그: id/number를 파일별 No.로 넣고 그 값으로 정렬해 전역 순번과 어긋났다. 아래는 그걸 제거한 버전.
//
// 주의: category 값은 각 마크다운의 `# 제목` 헤딩에서 가져온다. 현재 배포된 gallery-data.js는
// 한국어 카테고리(웹툰, 일러스트 등)로 재매핑된 수작업 큐레이션본이므로, 이 스크립트로 재생성하면
// 카테고리 이름과 구성이 달라질 수 있다. number/id 일관성만 보장한다.

// 루트에 복사된 gpt-image 폴더 기준 (프로젝트 루트에서 `node js/build-gallery-data.mjs`로 실행).
const referencesDir = "./gpt-image/references";
const files = readdirSync(referencesDir)
  .filter((file) => file.startsWith("gallery-") && file.endsWith(".md"))
  .sort();

const collected = [];

for (const file of files) {
  const markdown = readFileSync(join(referencesDir, file), "utf8");
  const category = markdown.match(/^#\s+(.+)$/m)?.[1].trim() ?? basename(file, ".md");
  const entryRegex =
    /### No\. (\d+) · ([\s\S]*?)(?=\n### No\. \d+ · |\s*$)/g;

  for (const match of markdown.matchAll(entryRegex)) {
    const block = match[2].trim();
    const title = block.split("\n")[0].trim();
    const image = block.match(/- Image:\s+`([^`]+)`/)?.[1] ?? "";
    const metadata = block.match(/- Metadata:\s+(.+)/)?.[1].trim() ?? "";
    const prompt = block.match(/```text\n([\s\S]*?)\n```/)?.[1].trim() ?? "";
    const alt = block.match(/alt="([^"]+)"/)?.[1] ?? title;

    collected.push({
      title,
      category,
      categoryFile: file,
      image: `../GPT-Image2-Skill/${image}`,
      alt,
      metadata,
      prompt,
    });
  }
}

// 전역 순번을 부여하고 id를 그 번호에서 파생한다.
const entries = collected.map((entry, index) => {
  const number = index + 1;
  return { id: `ref-${number}`, number, ...entry };
});

const out = `window.GALLERY_REFERENCES = ${JSON.stringify(entries, null, 2)};\n`;
writeFileSync("./js/gallery-data.js", out);

console.log(`Wrote ${entries.length} gallery references to js/gallery-data.js`);
