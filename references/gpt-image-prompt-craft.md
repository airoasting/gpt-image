# GPT Image Prompt Craft

This file is the English craft layer for the `references/` folder. It turns the repository's gallery examples, variation recipes, and OpenAI cookbook notes into reusable prompt-writing rules.

Use it with:
- `gallery.md` as the routing index.
- One matching `gallery-*.md` category file, or two to three files for mixed requests.
- `gpt-image-variation-recipes.md` when the user asks for multiple concepts or deliberate variants.
- `openai-cookbook.md` when the request depends on current model capabilities, generation/edit workflows, or API parameter behavior.

The gallery files are written in Korean because they mirror the site examples. This file is intentionally English so the craft rules can be inspected, reused, and maintained independently.

## Table Of Contents

0. Start from the references
1. Map the request to the real category files
2. Preserve the seven-block output contract
3. Put canvas, ratio, and layout before surface detail
4. Quote exact in-image text
5. Use positive restatement instead of negative prompting
6. Treat information design as a layout contract
7. UI prompts should read like product specifications
8. Product, brand, and food prompts need material control
9. Photography needs capture context
10. Architecture and interiors need usable spatial logic
11. Cinematic and game prompts need camera plus story state
12. Webtoon, manga, and illustration need identity consistency
13. Multi-panel and board prompts need consistency constraints
14. Use config-style prompts for complex visual systems
15. Edit prompts must preserve invariants
16. Dense Korean, Chinese, and multilingual text needs extra guards
17. Variant generation uses one changing axis
18. Attribution, safety, and public-use boundaries
19. Red-team scoring rubric

## 0. Start From The References

Do not draft from memory first. The skill is meant to remix the repository's collected patterns.

Reference workflow:
1. Open `gallery.md` and choose the closest category.
2. Read the matching `gallery-*.md` file and compare three to eight nearby examples.
3. Apply this `gpt-image-prompt-craft.md` file for cross-category rules.
4. For batches or concept variations, also read `gpt-image-variation-recipes.md`.
5. For generation/edit/API questions, check `openai-cookbook.md`.

The current reference set is exactly 100 gallery examples: 10 categories with 10 examples each. Do not cite obsolete example numbers from older atlases. Refer to the current category file and entry title instead.

## 1. Map The Request To The Real Category Files

Use these files exactly as they exist in `references/`:

| User intent | Primary file | What to borrow |
|---|---|---|
| Webtoon, manga, mobile comic hero cut | `gallery-webtoon.md` | Mobile vertical framing, story hook, character silhouette, webtoon finish |
| Character sheet, illustration, watercolor, pixel art, painterly image | `gallery-illustration.md` | Medium discipline, character identity, line/color treatment, sheet layout |
| Game screenshot, playable scene, game key visual, HUD | `gallery-gaming.md` | Camera state, playable objective, environment affordances, HUD restraint |
| Film still, storyboard, cinematic frame | `gallery-cinematic.md` | Shot language, foreground/midground/background, incident clues, lighting motivation |
| Poster, typography, editorial cover, campaign graphic | `gallery-typography-and-posters.md` | Text hierarchy, print layout, exact copy, distance readability |
| Product image, packaging, brand board, food image | `gallery-product-and-brand.md` | Materials, label integrity, packaging geometry, commercial lighting |
| Portrait, fashion editorial, street/documentary photo | `gallery-photography.md` | Real camera feel, ordinary props, natural imperfections, believable location |
| Building, interior, isometric space, architectural visualization | `gallery-architecture-and-interior.md` | Spatial use, material readability, entrance/circulation, lens discipline |
| Infographic, public guide, chart, field guide, explainer | `gallery-infographics-and-field-guides.md` | Modules, labels, legends, numbered steps, public-information hierarchy |
| UI mockup, dashboard, app screen, data product | `gallery-ui-ux-mockups.md` | Real UI structure, plausible data, components, chart labels, interaction affordance |

