---
name: title-text-design
description: "设计或拆解标题字形与标题图像提示词。适用于海报标题、片头字卡和透明标题资产；普通正文排版不使用。"
---

# Title Text Design

Use this skill to turn a topic, reference image, or visual direction into a controlled title typography system. Prioritize title-as-symbol: the title should visually carry the theme, not merely label it.

This skill preserves a method, not a fixed style library. Do not turn prior cases such as tropical travel, crime, fish markets, ocean, India, Seoul, football, deep charcoal, bone-white print, tactical lines, square heavy block lettering, modern title handwriting, dry-brush lettering, or grunge wear into defaults. Treat them as examples of theme-to-symbol and theme-to-font reasoning only.

## Design and delivery

Use the following design checks to produce the requested title asset or prompt. They are quality dependencies, not automatic user approval stages; scale exploration and explanation to the request. This entrypoint owns delivery and review conditions; references provide methods and examples under those conditions. For an existing selected title, export or local edits preserve its glyph structure and only recheck affected requirements instead of reopening the design.

1. **Role and context**: define asset role, usage, audience, background, language needs, and production stage.
2. **Theme diagnosis**: extract the central narrative tension, place/person/event cues, emotion, and what abstract content must not enter image generation directly.
3. **Narrative symbol**: for requested exploration, offer distinct candidate routes with symbolism, glyph integration, subtitle role, font base, palette/material direction, and risks. For a complete deliverable, choose a fitting route from the brief without requiring unused alternatives.
4. **Font exploration gate**: for open themes, the candidate routes must include visibly different lettering skeletons. Do not let every option become square heavy block / wide heavy black. Include a modern film-title handwriting or dry-brush route when it plausibly fits the theme.
5. **Route decision**: preserve the user's chosen route. For authorized complete delivery, choose a fitting route if none is supplied and briefly state material assumptions. Wait only for a user-reserved selection or a consequential unresolved choice.
6. **Font base gate**: lock the lettering skeleton for the selected route before texture, motif, or image prompt.
7. **Glyph-by-glyph design gate / 逐字字形设计关**: define each character's role, dominant strokes, silhouette, negative space, motif entry point, and inter-character relationship before writing an image prompt.
8. **Visual memory gate / 视觉记忆点门禁**: confirm the title has one memorable visual idea from the current topic that remains recognizable when the asset is reduced. If the idea is only a tiny line, faint texture, slight gravity shift, or mood word, go back to narrative-symbol routing.
9. **Controlled theme-anchor gate / 受控主题锚点门禁**: avoid clichés, but do not delete every topic cue. Preserve 1-2 low-density structural anchors derived from the current theme; never turn an old case's motif into a default.
10. **Image-generation executability gate / 生图可执行性门禁**: decide whether the design can be rendered by image generation. If it depends mainly on tiny percentage changes, micro-cuts, or very subtle spacing, strengthen the visible structure or choose a font draft / handwriting draft / vector rough path first.
11. **Anti-overblocking gate / 反过度禁用门禁**: ensure positive design instructions dominate. If the prompt is mostly no / avoid / do not and the positive symbol is weak, rewrite the concept before prompt output.
12. **Variant rules**: define allowed glyph changes and forbidden changes.
13. **Preview prompt**: use a neutral-background flat 2D preview when useful for design checks or requested review. It is not a mandatory separate-turn deliverable.
14. **Visual QA**: reject 3D, logo clichés, generic grunge, wrong characters, over-literal scenes, weak narrative symbol, missing visual memory point, missing controlled theme anchor, missing required subtitle layer, missing glyph-by-glyph plan, imagegen-unfriendly micro-adjustment-only design, overblocked prompts, over-reused square-heavy-block font defaults, and low readability.
15. **Export**: when transparent output is requested, complete the requested asset or prompt using the selected tool's native transparency where available. Use chroma-key instructions only when native transparency is unavailable or an inspected result needs that alternative. Preserve the selected glyph structure and exact text; inspect actual alpha and edges on the intended background. Wait for preview approval only when the user reserved that review; actual generation and paid calls retain their authorization boundaries.

