#!/usr/bin/env python3
"""Validate and aggregate gallery experiment scores.

This script checks `scores/gallery.scores.jsonl` against the fixed experiment
schema and recomputes the summary numbers quoted in REPORT.md.
"""

import argparse
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_SCORES = os.path.join(ROOT, "experiments/scores/gallery.scores.jsonl")

CATEGORIES = [
    "webtoon",
    "illustration",
    "gaming",
    "cinematic",
    "posters",
    "product-and-brand",
    "photography",
    "architecture-and-interior",
    "infographics",
    "ui-and-dashboard",
]
AXES = ["goal_fit", "text_accuracy", "layout", "material_realism"]
REQUIRED_QA = set(AXES)


def load_jsonl(path):
    rows = []
    errors = []
    with open(path, encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                row = json.loads(stripped)
            except json.JSONDecodeError as exc:
                errors.append({"line": line_no, "code": "E-JSON", "msg": str(exc)})
                continue
            row["_line"] = line_no
            rows.append(row)
    return rows, errors


def validate_row(row):
    errors = []
    line = row.get("_line")

    for key in ("id", "category", "qa", "neg_rendered", "notes"):
        if key not in row:
            errors.append({"line": line, "code": "E-MISSING", "msg": f"Missing required field: {key}"})

    if "qa" not in row or not isinstance(row["qa"], dict):
        return errors

    missing_axes = REQUIRED_QA - set(row["qa"])
    extra_axes = set(row["qa"]) - REQUIRED_QA
    if missing_axes:
        errors.append({"line": line, "code": "E-QA-MISSING", "msg": f"Missing qa axes: {sorted(missing_axes)}"})
    if extra_axes:
        errors.append({"line": line, "code": "E-QA-EXTRA", "msg": f"Unknown qa axes: {sorted(extra_axes)}"})

    for axis in AXES:
        value = row["qa"].get(axis)
        if axis == "text_accuracy" and value is None:
            continue
        if not isinstance(value, int) or not 0 <= value <= 5:
            errors.append(
                {
                    "line": line,
                    "code": "E-QA-RANGE",
                    "msg": f"{axis} must be an integer from 0 to 5, or null for text_accuracy: {value!r}",
                }
            )

    if "neg_rendered" in row and not isinstance(row["neg_rendered"], bool):
        errors.append({"line": line, "code": "E-NEG-TYPE", "msg": "neg_rendered must be a boolean."})

    if "category" in row and row["category"] not in CATEGORIES:
        errors.append({"line": line, "code": "E-CATEGORY", "msg": f"Unknown category: {row['category']}"})

    return errors


def aggregate(rows):
    axis_values = {axis: [] for axis in AXES}
    passes = 0
    text_rows = 0
    neg_count = 0

    for row in rows:
        qa = row["qa"]
        for axis in AXES:
            value = qa[axis]
            if value is not None:
                axis_values[axis].append(value)
        if qa["text_accuracy"] is not None:
            text_rows += 1
        if row["neg_rendered"]:
            neg_count += 1

        pass_axes = [qa["goal_fit"], qa["layout"], qa["material_realism"]]
        if qa["text_accuracy"] is not None:
            pass_axes.append(qa["text_accuracy"])
        average = sum(pass_axes) / len(pass_axes)
        if average >= 4 and (qa["text_accuracy"] is None or qa["text_accuracy"] >= 4):
            passes += 1

    averages = {
        axis: round(sum(values) / len(values), 4) if values else None
        for axis, values in axis_values.items()
    }

    return {
        "rows": len(rows),
        "text_rows": text_rows,
        "averages": averages,
        "neg_rendered": neg_count,
        "pass_count": passes,
        "pass_rate": round(passes / len(rows), 4) if rows else None,
    }


def validate_dataset(rows):
    errors = []
    for row in rows:
        errors.extend(validate_row(row))

    ids = [row.get("id") for row in rows]
    duplicate_ids = sorted({id_ for id_ in ids if ids.count(id_) > 1})
    if duplicate_ids:
        errors.append({"line": None, "code": "E-DUP-ID", "msg": f"Duplicate ids: {duplicate_ids}"})

    categories = [row.get("category") for row in rows]
    missing_categories = [category for category in CATEGORIES if category not in categories]
    if missing_categories:
        errors.append({"line": None, "code": "E-CAT-MISSING", "msg": f"Missing categories: {missing_categories}"})

    if len(rows) != len(CATEGORIES):
        errors.append({"line": None, "code": "E-ROW-COUNT", "msg": f"Expected {len(CATEGORIES)} rows, found {len(rows)}."})

    return errors


def parse_args(argv):
    parser = argparse.ArgumentParser(description="Validate and aggregate experiment score JSONL.")
    parser.add_argument("scores", nargs="?", default=DEFAULT_SCORES)
    parser.add_argument("--pretty", action="store_true", help="Print indented JSON.")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv or sys.argv[1:])
    rows, errors = load_jsonl(args.scores)
    if not errors:
        errors = validate_dataset(rows)

    summary = aggregate(rows) if not errors else None
    payload = {
        "ok": not errors,
        "scores": os.path.relpath(os.path.abspath(args.scores), ROOT),
        "errors": errors,
        "summary": summary,
    }
    print(json.dumps(payload, ensure_ascii=True, indent=2 if args.pretty else None))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