Mixed requests should add only the adjacent file that changes the output. For example, a product launch poster uses `gallery-product-and-brand.md` plus `gallery-typography-and-posters.md`; a data dashboard poster uses `gallery-ui-ux-mockups.md` plus `gallery-infographics-and-field-guides.md`.

## 2. Preserve The Seven-Block Output Contract

The skill's standard output is a seven-block prompt. Keep the block order stable:

```text
Output type:

Main subject:

Composition and ratio:

Context and background:

Style and medium:

Light and detail:

Accuracy conditions:
```

Each block should carry dense, visual information. A block title alone is not a prompt. The gallery examples work because they define the artifact type, subject, layout, background, medium, lighting, camera/view, detail targets, and correctness constraints.

When writing in Korean for the end user, keep the Korean block labels from `SKILL.md`. When documenting craft in this file, use English.

## 3. Put Canvas, Ratio, And Layout Before Surface Detail

State the output format before describing texture, mood, or decoration. The strongest examples allocate space first, then fill it.

Reliable first moves:
- `9:16 vertical mobile webtoon hero cut`
- `16:9 landscape cinematic frame`
- `3:4 vertical printed poster`
- `1:1 square isometric diorama`
- `9:16 smartphone UI screen`
- `3:4 public-safety infographic`
- `16:9 character reference sheet`

When layout matters, name regions explicitly: top title area, central map, bottom step list, left info panel, right chart column, foreground subject, midground objective, background context. This prevents the model from spending its visual budget on the object while improvising the composition.

## 4. Quote Exact In-Image Text

If text must appear in the image, quote it exactly. The gallery examples rely on literal quoted copy for Korean titles, product labels, app values, poster titles, and public-information labels.

Rules:
- Wrap every required displayed string in straight quotes.
- Preserve user-supplied Korean, Chinese, English, numbers, dates, and spacing verbatim.
- Separate text blocks by role: title, subtitle, label, legend, button, price, date, warning, fine print.
- For UI and infographics, include real labels and values, not placeholder text.
- For dense text, specify hierarchy and location, not just the words.
- If text is decorative, say it is decorative. If it must be readable, require crisp, legible, non-overlapping text.

Strong pattern:
```text
Use the exact title "Flood Evacuation Guide" at the top, a red warning banner "Move Early When Heavy Rain Alerts Arrive", five numbered steps "01 Check alerts" through "05 Call emergency services", and a bottom note "Keep exits clear".
```

## 5. Use Positive Restatement Instead Of Negative Prompting

Scene-level negatives can backfire. Restate the desired visible state.

| Weak negative | Strong positive restatement |
|---|---|
| No crowd | The frame contains one main person only; the remaining platform space stays open. |
| No messy background | A flat, single-tone background with generous empty space supports the subject. |
| No logos | The product surface is smooth and unmarked except for the supplied label text. |
| Avoid clutter | Each object has a clear role, with wide spacing between modules. |
| Do not make it scary | The expression stays calm, the lighting is soft, and the scene reads as reassuring. |

Exception: text-rendering guardrails may use limited avoidance language because they target rendering defects, not scene content. Example: `Readable text, no garbled characters, no duplicate letters, no fake watermark.`

## 6. Treat Information Design As A Layout Contract

Infographics, public guides, field guides, charts, science visuals, and educational boards are layout contracts, not general illustrations.

Include:
- Artifact type: public-safety infographic, field guide, checklist board, classroom chart, data dashboard.
- Fixed zones: title, map/diagram, steps, legend, callout box, footer note.
- Semantics: red = risk, blue = action, green = safe location; line thickness = quantity; dashed line = warning path.
- Exact labels, numbers, units, dates, axes, and legend values.
- Readability constraints: short labels, consistent numbering, clean margins, no overlapping modules.

