---
title: "Unity Marching Cubes GPU — ComputeShader Implementation"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [marching-cubes, unity, compute-shader, gpu, procedural-geometry]
summary: "A GPU ComputeShader implementation of Marching Cubes for Unity 5.6+, with density field generation on CPU and procedural geometry drawing."
---

# Unity Marching Cubes GPU — ComputeShader Implementation

## Summary

Pavel Kouril's Unity Marching Cubes GPU implementation uses ComputeShader for triangulation with CPU-based density field generation and a barebones procedural geometry shader for rendering.

## Content

The density field is generated on CPU (using Texture3D, with suggestion to switch to RenderTexture for real applications). The Marching Cubes ComputeShader performs triangulation on GPU, and results are drawn via a procedural geometry shader with basic diffuse lighting. Based on Paul Bourke's lookup tables and gradient normals calculation from MCAdvanced.

## Key Takeaways

- ComputeShader-based Marching Cubes triangulation
- CPU-based density field (Texture3D)
- Procedural geometry shader for rendering
- Requires DX11 hardware
- 75 stars, MIT license

## Related

- [[marching-cubes]] — core algorithm
- [[2026-06-11-scrawk-marching-cubes-gpu]] — related GPU implementation
- [[2026-06-11-voxel-game-rs]] — related compute shader approach

## Links

- Repository: https://github.com/pavelkouril/unity-marching-cubes-gpu
