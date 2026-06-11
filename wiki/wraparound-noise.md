---
title: "Wraparound Noise"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, noise, wraparound, tiling, maps]
aliases: [seamless-noise, tileable-noise, toroidal-noise]
summary: "Techniques for creating tileable noise maps using cylindrical (3D) or toroidal (4D) noise coordinate projections."
---

# Wraparound Noise

## Definition

A technique for generating seamless tileable noise maps by projecting 2D map coordinates onto higher-dimensional surfaces. For east-west wrapping, noise is sampled from a cylinder embedded in 3D space: `noise3D(cos(angle_x), sin(angle_x), ny)`. For full four-direction wrapping, a torus in 4D space: `noise4D(cos(angle_x), sin(angle_x), cos(angle_y), sin(angle_y))`.

## Key Properties

- **Cylindrical wrap**: East-west only — map rolls like a cylinder
- **Toroidal wrap**: Both east-west and north-south — map tiles in all four directions
- **Higher-dimensional noise**: Requires 3D or 4D noise functions with access to those input dimensions
- **Range adjustment**: Higher-dimensional noise has a narrower value range than 2D noise — multiply 3D noise by ~√1.5 and 4D noise by ~√2 to compensate
- **Octave correlation concern**: Per the Cook-DeRose Wavelet Noise paper, 2D surfaces sampled from 3D noise may not be perfectly band-limited even if the 3D function is
- **Coordinate scaling**: The circle's circumference must equal 1 (or equivalently the line length) to avoid seam distortion

## Examples

- Planet surface maps where east and west edges must match
- Tileable texture generation for terrain repetition

## Related Concepts

- [[fractional-brownian-motion]] — FBM can be applied to wraparound noise for fractal detail
- [[noise-based-terrain-generation]] — wraparound noise is a variant coordinate system for the same pipeline

## References

- Patel, Amit J., "Making maps with noise functions", Red Blob Games, 2015, https://www.redblobgames.com/maps/terrain-from-noise/
- Cook, Robert L. and Tony DeRose, "Wavelet Noise", Pixar, https://graphics.pixar.com/library/WaveletNoise/paper.pdf
- Valstar, Ron, "Creating tileable noise maps", https://ronvalstar.nl/creating-tileable-noise-maps
