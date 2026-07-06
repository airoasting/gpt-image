# Variation Recipes

Use this file when the user asks for multiple directions, differentiated concepts, mood variations, campaign options, or "start from concepts." A normal seven-block prompt narrows one intent into one strong image. This file deliberately expands one intent into several controlled variants.

The core rule is simple: change one axis at a time. Keep the subject, category, and accuracy conditions stable unless the user explicitly asks to vary them. If two or three axes change at once, the set becomes random instead of intentional.

## Table Of Contents

1. When to use this file
2. The invariant stack
3. Five recipe families
4. Recipe 1: Art-system swap
5. Recipe 2: Opposing qualities
6. Recipe 3: Mood to palette
7. Recipe 4: Emotion to visible signal
8. Recipe 5: Same subject, different composition
9. Category fit map
10. Output formats
11. Batch and JSONL rules
12. Anti-patterns
13. Red-team scoring rubric

## 1. When To Use This File

Open this file for requests like:
- "Make several options."
- "Give me differentiated concepts."
- "Start from the concept direction."
- "Only change the mood."
- "Show me three campaign routes."
- "Make versions that feel meaningfully different."

Do not use it for a single precise prompt unless the user asks for alternatives. For a single prompt, use `gallery.md`, the matching `gallery-*.md` file, and `gpt-image-prompt-craft.md`.

## 2. The Invariant Stack

Before varying anything, write down what must stay fixed.

| Layer | Usually fixed | May vary only when |
|---|---|---|
| Category | Poster, product image, UI mockup, webtoon cut, infographic, etc. | The user asks for cross-format exploration |
| Main subject | Product, character, building, app, event, diagram topic | The user asks for subject exploration |
| Audience/use | Ad, public guide, portfolio image, app screen, pitch slide | The brief is still strategic |
| Accuracy conditions | Exact text, labels, dates, product geometry, identity | The user asks for copy or information variants |
| Canvas family | 3:4 poster, 9:16 mobile, 16:9 slide, 1:1 square | The output channel changes |

Then choose exactly one changing axis from the recipes below.

## 3. Five Recipe Families

| Recipe | Use when | Primary changed block |
|---|---|---|
| Art-system swap | The user wants distinct visual directions | Style and medium, palette, layout discipline |
| Opposing qualities | The image feels flat and needs tension | Context/background, light/detail |
| Mood to palette | The user asks for mood or tone variants | Style and medium, light/detail |
| Emotion to visible signal | The request is abstract or feeling-led | Main subject, light/detail |
| Same subject, different composition | The subject is fixed but the set needs coverage | Composition and ratio |

Pick one recipe and repeat it. Do not combine recipes unless you are intentionally making a second exploration round.

## 4. Recipe 1: Art-System Swap

An art-system swap changes the design logic, not just the style label. Decompose each direction into shape, color, type, and composition.

| Art system | Shape | Color | Type/text | Composition |
|---|---|---|---|---|
| Swiss International | Grid, rectangles, strong alignment | White/black plus one signal color | Clean sans serif, left aligned | Asymmetric balance, generous margins |
| Bauhaus | Circles, triangles, squares, simple geometry | Red, yellow, blue, black, cream | Geometric sans serif | Diagonal movement, modular blocks |
| Art Deco | Symmetry, stepped forms, rays, frames | Gold, deep navy, emerald, black | High-contrast serif or geometric display | Centered vertical hierarchy |
| Memphis | Zigzags, dots, playful scattered forms | Pastels plus bright accents | Bold playful sans serif | Intentional pattern overload |
| Minimal editorial | One strong silhouette, few elements | Neutral field plus one accent | Thin or medium sans serif | Extreme negative space, one focal point |
| Ukiyo-e inspired | Flat planes, bold outlines, waves/clouds | Indigo, vermilion, ochre, rice paper | Usually no type, or restrained captions | Diagonal flow, layered planes |
| Y2K pop | Chrome, bubbles, lens flare, glossy surfaces | Holographic gradients, neon accents | Stretched sans serif, capsule labels | Central object, reflective framing |
| Brutalist web | Blocks, exposed grids, heavy borders | Black, white, acid accent | Condensed or mono type | Dense modules, hard edges |
| Quiet luxury | Simple forms, tactile materials | Warm gray, charcoal, muted gold | Small refined type | Calm symmetry, spacious product focus |

Application rule:
- Put the art system in `Style and medium`.
- Put the shape/composition logic in `Composition and ratio`.
- Put the palette and texture in `Light and detail`.
- Keep exact text and subject unchanged.

