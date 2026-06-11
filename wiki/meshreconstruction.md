---
title: "MeshReconstruction"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [marching-cubes, mesh-generation, signed-distance-functions, cpp, library]
aliases: []
summary: "A fast, lightweight, self-contained C++14 Marching Cubes library with no dependencies, featuring precomputed lookup tables and narrow-band surface tracking."
---

# MeshReconstruction

## Definition

MeshReconstruction is a minimal C++14 library that reconstructs triangle meshes from signed distance functions using Marching Cubes and exports them to Wavefront OBJ format. It is self-contained with zero external dependencies, using precomputed lookup tables for speed and a narrow-band approach that skips marching cubes cells far from the surface.

## Key Properties

- Zero external dependencies (self-contained)
- C++14 required
- Narrow-band optimization skips empty regions
- Precomputed lookup tables for fast edge/case resolution
- Exports to Wavefront OBJ format
- Tested on Visual Studio 2017 / Windows 10

## Related Concepts

- [[marching-cubes]] — core algorithm
- [[nii2mesh]] — related C-based marching cubes implementation

## References

- Repository: https://github.com/Magnus2/MeshReconstruction
