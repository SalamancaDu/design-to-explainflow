---
name: image-style
description: "Use when Codex needs to plan, generate, critique, or refine non-typographic image assets for finance explainer videos, documentary-style videos, video infographics, posters, data graphics, editing cutaway images, object transparent PNG cutouts, background plates, and related imagegen prompts. Do not use as the primary route for custom title typography, glyph design, or transparent title PNG assets; route those to title-text-design."
metadata:
  short-description: "Image style rules for video assets"
---

# Image Style

Use this project skill to create and maintain a coherent image style system for video production assets. It is optimized for finance explainer videos, documentary-style videos, video infographics, posters, data graphics, editing cutaways, object transparent PNG elements, and background plates.

This skill does not generate images by itself. Use it before `imagegen` to decide the asset role, visual direction, prompt structure, constraints, and review criteria.

## Boundary with title typography

Do not use `image-style` as the primary route for title text design. If the user's main task is custom Chinese title typography, font base selection, glyph-by-glyph design, narrative symbol inside letterforms, English / local-language subtitle hierarchy, or transparent title PNG export, route to `title-text-design` first.

Use `image-style` only around title typography when the needed asset is non-typographic:

- background plate behind a title
- poster image or scene that leaves a title-safe zone
- decorative bitmap asset used around typography
- object cutout, texture plate, or visual symbol that is not the lettering itself

Title typography prompts must not inherit the generic image prompt classification headers such as `Use case:`, `logo-brand`, `badge`, or `emblem`. Title preview and export follow title-text-design's requested-deliverable rules; native transparency is preferred, and a separate approval is needed only at a user-reserved checkpoint.

## Core workflow

1. Identify the asset role:
   - video infographic frame
   - poster or cover
   - data chart / data visual
   - editing cutaway image
   - object transparent PNG cutout
   - background plate
   - symbolic illustration
   - documentary chapter visual
   - non-typographic title background or title-safe plate
2. Identify the video context:
   - finance explainer
   - documentary
   - narrative explainer
   - data-heavy segment
   - title card or transition card
   - B-roll support visual
3. Analyze supplied references with `references/reference-analysis.md`, identifying their roles and what should transfer; then choose a fitting visual direction from `references/visual-directions.md`.
4. Choose color, light, texture, and material rules from `references/color-light-texture.md`.
5. Write an `imagegen` prompt using `references/imagegen-prompts.md`.
6. Confirm requested output, actual tool capabilities, and whether each input is a style/composition reference or an edit target. For edits, preserve specified invariants; do not regenerate the whole image to make an unrelated local change.
7. Review output against the checklist below. If the asset is for video editing, make sure it works at video scale, not only as a still image.

## Layout-to-imagegen bridge

Inherit the route selected with `layout-design`; do not re-open settled choices:

- **A 静态整图**: plan a complete still when internal editability is not needed. Reuse suitable assets; generate only required new bitmap content.
- **B 可编辑静态合成**: supply background, subject, or other necessary bitmaps; leave exact text, numbers, data geometry, and meaningful lines to the existing composition tool. Export a still after compositing.
- **C 整帧动效**: a suitable flat image can support whole-frame movement, crop, masks, and added overlays. Do not claim independent motion of baked-in elements.
- **D 逐元素动效**: inherit motion intent before splitting. Establish or reuse a visual master, then supply only bitmaps requiring separate control. Account for occlusion, background completion, shadow separation, and part-level control when movement requires them.

For B/D, hand off asset roles, actual paths when generated, master/reference roles, placement constraints, and preserved palette/light/perspective/material rules. A static composite with real text and data must be checked before detailed animation. HyperFrames is one possible implementation, not a prerequisite for editable static output.

## Accuracy and transparent assets

Keep supplied wording, numbers, units, dates, quotations, and names exact unless rewriting is authorized. For real charts, lengths, areas, positions, scales, and relationships must be drawn from explicit data and mappings using an appropriate deterministic tool. Image generation may supply atmosphere, textures, or symbolic illustrations around them. A mechanism diagram must be identified as schematic and must not imply unsupported ratios or factual evidence.

For transparent assets, prefer the selected tool's native transparency and inspect actual alpha and edges on intended backgrounds. Use chroma-key removal only when native transparency is unavailable or an inspected result needs that alternative; do not request key-color plates by default. Preserve valid glyph/subject structure when exporting a checked design.

