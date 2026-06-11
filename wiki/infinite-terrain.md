---
title: "Infinite Terrain"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, terrain, infinite-worlds, noise]
aliases: [endless-terrain, camera-offset-noise]
summary: "A locally-computed terrain generation technique where any position in an unbounded world can be generated on demand by offsetting noise coordinates by the camera position."
---

# Infinite Terrain

## Definition

An approach to generating unbounded (infinite) terrain by exploiting the locality of noise computation. Instead of pre-generating the entire world, the camera position is subtracted from the noise coordinates: `noise(nx - camera.x, ny - camera.y)`. This allows any position in the world to be generated independently, on demand, without storing or pre-computing the full map.

## Key Properties

- **Fully local**: Each position is computed independently — no global constraints (rivers, lakes, mountain chains) spanning across view boundaries
- **Parallelizable**: Multiple positions can be computed simultaneously
- **No memory ceiling**: Only the visible area needs to be stored
- **Inherently seamless**: Because the same coordinates always produce the same noise, there are no seams between computed regions
- **Camera-driven**: The camera position (or player position) determines the offset into noise space
- **Not suitable for all games**: Games requiring global features (hand-placed dungeons, continent-spanning rivers) need a hybrid approach

## Examples

- Scrolling terrain in sandbox games
- Procedural open worlds where players can travel arbitrarily far

## Related Concepts

- [[noise-based-terrain-generation]] — noise is the foundation technique for infinite terrain
- [[chunk-based-generation]] — infinite terrain can be divided into chunks for loading/unloading
- [[functional-approach-procgen]] — infinite terrain exemplifies purely functional/spatially-local generation
- [[deterministic-generation]] — infinite terrain is deterministic if the seed is fixed
- [[island-shaping]] — contrasts with infinite terrain (bounded vs unbounded)
- [[modifying-in-blocks]] — an alternative approach to infinite/unbounded generation using WFC
- [[terrain-lod-stitching]] — stitching LOD tile boundaries in infinite terrain rendering
- [[2026-06-11-terrain3d]] — a Godot 3.5 implementation of infinite terrain with LOD stitching

## References

- Patel, Amit J., "Making maps with noise functions", Red Blob Games, 2015, https://www.redblobgames.com/maps/terrain-from-noise/
