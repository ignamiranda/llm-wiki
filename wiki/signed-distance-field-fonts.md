---
title: "Signed Distance Field Fonts"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [font-rendering, signed-distance-fields, gpu-rendering, game-development]
aliases: [SDF fonts]
summary: "A font rendering technique that uses a signed distance field texture as an intermediate format between vector and bitmap fonts, enabling resolution-independent rendering with GPU-accelerated special effects."
source_url: "https://www.redblobgames.com/articles/sdf-fonts/"
---

# Signed Distance Field Fonts

## Definition
A signed distance field (SDF) font stores, for each texel, the signed distance to the nearest glyph outline. This allows a single low-resolution texture to generate high-resolution output at any size, supporting effects (outline, glow, shadow) that are difficult with vector or bitmap approaches.

## Key Properties
- Resolution-independent: single low-res texture renders sharply at any size
- GPU-accelerated: fragment shader evaluates a simple distance comparison
- Effect support: outlines, glows, shadows via distance threshold manipulation
- Limitations: limited character set, no hinting, no variable fonts, no color fonts

## Comparison
Vector fonts support all sizes, all characters, hinting, variable fonts, and color fonts but are not GPU-accelerated. Bitmap fonts are GPU-accelerated with small runtime code but don't support all sizes or effects. SDF combines GPU acceleration and effect support but sacrifices character set completeness and hinting.

## Key References
- Valve 2007 (Chris Green): single distance field, simple shader
- Chlumsky 2016: multi-channel distance field (MSDF) for sharp corners

## Related Concepts
- [[multi-channel-distance-field]] — MSDF improvement for sharp corners
- [[2026-06-11-sdf-msdf-fonts]] — Comprehensive guide to the technique
- [[chris-green]] — Valve SDF paper author
- [[viktor-chlumsky]] — msdfgen author
