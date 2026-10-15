# Review Checklists

Use the checklist matching the current stage. Combine checklists only when needed.

## Universal gate

- Asset role is explicit.
- Current stage is explicit.
- Proposed next stage is explicit.
- The artifact contains enough information to judge.
- The strongest visual decision is clear.
- Any blocking issue is supported by observed evidence; a clean review can report none.
- The output fits the intended tone and medium.
- The output avoids known project dislikes: oily AI gloss, cheap tech, excessive cyberpunk, blue-purple neon, variety-show effects, generic stock look.
- The next step is justified, not automatic.

## Prompt gate

Use before generation or motion execution.

- Asset role is stated in normal language, not unnecessary template headers.
- Medium, target format, and current stage are clear.
- Positive prompt is specific and not polluted by forbidden concepts.
- Avoid-list does not merely contradict a risky positive prompt.
- Text handling is realistic for image generation.
- For title assets: no generic Use case header; no logo/badge/emblem unless requested; font base is specified.
- For transparent assets: instructions match the requested stage and actual capability; native alpha is preferred when available, with no automatic extra preview-approval stage.
- Prompt avoids vague words like “高级一点” without explaining how.
- Prompt avoids unrelated objects, styles, and literalized metaphors.

## Typography / title gate

Use with `title-text-design`, title-card previews, generated title typography, and transparent title PNG assets.

- Exact title text is correct: no wrong character, missing stroke, extra stroke, pseudo-text, watermark, or unintended subtitle.
- For new custom lettering, glyph design / 逐字字形 is visible rather than only a generic surface treatment; export or local edits preserve the selected existing structure.
- Font base matches the chosen route rather than defaulting to square heavy block, generic calligraphy, sports logo, game title, 3D, bevel, stone, metal, or thick shadow.
- New lettering has deliberate character roles, strokes, silhouette, negative space and relationships; an existing-title export is checked for preservation instead of requiring a new design.
- The main narrative symbol is structural and low-density: it enters a stroke, counter, baseline, frame, subtitle relation, or one controlled motif entry point.
- Theme cues are not pasted on after the title and do not become a full illustration scene inside the letters.
- A clear visual memory point remains identifiable when the title is reduced.
- English or local-language text, if present, is exact, purposeful, lower hierarchy than the Chinese title, and not pseudo-text.
- Texture and wear support the selected route instead of becoming generic grunge, mud, cracked concrete, old game title texture, or random dirt.
- Preview approval is checked only when the user reserved that checkpoint; a suitable neutral inspection is a quality method, not automatic user permission.
- Transparent export preserves the selected design and exact characters; prefer native alpha, using chroma-key only as a justified fallback, with actual clean transparent edges.

## Image preview gate

Use after imagegen or still visual generation.

- Output matches the intended asset role.
- Main subject is readable within 1-2 seconds.
- Texture and style match the project tone.
- Color palette is intentional and not a default AI look.
- Visual metaphor does not obscure the message.
- Backgrounds have overlay-safe zones when needed.
- No unwanted artifacts, watermarks, pseudo-text, or extra objects.
- The output is strong enough to justify the next stage.

## Layout gate

Use with layout-design.

- Primary information is visible within 1-2 seconds.
- Supporting information has a clear reading path.
- Related items are grouped by proximity.
- At least one alignment system is visible or intentionally implied.
- Contrast clarifies hierarchy instead of creating noise.
- Repetition builds unity, with one controlled variation if needed.
- Negative space has a job.
- Image and text form one visual sentence.
- The layout works for the target ratio and medium.
- Exact text, numbers, units, names and quotations are preserved; real chart geometry matches supplied data and scales.

## Transparent asset gate

Use before accepting PNG cutouts or moving to compositing.

- Expected transparent pixels actually exist; a PNG extension, RGBA mode, opaque alpha plane, or baked checkerboard is not sufficient.
- Edges are clean at normal and enlarged view.
- No visible edge contamination on expected backgrounds; when chroma-key removal was used, check key-color fringes and lost subject detail.
- Padding and safe margins are sufficient.
- The silhouette or title remains readable on expected backgrounds.
- Fine texture is not destroyed by background removal.
- The asset has a clear compositing role.

## Motion readiness gate

Use checks matching the actual route and stage.

- Early movement intent names the information change and required independent controls; finished layers and detailed timing are not prerequisites.
- C whole-frame motion has suitable image quality, framing and edge coverage; do not require per-element layers or manifest.
- Detailed D motion has a real-content static composite and the independently controllable assets it needs.
- A manifest or equivalent positioning brief identifies paths, coordinate/anchor meaning, layout authority and movement roles when needed; a custom manifest is not assumed to be a native engine interface.
- Accurate text/data, sound mode, timing basis, hierarchy, reveal/hold logic and output requirements are clear: supplied audio cues, fixed silent timing, or provisional timing for pending narration as appropriate.
- The implementation entrypoint matches the project's actual version; runtime rules from different installations are not combined.
- Motion supports an already readable composition.

## Motion output gate

Use after motion generation.

- Motion reveals hierarchy instead of distracting from it.
- Segment duration has enough hold time for reading.
- Movement direction follows reading order or narrative logic.
- Text emphasis is readable and not overused.
- Initial visibility and reveal/emphasis order fit the explanation; do not require new entrances for an already-readable chart. Visible quantitative geometry and values stay consistent throughout motion.
- Transitions avoid jump cuts unless intentional.
- No exaggerated bounce, variety-show effect, cheap glow, or unwanted blue-purple neon.
- The actual requested export was inspected for dimensions, duration, format, text/assets and audio/alpha as relevant; source validation or a plan alone does not prove final output.

## Run review

Use after a creative run with multiple outputs.

- Original goal is clear.
- Best output is identified and justified.
- Failed branches are traced to prompt, layout, image, motion, or asset issues.
- Reusable guidance is separated from one-off taste.
- Next production step is clear.
- Run artifacts are organized enough to reuse.
