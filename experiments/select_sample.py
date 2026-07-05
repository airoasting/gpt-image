#!/usr/bin/env python3
"""RUBRIC.md 채점용 표본 선정 (재현 가능): 카테고리당 중앙 항목 1개.

`docs/js/gallery-data.js`가 정본이다. 이 스크립트는 그 안의 JSON 배열만 뽑아
카테고리별 중앙 항목을 골라 `experiments/_work/sample.json`으로 저장한다.
선택이 결정적이라(중앙 인덱스 고정) 누가 돌려도 같은 10컷이 나온다.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_JS = os.path.join(ROOT, "docs/js/gallery-data.js")
OUT_DIR = os.path.join(ROOT, "experiments/_work")
OUT = os.path.join(OUT_DIR, "sample.json")

# 사이트 갤러리의 10개 카테고리 (gallery-data.js의 category 값과 일치해야 함)
ORDER = ["웹툰", "일러스트", "게임", "시네마틱", "포스터",
         "제품 · 브랜드", "인물 사진", "건물 사진", "인포그래픽", "UI·대시보드"]


def load_references(path):
    """gallery-data.js에서 JSON 배열만 견고하게 추출한다.

    `window.GALLERY_REFERENCES = [ ... ];` 형태라 대입 접두어나 끝의 세미콜론
    표기가 바뀌어도 깨지지 않도록, 첫 '['부터 마지막 ']'까지를 파싱한다.
    """
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    start = raw.find("[")
    end = raw.rfind("]")
    if start == -1 or end == -1 or end < start:
        raise ValueError(f"{path}에서 JSON 배열을 찾지 못했다.")
    return json.loads(raw[start:end + 1])


def pick_middle(data):
    """카테고리별 중앙 항목 1개를 결정적으로 고른다."""
    by = {}
    for d in data:
        by.setdefault(d["category"], []).append(d)

    missing = [c for c in ORDER if c not in by]
    if missing:
        raise KeyError(f"gallery-data.js에 없는 카테고리: {missing}")

    sample = []
    for c in ORDER:
        items = by[c]
        d = items[len(items) // 2]
        sample.append({
            "id": d["id"],
            "category": c,
            "title": d["title"],
            "image": d["image"].lstrip("./"),
            "metadata": d["metadata"],
            "prompt": d["prompt"],
        })
    return sample


def main():
    data = load_references(DATA_JS)
    sample = pick_middle(data)
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(sample, f, ensure_ascii=False, indent=2)
    print(f"표본 {len(sample)}개 → {os.path.relpath(OUT, ROOT)}")
    for s in sample:
        print(f'  {s["id"]:8} {s["category"]}')


if __name__ == "__main__":
    main()
