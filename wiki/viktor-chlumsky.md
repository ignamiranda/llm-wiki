---
title: "Viktor Chlumsky"
type: person
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [font-rendering, signed-distance-fields, msdf, computer-graphics]
aliases: []
summary: "Author of the msdfgen library and the 2016 paper on multi-channel distance fields (MSDF), providing the first complete open-source implementation of sharp-corner distance field font rendering."
---

# Viktor Chlumsky

## Bio
Viktor Chlumsky authored the 2016 paper "Shape Decomposition for Multi-channel Distance Fields," which solved the rounded-corner limitation of single-channel SDF fonts by using three distance fields per glyph. He also created msdfgen, the reference open-source library for generating MSDF font textures, and msdf-atlas-gen for atlas generation.

## Key Contributions
- 2016 paper on multi-channel distance fields for sharp font corners
- msdfgen: complete open-source library for MSDF generation
- msdf-atlas-gen: atlas texture generation tool

## Related Work
- [[multi-channel-distance-field]] — The technique he invented
- [[signed-distance-field-fonts]] — Foundation his work improved

## References
- Viktor Chlumsky, "Shape Decomposition for Multi-channel Distance Fields" (2016) — https://github.com/Chlumsky/msdfgen/files/3739469/Shape_Decomposition_for_Multi-channel_Distance_Fields.pdf
- msdfgen — https://github.com/Chlumsky/msdfgen
- msdf-atlas-gen — https://github.com/Chlumsky/msdf-atlas-gen
