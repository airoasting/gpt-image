---
source: https://github.com/openai/openai-cookbook/blob/main/examples/multimodal/image-gen-models-prompting-guide.ipynb
reviewed: 2026-07-07
upstream_snapshot: 2026-04-23 local capture, checked against the official OpenAI cookbook source on 2026-07-07
license: MIT (OpenAI cookbook)
status: local operational digest, not a verbatim copy
---

# OpenAI Image Cookbook Notes

This file is the local operational digest of OpenAI's official image-generation prompting guide. It is designed for the `gpt-image` skill and the `references/` gallery in this repository.

Use this file when you need:
- model and parameter choices for generation or edits;
- practical prompting patterns from the official cookbook;
- a bridge between OpenAI API behavior and the local seven-block prompt format;
- a quick red-team checklist before shipping a prompt workflow.

For exact API behavior, always treat the source URL above as the living reference.

## Table Of Contents

1. Source status and scope
2. Model selection
3. Size and quality choices
4. Prompting fundamentals
5. Local seven-block bridge
6. Generate workflows
7. Edit workflows
8. Multi-image workflows
9. Text, UI, diagrams, and dense layouts
10. Product, ads, logos, and brand assets
11. Photorealism and people
12. Character consistency workflows
13. API parameter quick reference
14. Repository sync map
15. Red-team scoring rubric

## 1. Source Status And Scope

The upstream cookbook is an official OpenAI notebook with examples for `gpt-image` generation and editing. This local file is not a raw notebook export. It intentionally removes rendered-output placeholders, repeated code blocks, duplicated explanations, and notebook-only display helpers so the skill can use it as a fast reference.

Keep these boundaries clear:
- This file can summarize official cookbook patterns.
- `gpt-image-prompt-craft.md` decides how those patterns become reusable prompt-writing rules.
- `gallery.md` and the `gallery-*.md` files provide the repository's actual examples.
- `gpt-image-variation-recipes.md` controls multi-concept ideation.
- The upstream cookbook remains the source of truth for newly changed API details.

## 2. Model Selection

Use `gpt-image-2` as the default model for new image-generation and image-editing workflows when it is available.

| Model | Use it for | Notes |
|---|---|---|
| `gpt-image-2` | Production-quality generation and editing, text-heavy images, photorealism, compositing, identity-sensitive edits, fewer retries | Default for new work. Supports flexible sizing within constraints. The upstream cookbook states that `input_fidelity` is disabled/ignored for this model because fidelity is high by default. |
| `gpt-image-1.5` | Existing validated workflows that have not migrated yet | Keep only when stability of an older workflow matters more than the newest model behavior. |
| `gpt-image-1` | Legacy compatibility | Avoid for new prompt work. |
| `gpt-image-1-mini` | Low-cost drafts, high-volume exploration, lightweight previews | Use when throughput and cost dominate over final quality. |

Migration rule:
- Start by running existing prompts on `gpt-image-2` without heavy rewrites.
- Compare first-pass quality, text accuracy, edit drift, latency, and retry rate.
- Retune prompts only after seeing real output differences.

## 3. Size And Quality Choices

### `gpt-image-2` size constraints

The official cookbook describes `gpt-image-2` as accepting any `size` value that satisfies all of the following:

- maximum edge length is less than `3840px`;
- both edges are multiples of `16`;
- long edge divided by short edge is no greater than `3:1`;
- total pixels do not exceed `8,294,400`;
- total pixels are not less than `655,360`.

Treat outputs above `2560x1440` as experimental. They can work, but reliability can be more variable.

### Practical size defaults

| Intent | Size | Why |
|---|---:|---|
| Square concept or icon | `1024x1024` | Stable general default |
| Portrait product, poster, ad | `1024x1536` or `1536x2048` | Good vertical composition and readable copy |
| Landscape cinematic or slide | `1536x1024`, `1920x1080`, or `2560x1440` | Fits storyboards, slides, diagrams, wide scenes |
| Mobile UI or webtoon | `1080x1920` | Matches the local gallery's vertical mobile examples |
| Dense poster or infographic | `1536x2048` | More room for labels and hierarchy |
| Upper-end wide target | `3824x2144` | Valid near-UHD fallback when a strict max-edge rule rejects `3840x2160` |

