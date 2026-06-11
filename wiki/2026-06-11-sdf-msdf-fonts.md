---
title: "Guide to SDF+MSDF Fonts"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [font-rendering, signed-distance-fields, msdf, gpu-rendering, game-development]
summary: "Amit Patel's comprehensive guide to Signed Distance Field (SDF) and Multi-channel Signed Distance Field (MSDF) font rendering for games and maps, with shader implementation details."
source_url: "https://www.redblobgames.com/articles/sdf-fonts/"
source_hash: "e8b94ab0ca4acd1310d6be6a2138d2609164c98fbcda12540f304e98bd0b0ce0"
---

# Guide to SDF+MSDF Fonts

## Summary
Amit Patel's practical guide to rendering text effects (outline, glow, shadow) using SDF and MSDF fonts. Covers the full pipeline: understanding distance fields, mapping distances to colors with shader code, atlas generation and text layout, outline effects, and a comparison of the four key academic papers in the field.

## Key Techniques
- SDF as intermediate format between vector and bitmap fonts
- Single distance field (Valve 2007) for simple rendering
- Multi-channel distance field (Chlumsky 2016) for sharp corners
- Antialiasing using screen-space derivatives or precomputed scale
- Front-to-back blending for outline + text combinations

## Key Takeaways
- SDF allows resolution-independent font rendering from a single low-res texture
- SDF supports effects (outline, glow, shadow) that are difficult with vector or bitmap
- SDF does NOT support all characters, variable fonts, or hinting
- MSDF fixes rounded corners but may look worse for glow/shadow effects
- msdfgen is the recommended open-source library

## Related
- [[signed-distance-field-fonts]] — Core concept
- [[multi-channel-distance-field]] — MSDF concept
- [[chris-green]] — Valve SDF paper author
- [[viktor-chlumsky]] — msdfgen author
- [[amit-patel]] — Author
