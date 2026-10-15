# Text and Emphasis Motion

This project does not default to bottom lyric subtitles. Use on-screen text only when it helps explain, label, emphasize, or structure the video.

## Text roles

- title
- section label
- keyword
- number
- short quote
- chart label
- handwritten note
- warning / risk marker
- source or context label

## Emphasis patterns

### Keyword highlight

Use for one important phrase.

Motion:

- text appears normally
- muted marker sweep or underline passes behind/under it
- hold long enough to read

Best for:

- finance terms
- turning points
- definitions

Avoid:

- highlighting every word
- neon glow highlights

### Word-by-word reveal

Use only for short phrases when narration rhythm matters.

Rules:

- reveal 3-8 words maximum
- each word appears on a stable baseline
- no bouncy word effects
- final phrase must hold as a complete thought

### Handwritten annotation

Use for reasoning, evidence, or “look here” cues.

Motion:

- circle draw
- arrow sketch-in
- underline sweep
- margin note slide
- paper label pin

Rules:

- keep marks simple
- use one annotation color per scene
- do not cover the primary text

### Data emphasis

Use for numbers or changes.

Motion:

- for a staged build, shape → number → conclusion is one useful sequence
- for an existing readable chart, retain shape and labels from the start and emphasize only the relevant item
- reveal labels together with geometry when their relationship is needed for interpretation

Rules:

- do not count every number unless the count itself is meaningful; real values, geometry, units and scales must remain tied to supplied data
- during quantitative growth or counting, synchronize visible values and geometry, or make the reveal clearly non-quantitative; do not show a final value against a misleading intermediate length or area
- avoid fake precision
- keep labels large for video

## Typography motion rules

- Do not animate text layout properties that cause reflow unpredictably.
- Prefer reveal masks, opacity, y movement, or clip-path.
- Keep final text position defined by static layout.
- For HyperFrames, position the hero frame first, then animate from/to it.
