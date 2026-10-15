# HyperFrames Motion Brief

Use when HyperFrames is the selected implementation. This reference owns the design handoff and entrypoint selection, not a copied runtime API specification.

## Resolve the implementation

1. Read the user's selected entrypoint and the project's instructions, package.json, lockfile, existing scripts and actual installed command version.
2. Use documentation matching that implementation. Available local entrypoints may include standalone `hyperframes` with `hyperframes-core`, or the managed `hyperframes:hyperframes` plugin. They are alternative installations, not instructions to merge.
3. Use an existing project script or local executable for version/help checks; do not probe with a command that silently installs or upgrades dependencies. Preserve the project's pinned version rather than upgrading to fit another Skill. If versions cannot be matched, inspect the installed source/help or official documentation for that version before implementation.
4. For a new project, establish the selected tool and available implementation first. Missing dependencies or paid/external actions retain their actual authorization boundaries; a Skill does not grant them.
5. Carry the existing brief, assets, static composition and motion direction forward. Ask only for implementation-critical gaps; do not restart resolved creative interviews. If the framework requires its own brief or design settings file, derive it from the confirmed handoff instead of reselecting the design.

Resolve timeline registration, fonts, media attributes, determinism, validation commands and export support from the selected version's technical contract. Do not apply one installation's rules to another. Do not alter managed plugin caches to enforce project taste.

## Handoff fields

~~~text
Route / stage: C whole-frame motion or D element-level motion; detailed brief or local edit
Canvas and duration: actual dimensions, length and timing basis
Role and intent: what information changes and why
Static composite: file / selected source; real on-screen text and data
Elements: IDs, asset paths, editable controls and positioning source
Choreography: initial visibility, necessary entrances, emphasis, hold, ending, cuts/transitions
Sound mode and timing: actual audio file/cues, fixed silent duration, or provisional audio-dependent timing for pending narration
Implementation: selected entrypoint, project version and existing commands
Delivery: source, preview and/or final file; format, frame rate, sound and alpha as relevant
~~~

Keep file paths unambiguous. If a manifest is supplied, establish its coordinate semantics, path base and layout authority. It is a custom handoff unless the project explicitly implements a reader.

## Implementation and output checks

Build or reuse the correct static layout, then implement the selected choreography. Initial visibility and scene transitions follow narrative needs; do not require every element to enter or multiple easing types simply to satisfy a style recipe.

Run checks appropriate to the installed version and changed behavior. Inspect representative start, readable hold, action/scene boundaries, and ending states; verify assets/fonts, text fit, media and sound. Export when requested and authorized, then inspect the actual file for required dimensions, duration, format and audio/alpha. Passing source checks alone does not prove the export.

Use an existing static frame or a brief alone when that is the entire requested deliverable. Clearly distinguish plan, static composite, implemented preview and exported video.
