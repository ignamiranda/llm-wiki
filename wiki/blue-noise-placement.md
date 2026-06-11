---
title: "Blue Noise Placement"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, noise, placement, blue-noise]
aliases: [noise-object-placement, peak-detection-noise]
summary: "A technique using high-frequency noise to place irregularly spaced objects like trees and rocks by detecting local maxima."
---

# Blue Noise Placement

## Definition

A technique for placing irregularly spaced objects (trees, rocks, etc.) on a terrain map by evaluating high-frequency noise and detecting local maxima. The noise acts as a density function — louder peaks become object locations. The radius parameter controls the minimum spacing between objects.

## Key Properties

- **High frequency**: Unlike terrain noise (low frequency, high amplitude), object placement noise is high frequency (low wavelength)
- **Local maxima detection**: For each position, check if its noise value is the highest within a radius R of neighboring cells
- **Variable density**: Different biomes use different radius values to achieve different tree/object densities
- **Not recommended for production**: Patel recommends Poisson Disc sampling, jittered grids, or Wang tiles as more efficient alternatives with better distribution

## Examples

- Placing trees in forest biomes with density varying by biome type
- Scattering rocks on barren terrain

## Related Concepts

- [[noise-based-terrain-generation]] — part of the complete noise terrain pipeline
- [[biome-maps]] — biome type determines the placement density parameters

## References

- Patel, Amit J., "Making maps with noise functions", Red Blob Games, 2015, https://www.redblobgames.com/maps/terrain-from-noise/