Example variant axis:
```text
Axis: art system
Values: Swiss International / Art Deco / Y2K pop
Fixed: product, tagline, 3:4 poster, exact copy
```

## 5. Recipe 2: Opposing Qualities

Opposing qualities add tension by assigning contrast to different parts of the image. Do not blend both sides everywhere. Place each side in a region or role.

| Pair | Side A | Side B |
|---|---|---|
| Warm vs cool | Warm subject or foreground | Cool background or shadow field |
| Smooth vs rough | Clean product render | Rough paper, stone, brush, or street texture |
| Calm vs tension | Wide quiet space | One high-contrast focal point |
| Premium vs everyday | Refined material and light | Familiar daily-life prop or location |
| Order vs disruption | Grid, rows, clean alignment | One broken element, motion trail, scattered fragments |
| Natural vs synthetic | Plant, skin, wood, daylight | Glass, metal, neon, interface overlay |
| Heritage vs future | Traditional craft motif | Clean technical UI, chrome, or futuristic lighting |

Application rule:
- Name the contrast pair in the concept title.
- Assign each side to a visible place.
- Keep the subject and text fixed.

Good:
```text
The package stays centered in warm softbox light, while the background uses a cool blue shadow grid and sparse technical labels.
```

Weak:
```text
Make it warm and cool, premium and everyday, calm and intense.
```

## 6. Recipe 3: Mood To Palette

Mood words are too abstract by themselves. Convert the mood into three to five colors, a ratio, and lighting temperature.

| Mood | 60 percent base | 30 percent support | 10 percent accent | Light cue |
|---|---|---|---|---|
| Quiet luxury | `#EDE7DD` warm gray | `#2B2B2B` charcoal | `#B8975A` brushed gold | Soft warm studio light |
| Dawn calm | `#F4EEE6` pale linen | `#9CB7C8` mist blue | `#E6A15C` amber | Low morning side light |
| Spring pastel | `#FBEFF2` blush | `#CFE3D4` mint | `#F2B84B` soft yellow | Diffuse daylight |
| Dark tech | `#101418` ink | `#1F6FEB` electric blue | `#00E0A4` neon mint | Cool screen glow |
| Retro print | `#F4ECD8` cream | `#C0392B` brick red | `#2C6E63` teal | Flat print texture |
| Fresh public service | `#F7FAFC` near white | `#2563EB` civic blue | `#16A34A` safety green | Shadow-light vector style |
| Cinematic dusk | `#151923` night slate | `#D97745` sodium orange | `#8AB4F8` cool rim | Mixed practical light |
| Editorial monochrome | `#F5F5F0` off-white | `#111111` black | `#C8C8C8` silver gray | High-contrast print light |

Application rule:
- Put HEX values in `Style and medium` or `Context and background`.
- Put light temperature and contrast in `Light and detail`.
- Do not change the subject, copy, or layout unless the mood requires a minor spacing adjustment.

## 7. Recipe 4: Emotion To Visible Signal

An emotion must become visible through pose, light, framing, texture, and environment.

| Emotion | Visible signals |
|---|---|
| Excitement | Upward motion, floating particles, brighter highlights, open posture |
| Focus | Shallow depth, one sharp focal point, quiet background, downward gaze |
| Relief | Lowered shoulders, warm diffuse light, open space, softened contrast |
| Tension | Narrow crop, hard shadow edge, tilted horizon, compressed space |
| Nostalgia | Film grain, faded saturation, window backlight, worn objects |
| Trust | Stable symmetry, clear labels, gentle contrast, human-scale details |
| Urgency | Numbered steps, directional arrows, high-contrast warning color |
| Wonder | Small figure against large environment, glow source, layered depth |
| Precision | Thin lines, aligned modules, measured spacing, crisp annotations |

Application rule:
- Use this for abstract requests like "make it hopeful," "more immersive," or "calmer."
- Translate the emotion into visible choices.
- Avoid adding a slogan or extra text unless the user asks for copy variants.

## 8. Recipe 5: Same Subject, Different Composition

Use this when the subject is fixed and the user needs coverage: poster, social crop, hero image, thumbnail, close-up, detail shot, or storyboard range.

Composition ladders:
- Scale: wide environment -> medium subject with context -> close detail.
- Angle: front -> low three-quarter -> top-down.
- Channel: 3:4 poster -> 1:1 social post -> 16:9 thumbnail.
- Focus: product silhouette -> label readability -> material macro detail.
- Story: before action -> peak action -> aftermath.
- UI: home overview -> detail screen -> analytics/report view.