If the user asks for a transparent PNG and an imagegen prompt in the same request, complete both requested outputs using an available authorized capability. Keep preview and export instructions distinct when both are useful. If only prompts are requested or generation is unavailable, provide the requested prompts and state the actual delivery limitation.

## Reference image use

Use references to extract design logic, not to copy surface style.

- Extract: how the title compresses a theme into glyph structure, motif, subtitle, material, and layout hierarchy.
- Do not extract as defaults: exact color palette, texture, regional symbols, decorative objects, font category, or motif type.
- When a reference has English or local-language text, decide whether the current title also needs a secondary language layer. Do not add pseudo-English.
- When a reference has a strong symbol, ask what equivalent symbol the current topic deserves instead of reusing that symbol.

## Role and stage control

- Use **title-card typography asset** for end-credit titles, chapter cards, cover titles, and transparent PNG text assets.
- Use **poster headline** for titles integrated into a poster composition.
- Use **scene overlay** for text placed on photo/video footage.
- Use **logo / badge / emblem** only when the user explicitly asks for a logo-like identity.
- Never use 'Use case:' classification headers in imagegen prompts for title assets. These headers push the model toward template categories and should be removed entirely. Also never use 'logo-brand', 'badge', 'emblem', or 'team logo' unless the user explicitly asks for a logo-like identity.

## Narrative symbol gate

A 主叙事符号 is the one visual idea that makes the title about this topic, not just a nice type treatment.

For requested exploration of open or abstract themes, use the following route fields; choose the number of alternatives to match the user's request. For complete delivery, use these fields only as needed to choose and explain the selected route:

- **Route name**: concise visual premise.
- **Symbolic meaning**: what the route says about the topic.
- **Glyph integration**: where it enters the characters: inner counters, stroke cuts, baseline, line overlay, one replaced stroke, frame, negative space, or subtitle relationship.
- **Subtitle layer**: whether Chinese-only, English subtitle, local-language line, number/date, or no secondary text is appropriate.
- **Font base direction**: the skeleton supporting the route. When comparing alternatives, vary the skeletons rather than repeating a square-heavy-block direction.
- **Palette/material direction**: broad direction only, not locked style unless selected.
- **Risk**: what may become literal, cliché, unreadable, or off-tone.

Default behavior:

- If exploration is requested, deliver useful alternatives in the requested scope. Wait for selection only when the user reserved that choice or a consequential unresolved choice cannot be responsibly inferred. A broad topic alone does not create a review checkpoint.
- If the user asks for direct execution or complete delivery, choose a fitting route and continue; include alternatives only when they help explain a material tradeoff.
- If the user gives a specific route, do not generate unnecessary alternatives; use it and proceed.
- If the user says the outputs all look like the same font, stop prompt iteration and return to font exploration first.

## Font exploration gate

Use this gate to prevent hidden font defaults. For open themes, font exploration is part of the concept stage, not polish.

- Compare visibly different font-base directions when exploring alternatives; preserve a supplied font and do not impose a minimum candidate count on complete delivery.
- Do not use square heavy block / wide heavy black for every route. No more than two candidates should share the same broad skeleton.
- Include at least one non-block direction when suitable: modern film-title handwriting, bold dry-brush title lettering, Song/Ming stele, ticket-stamp lettering, vintage signboard, stencil, or local-script hybrid.
- For each font candidate, explain what it changes in emotion, readability, motif integration, and production risk.
- Justify the chosen skeleton against the topic and readability needs. Compare another direction when the rationale is weak; do not reject a suitable block font merely to avoid a default.

### Modern film-title handwriting / dry-brush route

Use this route for human, travel, fate, injury, memory, comedy-with-bitterness, regional, migration, conflict, and emotionally driven documentary titles. It is not traditional calligraphy by default.

