# Gallery Prompt-Fit Evaluation Report (2026-07-05)

This report evaluates 10 gallery images, one deterministic sample from each
category, against the prompt that produced it. The fixed rubric is
[`RUBRIC.md`](RUBRIC.md), raw scores live in
[`scores/gallery.scores.jsonl`](scores/gallery.scores.jsonl), samples are
reproducible with [`select_sample.py`](select_sample.py), and schema plus
aggregate checks run through [`validate_scores.py`](validate_scores.py).

The purpose is narrow: verify whether the current skill rules are supported by
observed prompt-image fit, text rendering quality, and negative-instruction
behavior. The conclusion is intentionally limited to this sample.

## Method

- **Sample**: one middle item per gallery category, selected deterministically by `select_sample.py`.
- **Scoring**: each image-prompt pair is scored once on four 0-5 axes: `goal_fit`, `text_accuracy`, `layout`, and `material_realism`.
- **Text rows**: `text_accuracy` is `null` when the image has no intentional text, and those rows are excluded from the text average.
- **Pass rule**: an image passes when the scored axes average at least 4, and any text-bearing image also has `text_accuracy >= 4`.
- **Validation**: `python3 experiments/validate_scores.py --pretty` must return `ok: true`.

## Per-Image Scores

| Image | Category | goal_fit | text | layout | material | neg_rendered |
|---|---|:--:|:--:|:--:|:--:|:--:|
| ref-6 | webtoon | 5 | 4 | 5 | 5 | false |
| ref-16 | illustration | 5 | none | 5 | 5 | false |
| ref-26 | gaming | 5 | 5 | 5 | 5 | false |
| ref-36 | cinematic | 5 | none | 5 | 5 | false |
| ref-46 | posters | 5 | 4 | 5 | 5 | false |
| ref-56 | product-and-brand | 5 | 4 | 5 | 5 | false |
| ref-66 | photography | 5 | none | 5 | 5 | false |
| ref-76 | architecture-and-interior | 5 | none | 5 | 5 | false |
| ref-86 | infographics | 5 | 5 | 5 | 5 | false |
| ref-96 | ui-and-dashboard | 5 | 5 | 5 | 5 | false |

`none` means the image contains no intentional text, so `text_accuracy` is
excluded from the text average.

## Aggregate Results

| Metric | Value | Note |
|---|---:|---|
| goal_fit | **5.00 / 5** | All 10 images scored 5 |
| text_accuracy | **4.50 / 5** | Six text-bearing images: 4, 5, 4, 4, 5, 5 |
| layout | 5.00 / 5 | All 10 images scored 5 |
| material_realism | 5.00 / 5 | All 10 images scored 5 |
| neg_rendered | **0 / 10** | No exclusion phrase or excluded object appeared |
| pass_count | **10 / 10** | Every sampled image passed |

## Findings

1. Prompt-image fit is excellent in this sample. Every image scored 5 on
   `goal_fit`, with no missing required subject, wrong count, or unsupported
   major object.

2. Text rendering is strong but not perfect. The text average is 4.50/5 across
   six text-bearing images. The only losses are small: an extra tiny string on a
   potion label, one missing word in a poster title, and soft SPF/PA fine print
   on a product tube. This supports the rule that quoted text should be fixed
   explicitly, while very small dense text should be minimized or rendered at a
   larger canvas size.

3. Negative tail phrases did not appear in the image output. `neg_rendered` is
   0/10, and no image lost `goal_fit` because of an exclusion phrase. This
   supports treating negative phrasing as a quality warning rather than an
   automatic failure, while still preferring clear positive phrasing.

## Limits

- The sample is small: one image per category, 10 images total.
- Each image was scored once, so inter-rater agreement was not measured.
- This is not a causal test. For example, measuring the effect of canvas size on
  text accuracy would require regenerating images under controlled conditions.

## Reproduction

```bash
# 1. Recreate the deterministic sample.
python3 experiments/select_sample.py

# 2. Score each image-prompt pair with RUBRIC.md and write one JSON object per
#    line to experiments/scores/gallery.scores.jsonl.

# 3. Validate the score file and recompute the aggregate metrics.
python3 experiments/validate_scores.py --pretty
```

The current source scores validate with `goal_fit=5.0`, `text_accuracy=4.5`,
`layout=5.0`, `material_realism=5.0`, `neg_rendered=0`, and `pass_count=10`.
