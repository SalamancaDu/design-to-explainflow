---
name: layout-design
description: "Use when Codex needs to design, critique, or refine layouts for posters, covers, social graphics, slides, long images, or video title frames using hierarchy, spacing, alignment, contrast, repetition, proximity, image-text relationships, restrained negative space, and motion-ready composition."
metadata:
  short-description: "Project layout rules for visual hierarchy"
---

# Layout Design

Use this project skill to turn a rough visual request into a clear, readable layout system. It applies to static images made with `imagegen`, design documents, posters, covers, social posts, long images, and HyperFrames title-card or scene layouts.

The skill is based on this project's layout rule extraction from a Japanese layout manual, transformed into original project rules. Do not quote or reproduce the source book; use the rules as design heuristics.

## Boundary with title typography

Use `layout-design` to decide where a title sits, how it relates to images, and how supporting information is arranged. Do not use it to design custom letterforms, font bases, glyph-by-glyph structures, or transparent title PNG assets. Route those to `title-text-design`, then bring the approved title asset back into the layout.

## Core workflow

1. Confirm the medium, audience, intended deliverable, existing assets, and editing needs from available context. Separate exact copy, numbers, units, quotations, and names from wording the user permits rewriting; carry exact content unchanged into later stages.
2. Define the information hierarchy before discussing style:
   - primary information: the message the viewer must notice first
   - main supporting information: date, subtitle, key claim, CTA, or identity
   - secondary supporting information: details that can be read later
   - image or graphic role: subject, atmosphere, proof, decoration, symbol, or navigation
3. Choose one layout pattern from `references/layout-patterns.md` instead of inventing from scratch.
4. Apply the principles in `references/layout-principles.md`: contrast, repetition, alignment, proximity, negative space, image-text relationship, and controlled rule-breaking.
5. Hand composition constraints to `image-style` for bitmap prompts. Keep accuracy-critical text and data geometry in editable typesetting or drawing; a short text string is not automatically safe to bake into a generated image. Provide a layout-only prompt directly when that is the requested deliverable.
6. For motion, state the intended information changes before asset splitting. Build the static composite with real content before detailed choreography or implementation. Motion supports the hierarchy; it must not repair a weak layout.
7. Critique the result with the checklist below before delivery.

## Response and handoff

Scale the response to the task. For a new layout, state the intended route, primary/supporting information, dominant pattern, concrete placement and safe zones, and the visual constraints the next stage needs. Explain material choices briefly.

Use these fields when they help; do not repeat resolved exploration or fill every field for a local edit:

- 主信息 / 辅助信息
- 推荐版式与阅读顺序
- 画面排布、安全区域与图文关系
- 视觉方向：palette roles, typography role, image role, meaningful constraints
- 制作路由与交接：editable elements, needed assets, output requirements

Rewrite titles or labels only when copywriting is requested or permitted. Keep exact text, quoted claims, numbers, units, dates, and names intact. For supplied data, preserve the numeric relationships as well as the labels; missing values or sources must not be invented.

For critique-only, prompt-only, or focused repairs, return that deliverable without a full planning ceremony.

## Handoff route after layout

Choose by final output and internal editability, not by tool name:

| Route | Use when | Handoff |
|---|---|---|
| A 静态整图 / static complete image | A final still mainly needs atmosphere and composition, with no internal editability requirement | `image-style` for needed bitmap direction, then generation or reuse and still-image review |
| B 可编辑静态合成 / editable static composite | A still needs accurate or replaceable text, data graphics, or assets | Bitmap direction as needed, exact typesetting/data drawing in an existing composition tool, then composite and static export |
| C 整帧动效 / whole-frame motion | A flat image only needs camera movement, crop, masks, or added overlays | `motion-style`; no independent control of baked-in content is implied |
| D 逐元素动效 / element-level motion | Subject, title, data, or other elements must move independently | Motion intent before splitting, suitable layers and editable content, static composite, then detailed motion and implementation |

For B/D, identify bitmaps, accurate text/data/lines, and optional custom title assets. Use `title-text-design` only for custom lettering; ordinary typesetting stays in the composition tool. Preserve the user's chosen software and existing project; editable static work does not require HyperFrames.