Use this pattern for the current `gallery-infographics-and-field-guides.md` examples such as flood evacuation, subway transfer guidance, electricity billing, recycling schedules, health-check procedures, fine-dust response, contract checklists, sales boards, kimchi-prep tables, and travel packing lists.

## 7. UI Prompts Should Read Like Product Specifications

UI prompts succeed when they describe a real product screen rather than a generic beautiful interface.

Include:
- Device/canvas: `9:16 smartphone screen`, `16:10 desktop dashboard`, `tablet admin view`.
- Product context and user: salary budgeting app, delivery operations dashboard, public-service design system, transit wallet, health routine app.
- Information architecture: header, summary card, charts, tables, lists, bottom nav, action buttons.
- Real copy and values: balances, percentages, dates, labels, tab names, chart axes.
- Component behavior: selected states, badges, progress rings, heatmaps, filters, map legends.
- Quality constraints: crisp typography, aligned icons, touch-sized controls, non-overlapping numbers.

Avoid UI filler such as `modern dashboard with charts`. Replace it with the actual screen structure and plausible data.

## 8. Product, Brand, And Food Prompts Need Material Control

Do not compress product quality into words like premium or luxury. Split the controls:

- Geometry: package shape, visible sides, label zones, cap/lid/box seams, tray placement.
- Materials: matte paper, brushed metal, glass thickness, condensation, ceramic glaze, chocolate wafer texture, leafy greens.
- Lighting: softbox, rim light, morning side light, reflective highlights, warm studio ambience.
- Surface behavior: shadow contact, edge sharpness, print registration, droplets, crumbs, folds.
- Brand integrity: exact supplied text, fictional brand names when needed, no fake real-brand confusion.

For brand boards, describe the system: wordmark, palette, typography, packaging, social tile, icon set, business card, shopping bag, and how they align in one board.

For food and motion product scenes, specify what is suspended, falling, poured, sliced, splashing, or resting. Motion needs visible physics, not just energy.

## 9. Photography Needs Capture Context

Photorealistic prompts become more believable when they name how the image was captured.

Useful capture anchors:
- `realistic street photograph`
- `phone snapshot at eye level`
- `documentary photo from a commuter platform`
- `fashion editorial portrait with controlled studio lighting`
- `slightly wide lens feel without face distortion`
- `natural morning side light`
- `ordinary background noise and small imperfections`

Pick one dominant capture frame. Too many camera specs can conflict. The current photography gallery emphasizes believable Korean places, clothing, props, gesture, light, and the small imperfections that make a generated portrait feel photographed.

## 10. Architecture And Interiors Need Usable Spatial Logic

For buildings and interiors, the viewer should understand how the space works.

Include:
- Space type: cafe street, fantasy village map, museum atrium, office, biotech lab, cathedral, hanok gallery, coworking atrium, coastal pavilion, popup space.
- View discipline: isometric, 45-degree bird's-eye, eye-level architectural photo, wide interior view, low exterior angle.
- Circulation: entrances, stairs, corridors, seating zones, display routes, walkways.
- Scale cues: people, tables, doors, railings, signage, bikes, furniture.
- Materials: brick, stucco, glass, concrete, wood, tile, steel, fabric, planting.
- Lighting: daylight direction, interior glow, skylight, soft shadows, realistic reflections.

Avoid decorative fantasy space that cannot be used. Even stylized architecture should have readable scale, structure, and circulation.

## 11. Cinematic And Game Prompts Need Camera Plus Story State

Cinematic frames and game screenshots need a moment, not only an atmosphere.

Cinematic prompts should define:
- The event happening now.
- Foreground, midground, and background roles.
- Camera height and lens feel.
- Lighting motivation: window light, neon spill, storm sky, firelight, projector light.
- Story clues before and after the frame.

Game prompts should define:
- Playable camera: third-person over-shoulder, top-down tactical, side-scroller, first-person, racing chase cam.
- Objective and threat: target door, boss arena, stealth guard, resource node, finish line.
- HUD elements only where useful: minimap, health bar, inventory, quest marker, status gauge.
- Environment affordances: cover, climbable paths, hazards, lanes, interactive objects.

