# Imagegen Prompt Recipes

Use these prompt recipes with the built-in `imagegen` skill. Keep prompts structured and explicit about asset role, video context, and constraints.


These recipes are for non-typographic assets. Custom letterforms and title PNGs use `title-text-design`; preview and export follow the requested deliverable and user-reserved review points. Do not inherit `Use case:`, `logo-brand`, `badge`, or `emblem` headers for title typography. Preserve already-selected art direction and accurate content rather than adding default exploration.

## Finance explainer infographic frame

```text
Use case: productivity-visual
Asset type: video infographic frame for a finance explainer
Primary request: <describe the clearly schematic concept; actual numeric geometry is drawn separately from supplied data>
Video context: <topic, chapter, tone>
Visual direction: editorial finance restraint with minimal data clarity
Composition: clear primary focal concept, large readable shapes, reserved space for title and labels, strong hierarchy, generous margins
Style/medium: editorial graphic illustration, print-informed, not photographic
Color palette: restrained muted base with one accent color, avoid blue-purple tech palette
Lighting/mood: flat editorial light, calm and credible
Materials/textures: subtle paper grain or print texture
Text: leave exact text and numbers for editable typesetting; no fabricated labels
Constraints: readable at video scale, simple schematic shapes, compatible with overlays; do not imply unprovided numerical proportions
Avoid: oily AI gloss, cheap fintech dashboard, dense tiny labels, neon cyberpunk, blue-purple gradient, watermark
```

## Poster or video cover

```text
Use case: ads-marketing
Asset type: finance documentary poster / video cover
Primary request: <main idea or episode theme>
Visual direction: high-contrast symbolic poster + editorial restraint
Composition: one strong symbolic focal object, bold scale contrast, intentional negative space for title, memorable silhouette
Style/medium: editorial illustration or graphic poster, not photography unless requested
Color palette: limited palette, high contrast, muted but impactful
Lighting/mood: serious, intelligent, restrained, cinematic without action-movie clichés
Materials/textures: subtle print grain, paper or ink texture
Text: leave clean title area; do not render dense text
Constraints: works as thumbnail and title card, clear first-read focus
Avoid: overdramatic fire/lightning, cheap tech glow, AI gloss, generic stock finance imagery, blue-purple cyberpunk
```

## Documentary background plate

```text
Use case: historical-scene
Asset type: documentary background plate for video editing
Primary request: <topic atmosphere, e.g. central bank archive, old trade map, newspaper-like market history>
Visual direction: documentary archive mood
Composition: layered but calm background, clear empty zone for subtitles or chart overlay, subtle focal texture on one side
Style/medium: archival paper collage, scanned document atmosphere, editorial not literal evidence
Color palette: aged neutrals, charcoal, sepia, muted stamp red or olive accent
Lighting/mood: quiet, serious, reflective
Materials/textures: paper grain, scan texture, faded ink, map/document fragments
Text: no readable fake headlines unless provided verbatim
Constraints: background must not compete with foreground typography or charts
Avoid: fake evidence, conspiracy-board clutter, excessive grunge, glossy AI look, watermark
```

## Low-saturation newspaper halftone collage

```text
Use case: historical-scene
Asset type: finance documentary collage asset / background plate / cutout set
Primary request: <business biography, company investment map, platform ecosystem, consumer industry timeline, or local services scene>
Video context: <topic, chapter, tone>
Visual direction: low-saturation newspaper halftone collage
Composition: warm aged-paper field, calm text-safe zone, collage density along sides or lower edge, clear foreground/midground/background logic, no clutter in title area
Style/medium: editorial documentary collage, old newspaper halftone, finance magazine clipping, paper archive texture, not glossy photography
Color palette: aged ivory, newsprint gray, ink charcoal, sepia brown, one muted accent derived from the current theme, optional warning accent only if the topic needs risk or turning-point emphasis
Lighting/mood: flat editorial light, credible, reflective, business documentary tone
Materials/textures: newspaper halftone dots, old paper grain, light scan texture, subtle print wear, slight misregistration, cut-paper edges, hand-drawn annotation lines
Portrait treatment: warm grayscale or sepia documentary portrait, no vivid skin tone, no beauty retouching, no strong studio light, no hard HD cutout edge
Object treatment: receipts, maps, buildings, delivery boxes, food, hotels, tickets, shopping bags, and chart fragments should feel like paper clippings from finance magazines or old newspapers
Text: do not render important Chinese text, exact numbers, labels, or fake headlines; leave space for manual typography
Constraints: readable at video scale, restrained collage density, compatible with overlays, use the theme-derived accent sparingly for pins, highlights, or key objects; do not inherit accent colors from unrelated examples
Avoid: ecommerce poster style, saturated product photography, glossy 3D render, neon fintech dashboard, blue-purple gradient, glowing chart lines, cyberpunk effects, overcrowded scrapbook clutter, watermark
```

## Object transparent PNG cutout

```text
Use case: <generate taxonomy for a new object, or background-extraction when editing an existing asset>
Asset type: object transparent PNG cutout for video editing
Primary request: <single object or visual element>
Visual direction: handmade explainer collage / editorial graphic object
Composition: isolated object centered with generous padding, clean silhouette, no overlap with background
Style/medium: <paper cutout / hand-drawn marker / editorial icon / flat graphic / document stamp>
Color palette: muted, video-friendly, compatible with finance explainer palette
Lighting/mood: flat, clean, no cast shadow unless requested
Materials/textures: subtle paper, ink, pencil, stamp, or print texture
Constraints: request native transparent output and preserve alpha; use a key-color plate only if the selected tool lacks usable native transparency and that method is chosen
Avoid: unwanted opaque background, checkerboard baked into the image, edge contamination, watermark, blue-purple tech palette; require a suitable transparency method for hair, glass, smoke, or other complex edges
```

## Data graphic asset

For a real bar comparison, timeline, risk scale, or other factual chart, draw geometry and labels from supplied data in the project. Confirm units, time range, scale/baseline, and source or user-provided basis. This recipe produces supporting artwork or an explicitly schematic mechanism illustration, not a finished quantitative chart.

~~~text
Use case: productivity-visual
Asset type: non-quantitative supporting illustration for a data graphic
Primary request: <symbolic mechanism or background; no exact chart geometry>
Visual direction: minimal data clarity
Composition: reserved space for separately drawn chart and accurate labels
Style/medium: editorial illustration, print-informed
Color palette: inherit the selected palette
Lighting/mood: calm and restrained
Materials/textures: subtle paper grain where it does not impair data reading
Text: no exact labels, numeric scales, fake values, or pseudo-text
Constraints: schematic only; actual data marks, axes, ratios, and relationships are supplied by editable drawing
Avoid: decorative chart junk, tiny axes, implied unprovided proportions, neon fintech dashboard
~~~

## Editing cutaway image

```text
Use case: illustration-story
Asset type: cutaway image for video edit
Primary request: <concept metaphor or chapter support visual>
Visual direction: soft illustrated systems or handmade explainer collage
Composition: one clear metaphor, simple foreground object, calm background, readable in 1-2 seconds
Style/medium: editorial illustration, tactile, controlled detail
Color palette: low saturation with one accent
Lighting/mood: human, clear, slightly thoughtful
Materials/textures: paper grain, soft ink, hand-drawn annotation if useful
Text: no text unless explicitly requested
Constraints: must support narration without requiring close inspection
Avoid: clutter, stock-vector corporate people, AI gloss, cheap tech elements, blue-purple palette
```