- **Look**: contemporary handwritten title lettering, strong brush pressure, fast strokes, dry-brush flying-white, broken ink edges, irregular but controlled character rhythm.
- **Motif integration**: theme elements can hide naturally in stroke tails, dry-brush gaps, ink breaks, one pictorial stroke, seals, small English subtitles, or local-language notes.
- **Prompt language**: say modern film-title handwritten Chinese lettering or bold dry-brush title lettering; avoid generic Chinese calligraphy unless a classical calligraphic tone is intended.
- **Risks**: fake calligraphy, wuxia/ancient-drama tone, illegible characters, cheap brush font, random splatter. Keep exact text accuracy and thumbnail readability as hard gates.
- **Precision path**: for final Chinese assets, prefer a real handwritten base, selected font, or vector rough before image generation when exact characters matter.

## Font base gate

For new lettering, specify the base skeleton before texture or motif; existing-title export or local edits preserve the selected skeleton:

- **Base category**: modern heavy block Chinese, wide compressed heavy block, modern film-title handwriting, bold dry-brush title lettering, Song/Ming serif, brush calligraphy, stencil, vintage signboard, ticket-stamp lettering, condensed Latin, script Latin, or local-script hybrid.
- **Shape metrics**: width, weight, center of gravity, spacing rhythm, stroke endings, corners, inner counters, and contrast.
- **Route fit**: explain why this skeleton supports the selected narrative symbol.
- **Reference direction**: describe a font family direction when useful, but do not claim image generation can call a real font file.
- **Precision path**: when exact Chinese characters are critical, prefer rendering a base title from a selected local font and use image generation only for controlled surface treatment or reference exploration.

## Glyph-by-glyph design gate / 逐字字形设计关

Use this gate when designing or substantially rebuilding lettering. A font style word is not enough: define how every character contributes to the title system before generating new glyphs. For export or a local edit of an existing selected title, reuse its structure/reference and preserve invariants rather than inventing a new per-character design.

For each main-title character, specify:

- **Role**: visual anchor, rhythm carrier, narrative carrier, opening force, closing weight, or support.
- **Dominant stroke**: the stroke direction, length, pressure, speed, and ending that should define the character.
- **Silhouette**: the outer contour, crop, width/height, tilt, exaggeration, and thumbnail shape.
- **Gravity and proportion**: character weight, center of gravity, width, height, density, and spacing.
- **Negative space / counters**: which inner spaces remain open, compressed, cut, or used as a motif entry.
- **Character relationship**: overlap, connection, air gap, baseline rhythm, shared stroke direction, and visual breathing.
- **Motif entry point**: at most one or two characters should carry the key motif. The motif must enter a stroke, counter, cut, or negative space; it must not be pasted on top after the font is generated.
- **Readability boundary**: what must not change because it would break the exact Chinese character.

When designing new modern film-title handwriting / dry-brush lettering, name the dominant stroke and ending for every character before discussing flying-white texture. If the output only says "modern handwriting", "dry brush", "heavy strokes", or "cinematic" without per-character structure, go back to this gate and do not expose an imagegen prompt.

Reference-level threshold:

- From far away, the title has a strong silhouette and not just brush texture.
- Up close, every character has a design role and a controlled difference.
- The strongest narrative symbol is concentrated in one structural entry point.
- The subtitle or local-language layer is designed as hierarchy, not decoration.
- The prompt can explain why each character looks different; if it cannot, the design is not ready for image generation.

## Pre-prompt viability gates / 生成前通用门禁

For new or substantially redesigned lettering, apply these gates after the glyph plan and before its production prompt. For a selected existing title, check only affected requirements and preserve its design. The method is topic-agnostic: derive motifs, palette and texture from the current subject rather than historical examples.

### Visual memory gate / 视觉记忆点门禁

