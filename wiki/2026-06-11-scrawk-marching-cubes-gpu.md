---
title: "Marching Cubes on the GPU — Unity Compute Shader Implementation"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [marching-cubes, unity, compute-shader, gpu, voxel, perlin-noise]
summary: "A Unity implementation of Marching Cubes entirely on the GPU using compute shaders, with Perlin noise-based voxel generation and procedural rendering."
---

# Marching Cubes on the GPU — Unity Compute Shader Implementation

## Summary

Scrawk's GPU Marching Cubes project implements the entire voxel generation and mesh extraction pipeline on the GPU using Unity compute shaders, with Perlin noise-based density generation and procedural rendering via compute buffers.

## Content

The implementation uses compute shaders for both voxel generation (improved Perlin noise) and Marching Cubes triangulation. Vertices are written to a compute buffer and rendered using Unity's DrawProcedural. A fixed-size buffer is pre-allocated for the maximum possible vertices (5 triangles per voxel), with zero-filled unused vertices resulting in zero-area triangles that produce no fragments. The project also includes smoothed normal computation via voxel derivative interpolation and 4D Perlin noise animation for dynamic mesh sequences.

## Key Takeaways

- Full GPU pipeline: voxel generation + triangulation
- DrawProcedural rendering from compute buffers
- Fixed-size buffer with zero-area triangle culling
- 299 stars, MIT license

## Related

- [[marching-cubes]] — core algorithm
- [[2026-06-11-scrawk-marching-cubes]] — CPU implementation by same author
- [[2026-06-11-unity-marching-cubes-gpu]] — related GPU implementation

## Links

- Repository: https://github.com/Scrawk/Marching-Cubes-On-The-GPU
