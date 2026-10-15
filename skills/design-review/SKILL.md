---
name: design-review
description: Use when Codex needs to perform stage-gate review, critique, score, or extract reusable learnings from prompts, generated images, typography/title designs, layout drafts, posters, video frames, HyperFrames motion, transparent PNG assets, backgrounds, data visuals, or completed design runs. Use for requested design critique or a concrete artifact-quality concern; ordinary creation does not automatically require this separate review workflow.
---

# Design Review

Use the relevant review criteria for the requested artifact. This skill supplies quality assessment, not user authorization. Do not add a separate review ceremony after every creation step, and continue authorized repairs once concrete issues are identified.

The goal is to answer two questions:

1. **流程是否正确**: does the work have the inputs and quality evidence needed for the next production stage? This is a quality judgment, not user authorization.
2. **效果是否达标**: does the output fit the asset role, design intent, craft bar, and next production step?

## Review modes

Select the narrowest relevant mode:

- **Prompt gate**: before imagegen, HyperFrames, layout, or motion execution.
- **Typography gate**: title text, font framework, lettering skeleton, transparent title assets.
- **Image preview gate**: generated image, poster, cover, background plate, visual asset.
- **Layout gate**: composition, hierarchy, spacing, reading path, image-text relationship.
- **Transparent asset gate**: PNG cutouts, alpha edges, padding, compositing readiness.
- **Motion readiness gate**: static hero frame, layered assets, scene manifest, motion brief.
- **Motion output gate**: timing, readability, transitions, hierarchy, export quality.
- **Run review**: full creative run, reusable learnings, prompt/motion/layout deltas.

## Gate verdicts

Use one verdict:

- **PASS**: can proceed to the next stage.
- **PASS WITH NOTES**: usable now, but carry specific constraints into the next stage.
- **REVISE BEFORE NEXT STAGE**: direction is useful, but one or more issues must be fixed first.
- **GO BACK A STAGE**: the current output reveals a brief/prompt/font/layout problem; return to the previous design stage.
- **REDO**: wrong direction for the asset role, tone, or production path.
- **BLOCKED**: cannot judge because required artifact, prompt, reference, or context is missing.

For a checkpoint review, state the supported quality verdict rather than only “looks good”. Recommend the next production step only when its relevant quality conditions are met. A PASS is not external-action authorization, and a missing optional learning note does not block a usable artifact.

## Core workflow

1. Identify the artifact and its intended role.
2. Identify the current stage and the proposed next stage.
3. Load references/review-checklists.md and use the relevant mode checklist.
4. Use references/scoring-rubric.md only when scoring is requested or materially helps a comparison; do not add numeric scoring to every review.
5. Decide the gate verdict.
6. Give priority-ordered fixes. Start with role/stage failures, then structure, style, craft, and polish.
7. Extract reusable learnings with references/learning-capture.md only when the learning is reusable.
8. If a full run note is requested, use references/run-note-template.md.

## Review principles

- Judge against the asset's role and production stage, not generic beauty.
- Separate stage correctness from visual quality.
- Preserve what works before changing what fails.
- Identify meaningful strengths and supported blocking issues, if any; a clean review is valid.
- Give concrete next edits, not vague comments like “make it better”.
- Recommend “go back a stage” when the problem is caused by prompt, font base, layout brief, or motion brief.
- Do not turn a one-off taste observation into a permanent rule.
- Do not copy external references directly; extract reusable structure, tone, or constraints.

## Cross-skill gates

Use these domain-specific checks when relevant:

- **title-text-design**: font base exists; prompt stage is correct; no generic Use case header; no logo/badge drift; texture and motif do not damage legibility.
- **layout-design**: hierarchy, alignment, spacing, reading path, safe margins, and composition role are clear before visual polish.
- **image-style**: image direction, texture, color, and asset role match the project; avoid AI gloss, generic stock, cheap tech, and unwanted blue-purple neon.
- **motion-style / implementation**: distinguish C whole-frame from D element-level motion and early intent from detailed choreography; D has a real-content composite before detailed animation. Validate the chosen runtime/version and actual requested export, not only the motion brief.
- **exact content / data**: preserve exact wording, numbers, units and names; factual chart geometry matches its data and mappings, and schematic imagery is not presented as evidence.

## Required output

When reviewing a checkpoint, return:

- **结论 / Gate verdict**: PASS, PASS WITH NOTES, REVISE BEFORE NEXT STAGE, GO BACK A STAGE, REDO, or BLOCKED.
- **当前阶段 → 下一阶段**: e.g. prompt → image preview, preview → transparent export, hero frame → motion.
- **下一步质量条件是否满足**: yes/no and why; distinguish missing evidence from a confirmed defect and from user authorization.
- **最有效的地方**: 1-3 concrete strengths.
- **阻塞问题**: evidence-backed issues affecting the next stage, or explicitly none; do not invent issues to meet a quota.
- **具体修改建议**: priority-ordered fixes.
- **下次提示词 / 版式 / 动效调整**: only when relevant.
- **可复用经验**: what should be saved to a skill or run note, or “none”.

For full run review, also include: best output, failed branch, reusable learning, one-off note, and recommended archive/run-note action.

## Knowledge update rule

Only propose updating skill references when a learning is:

- repeated or likely to recur;
- general enough to reuse;
- tied to role, clarity, style, craft, or production reliability;
- compatible with existing project quality direction.

For one-off choices, keep the decision in the current task or existing requested artifact. Create run notes only when requested or required by the project; do not automatically update memory or skills.