Use the local gallery defaults when writing prompts for this repository:
- `1:1` -> `1024x1024`
- `3:4` -> `1536x2048`
- `16:9` -> `1920x1080`
- `9:16` -> `1080x1920`
- `21:9` -> `2520x1080`

### Quality defaults

| Quality | Use it for | Avoid it when |
|---|---|---|
| `low` | Fast ideation, high-volume variants, early thumbnails | Text accuracy, dense UI, final product assets, identity-sensitive edits |
| `medium` | Default exploratory quality and many production drafts | Very small labels, publication-grade diagrams, final brand/text assets |
| `high` | Dense text, infographics, UI mockups, scientific diagrams, close-up portraits, high-stakes edits | Large batches where speed and cost matter more than fidelity |

Rule: choose the smallest reliable size and lowest acceptable quality for exploration, then raise quality only for the candidate that matters.

## 4. Prompting Fundamentals

The cookbook's useful patterns reduce to these controls:

- **Artifact type first.** Name the intended deliverable: ad, infographic, UI mockup, logo, photorealistic image, product render, comic strip, classroom diagram, slide.
- **Structure beats prose length.** Use labeled sections or short paragraphs when the prompt has many constraints.
- **Concrete details beat praise.** Replace `beautiful`, `premium`, and `high quality` with materials, layout, lighting, camera, labels, and use case.
- **One dominant visual mode.** Do not mix conflicting media cues such as phone snapshot, studio render, watercolor, and cinematic key art in one prompt unless the artifact is explicitly a hybrid board.
- **Layout before detail.** Put canvas, ratio, and region layout before small surface effects.
- **Text in quotes.** Quote exact text and place it in the layout.
- **Edit invariants repeat.** For edits, state what changes and repeat what must remain unchanged.
- **Iterate with one change.** When improving output, change one axis at a time so failures can be diagnosed.

## 5. Local Seven-Block Bridge

The cookbook often writes prompts as paragraphs or Python strings. This skill outputs seven-block prompts. Convert official cookbook patterns into the local block contract:

```text
Output type:
Name the deliverable, model workflow, canvas, and intended use.

Main subject:
Define the central person, product, scene, UI screen, chart, object, or character.

Composition and ratio:
Define aspect ratio, camera/view, layout regions, panel count, hierarchy, and spacing.

Context and background:
Define setting, audience, use case, real-world cues, data context, or story state.

Style and medium:
Choose one visual mode: photo, 3D render, vector infographic, UI mockup, watercolor, webtoon, product photography, etc.

Light and detail:
Specify lighting, material behavior, camera/capture context, texture, labels, icons, and fine details.

Accuracy conditions:
Quote exact text, preserve invariants, lock identity/layout/geometry, and add readability or safety constraints.
```

When the end user wants Korean output, keep the Korean block labels from `SKILL.md`. This file stays English as the API/cookbook reference layer.

## 6. Generate Workflows

Use `client.images.generate` when everything comes from text.

Minimal pattern:

```python
result = client.images.generate(
    model="gpt-image-2",
    prompt=prompt,
    size="1536x2048",
    quality="medium",
)
```

Good generation prompts include:
- output type and purpose;
- subject and layout;
- exact text if any;
- material, lighting, and style controls;
- audience or use context;
- concise constraints.

Generation is the right workflow for:
- new posters, ads, logos, product concepts, and style boards;
- new UI mockups and dashboards;
- new infographics, diagrams, charts, and educational visuals;
- new photorealistic scenes;
- comic strips, storyboards, character sheets, and illustration concepts.

## 7. Edit Workflows

Use `client.images.edit` when one or more images already exist and some part must be changed, preserved, translated, composited, or restyled.

Minimal pattern:

```python
result = client.images.edit(
    model="gpt-image-2",
    image=[
        open("input.png", "rb"),
    ],
    prompt=prompt,
    size="1536x2048",
    quality="medium",
)
```

