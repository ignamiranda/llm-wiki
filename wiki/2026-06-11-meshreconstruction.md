---
title: "MeshReconstruction — Lightweight C++ Marching Cubes Library"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [marching-cubes, cpp, signed-distance-functions, mesh-generation, library]
summary: "A fast, dependency-free C++14 library for Marching Cubes mesh reconstruction from signed distance functions."
---

# MeshReconstruction — Lightweight C++ Marching Cubes Library

## Summary

MeshReconstruction by Magnus2 is a minimal C++14 library that extracts triangle meshes from signed distance functions using Marching Cubes with narrow-band optimization, precomputed lookup tables, and OBJ export — all with zero external dependencies.

## Content

The library is self-contained (single header + implementation pattern), uses precomputed lookup tables for fast triangulation, and employs a narrow-band approach that skips marching cubes cells far from the surface. It exports to Wavefront OBJ format.

## Key Takeaways

- Zero external dependencies
- Narrow-band surface tracking for efficiency
- Precomputed lookup tables
- Single commit repository (stable/reference implementation)
- 182 stars, MIT license

## Related

- [[meshreconstruction]] — concept page
- [[marching-cubes]] — core algorithm
- [[nii2mesh]] — related C-based implementation

## Links

- Repository: https://github.com/Magnus2/MeshReconstruction
