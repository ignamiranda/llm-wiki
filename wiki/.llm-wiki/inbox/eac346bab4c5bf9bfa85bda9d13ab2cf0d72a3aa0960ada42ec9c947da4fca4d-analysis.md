# Ingest Analysis — Making maps with noise functions
**Source hash:** `eac346bab4c5bf9bfa85bda9d13ab2cf0d72a3aa0960ada42ec9c947da4fca4d`
**Language detected:** en
**Analyzed:** 2026-06-11T08:05:00Z

## Source Summary / 来源摘要

Amit Patel's tutorial on using Perlin/Simplex noise functions to generate 2D terrain maps for games. Covers elevation maps, fractal octaves (FBM), redistribution, biomes from elevation+moisture, climate modeling, island shaping, ridged noise, terraces, tree placement, wraparound maps, and infinite terrain. Targeted at indie developers and game jams — emphasizes simplicity over global constraints.

## Concepts to Extract / 待提取概念

| Concept | Action | Reason |
|---------|--------|--------|
| noise-based-terrain-generation | create | Core methodology of using noise for terrain |
| fractional-brownian-motion | create | Octave stacking with decreasing amplitudes |
| elevation-redistribution | create | Power functions, terraces, curves tools |
| biome-maps | create | Two-noise-map (elevation + moisture) biome assignment |
| ridged-noise | create | Absolute-value noise for sharp ridge features |
| blue-noise-placement | create | High-frequency noise for object (tree) placement |
| wraparound-noise | create | Cylindrical/toroidal noise for seamless maps |
| island-shaping | create | Distance + shaping functions to create islands |
| infinite-terrain | create | Camera-offset local computation for endless maps |

## Persons to Create/Update / 待创建/更新的人物

| Person | Action | Details |
|--------|--------|---------|
| amit-patel | create | Amit J. Patel — creator of Red Blob Games, author of this tutorial |

## Pages to Create

| Filename | Type | Title | Key Content |
|----------|------|-------|-------------|
| 2015-07-07-noise-terrain-maps | article | Noise-Based Terrain Maps | Summary of the full tutorial article |
| noise-based-terrain-generation | concept | Noise-Based Terrain Generation | Core methodology |
| fractional-brownian-motion | concept | Fractional Brownian Motion (FBM) | Octave stacking, amplitudes, gain |
| elevation-redistribution | concept | Elevation Redistribution | Power functions, terraces, curves |
| biome-maps | concept | Biome Maps | Elevation + moisture lookup |
| ridged-noise | concept | Ridged Noise | Absolute-value ridged noise |
| blue-noise-placement | concept | Blue Noise Placement | Object placement with noise |
| wraparound-noise | concept | Wraparound Noise | Cylinder/torus noise |
| island-shaping | concept | Island Shaping | Distance + shaping for islands |
| infinite-terrain | concept | Infinite Terrain | Local computation for endless maps |
| amit-patel | person | Amit Patel | Red Blob Games founder |

## Contradictions Detected / 检测到的矛盾

None. The existing wiki covers layer-based procedural generation (LayerProcGen), which operates at a different architectural level. Noise-based terrain generation as described here is a functional/locally-computed approach that aligns with and could serve as an input to layer-based systems — complementary, not contradictory.

## Proposed Cross-Links / 建议的交叉链接

- [[noise-based-terrain-generation]] ↔ [[functional-approach-procgen]] — noise-based terrain is a concrete example of functional, spatially-local generation
- [[noise-based-terrain-generation]] ↔ [[deterministic-generation]] — noise with fixed seed is deterministic
- [[infinite-terrain]] ↔ [[chunk-based-generation]] — infinite terrain can feed into chunk-based systems
- [[amit-patel]] ↔ [[rune-skovbo-johansen]] — both contributors to procedural generation

## Items for User Review / 待用户审核

- [ ] Proceeding automatically to Phase 2 (require_review not set in config)