If missing information materially changes output or editability, ask only for that gap; otherwise infer from the brief and state material assumptions.

## Optional layered PNG workflow

Use layered PNG output only when it has a production purpose: motion, video editing, reusable assets, later text replacement, or separate element control. For pure mood exploration or one-off still images, a single complete image is usually better.

For a new complex direction, establish the visual master before generating separate layers. Reuse a suitable master or existing layers when available. Its review is an internal quality check unless the user reserved approval. Layering serves actual editing or movement needs.

Recommended output package:

```text
outputs/images/<project-name>/
├─ background.png
├─ subject.png
├─ title.png              # optional checked custom lettering; ordinary text stays editable
├─ decorations.png
├─ composite-preview.png
└─ prompt.md
```

Layer rules:

- **Master frame**: the selected reference for color, light, lens, texture, atmosphere, and primary visual scale. A text-free master does not establish final typography or data layout.
- **Background**: remove text, logos, and main numbers; preserve atmosphere, perspective, lighting, and overlay-safe zones.
- **Subject**: isolate only the main symbol, person, object, or visual focus; keep the same light direction and material language as the master frame.
- **Text and data**: typeset exact text and draw real data geometry in the chosen composition source. A checked custom title bitmap is optional; preserve exact source text and separate characters only if motion needs that control.
- **Decorations**: keep only accents that support motion or emphasis; avoid decorative HUD frames, cheap glow panels, unnecessary tech lines, and baked-in data cards.
- **Composite preview**: inspect the merged frame with real content. Final quality is judged by this composite, not isolated layers. Use the project/run directory already chosen rather than creating a second output tree.

Failure signal: if the layered result looks worse than the direct master image, return to the master frame, extract its visual rules again, and reduce decorative layers before regenerating.

## Always apply these constraints

- Avoid oily AI gloss, cheap tech aesthetics, excessive cyberpunk, and blue-purple default palettes.
- Prefer restrained, editorial, documentary, handmade, or illustration-led visual language unless the specific video needs another tone.
- Do not default to photography. Use photography only when the brief explicitly needs realism or documentary evidence.
- For finance content, make visuals credible before making them flashy.
- For data graphics, clarity is more important than decorative density.
- For transparent PNG elements, keep silhouettes clean, avoid soft shadows unless they are removable, and preserve usable padding.
- For transparent title PNG assets, do not use this skill as the main process; use `title-text-design` for typography and use `image-style` only for supporting background, texture, or non-text symbols.
- For background plates, keep enough calm space for titles, subtitles, charts, or motion overlays.
- Match `layout-design` for hierarchy and composition whenever the asset contains text or will become a video frame.

## Common asset decisions

- **Infographic frame**: prioritize hierarchy, large readable labels, restrained palette, and strong negative space.
- **Poster / cover**: use a stronger focal symbol and a more memorable composition.
- **Data graphic**: draw true numeric relationships from verified inputs; use a visual metaphor only as a clearly schematic supporting layer, not as a substitute for correct geometry.
- **Cutaway image**: make it fast to read in 1-2 seconds; avoid dense small details.
- **Object transparent PNG**: isolate one object, symbol, paper scrap, annotation mark, icon-like object, chart element, or handmade accent. For title typography PNGs, use `title-text-design`.
- **Background plate**: avoid busy texture in text zones; provide a clear foreground/midground/background logic.

## Delivery checklist

Use this checklist for prompt creation, critique, and final asset selection:

- [ ] Asset role is explicit.
- [ ] Visual direction matches the video's tone.
- [ ] The asset is readable at video scale.
- [ ] Color palette avoids default blue-purple tech clichés unless intentionally requested.
- [ ] Texture feels editorial or handmade, not AI-glossy.
- [ ] If finance-related, the image feels credible and restrained.
- [ ] If documentary-related, the image supports atmosphere without fake evidence.
- [ ] If transparent PNG, expected transparent pixels actually exist, edges are clean on intended backgrounds, and the object has useful padding.
- [ ] If background, there is reserved space for overlays.
- [ ] Positive instructions specify desired palette, lighting, texture, and spatial relationships; negatives are limited to relevant failure modes.
- [ ] Exact text and true data geometry are assigned to appropriate editable production.
- [ ] Required generated assets have real project paths, dimensions, and checked transparency; prompt-only work is not reported as generated output.