Every title must have one clear visual memory point from the current topic. It may be a line logic, negative-space move, subtitle relationship, local script layer, structural cut, emblematic detail, material mechanism, or one pictorial stroke. It must remain identifiable when the design is reduced.

Reject or reroute when the memory point is only a mood word, a barely visible line, a slight weight shift, generic texture, or a weak decorative accent.

### Controlled theme-anchor gate / 受控主题锚点门禁

Avoiding clichés must not erase the topic. Keep 1-2 controlled theme anchors that are structural, sparse, and derived from the current theme. A theme anchor can enter through a counter, stroke cut, baseline, frame, subtitle layer, local note, small diagrammatic trace, or one replaced stroke.

Do not paste theme objects on top of finished type. Do not forbid every topic cue unless the intended result is intentionally abstract and the user has accepted that risk.

### Image-generation executability gate / 生图可执行性门禁

Before writing a prompt, test whether image generation can plausibly render the design. If the design depends mainly on 3-5% gravity shifts, 5-8% stroke extensions, micro bevels, very fine lines, subtle spacing, or tiny texture differences, it is probably too subtle for image generation alone.

When executability is weak, either strengthen the visible structure, simplify the character plan, or move to a precision path: selected local font, handwritten base, vector rough, or post-generation typography editing.

### Anti-overblocking gate / 反过度禁用门禁

Negative constraints prevent drift; they should not become the design. The positive prompt must clearly state the visual premise, font base, character plan, theme anchor, hierarchy, palette, and material. If the avoid list is longer and more vivid than the desired design, rewrite the positive design before adding avoid terms.

## Theme translation rules

Abstract theme words may appear in design language, but must be translated before image generation. The translations below are examples, not defaults.

- 困境 / 压力 → weight, compression, blocked rhythm, lowered center of gravity. Do not directly prompt dirt, mud, collapse, or disaster unless required.
- 进步 / 追赶 → controlled directional rhythm, sequence marks, time progression, repeated steps. Do not default to stairs, trophy, upward arrows, or victory scenes.
- 代际 / 传承 → layered traces, repeated marks, archive rhythm, small-to-large scale shifts. Do not default to children, family portraits, or literal crowds.
- 地域 / 城市 → map logic, skyline fragment, street grid, local sign system, dialect or local script layer. Do not create a full city illustration inside every stroke.
- 节庆 / 市井 → gesture, hand-drawn line, crowd rhythm, food/tool/object cue, color contrast. Do not let decorative figures overwhelm the title.
- 犯罪 / 悬疑 → evidence mark, cut line, surveillance crop, file stamp, cold spacing. Do not default to blood, weapons, police tape, or horror clichés.
- 海洋 / 鱼市 / 热带等参考题材 → only use when the current topic demands them; never carry them into unrelated themes.

## English / local-language subtitle layer

Decide the secondary language layer intentionally.

Use it when it improves documentary tone, international readability, chapter structure, regional authenticity, or hierarchy. Do not add it only because references have English.

If included, specify:

- Exact subtitle text once.
- Function: explanation, poetic counterpoint, chapter label, location/date, or rhythm line.
- Typography: condensed uppercase, small caps, monospaced archival, handwritten script, local script, etc.
- Placement: under title, through baseline, inside frame, vertical side note, or small top label.
- Restraint: subtitle must support the Chinese title, not become random decorative pseudo-text.

## Output adapted to the requested deliverable

Show the design decisions that affect the requested result, not a fixed thirteen-section report.

- **Exploration requested**: compare a suitable number of genuinely distinct narrative-symbol and font-base routes. Include meaning, glyph integration, subtitle role, emotional/readability tradeoffs, and production risk. Wait only if the user reserved selection.
- **Complete new title design**: choose a fitting route, state the core judgment, exact text and language layers, font skeleton, per-character structure, theme anchor, palette/material, and permitted transformations. Carry out the quality checks below; explain only material decisions and risks.
- **Prompt-only request**: deliver the requested production prompt(s), keeping accurate text, selected structure, and actual tool capability explicit. Do not claim an image or alpha has been inspected when only prompts exist.
- **Transparent title asset**: generate/edit and deliver the actual asset when authorized and available, using native transparency where supported. A neutral preview can help quality checks but is a separate approval stage only when reserved by the user.
- **Existing title export or focused edit**: preserve selected glyph structure, exact text, motif, subtitle, and palette. Reuse the existing plan/reference and report the requested change without a new exploration set.

