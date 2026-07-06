#!/usr/bin/env python3
"""Select deterministic samples for gallery scoring.

`docs/js/gallery-data.js` is the source of truth. This script extracts the
embedded JSON array, selects one sample per gallery category, and writes the
result to `experiments/_work/sample.json`.

The default strategy is `middle`. With 10 items per category, this selects
zero-based index 5, producing ref-6, ref-16, ..., ref-96. The selection is
deterministic so every reviewer evaluates the same sample set.
"""

import argparse
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_JS = os.path.join(ROOT, "docs/js/gallery-data.js")
OUT_DIR = os.path.join(ROOT, "experiments/_work")
OUT = os.path.join(OUT_DIR, "sample.json")

CATEGORY_FILES = [
    ("gallery-webtoon.md", "webtoon"),
    ("gallery-illustration.md", "illustration"),
    ("gallery-gaming.md", "gaming"),
    ("gallery-cinematic.md", "cinematic"),
    ("gallery-typography-and-posters.md", "posters"),
    ("gallery-product-and-brand.md", "product-and-brand"),
    ("gallery-photography.md", "photography"),
    ("gallery-architecture-and-interior.md", "architecture-and-interior"),
    ("gallery-infographics-and-field-guides.md", "infographics"),
    ("gallery-ui-ux-mockups.md", "ui-and-dashboard"),
]


def load_references(path):
    """Extract the JSON array from `gallery-data.js`."""
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    start = raw.find("[")
    end = raw.rfind("]")
    if start == -1 or end == -1 or end < start:
        raise ValueError(f"Cannot find a JSON array in {path}.")
    return json.loads(raw[start:end + 1])


def group_by_category_file(data):
    grouped = {}
    for item in data:
        for key in ("id", "categoryFile", "title", "image", "metadata", "prompt"):
            if key not in item:
                raise KeyError(f"gallery-data.js item is missing required key: {key}")
        grouped.setdefault(item["categoryFile"], []).append(item)

    expected_files = [category_file for category_file, _category in CATEGORY_FILES]
    missing = [category_file for category_file in expected_files if category_file not in grouped]
    if missing:
        raise KeyError(f"gallery-data.js is missing category files: {missing}")

    extra = sorted(set(grouped) - set(expected_files))
    if extra:
        raise KeyError(f"Unknown category files in gallery-data.js: {extra}")

    return grouped


def pick_index(items, strategy):
    if strategy == "first":
        return 0
    if strategy == "last":
        return len(items) - 1
    if strategy == "middle":
        return len(items) // 2
    raise ValueError(f"Unknown selection strategy: {strategy}")


def pick_sample(data, strategy="middle", expected_per_category=10):
    """Pick one deterministic sample from each gallery category."""
    grouped = group_by_category_file(data)
    sample = []
    for category_file, category in CATEGORY_FILES:
        items = grouped[category_file]
        if expected_per_category and len(items) != expected_per_category:
            raise ValueError(
                f"{category_file} has {len(items)} item(s), expected {expected_per_category}."
            )
        index = pick_index(items, strategy)
        item = items[index]
        sample.append({
            "id": item["id"],
            "category": category,
            "category_file": category_file,
            "category_count": len(items),
            "selected_index": index,
            "selection_strategy": strategy,
            "title": item["title"],
            "image": item["image"].lstrip("./"),
            "metadata": item["metadata"],
            "prompt": item["prompt"],
        })
    return sample


def parse_args(argv):
    parser = argparse.ArgumentParser(description="Select deterministic gallery scoring samples.")
    parser.add_argument("--strategy", choices=("first", "middle", "last"), default="middle")
    parser.add_argument("--output", default=OUT, help="Path for the sample JSON output.")
    parser.add_argument(
        "--expected-per-category",
        type=int,
        default=10,
        help="Expected item count per category. Use 0 to skip this check.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print the sample without writing a file.")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv or sys.argv[1:])
    data = load_references(DATA_JS)
    sample = pick_sample(data, args.strategy, args.expected_per_category)

    output = os.path.abspath(args.output)
    if not args.dry_run:
        os.makedirs(os.path.dirname(output), exist_ok=True)
        with open(output, "w", encoding="utf-8") as f:
            json.dump(sample, f, ensure_ascii=False, indent=2)

    target = "(dry run)" if args.dry_run else os.path.relpath(output, ROOT)
    print(f"Selected {len(sample)} sample item(s) -> {target}")
    for item in sample:
        print(
            f'  {item["id"]:8} {item["category"]} '
            f'(file {item["category_file"]}, index '
            f'{item["selected_index"]}/{item["category_count"] - 1}, '
            f'{item["selection_strategy"]})'
        )


if __name__ == "__main__":
    main()
