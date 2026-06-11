---
title: "Phacelle Noise"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, noise, directional-noise, shadertoy, terrain]
aliases: []
summary: "A directional noise function extracted by Rune Skovbo Johansen from the erosion filter technique, producing gradient-aligned stripes with consistent magnitude via partial normalization."
---

# Phacelle Noise

## Definition

A directional noise function extracted by [[rune-skovbo-johansen]] from the [[erosion-filter-technique|erosion filter technique]]. It produces gradient-aligned stripe patterns with consistent magnitude, achieved by normalizing interpolated cosine/sine pairs (treated as points on a unit circle) back to radius 1. Partial normalization (threshold at 0.5) avoids spiky artifacts that full normalization would cause.

## Key Properties

- **Directional**: Stripes align with an input gradient direction
- **Consistent magnitude**: Normalization keeps gully/ridge amplitude uniform
- **GPU-compatible**: Each point evaluates independently
- **Extracted from**: The erosion filter technique, usable standalone for other purposes
- **Cell-based**: Divides space into cells with individual pivot points, blends between neighbors

## Examples

- [Phacelle Noise Animation](https://www.shadertoy.com/view/t3dyWl) — demonstration Shadertoy
- [Blog post: Phacelle — Cheap Directional Noise](https://blog.runevision.com/2026/01/phacelle-cheap-directional-noise.html)

## Related Concepts

- [[erosion-filter-technique]] — the filter technique from which Phacelle Noise was extracted
- [[directional-noise]] — broader category
- [[ridged-noise]] — another noise variant for terrain features

## References

- [Phacelle — Cheap Directional Noise (blog post)](https://blog.runevision.com/2026/01/phacelle-cheap-directional-noise.html)
- [Phacelle Noise Shadertoy](https://www.shadertoy.com/view/t3dyWl)
