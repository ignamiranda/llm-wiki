---
title: "Noise-Based Terrain Generation"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, terrain, noise, game-development]
aliases: [noise-terrain, gradient-noise-terrain]
summary: "A methodology for generating 2D terrain maps using Perlin/Simplex noise as the primary building block, transformed through octave stacking, redistribution, and biome lookup."
---

# Noise-Based Terrain Generation

## Definition / 定义

A terrain generation approach where bandwidth-limited gradient noise (Perlin, Simplex, OpenSimplex) is evaluated at each map position and then transformed through a pipeline of octave stacking (FBM), elevation redistribution, and biome lookup to produce height maps and biome maps. Each position is computed independently, enabling parallel generation and infinite terrain.

## Key Properties / 关键特性

- **Purely local computation** — each position is independent of all others, enabling parallelism and infinite terrain
- **Simple implementation** — core loop in under 50 lines of code in most languages
- **Deterministic** — same seed + same parameters always produces the same map
- **Limited by locality** — no global features (rivers, lakes, mountain ranges with intent), no spatial relationships beyond local noise correlation
- **Parameter-heavy** — requires significant tweaking of frequencies, amplitudes, exponents, and biome thresholds

## Examples / 示例

- Early alpha maps for Realm of the Mad God
- Prototyping terrain for game jams and indie games
- Procedural planet surfaces in space games

## Related Concepts / 相关概念

- [[fractional-brownian-motion]] — the octave stacking technique that produces fractal terrain detail
- [[elevation-redistribution]] — reshaping noise values with power functions and curves
- [[biome-maps]] — using two noise maps (elevation + moisture) for biome assignment
- [[ridged-noise]] — absolute-value noise for sharp ridge features
- [[blue-noise-placement]] — high-frequency noise for object placement
- [[island-shaping]] — constraining noise terrain to island forms
- [[wraparound-noise]] — seamless tileable noise maps
- [[infinite-terrain]] — locally-computed endless worlds
- [[functional-approach-procgen]] — noise-based generation is an example of functional, spatially-local generation
- [[deterministic-generation]] — noise with fixed seed is deterministic
- [[chunk-based-generation]] — noise terrain can feed chunk-based world systems
- [[amit-patel]] — author of the Red Blob Games tutorial on this technique
- [[wave-function-collapse]] — alternative constraint-based approach
- [[2026-06-11-wfc-implementations-survey]] — survey of WFC implementations

## References / 参考资料

- Patel, Amit J., "Making maps with noise functions", Red Blob Games, 2015, https://www.redblobgames.com/maps/terrain-from-noise/