Make promotional key art only when the request asks for key art. Otherwise, game examples should read like real gameplay capture.

## 12. Webtoon, Manga, And Illustration Need Identity Consistency

Character-driven prompts fail when identity drifts across views, panels, or props. Lock the identity early.

Include:
- Original character premise and age/role when relevant.
- Hair, clothing, silhouette, signature object, color motif.
- Pose/action and emotional state.
- View requirements: front/side/back, expressions, detail cuts, equipment, turnarounds.
- Style boundary: Korean mobile webtoon, anime/manga color art, watercolor, pixel art, oil paint, poster illustration.
- Originality boundary when borrowing a style family: keep characters, products, and symbols original.

For webtoon hero cuts, write a single readable hook: who is present, what just happened, what visual tension points upward/downward/forward, and why the next panel is implied.

## 13. Multi-Panel And Board Prompts Need Consistency Constraints

Grids, proof sheets, character sheets, brand boards, field guides, and storyboards need consistency rules.

State:
- Exact panel count and grid: `3x2`, `3x3`, `4x3`, `16-panel`, `front/side/back plus expressions`.
- A role for each region or panel.
- Shared palette, character identity, lighting logic, line style, and typography.
- Consistent axes, labels, and scale when the board contains data.
- Alignment rules: equal spacing, thin dividers, stable margins, readable labels.

For storyboards, include shot language: WIDE, OTS, CU, low angle, aerial, match cut, pan, tilt, static hold, and duration when useful.

## 14. Use Config-Style Prompts For Complex Visual Systems

The gallery and cookbook both support structured prompts when a scene contains many interacting systems: product, environment, materials, lighting, particles, labels, motion, and output goals.

Use config-style prompts for:
- Premium product renders.
- Food images with suspended ingredients or splashes.
- Brand systems with many touchpoints.
- Technical boards with strict modules.
- Multi-reference edits where each image has a role.

Recommended pattern:

```text
/* PRODUCT_RENDER_CONFIG: Short Name
   VERSION: 1.0.0
   AESTHETIC: Premium commercial photography */
{
  "GLOBAL_SETTINGS": {
    "aspect_ratio": "3:4 vertical",
    "style": "hyper-realistic commercial product image",
    "clarity": "sharp foreground, readable label, visible material texture"
  },
  "ENVIRONMENT": {
    "background": "warm cream studio sweep",
    "lighting": "large softbox from upper left with subtle contact shadow"
  },
  "CORE_ASSETS": {
    "primary_subject": "single matte paper coffee package",
    "label_text": ["SANDEUL BOM COFFEE", "Cold Brew", "250 mL"],
    "materials": ["matte paper", "printed ink", "soft cardboard seams"]
  },
  "DETAIL_SYSTEMS": [
    {"object": "coffee beans", "role": "scale and flavor cue"},
    {"object": "condensation on glass", "role": "cold beverage signal"}
  ],
  "OUTPUT": {
    "mood": "clean, trustworthy, commercial",
    "constraints": ["one package only", "no unrelated logos", "readable supplied text"]
  }
}
```

Keys should describe visible subsystems, not software internals. Values should be concrete visual constraints, not praise. Avoid old quality tokens such as `masterpiece`, `best quality`, or `8K UHD`; they do not replace specific visual instructions.

## 15. Edit Prompts Must Preserve Invariants

For image edits, be surgical. State what changes and what stays fixed.

Edit pattern:
```text
Change the scene to a winter evening with soft snowfall, snow dust on the board, cold blue-gray light, and visible breath vapor. Keep the original chess position, board orientation, camera angle, piece identities, and text labels unchanged.
```

Rules:
- Name the target transformation first.
- Preserve identity, layout, position, geometry, text, and readability explicitly.
- If editing a poster, package, or UI mockup, preserve original text unless replacement is requested.
- For localized changes, describe only the masked region plus the invariants around it.
- For multi-image references, identify each input by index and role.

