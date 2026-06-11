---
title: "Multi-channel Distance Field (MSDF)"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [font-rendering, signed-distance-fields, msdf, gpu-rendering]
aliases: [MSDF]
summary: "An improvement over single-channel SDF font rendering that uses three distance fields (RGB channels) to preserve sharp corners, addressing the rounded-corner limitation of single-channel SDF."
source_url: "https://www.redblobgames.com/articles/sdf-fonts/"
---

# Multi-channel Distance Field (MSDF)

## Definition
MSDF extends the single-channel SDF approach by storing three signed distance fields in the red, green, and blue channels of a texture. The median of the three channels is used to determine the glyph boundary, preserving sharp corners that a single distance field would round.

## Key Properties
- Sharp corners: three distance fields capture corner geometry better than one
- Same simple shader: median of three channels instead of single channel
- Implementation: msdfgen library (Chlumsky) is the reference implementation
- Quality: may look worse than SDF for glow and shadow effects

## Key Papers
- 2016: Shape Decomposition for Multi-channel Distance Fields (Chlumsky) — introduces MSDF with complete open-source implementation
- 2007: Improved Alpha-Tested Magnification (Valve/Chris Green) — single channel SDF, suggests multi-channel for sharp corners without method

## Related Concepts
- [[signed-distance-field-fonts]] — Base technique that MSDF improves
- [[viktor-chlumsky]] — Author of msdfgen

## References
- Viktor Chlumsky, "Shape Decomposition for Multi-channel Distance Fields" (2016)
- Chris Green, "Improved Alpha-Tested Magnification for Vector Textures and Special Effects" (2007)
- msdfgen — https://github.com/Chlumsky/msdfgen
