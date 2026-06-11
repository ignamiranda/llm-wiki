---
title: "Ridged Noise"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, noise, terrain, ridges]
aliases: [ridged-multifractal, absolute-value-noise]
summary: "A noise variant that uses the absolute value of noise to create sharp ridge features, often used for mountain ranges."
---

# Ridged Noise

## Definition

A noise variant where the absolute value of the noise function is taken to create sharp V-shaped ridges. The formula is `ridged = 2 * (0.5 - abs(0.5 - noise(nx, ny)))`, which folds the noise values back on themselves, producing a crease at the fold line.

## Key Properties

- **Sharp ridges**: The absolute value creates a sharp discontinuity at the midpoint, producing ridge-like features
- **Amplitude damping for multi-octave**: Higher octaves can be multiplied by the accumulated lower-frequency elevation so that ridged detail only appears in mountainous areas, not on flat terrain
- **Mixable**: Ridged noise can be used for low frequencies while regular noise handles high frequencies

## Examples

- Mountain ridge lines in terrain generation
- Sharp crease features on otherwise smooth terrain

## Related Concepts

- [[fractional-brownian-motion]] — ridged noise can be used within FBM octave stacking
- [[noise-based-terrain-generation]] — ridged noise is an alternative elevation technique
- [[elevation-redistribution]] — ridged noise output can be further reshaped

## References

- Patel, Amit J., "Making maps with noise functions", Red Blob Games, 2015, https://www.redblobgames.com/maps/terrain-from-noise/