Multi-reference pattern:
```text
Image 1 is the product photo. Image 2 is the color-and-lighting reference. Image 3 is the label artwork. Keep the product shape and camera angle from Image 1, apply the warm studio lighting from Image 2, and place the exact label from Image 3 on the front panel.
```

## 16. Dense Korean, Chinese, And Multilingual Text Needs Extra Guards

The reference set contains Korean-heavy UI, posters, packaging, and public guides. Text-heavy prompts need explicit language and typography constraints.

Rules:
- State the language: Korean, English, Simplified Chinese, Traditional Chinese, bilingual Korean-English, etc.
- Quote every required string exactly.
- Specify which text is largest, secondary, label-size, or fine print.
- Give placement: top header, central title, right-side label, bottom footer, button, chart axis, package side panel.
- Require readable text, consistent typography, no garbled characters, and no duplicate letters.
- Use fewer words if the canvas is small; readability beats text volume.

For bilingual layouts, define hierarchy. Example: Korean headline first, English subtitle smaller below, numerical values aligned right.

## 17. Variant Generation Uses One Changing Axis

When the user asks for multiple directions, do not make random variations. Use `gpt-image-variation-recipes.md` and change one axis at a time.

Available axes:
- Art movement swap: same subject, different shape/color/type/composition system.
- Opposing qualities: warm subject against cool background, order against disruption, premium material against everyday prop.
- Mood to palette: convert mood into three to five HEX colors with a 60/30/10 hierarchy.
- Emotion to visible signal: translate excitement, calm, tension, nostalgia, relief into light, pose, framing, and texture.
- Same subject, different composition: wide, medium, close; front, low three-quarter, top-down; vertical, square, landscape.

For batch output, keep unchanged blocks fixed and vary only the chosen axis. One image per prompt. Do not pack unrelated concepts into one canvas unless the requested artifact is a board.

## 18. Attribution, Safety, And Public-Use Boundaries

Gallery entries may contain curated metadata or outside-source attribution. Preserve attribution when adapting reference material into public docs, README examples, or gallery entries.

Safety and public-use rules:
- Keep real-person likeness edits within the host model and API policy; if moderation rejects a request, report the error plainly.
- Keep fashion/adult-looking prompts tasteful, non-explicit, and non-nude.
- Use fictional brands unless the user supplies a real brand context and the intended use is legitimate.
- Keep public reusable examples original even when they reference a style family.
- For security, prompt-injection, or risk diagrams, keep the framing defensive and explanatory. Do not include operational attack instructions beyond harmless illustrative labels.
- For medical, legal, financial, or public-safety visuals, use cautious wording and avoid presenting generated images as authoritative instructions without review.

## 19. Red-Team Scoring Rubric

Use this 10-point rubric before accepting a prompt or a craft change:

| Area | Points | Red-team question |
|---|---:|---|
| Reference sync | 2 | Does it match the actual `references/` files and current 10x10 gallery structure? |
| Output contract | 1.5 | Does it preserve the seven-block prompt shape and the skill's workflow? |
| Visual specificity | 1.5 | Are vague adjectives replaced with objects, layout, materials, light, camera, and data? |
| Text handling | 1 | Are all required strings quoted, placed, and guarded for readability? |
| Category routing | 1 | Does it tell the writer which category file to open and what to borrow? |
| Edit and variation handling | 1 | Does it cover invariants for edits and one-axis changes for variants? |
| Safety and public-use boundary | 1 | Does it avoid unsafe, misleading, or IP-confusing reuse patterns? |
| Maintainability | 1 | Is it English-only, free of obsolete numbering, and easy to update? |

Score 9 or below: revise before shipping. A 10-point version is synchronized with the real repository, language-consistent, actionable, and strict enough that another agent can follow it without guessing.
