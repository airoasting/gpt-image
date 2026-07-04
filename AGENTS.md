# AGENTS.md

## Project Goal

This project is a Korean guide website for writing image generation prompts.
The site should feel like a professional, practical guidebook for Korean users who want to turn their ideas into prompts they can paste directly into GPT image generation tools.

The current site structure is:

1. 7가지 원칙
2. 이미지 생성 도움창
3. 레퍼런스 갤러리

Do not add back the removed formula-by-category section unless the user explicitly asks for it.

## Product Positioning

- Page title: `GPT 이미지 생성 프롬프트 가이드`
- The site is not a CLI guide.
- The site is not a generic model-version prompt page.
- The site is a Korean image generation prompt guidebook.
- The primary user is a Korean speaker who wants practical prompt-writing help without technical friction.

## Core Prompt Framework

The whole guide must align to these 7 principles, in this exact order:

1. 결과물 유형을 정하기
2. 주 피사체를 고정하기
3. 구도와 비율을 지정하기
4. 맥락과 배경을 설명하기
5. 스타일과 매체를 선택하기
6. 빛과 디테일을 구체화하기
7. 정확성 조건을 덧붙이기

The prompt builder must also follow this same order:

1. 결과물 유형
2. 주 피사체
3. 구도와 비율
4. 맥락과 배경
5. 스타일과 매체
6. 빛과 디테일
7. 정확성 조건

Use pill buttons numbered `01` through `07` for the builder fields so they visibly match the 7 principles.

`조명` and `카메라 시점` are sub-controls under principle 06, `빛과 디테일`.

## Korean Copy Rules

- Use natural, professional Korean.
- Match subject and predicate clearly.
- Avoid translated or stiff phrasing.
- Never use the previously banned two-syllable Korean term that means "flow" in site copy, prompts, comments intended for display, or generated guide text.
- Avoid casual filler such as `있으면 좋음`, `알아서`, `너무 이상하지만 않게`, or explanatory notes inside example prompts.
- Bad prompt examples should look like actual weak prompts, not like commentary about why they are weak.
- Good prompt examples should be specific enough to be directly useful.

Preferred wording style:

- Use `차례대로 정리하면` instead of vague process wording.
- Use `이미지 생성용 프롬프트 만들기` for the builder title.
- Use `갤러리` for the hero link to the gallery.

## Typography Rules

- Korean text must use Pretendard.
- English and numbers must use a site-appropriate Latin font. The current selected Latin font is Archivo.
- Keep fonts unified through CSS variables:
  - `--font-latin`
  - `--font-korean`
  - `--font-site`
- Do not reintroduce mixed decorative fonts such as serif display fonts unless the user explicitly asks.
- Do not use monospace for number pills or normal UI labels.

## Visual Design Rules

The site follows a professional "Sunshine Yellow" guidebook style:

- Warm paper background
- Sunshine yellow highlights
- Deep indigo text and linework
- Thin indigo borders
- Sharp or lightly restrained corners
- Editorial, practical, guidebook-like composition

Avoid:

- Fantasy/game-like hero art
- Cute character-heavy banners
- Heavy gradients as the main design language
- Decorative orbs/blobs
- Overly rounded card-heavy UI
- Random bright yellow blocks that do not serve the layout

## Hero Image Rules

The hero image should match the site design and purpose:

- Professional editorial flat-lay or guidebook workspace
- Prompt cards, reference thumbnails, prompt builder panel, color swatches, and paper texture are appropriate
- Use sunshine yellow and indigo
- Avoid readable generated text inside the image when possible
- Avoid logos, brand names, malformed typography, and game/fantasy characters

Current hero asset:

- `guide-site/assets/gptimage2skill-banner.png`

## Principle Example Image Rules

The 7 principle cards use 14 generated images:

- `guide-site/assets/principles/principle-01-weak.png`
- `guide-site/assets/principles/principle-01-strong.png`
- ...
- `guide-site/assets/principles/principle-07-weak.png`
- `guide-site/assets/principles/principle-07-strong.png`

Rules for these images:

- Use the same comparison logic across all 7 principles.
- Bad examples should visibly feel vague or under-specified.
- Good examples should visibly feel specific and controlled.
- The image files themselves must not contain external borders, labels, captions, UI chrome, or split-screen frames.
- Any comparison labels belong in HTML/CSS, not inside the image.

## Layout Rules

- Section order must be:
  1. 7가지 원칙
  2. 이미지 생성 도움창
  3. 레퍼런스 갤러리
- The gallery stays at the bottom.
- The prompt builder output box should align visually with the left form on desktop.
- Long prompt output must scroll inside its panel.
- Gallery cards should show sample images in a 3-column desktop grid with consistent image size.
- Clicking a gallery item opens a modal with the full prompt.
- Prompt text inside the modal must be scrollable.

## Gallery Rules

- Curate the source references down toward 100 strong examples.
- Remove clearly Chinese-style references first unless the user asks to restore them.
- Keep gallery categories MECE and practical; avoid many tiny source-folder categories.
- Gallery modal must show:
  - image
  - metadata
  - full prompt
  - copy prompt button
  - `MD 다운로드` button
- Do not rename `MD 다운로드` back to the old "original MD" label.

## Implementation Notes

- The static site is in `guide-site/`.
- Main files:
  - `guide-site/index.html`
  - `guide-site/styles.css`
  - `guide-site/script.js`
  - `guide-site/gallery-data.js`
- The downloaded source repo is `GPT-Image2-Skill/`.
- Gallery image paths depend on serving from the project root, not only from `guide-site/`.
- When previewing locally, run the server from the project root.

## Verification Checklist

Before finishing any site change:

- Run a JavaScript syntax check on `guide-site/script.js`.
- Search to make sure forbidden or outdated copy did not return:
  - the previously banned two-syllable Korean term that means "flow"
  - outdated model-version wording
  - removed category-formula section labels
  - the old "original MD" label
- If layout changed, preview the page in a browser and check desktop width.
- Stop any local preview server before finishing.
