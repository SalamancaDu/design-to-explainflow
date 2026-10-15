---
name: motion-style
description: "Use when Codex needs to plan, critique, or author restrained information-led motion for short 16:9 video segments, HyperFrames scenes, title cards, chapter transitions, data animation, keyword emphasis, handwritten annotations, PNG element motion, background loops, or documentary and finance explainer visual motion."
metadata:
  short-description: "Motion rules for short video segments"
---

# Motion Style

Use this project skill to plan motion language for short video segments. It is optimized for 16:9 video fragments, usually 3-10 seconds, used in finance explainers, documentary-style videos, information graphics, title cards, transitions, visual emphasis, PNG element animation, and HyperFrames compositions.

This skill is adaptive. Reuse the brief, selected visual direction, and existing project. Ask only for missing information that materially changes the result. Compare directions only when exploration is requested or a consequential choice remains; otherwise select a fitting motion treatment and continue.

## Boundary with layout and image assets

Use `motion-style` for early movement intent, timing, pacing, choreography, and handoff to the chosen implementation. Do not regenerate visual direction or bitmap prompts: hierarchy belongs to `layout-design`, bitmap art direction to `image-style`, custom lettering to `title-text-design`. Runtime API rules belong to the selected tool/version.

## Default context

Assume these defaults unless the current request says otherwise:

- canvas: 16:9
- duration: 3-10 seconds
- video type: finance explainer or documentary-style segment
- goal: clarify information, guide attention, and support narration
- subtitle policy: no bottom karaoke lyric subtitles by default
- on-screen text: titles, key terms, labels, emphasized words, and handwritten annotations may appear when needed
- avoid: exaggerated bounce, variety-show effects, cheap tech light effects, blue-purple neon, noisy cyberpunk aesthetics

## Core workflow

1. Identify the role, actual deliverable, and whether this is early intent, detailed choreography, or a local edit. Reuse existing context; use `references/briefing-questions.md` only for material gaps.
2. Distinguish **C 整帧动效** (whole-frame movement/crop/mask/new overlays) from **D 逐元素动效** (independent internal elements). Editable stills use **B 可编辑静态合成** and need no animation.
3. Before splitting D assets, describe what changes, why it changes, and the control required: separate subject parts, occlusion, background completion, shadows, accurate text or chart elements. This intent pass does not require a finished composite.
4. For detailed D choreography, inspect the static composite with real content and confirm independently controllable elements plus a manifest or equivalent positioning brief. For C, inspect the supplied image and edge coverage; do not require layers or a per-element manifest.
5. Use `references/motion-directions.md` and `references/timing-pacing.md` to choose actions, hold time, and transitions fitting the information. Preserve an existing direction; compare alternatives only when useful.
6. Use `references/text-emphasis.md` for text. Distinguish supplied audio, an explicitly silent piece, and pending narration. Use actual audio cues when supplied; a silent piece can have a fixed duration. Mark audio-dependent timing provisional only when intended audio is missing, and do not claim exact narration alignment.
7. Hand the concrete motion brief to the requested/available implementation. For HyperFrames use `references/hyperframes-motion-brief.md` to resolve the project version and entrypoint. Complete implementation, preview, export, and actual-output checks when that is the authorized deliverable.

## Flat-image and layered boundaries

A flat image supports whole-frame motion, crop, masks, and additional overlays. It does not provide independent control of baked-in subjects, titles, numbers, or lines. Keep C when that meets the request. Switch to D only when independently controlled content is needed, then reuse the image as a visual reference and recreate only the affected assets.

For D, check the real composite before detailed animation. Name the editable text/data/lines and the independently movable bitmaps; do not infer readiness from a text-free aesthetic master alone. Existing approved choices carry forward; a quality check does not create a new user approval stage.

If a changed motion idea needs new asset control, return that specific requirement to image-style/layout-design rather than rebuilding every layer.

## Optional layered image assets

Use layered image assets only when they help animation or editing. Prefer a complete aesthetic master frame first, then request separate layers that recreate the same visual direction.

When new bitmap layers are needed, hand off their prompts and visual constraints to `image-style`. `motion-style` should name which elements need to move and what role each element plays, not write full imagegen prompts for every layer.

For motion work, useful layers are usually:

- `background.png`: stable atmosphere or environment layer.
- `subject.png`: the main object, person, symbol, or visual focus that may enter, scale, mask, or parallax.
- editable text/data graphics: accurately typeset or drawn in the composition source; checked custom title bitmaps are optional, with per-character splitting only when needed.
- optional decorations: bitmaps or editable marks as appropriate; keep meaningful data relationships accurate and separately controlled when needed.
- `composite-preview.png`: the paused hero frame that must look good before animation.

Do not animate a layered composition whose composite preview is weaker than the original master frame. Motion should amplify an already strong frame, not rescue mismatched layers.

## Motion principles

- Motion must serve hierarchy, not decorate the frame.
- Design the static hero frame first. If the paused frame is unclear, animation will not fix it.
- Use motion to reveal, connect, compare, emphasize, or transition.
- Keep primary information movement clearer and stronger than secondary information movement.
- Use fewer, more meaningful animated properties: opacity, x/y, scale, mask/reveal, clip-path, line draw, blur only when justified.
- Prefer restrained easing and deliberate timing over energetic bounce.
- Avoid moving every element at the same speed or in the same direction.
- Maintain enough hold time for viewers to read.

## Output scaled to the stage

For early intent, state the information change, independent controls, and implications for assets or layout. Do not demand a detailed timeline or completed layers at this stage.

For detailed motion, provide only the fields needed to implement:

- route, role, canvas, duration and requested outputs;
- actual static frame and element IDs/asset paths or equivalent positioning references;
- initial visibility, necessary entrances, emphasis, holds, ending and transitions;
- sound mode and timing basis: supplied audio cues, fixed silent timing, or provisional audio-dependent timing for pending narration;
- selected movement/easing language, constraints, and the owning implementation.

For a local edit, report and repair the affected behavior while preserving unrelated timing and layout. A motion brief alone is not a finished animation. On complete production requests, implementation owns playable source, preview, export, and final-file checks. Report the actual achieved stage and any missing deliverable.

Use transitions, hard cuts, stillness, and entrances for narrative reasons; every element need not enter, nor every scene use an effect transition. Engine-specific constraints must be checked against the chosen runtime rather than inferred from aesthetic conventions.

## Delivery checklist

- [ ] Segment role is explicit.
- [ ] Duration and canvas are clear or defaulted to 16:9, 3-10 seconds.
- [ ] Detailed D motion is based on a real-content composite; C has suitable whole-frame coverage. Early intent is not blocked by missing layers.
- [ ] Motion direction matches video tone.
- [ ] Text emphasis is readable and not over-animated.
- [ ] Timing includes enough hold time.
- [ ] No exaggerated bounce, variety-show style, cheap glow, or blue-purple neon by default.
- [ ] Sound mode is explicit: actual audio cues when supplied, agreed timing for a silent piece, or provisional audio-dependent timing when narration is pending.
- [ ] Tool/version and requested deliverables are clear enough to implement; runtime rules are not mixed between installations.
- [ ] Cuts, holds, entrances, and transitions support the narrative and readability.
- [ ] When a finished animation is requested, actual source/preview/export checks are completed and reported separately from planning.
