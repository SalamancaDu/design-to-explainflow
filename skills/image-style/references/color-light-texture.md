# Color, Light, and Texture

Use this file to choose visual treatment before writing prompts.

## Palette principles

- Choose palette from video tone, not from tool defaults.
- Avoid default blue-purple tech palettes unless the user explicitly asks for that tone.
- For finance explainers, prefer credibility: muted base colors, one accent, high legibility.
- For documentary segments, prefer historical atmosphere: aged neutrals, charcoal, ivory, olive, muted red, ink blue, deep brown.
- For handmade explainers, use paper whites, pencil gray, muted marker colors, kraft paper, warm neutrals.

## Recommended palettes

### Editorial neutral

- ivory `#F3EFE4`
- charcoal `#1F2326`
- warm gray `#A7A093`
- muted gold `#B89B5E`
- deep red accent `#9E3B32`

### Documentary archive

- aged paper `#E6D8B8`
- faded black `#202020`
- sepia `#7A5638`
- olive gray `#6D725F`
- muted stamp red `#A34B3F`

### Minimal data

- off-white `#F7F5EF`
- ink `#151515`
- grid gray `#D8D3C8`
- accent green `#3E8F6B`
- accent orange `#C56A3B`

### High contrast poster

- near black `#111111`
- warm white `#F2EBDD`
- signal red `#C93A2E`
- muted yellow `#D7A84F`

### Handmade collage

- paper `#F6EEDC`
- graphite `#343434`
- kraft `#B98F62`
- muted blue-gray `#61717A`
- dull red `#AA5146`

### Newspaper halftone collage

- aged ivory `#E8DEC9`
- newsprint gray `#B9B0A2`
- ink charcoal `#262522`
- sepia brown `#7A5A3C`
- theme-derived accent `<choose from the current brand, industry, or story topic>`
- optional warning accent `<use only when the topic needs risk, conflict, or turning-point emphasis>`

## Light rules

Most project assets should not look like glossy AI studio photography. Prefer:

- flat editorial light
- soft paper-like shadows
- print-like texture
- subtle vignette only when it supports focus
- controlled contrast instead of dramatic neon glow

Use hard light only for poster drama. Use naturalistic light only when documentary realism is needed.

## Texture rules

Good texture:

- paper grain
- risograph-like ink variation
- pencil or marker trace
- scan texture
- subtle print misregistration
- archival wear
- simple material surfaces such as paper, card, cloth, map, document, screen, or coin silhouette

Avoid:

- shiny plastic skin
- over-smoothed 3D render surfaces
- fake holographic tech overlays
- excessive lens flare
- random grunge that does not match the topic

## Low-saturation newspaper halftone collage rules

Use this treatment when the visual direction is `Low-saturation newspaper halftone collage` / `低饱和报纸网点拼贴风`.

Portrait treatment:

- Convert people into warm grayscale, sepia, or faded black documentary portraits.
- Add newspaper halftone dots, old-paper grain, light scan texture, and restrained print wear.
- Use slightly feathered, torn-paper, or cut-paper edges instead of hard HD cutout edges.
- Avoid vivid skin tones, glossy skin, beauty retouching, strong studio lighting, and commercial headshot polish.

Object and material treatment:

- Make receipts, maps, buildings, delivery boxes, food, hotel objects, tickets, shopping bags, and investment charts feel like paper clippings from a finance magazine, old newspaper, or business archive.
- Keep most objects low-saturation in gray, ivory, charcoal, sepia, and light brown, then add one accent derived from the current theme.
- Choose the accent from the current brand, industry, chapter, or story symbol; do not automatically reuse yellow, red, or any previous project color.
- Use a secondary warning color only when the topic needs risk points, inflection points, warnings, or conflict emphasis.

Line and annotation treatment:

- Use thin hand-drawn graphite, faded ink, or muted accent lines for arrows, route traces, chart lines, and data annotations.
- Use imperfect but controlled paper-and-pencil styling without changing factual data geometry or route relationships; those remain accurately drawn and editable.
- Avoid neon chart lines, holographic panels, fintech dashboards, and dense decorative HUD frames.

Composition treatment:

- Preserve a calm central or upper text-safe zone for titles, subtitles, charts, and motion overlays.
- Place dense collage detail along the sides, corners, or lower edge unless the asset is a standalone poster.
- Let the composite read as a credible investment landscape or business archive, not an ecommerce product layout.

## Transparent PNG rules

For video editing cutouts:

- subject must be a single usable element or coherent cluster
- clean silhouette
- generous padding
- no cast shadow unless requested separately
- avoid hair, smoke, glass, liquid, fur, or translucent materials unless true transparency workflow is confirmed
- prefer the selected tool's native transparent output and preserve alpha; use chroma-key removal only when native transparency is unavailable or an inspected result requires the alternative
- check that expected transparent pixels actually exist, not merely a PNG extension or RGBA mode; inspect normal/enlarged edges on the intended background
- use a separate shadow layer when motion or compositing requires control; select any key color to avoid removing subject colors

Useful transparent PNG element types:

- paper label
- torn note
- arrow
- underline stroke
- chart bar
- coin-like symbol
- document stamp
- map pin
- hand-drawn circle
- warning marker
- minimal icon object
- abstract flow line
- textured rectangle panel

## Background plate rules

A background plate must leave room for motion graphics and subtitles.

Specify:

- calm zone for text
- focal zone for symbol or texture
- depth level: flat, shallow, or layered
- overlay compatibility: subtitles, charts, labels, title, or PNG cutouts

Avoid dense all-over detail unless the asset is not meant to carry text.
