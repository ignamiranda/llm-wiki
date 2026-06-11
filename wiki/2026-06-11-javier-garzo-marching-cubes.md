---
title: "Marching Cubes on Unity 3D (Javier Garzo) — Voxel Engine"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [marching-cubes, unity, voxel-engine, terrain-generation, biome-system, chunk-system]
summary: "A full voxel engine for Unity 2020 (LTS) with Marching Cubes terrain generation, biome system, chunk management, real-time editing, and save/load functionality."
---

# Marching Cubes on Unity 3D (Javier Garzo) — Voxel Engine

## Summary

Javier Garzo's project is a comprehensive voxel engine for Unity 2020.3 LTS implementing Marching Cubes with a biome system, chunk-based infinite terrain, real-time editing (add/remove voxels), and region-based save/load.

## Content

The engine features a biome system using noise-based blending for varied terrain types (desert, ice, plains, mountains), a chunk system with view-distance management, surface tracking for mesh generation, and a region file system for persistent worlds. It uses the Job System and Burst Compiler for chunk generation. Configuration is exposed through constants and manager GameObjects for easy customization.

## Key Takeaways

- Full voxel engine with biome blending and infinite terrain
- Real-time terrain editing with left-click add / right-click remove
- Region file system for world persistence (.reg files)
- 378 stars, MIT license
- References Sebastian Lague's tutorials and Paul Bourke's algorithm description

## Related

- [[marching-cubes]] — core algorithm
- [[2026-06-11-eldemarkki-marching-cubes-terrain]] — related Unity terrain project
- [[biome-maps]] — related biome generation concept

## Links

- Repository: https://github.com/Javier-Garzo/Marching-cubes-on-Unity-3D