Application rule:
- Keep subject identity, style, palette, and accuracy conditions fixed.
- Change only framing, camera/view, and layout.
- Use one prompt per image unless the requested output is a single storyboard or reference board.

## 9. Category Fit Map

| Category | Best recipes | Notes |
|---|---|---|
| Webtoon | Emotion to visible signal; same subject, different composition | Keep character identity fixed across cuts. |
| Illustration | Art-system swap; emotion to visible signal | Useful for character sheets, posters, painterly variants. |
| Gaming | Same subject, different composition; opposing qualities | Vary camera and objective state, not the core game world. |
| Cinematic | Opposing qualities; emotion to visible signal; composition ladder | Make each frame a different story moment or camera decision. |
| Posters | Art-system swap; mood to palette | Keep exact copy fixed while changing design system. |
| Product and brand | Mood to palette; opposing qualities; composition ladder | Preserve product geometry and label integrity. |
| Photography | Mood to palette; composition ladder | Change capture context carefully; keep subject identity stable. |
| Architecture and interior | Composition ladder; mood to palette | Vary viewpoint, light, and use case while preserving spatial logic. |
| Infographics | Mood to palette; same subject, different layout | Preserve data, labels, numbering, and legend semantics. |
| UI and dashboard | Same subject, different screen; mood to palette | Preserve data model and interaction logic. |

## 10. Output Formats

Use one of these formats depending on the user's request.

### A. Concept list

Use when the user wants directions before full prompts.

```text
1. Title:
Axis:
Fixed elements:
Changed value:
Why it is different:
```

### B. Prompt entries

Use when the user wants ready-to-generate prompts.

```text
Title:
Category:
Recipe:
Axis value:
Size:

Output type:
...

Main subject:
...
```

### C. JSONL

Use when prompts will be generated in a batch.

```json
{"id":"cut-01","title":"Swiss Launch Poster","category":"poster","recipe":"art-system-swap","axis":"Swiss International","size":"1536x2048","prompt":"Output type:\n..."}
```

One JSON object per image. Do not put multiple unrelated concepts in a single prompt field.

## 11. Batch And JSONL Rules

For `N` variants:

1. Choose one category and one recipe.
2. Define the invariant stack.
3. Choose exactly `N` axis values.
4. Produce one complete seven-block prompt per axis value.
5. Keep fixed blocks actually fixed. Only edit the block touched by the recipe and any necessary supporting phrase.
6. Use consistent IDs: `cut-01`, `cut-02`, `cut-03`.
7. Use the local size defaults from `openai-cookbook.md` or `SKILL.md`.

If the user asks for a single board containing several variants, make the board itself the artifact. Otherwise, create separate prompts.

## 12. Anti-Patterns

Avoid:
- changing subject, style, palette, camera, and copy all at once;
- making every variant a different category;
- using mood labels without visual signals;
- adding new text to differentiate variants when copy should be fixed;
- packing many unrelated ideas into one canvas;
- using fake sponsor logos or invented brand clutter;
- treating `beautiful`, `premium`, or `modern` as a sufficient axis;
- producing variants with no shared identity.

Red-team question: could the user recognize these as one intentional set? If not, tighten the invariant stack and reduce the number of changing variables.

## 13. Red-Team Scoring Rubric

Use this 10-point rubric before accepting a variation set or future changes to this file:

| Area | Points | Red-team question |
|---|---:|---|
| Single-axis discipline | 2 | Does each variant change one declared axis instead of drifting randomly? |
| Invariant preservation | 1.5 | Are subject, category, exact text, identity, and accuracy conditions stable where needed? |
| Visual specificity | 1.5 | Are abstract moods translated into visible layout, palette, light, pose, material, or camera choices? |
| Category fit | 1 | Does the recipe match the selected gallery category and output format? |
| Batch usability | 1 | Are IDs, sizes, titles, and prompts ready for separate generation? |
| Distinctiveness | 1 | Are the variants meaningfully different at first glance? |
| Set coherence | 1 | Do the variants still feel like one family or campaign? |
| Maintainability | 1 | Is the document English-only, concise, synced with `gpt-image-prompt-craft.md`, and easy to update? |

Score 9 or below: revise before shipping. A 10-point variation set is controlled, visibly distinct, coherent as a family, and directly usable as separate seven-block prompts or JSONL rows.