For D, describe what changes and why, including masking, occlusion, independent shadows, or part-level control when relevant. `motion-style` can help this early decision without requiring a finished composite. Detailed timing follows the static composite.

Carry exact content, placement constraints, asset roles, motion intent if relevant, and requested output into the next stage. Handoffs are quality dependencies, not automatic user approval stages.

## Optional imagegen layering workflow

Use this workflow only when the image will later need motion, editing, element replacement, or reusable layered assets. Do not treat layering as the default starting point for every image.

For a new or complex visual direction, establish a complete aesthetic master before splitting assets; reuse an existing suitable master. It locks palette, light, perspective, texture, and visual scale. The later composite with accurate typesetting/data is the layout-quality benchmark; a text-free master alone cannot prove the final information hierarchy.

Recommended sequence:

1. Create, design, or reuse one suitable master frame and check its aesthetic direction. Wait for approval only at a user-reserved review point.
2. Extract the shared visual rules from the master frame:
   - color palette
   - light direction
   - camera / perspective logic
   - grain, texture, and material language
   - primary visual scale
   - negative-space and safe-zone logic
3. Split only the layers that need motion, editing, replacement, or reuse:
   - `background.png`: no text and no main number, but keeps the same atmosphere, light, and perspective.
   - `subject.png`: the core symbol, person, object, or visual focus; it must share the same light source as the background.
   - editable text and data graphics: accurately typeset or drawn in the composition source; use a separate title bitmap only for checked custom lettering.
   - optional decorations: only necessary bitmap texture or accents; keep meaningful lines, labels, and data relationships editable and split separately moving parts.
   - `composite-preview.png`: final merged preview; judge the design by this composite, not by isolated layers.

Avoid starting from separated layers when no master frame exists. Separate layer prompts tend to optimize each part in isolation, which often creates pasted-on UI, mismatched lighting, weak hierarchy, or cheap tech-panel aesthetics.

## When to load references

- Read `references/layout-principles.md` when designing or critiquing a layout.
- Read `references/layout-patterns.md` when selecting composition structure or adapting a layout to a new format.
- Read `references/prompt-recipes.md` when writing prompts for `imagegen`, HyperFrames, or layout critique.

## Design rules that always apply

- Start from communication: a layout fails if the viewer cannot identify the main message quickly.
- Treat layout as structure, not decoration. Spacing, grouping, and alignment carry meaning.
- Use contrast to create hierarchy, not noise. Contrast may come from space, size, weight, direction, color, texture, or image scale.
- Use repetition to create a system, then introduce one controlled variation to create focus.
- Every visible element must have a relationship with another element: aligned edge, shared axis, repeated shape, shared spacing, or intentional tension.
- Group related information through proximity. Separate unrelated information with negative space.
- Do not fill negative space by default. Empty space can be the main device.
- Break alignment, symmetry, or grid only after the base order is clear.

## Common failure modes

- No primary message: every element competes for attention.
- Decorative style overpowers communication.
- Text blocks float without alignment or grouping.
- Repetition becomes clutter because there is no controlled variation.
- Contrast is added only by making things bigger, bolder, or brighter.
- Negative space is treated as unused space and filled unnecessarily.
- Image and text feel pasted together instead of forming one visual sentence.
- Motion or effects are used to hide a weak static composition.

## Delivery checklist

Use this checklist for layout design, critique, or prompt creation:

- [ ] Primary information is identifiable within 1-2 seconds.
- [ ] Supporting information has a clear reading order.
- [ ] Related items are grouped; unrelated items are separated.
- [ ] At least one alignment system is visible or intentionally implied.
- [ ] Contrast is purposeful and does not damage harmony.
- [ ] Repeated elements create unity without flattening the focal point.
- [ ] Negative space is intentional, not accidental.
- [ ] Image, typography, and graphic elements support the same mood.
- [ ] The layout pattern fits the medium and aspect ratio.
- [ ] Exact content and data geometry match the supplied basis; rewritten copy is limited to the authorized portion.
- [ ] The chosen route matches both final output and internal editing needs.
- [ ] If element-level motion is involved, the composite with real content works before detailed animation is implemented.
