---
title: "Island Shaping"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, noise, terrain, islands]
aliases: [island-noise, terrain-constraint]
summary: "A technique for constraining noise-generated terrain to island shapes by combining noise elevation with a distance-based shaping function."
---

# Island Shaping

## Definition / 定义

A technique for creating island-shaped terrain from noise by combining the noise-based elevation with a distance-based shaping function. At the map center (distance 0), the shaping function outputs land; at the border (distance 1), it outputs water. The two values are mixed to produce an island that retains noise-driven detail while ensuring the edges are submerged.

## Key Properties / 关键特性

- **Distance functions**: Common choices include square bump (`d = 1 - (1-nx²)(1-ny²)` for filling a square map) and Euclidean-squared (`d = min(1, (nx²+ny²)/√2)` for round islands)
- **Shaping via linear mixing**: `e = lerp(e, 1-d, mix_amount)` where mix_amount controls how strongly the island shape constrains the noise
- **Non-linear alternatives**: The shaping need not be linear — exponent changes, lookup tables, or applying only to low-frequency octaves produce different island shapes
- **Land area control**: After shaping, elevations can be shifted up or down to achieve a desired land-to-water ratio
- **Separate shape from elevation**: The island shape and the elevation detail can be generated independently and combined

## Examples / 示例

- Single-island maps where the entire playable area is one landmass
- Archipelago maps with multiple shaped islands
- Continent outlines for world maps

## Related Concepts / 相关概念

- [[noise-based-terrain-generation]] — island shaping is applied on top of noise terrain
- [[elevation-redistribution]] — the shaping function is a form of redistribution
- [[infinite-terrain]] — island shaping differs from infinite terrain in that the bounds are fixed

## References / 参考资料

- Patel, Amit J., "Making maps with noise functions", Red Blob Games, 2015, https://www.redblobgames.com/maps/terrain-from-noise/
