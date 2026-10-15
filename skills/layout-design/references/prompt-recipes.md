# Prompt Recipes

Use these templates when translating layout rules into `imagegen`, HyperFrames, or critique prompts.

## Imagegen layout prompt

Use for A 静态整图 or a non-typographic visual concept. For B 可编辑静态合成 and D 逐元素动效, send only needed bitmap composition constraints to image-style, then typeset exact content and draw data geometry in the composition tool. C 整帧动效 can reuse a suitable flat image.

```text
Purpose: <poster / cover / social graphic / visual concept>
Aspect ratio: <1:1 / 3:4 / 4:5 / 16:9 / 9:16>
Primary information: <what must be seen first>
Supporting information: <what is read second>
Image / graphic role: <subject / symbol / atmosphere / guide / texture>
Layout pattern: <choose one pattern from layout-patterns.md>
Composition: <describe placement, scale, negative space, alignment, and reading path>
Typography direction: <large title / editorial / geometric / handwritten / restrained / type-as-image>
Color direction: <restrained base + accent / monochrome / muted / high contrast / gradient>
Mood: <calm / refined / urgent / playful / mysterious / ceremonial / technical>
Text (verbatim): "<exact short text only if necessary>"
Constraints: clear hierarchy, intentional negative space, aligned visual relationships, no clutter
Avoid: generic template look, random Japanese clichés, dense tiny text, unrelated decorative elements, watermark
```

When text accuracy or editability matters, typeset it in the project even if it is short. Preserve exact supplied text, units, names, and quotations. Real charts require data-driven geometry, not only correct labels. Route custom lettering to title-text-design and preserve its prompt rules.

## HyperFrames layout brief

Use for layout handoff to a chosen HyperFrames implementation. Resolve the project's actual version and matching entrypoint before coding; implementation selection is described by the [motion handoff reference](../../motion-style/references/hyperframes-motion-brief.md). Reuse an existing brief and do not restart resolved exploration.

```text
Composition: <video title / opener / section card / caption scene / transition scene>
Canvas: <1920x1080 / 1080x1920 / other>
Duration: <seconds>
Primary information: <main text or visual>
Supporting information: <subtitle, date, label, CTA>
Layout pattern: <choose one pattern from layout-patterns.md>
Hero frame: <static end-state layout before animation>
Reading order: <first -> second -> third>
Motion role: <reveal hierarchy / emphasize rhythm / guide eye / transition mood>
Visibility logic: <what is visible initially, what enters, and how changes follow the reading order>
Typography: <font mood, weight, scale, alignment>
Color: <palette roles and contrast>
Constraints: layout works when paused; motion follows information relationships; cuts or transitions fit the narrative
Avoid: animating everything equally, generic gradients, full-page spinner, unreadable small text
```

## Layout critique prompt

Use this when reviewing an existing image, screenshot, poster, or video frame.

```text
Critique this layout using layout-design.
Check:
- primary information clarity
- reading order
- grouping and proximity
- alignment system
- contrast quality
- repetition and variation
- negative space use
- image-text relationship
- suitability for the medium and aspect ratio
Return:
- strongest layout decision
- evidence-backed layout problems, or explicitly none
- specific revision plan
- rewritten imagegen or HyperFrames prompt if useful
```

## Quick repair patterns

Use these when a layout feels wrong:

- If everything competes: reduce to one primary element, one support block, one graphic role.
- If it feels scattered: group related text, align edges, and create one visible axis.
- If it feels boring: keep the grid but add one asymmetry, crop, diagonal, or texture contrast.
- If it feels crowded: remove decorative elements before reducing text size.
- If it feels empty: assign a job to the negative space instead of filling it.
- If image and text feel unrelated: align text to an image edge, object direction, or empty image zone.
- If motion feels noisy: return to the static hero frame and animate only the reading path.