For a new lettering prompt, include enough visible character structure to execute; keep the extensive reasoning in the design explanation instead of burying the prompt in process labels. When requested, provide both the production prompt and final asset path. If a required generation/export capability is unavailable, deliver the independent work and state the actual missing output.

Preview and export instructions must describe their actual purpose. A native-transparent result may be composited on a neutral background for inspection without regenerating or redesigning its glyphs.

## Prompt lint before output

Before exposing any imagegen prompt, audit and rewrite it until it passes:

- **Stage**: match the requested deliverable. Keep preview and export purposes distinct; wait for preview approval only at a user-reserved checkpoint. Prefer native transparent export when available, preserve the selected design, and do not claim unperformed visual or alpha checks.
- **Role**: title asset → say title-card typography asset or title text asset. Do not include any 'Use case:' header. Do not say logo-brand, badge, emblem, or team logo unless requested.
- **Narrative route**: prompt must reflect the selected route. Do not reuse a previous case's motif, palette, or texture by default.
- **Font diversity**: avoid habitual font defaults. Compare alternatives when exploration is requested or the selected skeleton has a concrete weakness; a completed route does not require a separate exploration set.
- **Font base**: name the skeleton and describe width, weight, gravity, stroke character, counters, and spacing.
- **Glyph design**: for new lettering, include the executable character-by-character structure: role, dominant stroke, silhouette, negative space, motif entry point, character relationship, and readability boundary. Style words alone are insufficient. For export or a focused edit, reference the selected title and preserve this structure instead of redesigning it.
- **Visual memory**: identify one memorable visual idea from the current topic. If it is only a mood word, tiny line, weak accent, or subtle micro-adjustment, return to narrative-symbol routing.
- **Controlled theme anchor**: keep 1-2 structural topic anchors after removing clichés. Do not remove all topic cues unless the user accepted a deliberately abstract result.
- **Image-generation executability**: confirm the design is visible enough for image generation. If it depends mainly on micro percentages, very fine lines, or subtle spacing, strengthen the structure or use a font draft / handwriting draft / vector rough path.
- **Avoid balance**: positive instructions must be stronger than the avoid list. If no / avoid / do not dominates the prompt, rewrite the positive design.
- **Motif density**: use one clear motif route with controlled density. Keep title body readable; do not create complete scenes, diagrams, cityscapes, crowds, pitch maps, or object collages inside every stroke.
- **Subtitle**: if English or local-language text is required, state exact subtitle text once and specify typography. If not required, say no subtitle / no extra words. Never allow pseudo-text.
- **Texture**: positive prompt may use flat print, screen-print wear, ink grain, archival film grain, edge abrasion, paper fiber, ink bleed, brush dry edge, or other 2D surface cues that fit the selected route. Do not positively prompt mud, dirt, cracked concrete, ancient texture, generic grunge texture, stone, metal, bevel, extrusion, or heavy shadow unless explicitly selected for the project.
- **Text accuracy**: exact title text must be stated once, with no watermark, pseudo-text, or unintended extra words.
- **Template-header check**: remove classification headers such as 'Use case: stylized-concept', 'Use case: logo-brand', 'Asset type:' when they are not needed. Express the asset role in the first sentence instead.
- **Rewrite rule**: if a prompt fails any item, rewrite the prompt; do not merely add negative words at the end.

## Reference

Read references/title-text-system.md when the task needs deeper style selection, narrative-symbol route examples, font-base examples, prompt templates, or transparent PNG workflow details.
