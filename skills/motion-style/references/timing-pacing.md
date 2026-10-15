# Timing and Pacing

Default segment length is 3-10 seconds in 16:9 when unspecified. Supplied dimensions, duration and actual audio take precedence. The skeletons below are starting points, not proof of narration alignment. Explicitly silent work may use an agreed fixed duration; when narration is intended but its audio is missing, mark the audio-dependent timing provisional.

## Default timing skeletons

### 3-second emphasis hit

Use for one keyword, one object, one quick visual support.

- 0.0-0.2s: settle / pre-roll frame
- 0.2-0.8s: primary element enters
- 0.8-1.4s: emphasis mark or supporting element appears
- 1.4-2.6s: hold for reading
- 2.6-3.0s: transition-ready end or subtle exit

### 6-second explainer card

Use as the default for finance explainer fragments.

- 0.0-0.3s: quiet start
- 0.3-1.2s: title or primary symbol enters
- 1.0-2.4s: supporting labels, arrows, or blocks reveal
- 2.4-3.6s: keyword / number emphasis
- 3.6-5.4s: readable hold
- 5.4-6.0s: transition-ready movement or final settle

### 10-second mini-sequence

Use when showing a small process or comparison.

- 0.0-0.5s: establish frame
- 0.5-2.0s: first idea
- 2.0-4.0s: second idea or contrast
- 4.0-6.5s: connection / cause-effect reveal
- 6.5-8.5s: summary emphasis
- 8.5-10.0s: hold and transition-ready ending

## Easing guidance

Prefer:

- `power2.out` for calm reveals
- `power3.out` for stronger but still restrained entrances
- `expo.out` for precise editorial motion
- `sine.inOut` for ambient drift
- `power2.inOut` for transitions and masks

Avoid by default:

- elastic bounce
- back overshoot
- chaotic shake
- excessive spring-like movement

## Readability rules

- On-screen title: start with roughly 1.5-2 seconds after entrance, then verify against text length, complexity, viewing size and actual narration; longer content needs more time.
- Keyword highlight: hold at least 0.8-1.2 seconds.
- Number or label: do not animate faster than viewers can read.
- Data chart: choose initial visibility, synchronized reveals, or staged reveals to suit comprehension. Existing charts may remain visible and receive emphasis only; visible values and quantitative geometry must stay consistent during motion, not only at the end.
- Handwritten mark: draw speed should feel intentional, not frantic.

## Motion density

For 3-10 seconds, use:

- 1 primary movement
- 1 support reveal
- 1 emphasis moment
- optional ambient background motion

If many important elements compete, reduce simultaneous movement or split information by meaning; element count alone is not a mandatory split threshold.
