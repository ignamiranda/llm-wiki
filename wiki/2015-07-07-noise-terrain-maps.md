---
title: "Noise-Based Terrain Maps"
type: article
language: en
created: 2015-07-07
modified: 2026-06-11
tags: [procedural-generation, terrain, noise, game-development]
summary: "Amit Patel's tutorial on using Perlin/Simplex noise functions to generate 2D terrain maps for games, covering elevation, biomes, climate, islands, and infinite terrain."
source_url: "https://www.redblobgames.com/maps/terrain-from-noise/"
source_hash: "eac346bab4c5bf9bfa85bda9d13ab2cf0d72a3aa0960ada42ec9c947da4fca4d"
---

# Noise-Based Terrain Maps

## Summary

Amit Patel's comprehensive tutorial on using gradient noise (Perlin, Simplex) as a building block for 2D game terrain generation. Covers the entire pipeline from raw noise values to elevation maps, biome assignment, climate modeling, island shaping, and infinite/wraparound terrain. Emphasizes simplicity — the core loop fits in under 50 lines of code — while noting the limitations of purely local computation.

## Content

### Noise as a Building Block

The foundation is a bandwidth-limited gradient noise function (Perlin, Simplex, OpenSimplex) that maps each 2D location to a value in [0, 1]. This raw noise is then transformed through successive layers: octave stacking, redistribution, biome lookup, and shaping.

### Octaves and Fractional Brownian Motion

A single noise frequency produces bland terrain. By summing noise at multiple octaves with decreasing amplitudes (a technique known as Fractional Brownian Motion or FBM), the terrain gains realistic fractal detail. Typical amplitudes follow a geometric sequence: `[1, 1/2, 1/4, ...]`, but Patel notes that alternative amplitude sequences like `[1, 1/2, 1/3, 1/4, 1/5]` can produce more fine detail.

### Elevation Redistribution

Raw noise values are reshaped using mathematical functions. Raising elevation to a power pushes middle values down into valleys (creating flatter lowlands). Other redistribution functions produce terraces by rounding to discrete levels, or can be arbitrary curves like Photoshop's "curves" tool.

### Biomes from Two Noise Maps

Using only elevation for biomes creates banded terrain. By introducing a second noise map — moisture — and looking up biomes in a 2D table (elevation × moisture), the terrain becomes far more diverse. This mirrors ecologist Robert Whittaker's classification of biomes.

### Climate Modeling

Temperature is derived from both elevation and latitude. Near the poles, the climate is colder at the same elevation, and the equator is warmer. Seasonal variation and prevailing winds are noted as possible extensions.

### Island Shaping

Islands are created by combining the noise-based elevation with a distance-based shaping function. At the map center (distance 0), the shaping function outputs land; at the border (distance 1), it outputs water. Various distance functions (square bump, Euclidean-squared) produce different island shapes.

### Ridged Noise

Taking the absolute value of noise creates sharp ridge features. The ridges can be limited to mountains by multiplying higher octaves by lower-frequency elevation, so the ridged detail only appears where the terrain is already mountainous.

### Tree Placement with Blue Noise

High-frequency noise (blue noise) can place irregularly spaced objects like trees. A local maxima detection finds the noise peaks, which become tree locations. Patel recommends Poisson Disc sampling or jittered grids as more efficient alternatives.

### Wraparound Maps

Seamless wrapping maps use 3D or 4D noise, where 2D map coordinates are projected onto a cylinder (east-west wrap) or torus (north-south wrap) by converting to angles and using trigonometric functions.

### Infinite Terrain

Because each position is computed independently, the noise function supports infinite terrain. The camera position is subtracted from noise coordinates, allowing the player to scroll arbitrarily without pre-generating or storing the entire map.

## Key Takeaways

- Noise-based terrain generation is simple (<50 lines) and fast, ideal for prototyping and game jams
- The pure FBM approach is purely local — no global constraints like "there should be 3-5 lakes" or river systems
- Two noise maps (elevation + moisture) produce dramatically better biomes than one
- The technique was used in the alpha version of Realm of the Mad God, then replaced with a Voronoi-based generator
- Patel recommends starting with this approach and replacing it once the game design clarifies what the map needs

## Related

- [[functional-approach-procgen]] — noise-based terrain is a concrete example of spatially-local, functional generation
- [[deterministic-generation]] — noise with a fixed seed produces deterministic output
- [[noise-based-terrain-generation]] — the core methodology
- [[fractional-brownian-motion]] — octave stacking technique
- [[elevation-redistribution]] — power functions and curves for elevation shaping
- [[biome-maps]] — elevation × moisture biome lookup
- [[ridged-noise]] — absolute-value noise for sharp ridges
- [[blue-noise-placement]] — high-frequency noise for tree placement
- [[island-shaping]] — distance-based island constraint
- [[wraparound-noise]] — seamless tileable noise maps
- [[infinite-terrain]] — locally-computed infinite worlds
- [[amit-patel]] — author of this tutorial
- [[rune-skovbo-johansen]] — another contributor to procedural generation techniques
