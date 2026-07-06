#!/usr/bin/env python3
"""RUBRIC.md 채점용 표본 선정기.

`docs/js/gallery-data.js`가 정본이다. 이 스크립트는 그 안의 JSON 배열만 뽑아
카테고리별 표본을 골라 `experiments/_work/sample.json`으로 저장한다.

기본 전략은 `middle`이다. 각 카테고리 항목 수가 10개라면 0-based index 5,
즉 ref-6, ref-16 ... ref-96이 선택된다. 결정적 선택이라 누가 돌려도 같은
표본이 나온다.
"""
import argparse
import json
import os
import sys

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


def group_by_category(data):
    by = {}
    for d in data:
        for key in ("id", "category", "title", "image", "metadata", "prompt"):
            if key not in d:
                raise KeyError(f"gallery-data.js 항목에 필수 키가 없음: {key}")
        by.setdefault(d["category"], []).append(d)

    missing = [c for c in ORDER if c not in by]
    if missing:
        raise KeyError(f"gallery-data.js에 없는 카테고리: {missing}")

    extra = sorted(set(by) - set(ORDER))
    if extra:
        raise KeyError(f"ORDER에 없는 카테고리: {extra}")

    return by


def pick_index(items, strategy):
    if strategy == "first":
        return 0
    if strategy == "last":
        return len(items) - 1
    if strategy == "middle":
        return len(items) // 2
    raise ValueError(f"알 수 없는 전략: {strategy}")


def pick_sample(data, strategy="middle", expected_per_category=10):
    """카테고리별 표본 1개를 결정적으로 고른다."""
    by = group_by_category(data)
    sample = []
    for c in ORDER:
        items = by[c]
        if expected_per_category and len(items) != expected_per_category:
            raise ValueError(
                f"{c} 항목 수가 {expected_per_category}개가 아님: {len(items)}개"
            )
        index = pick_index(items, strategy)
        d = items[index]
        sample.append({
            "id": d["id"],
            "category": c,
            "category_count": len(items),
            "selected_index": index,
            "selection_strategy": strategy,
            "title": d["title"],
            "image": d["image"].lstrip("./"),
            "metadata": d["metadata"],
            "prompt": d["prompt"],
        })
    return sample


def parse_args(argv):
    parser = argparse.ArgumentParser(description="갤러리 채점 표본을 결정적으로 선정한다.")
    parser.add_argument("--strategy", choices=("first", "middle", "last"), default="middle")
    parser.add_argument("--output", default=OUT, help="표본 JSON 출력 경로")
    parser.add_argument(
        "--expected-per-category",
        type=int,
        default=10,
        help="카테고리별 기대 항목 수. 0이면 검사하지 않음",
    )
    parser.add_argument("--dry-run", action="store_true", help="파일을 쓰지 않고 표본만 출력")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv or sys.argv[1:])
    data = load_references(DATA_JS)
    sample = pick_sample(data, args.strategy, args.expected_per_category)

    output = os.path.abspath(args.output)
    os.makedirs(OUT_DIR, exist_ok=True)
    if not args.dry_run:
        os.makedirs(os.path.dirname(output), exist_ok=True)
        with open(output, "w", encoding="utf-8") as f:
            json.dump(sample, f, ensure_ascii=False, indent=2)

    target = "(dry-run)" if args.dry_run else os.path.relpath(output, ROOT)
    print(f"표본 {len(sample)}개 → {target}")
    for s in sample:
        print(
            f'  {s["id"]:8} {s["category"]} '
            f'(index {s["selected_index"]}/{s["category_count"] - 1}, {s["selection_strategy"]})'
        )


if __name__ == "__main__":
    main()
