---
title: "Elevation Redistribution"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, noise, terrain, elevation]
aliases: [height-redistribution, elevation-shaping]
summary: "Techniques for reshaping noise-based elevation values using mathematical functions to create specific terrain characteristics like flat valleys or terraced hills."
---

# Elevation Redistribution

## Definition

The process of applying a function to raw noise-generated elevation values to reshape their distribution. Common redistribution functions include power functions (raising elevation to an exponent to flatten valleys), rounding to discrete levels (creating terraces), and arbitrary user-defined curves.

## Key Properties

- **Power function**: `e = Math.pow(e * fudge, exponent)` — exponent > 1 pushes middle elevations down into valleys, exponent < 1 pulls them up toward peaks
- **Fudge factor**: A multiplier near 1 (e.g., 1.2) can be applied before the power function to shift the distribution
- **Terraces**: `e = Math.round(e * n) / n` creates discrete elevation bands
- **Arbitrary curves**: Any function can be used, including curves tools from photo editors
- **Must be tuned per generator**: Optimal redistribution depends on the noise library, octave amplitudes, and desired aesthetic

## Examples

- Flat valley floors under steep mountains (power function with exponent 3-5)
- Step-like terraced hillsides for stylized or strategy-game terrain
- Custom curve profiles for specific planet types (water worlds, volcanic, etc.)

## Related Concepts

- [[noise-based-terrain-generation]] — redistribution is a step in the noise terrain pipeline
- [[fractional-brownian-motion]] — produces the input that redistribution transforms
- [[biome-maps]] — redistributed elevation is used as input to biome lookup
- [[island-shaping]] — uses similar shaping functions to constrain terrain to island forms

## References

- Patel, Amit J., "Making maps with noise functions", Red Blob Games, 2015, https://www.redblobgames.com/maps/terrain-from-noise/
