---
title: "Erosion Filter Technique"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, terrain, erosion, noise, directional-noise, shadertoy]
aliases: [non-simulated erosion, stripe-noise erosion, eroded terrain noise]
summary: "A non-simulated terrain erosion technique that produces branching gullies and ridges using gradient-aligned stripe noise, where every point can be evaluated in isolation."
---

# Erosion Filter Technique

## Definition

An erosion filter technique that produces the appearance of hydraulic erosion on terrain without simulating water flow. Instead, it uses gradient-aligned stripe noise — stripes generated along the direction of steepest descent — to carve gullies and ridges that naturally branch at multiple scales. Every point evaluates independently, making it fast, GPU-friendly, and suitable for chunk-based infinite terrain.

## Key Properties

- **Non-simulated**: No particle-based water simulation; purely noise-driven
- **GPU-friendly**: Each point evaluated in isolation — perfect for pixel shaders
- **Chunk-compatible**: Trivial to generate in independent chunks
- **Filter architecture**: Applied on top of any height function as a post-process
- **Multi-octave**: Repeated at decreasing scales for branching detail
- **Analytical derivatives**: Outputs both height and slope/gradient
- **Open source**: [[rune-skovbo-johansen]]'s implementation released under MPL-2.0

## Evolution

1. **Clay John (2018)**: Original *Eroded Terrain Noise* Shadertoy — proof of concept with frequency approach for peaks/valleys
2. **Felix Westin / Fewes (2023)**: Visual refinement with polished presentation, same core technique
3. **Rune Skovbo Johansen (2025-2026)**: Derivative corrections, fade approach, stacked fading, normalized gullies, straight gullies, Phacelle Noise extraction, ridge maps, edge rounding

## Examples

- [Advanced Terrain Erosion Filter](https://www.shadertoy.com/view/wXcfWn) — Johansen's final iteration on Shadertoy
- [Mouse-Paint Eroded Mountains](https://www.shadertoy.com/view/sf23W1) — interactive version
- [Clean Terrain Erosion Filter](https://www.shadertoy.com/view/33cXW8) — frequency-approach rewrite
- [Eroded Terrain Noise](https://www.shadertoy.com/view/MtGcWh) — original by Clay John
- [Terrain Erosion Noise](https://www.shadertoy.com/view/7ljcRW) — Fewes' refinement

## Related Concepts

- [[phacelle-noise]] — directional noise function extracted from this technique
- [[directional-noise]] — broader category of directional noise
- [[fractional-brownian-motion]] — another multi-octave noise technique
- [[infinite-terrain]] — chunk-based terrain this technique enables
- [[layerprocgen]] — related work by the same author

## References

- [Blog post: Fast and Gorgeous Erosion Filter](https://blog.runevision.com/2026/03/fast-and-gorgeous-erosion-filter.html)
- [YouTube: Fast & Gorgeous Erosion Filter Explained](https://www.youtube.com/watch?v=r4V21_uUK8Y)