The edit prompt should separate:
- target transformation;
- preserved identity;
- preserved layout and geometry;
- preserved text or replacement text;
- lighting and shadow integration;
- forbidden drift such as changed camera angle or added objects.

Strong edit skeleton:

```text
Change only the background season to a quiet snowy evening. Add soft snowfall, cool blue-gray ambient light, and realistic snow accumulation on horizontal surfaces. Keep the original person, pose, clothing, face, camera angle, crop, product label, object positions, and all existing text unchanged.
```

For `gpt-image-2`, omit `input_fidelity` unless the current official API documentation says it applies. The upstream cookbook notes that `input_fidelity` is disabled/ignored for `gpt-image-2`, even though some older examples may still show it in edit calls.

## 8. Multi-Image Workflows

When multiple image inputs are used, identify each one by index and role.

Pattern:

```text
Image 1: base product photo. Preserve its camera angle, product geometry, and label placement.
Image 2: lighting reference. Apply its warm studio light and soft contact shadow.
Image 3: label artwork. Place this exact label on the front panel.

Create one final commercial product image. Keep the product shape from Image 1, the lighting mood from Image 2, and the label content from Image 3.
```

Use multi-image edits for:
- product plus label art;
- person plus outfit references;
- subject plus background;
- object insertion;
- style transfer;
- character consistency across pages.

Do not say only `use these references`. Explain exactly how each reference controls the result.

## 9. Text, UI, Diagrams, And Dense Layouts

Text-heavy images require stricter prompting and often higher quality.

Use `quality="high"` when:
- the image contains small text, axes, labels, footnotes, table cells, app values, or multilingual copy;
- the output is a public guide, educational diagram, UI mockup, slide, or product label;
- a wrong number or unreadable label would make the result unusable.

Text rules:
- quote every required string;
- define placement and hierarchy;
- keep copy short enough for the canvas;
- request readable, non-overlapping typography;
- ask for no garbled characters, no duplicate letters, and no unintended extra text when correctness matters.

UI rules:
- describe the app as if it already exists;
- name device/canvas, header, cards, charts, nav, buttons, rows, and states;
- provide real values and labels;
- avoid concept-art language.

Diagram rules:
- name the visual format first;
- define regions, arrows, legends, axes, steps, and labels;
- specify visual semantics such as color meaning or line thickness;
- prefer clean educational or publication-grade layout over decorative detail.

## 10. Product, Ads, Logos, And Brand Assets

### Product and packaging

Product prompts need geometry and label integrity:
- visible product sides;
- package seams, lid, cap, label area, front/side panels;
- material response;
- contact shadow;
- exact label text;
- plain or controlled background.

For extraction/mockup edits, keep the background opaque and use a downstream background-removal step if a final transparent asset is needed.

### Ads

Ad prompts work best as creative briefs:
- brand or fictional brand;
- target audience;
- culture and mood;
- scene or hero object;
- exact tagline;
- composition and typography;
- constraints on extra logos or fake sponsor text.

### Logos

Logo prompts should favor simplicity:
- original, non-infringing mark;
- flat/vector-like shape language;
- strong silhouette;
- balanced negative space;
- scalable at small size;
- one centered logo with padding.

Avoid over-detailed illustrated logos unless the user explicitly wants an emblem or mascot.

## 11. Photorealism And People

Photorealism improves when the prompt sounds like a real capture scenario.

Include:
- camera/capture style: phone snapshot, documentary photo, editorial portrait, studio product photo;
- subject framing: full body, waist-up, close-up, object scale;
- gaze, pose, and interaction;
- natural imperfections: fabric wear, skin texture, environmental noise, reflections;
- believable light: coastal daylight, fluorescent subway light, window side light, dusk ambient light.

For people:
- lock face, body shape, pose, skin tone, hair, expression, and identity in edits;
- describe hands and object interactions when hands matter;
- keep scenes grounded and tasteful;
- do not over-style documentary images with cinematic grading unless requested.

## 12. Character Consistency Workflows

For multi-image character workflows, create an anchor first, then reuse it.

Anchor prompt should define:
- character role and age/scale;
- face, hair, body proportions, outfit, palette, signature prop;
- style and medium;
- plain enough background to show the character clearly;
- no text unless the design sheet requires labels.

