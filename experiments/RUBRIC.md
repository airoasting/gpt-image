# Gallery Evaluation Rubric

Use this rubric to judge how faithfully each gallery prompt produced its
paired image. The goal is to evaluate the skill rules with observable evidence,
not taste or memory.

## File Roles

- `select_sample.py`: selects one deterministic sample from each category in `docs/js/gallery-data.js`.
- `scores/gallery.scores.jsonl`: stores one scored JSON object per sampled image.
- `validate_scores.py`: checks the JSONL schema and recomputes aggregate metrics.
- `REPORT.md`: explains the result, limits, and reproduction steps for humans.

## JSONL Schema

Write one JSON object per line in `scores/gallery.scores.jsonl`.

```json
{
  "id": "ref-6",
  "category": "webtoon",
  "qa": {
    "goal_fit": 5,
    "text_accuracy": 4,
    "material_realism": 5,
    "layout": 5
  },
  "neg_rendered": false,
  "notes": "One-sentence finding."
}
```

- The four `qa` axes use integer scores from 0 to 5.
- Use `null` for `text_accuracy` when the image contains no intentional text.
- Set `neg_rendered` to `true` only when an exclusion phrase appears in the image as visible text or as a visible unwanted object.
- Keep `notes` short. If a score drops below 5, state the reason.

Validate the file with:

```bash
python3 experiments/validate_scores.py --pretty
```

The command must return `ok: true` before `REPORT.md` can cite the aggregate numbers.

## Aggregation

- **Axis average**: arithmetic mean for each axis. Rows with `text_accuracy: null` are excluded only from the text average.
- **Image pass**: average of `goal_fit`, `layout`, `material_realism`, and `text_accuracy` when present is at least 4. If text is present, `text_accuracy` must also be at least 4 on its own.
- **Sample pass rate**: passed images divided by total scored images.
- **Experiment pass**: the score file validates, `REPORT.md` states the limits, and the conclusion does not exceed the data.

## goal_fit

Measures whether the prompt and image describe the same core result: subject,
count, composition, color, mood, and required details.

- 5: All required prompt elements are present, and the image's major elements are explained by the prompt.
- 4: Subject and composition are right, with minor color or mood drift.
- 3: Main subject is right, but count or placement differs.
- 2: Main subject is recognizable, but several core details are wrong.
- 1: The image is effectively a different result.
- 0: The image is unrelated to the prompt.

Check especially for requested people or objects that are missing, extra major
objects that the prompt never asked for, and missing required details.

## text_accuracy

Measures visible text inside the image.

- 5: Quoted text appears exactly, does not overlap, and no stray text appears.
- 4: Text content is correct, but spacing, weight, or small styling details drift.
- 3: One character is wrong, or one specified phrase is duplicated.
- 2: Two or more characters are wrong, or unreadable stray text appears.
- 1: More than half of the requested text is broken.
- 0: Requested text cannot be recognized.

Check spelling, spacing, duplicate phrases, and text that was not requested.

## layout

Measures placement, ordering, and visual structure.

- 5: Regions match the prompt exactly, such as title at top, steps in order, or correct grid count.
- 4: Regions are correct, with minor uneven spacing or alignment.
- 3: Regions are recognizable, but spacing or alignment is unstable.
- 2: Some major regions are misplaced.
- 1: Most placement instructions are ignored.
- 0: Layout is unusable or unrelated.

## material_realism

Measures whether the requested surface, medium, and physical feel are believable.

- 5: Requested material or medium is convincing, such as matte product finish, watercolor bleed, flat vector, natural skin, or architectural light.
- 4: Material is mostly right, with one or two awkward areas.
- 3: Material is generic, plastic, or too smooth.
- 2: Material visibly contradicts the prompt.
- 1: Material is heavily distorted or visibly artificial.
- 0: Material cannot be evaluated or is unrelated.

## neg_rendered

Tracks whether a negative instruction was rendered into the image. Mark `true`
only when an exclusion phrase itself appears as visible text, or when the image
visibly includes the object or effect that the prompt explicitly excluded.

This metric is a policy check. A high rate supports stricter positive rewriting;
a low rate means negative phrasing should remain a quality warning rather than
an automatic failure.

## Red-Team Checklist

- Apply the same anchors to every image.
- Make sure scores and `notes` do not contradict each other.
- Use `text_accuracy: null` only when there is no intentional text.
- Use `neg_rendered: false` when no excluded phrase or object is visible.
- Record limits in `REPORT.md` instead of overstating a good sample.

## Report Expectations

`REPORT.md` should include category-level rows, overall averages, text accuracy
distribution for text-bearing images, `neg_rendered` rate, and a concise list of
limits. Any low `goal_fit` image should become a prompt repair candidate.
