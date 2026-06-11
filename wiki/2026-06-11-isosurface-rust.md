---
title: "isosurface — Rust Isosurface Extraction Library"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [marching-cubes, dual-contouring, rust, isosurface-extraction, graphics]
summary: "A Rust library implementing Marching Cubes, Dual Contouring, and related isosurface extraction algorithms with educational documentation."
---

# isosurface — Rust Isosurface Extraction Library

## Summary

The isosurface Rust library by Tristam MacDonald provides implementations of classic Marching Cubes, Dual Contouring, and modern variants, with documentation linking each algorithm to its academic papers.

## Content

The library intentionally has zero dependencies (reimplementing Vec3 etc. internally) to keep footprint small. Includes Marching Cubes and Dual Contouring with modern variations. Examples demonstrate a sampler for comparing algorithms and GPU-side deferred rasterisation from point clouds (based on Voxel Quest techniques). Uses 32-bit indices for chunks up to 32x32x32 and beyond.

## Key Takeaways

- Zero-dependency Rust library
- Marching Cubes + Dual Contouring implementations
- Educational docs linking to academic papers
- GPU deferred rasterisation example
- 80 stars, Apache-2.0 license

## Related

- [[marching-cubes]] — one of the implemented algorithms
- [[tristam-macdonald]] — author

## Links

- Repository: https://github.com/swiftcoder/isosurface