Continuation prompt should repeat:
- same character;
- unchanged outfit, facial features, proportions, palette, and personality;
- new scene and action;
- same medium and tone;
- no redesign.

For this repository, character consistency guidance should also consult:
- `gallery-webtoon.md` for mobile comic story hooks;
- `gallery-illustration.md` for reference sheets and character boards;
- `gpt-image-prompt-craft.md` for identity consistency and multi-panel constraints.

## 13. API Parameter Quick Reference

Parameters shown or discussed in the official cookbook:

| Parameter | Generation | Edit | Local note |
|---|---:|---:|---|
| `model` | yes | yes | Default to `gpt-image-2` for new work. |
| `prompt` | yes | yes | Use seven-block prompts for this skill. |
| `size` | yes | yes | Must satisfy model constraints; use local gallery defaults where possible. |
| `quality` | yes | yes | `low`, `medium`, `high`; raise for dense text and final assets. |
| `n` | yes | sometimes | Useful for logo/variant exploration. |
| `background` | yes | yes | Use `opaque` for product extraction unless a workflow explicitly supports transparency. |
| `moderation` | yes | no | Follow current API docs for accepted values. |
| `output_format` | yes | yes | Choose based on downstream needs. |
| `output_compression` | yes | yes | Relevant for compressed formats. |
| `input_fidelity` | model-dependent | model-dependent | Upstream notes say it is ignored/disabled for `gpt-image-2`; verify before using. |
| `image` | no | yes | One or more input images. |
| `mask` | no | yes | Use for localized edits when available. |
| `user` | yes | yes | Optional end-user identifier for API use. |

## 14. Repository Sync Map

Use the official cookbook patterns together with the local reference files:

| Cookbook use case | Local reference file |
|---|---|
| Infographics, educational visuals, slides, charts | `gallery-infographics-and-field-guides.md`, `gallery-ui-ux-mockups.md`, `gpt-image-prompt-craft.md` |
| Translation and text replacement | `gpt-image-prompt-craft.md` sections on exact text and edit invariants |
| Photorealistic images and people | `gallery-photography.md`, `gpt-image-prompt-craft.md` |
| Logo, ads, products, packaging, merch | `gallery-product-and-brand.md`, `gallery-typography-and-posters.md`, `gpt-image-prompt-craft.md` |
| Story-to-comic and character consistency | `gallery-webtoon.md`, `gallery-illustration.md`, `gpt-image-prompt-craft.md` |
| UI mockups | `gallery-ui-ux-mockups.md`, `gpt-image-prompt-craft.md` |
| Interior swap and architecture edits | `gallery-architecture-and-interior.md`, `gpt-image-prompt-craft.md` |
| Multi-concept batches | `gpt-image-variation-recipes.md` |

This file should not duplicate every gallery example. It should explain how OpenAI API behavior and cookbook workflow patterns affect the local prompt design.

## 15. Red-Team Scoring Rubric

Use this 10-point rubric before accepting future changes to this file:

| Area | Points | Red-team question |
|---|---:|---|
| Official-source honesty | 1.5 | Does the file preserve source/license and avoid pretending to be a verbatim official doc? |
| API usefulness | 1.5 | Are model, size, quality, generate, edit, and parameter notes actionable? |
| Current-model caution | 1 | Does it flag model-dependent details and avoid overclaiming unstable API behavior? |
| Local skill integration | 1.5 | Does it map cookbook patterns into the seven-block output and local reference files? |
| Prompt quality | 1.5 | Does it improve specificity, text handling, layout, edits, and invariants? |
| Workflow coverage | 1 | Does it cover generation, edits, multi-image, text-heavy, product, people, and character workflows? |
| Maintainability | 1 | Is it concise, English-only, free of notebook clutter, and easy to update? |
| Safety and public use | 1 | Does it keep identity, brand, public-safety, and high-stakes visuals bounded? |

Score 9 or below: revise before shipping. A 10-point version is concise, source-honest, synchronized with the local reference system, and useful without opening the full upstream notebook for routine prompt work.
