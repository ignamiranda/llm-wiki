---
title: "Transvoxel Algorithm"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [marching-cubes, transvoxel, level-of-detail, voxel, algorithm]
aliases: [transvoxel]
summary: "Eric Lengyel's Transvoxel Algorithm extends Marching Cubes with seamless level-of-detail transitions between adjacent voxel chunks at different resolutions."
---

# Transvoxel Algorithm

## Definition

The Transvoxel Algorithm, developed by Eric Lengyel, extends the classic Marching Cubes algorithm to support seamless level-of-detail (LOD) transitions between adjacent voxel blocks at different resolutions. It introduces additional lookup tables for "transvoxel" cells at the boundary between high-resolution and low-resolution regions, eliminating cracks and T-junctions without requiring crack patching.

## Key Properties

- Adds ~512 supplementary lookup table entries for transition cells
- Guarantees watertight seams between LOD levels
- Commonly used in voxel terrain engines with clipmap LOD schemes
- Described in Lengyel's book "Game Engine Gems"
- Official reference implementation and data tables hosted at transvoxel.org

## Related Concepts

- [[marching-cubes]] — base algorithm extended by Transvoxel
- [[terrain-lod-stitching]] — related approach for LOD transitions in terrain

## References

- Official site: https://transvoxel.org
- Repository: https://github.com/EricLengyel/Transvoxel
