---
title: "Scrawk Marching Cubes — Unity CPU Implementation"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [marching-cubes, unity, voxel, marching-tetrahedra, mesh-generation]
summary: "A Unity implementation of Marching Cubes and Marching Tetrahedra algorithms for CPU-based voxel mesh generation."
---

# Scrawk Marching Cubes — Unity CPU Implementation

## Summary

Scrawk's Marching-Cubes repository provides both Marching Cubes and Marching Tetrahedra implementations in Unity C#. Based on a well-regarded reference implementation, it offers optional smooth normal computation through gradient-based interpolation.

## Content

The implementation is based on Paul Bourke's polygonization code and a reference from siafoo.net that also includes the harder-to-find Marching Tetrahedra algorithm. The Marching Tetrahedra variant produces meshes that match voxel data more faithfully than standard cubes but yields more vertices. Smooth normals can be optionally computed using the gradient of the voxel field for improved visual quality.

## Key Takeaways

- Implements both Marching Cubes and Marching Tetrahedra
- Optional gradient-based smooth normal computation
- 521 stars, MIT license
- Pure C# (no compute shaders)

## Related

- [[marching-cubes]] — core algorithm
- [[marching-tetrahedra]] — alternative algorithm also implemented
- [[2026-06-11-scrawk-marching-cubes-gpu]] — GPU version by the same author

## Links

- Repository: https://github.com/Scrawk/Marching-Cubes
