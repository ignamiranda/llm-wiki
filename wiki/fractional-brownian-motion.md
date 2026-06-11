---
title: "Fractional Brownian Motion (FBM)"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, noise, fractals, terrain]
aliases: [fbm, noise-octaves, fractal-noise]
summary: "A technique that sums noise at multiple octaves with decreasing amplitudes to produce fractal-like detail in terrain generation."
---

# Fractional Brownian Motion (FBM)

## Definition / 定义

A technique for generating fractal-like detail by summing noise at integer-multiple frequencies (octaves), each with decreasing amplitude. The resulting signal combines large-scale structure from low octaves with fine detail from high octaves, mimicking the statistical properties of natural terrain.

## Key Properties / 关键特性

- **Octaves**: Each successive octave doubles the frequency (halves the wavelength)
- **Amplitudes**: Traditionally follow a geometric series `[1, 1/2, 1/4, 1/8, ...]` where the ratio (gain/persistence) is 0.5
- **Amplitude normalization**: The sum must be divided by the total amplitude to stay in [0, 1]
- **Alternatives**: Non-geometric amplitudes like `[1, 1/2, 1/3, 1/4, ...]` can produce more fine detail
- **Correlation issue**: Without independent seeding or offsets, octaves sampling near the origin are correlated, producing artifacts
- **Range compression**: Higher-dimensional noise has a narrower value range — 3D noise may need √1.5 scaling, 4D noise √2

## Examples / 示例

- Generating realistic terrain elevation maps with rolling hills and rugged mountains
- Creating moisture maps with multi-scale detail

## Related Concepts / 相关概念

- [[noise-based-terrain-generation]] — FBM is the core elevation step in noise-based terrain
- [[elevation-redistribution]] — FBM output is further reshaped by power functions
- [[ridged-noise]] — a variant where FBM uses absolute-value noise
- [[wraparound-noise]] — FBM applied to cylindrical/toroidal noise coordinates

## References / 参考资料

- Patel, Amit J., "Making maps with noise functions", Red Blob Games, 2015, https://www.redblobgames.com/maps/terrain-from-noise/
