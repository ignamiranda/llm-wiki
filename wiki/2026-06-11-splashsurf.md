---
title: "splashsurf — SPH Surface Reconstruction in Rust"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [sph, fluid-simulation, surface-reconstruction, marching-cubes, rust, blender]
summary: "A Rust library and CLI for fast Marching Cubes-based surface reconstruction from SPH fluid simulation particle data."
---

# splashsurf — SPH Surface Reconstruction in Rust

## Summary

splashsurf is a Rust surface reconstruction tool from Interactive Computer Graphics (RWTH Aachen) that converts SPH particle data into triangle meshes using Marching Cubes with domain decomposition, weighted Laplacian smoothing, and Python/Blender bindings.

## Content

The project comprises a CLI binary (splashsurf), a library (splashsurf_lib), Python bindings (pysplashsurf), and a Blender add-on (splashsurf_studio). It uses subdomain grid-based decomposition for parallelism, SPH density field reconstruction, Marching Cubes triangulation, and weighted Laplacian smoothing (Löschner et al. 2023). Handles 13M particles in ~2.5 seconds on an M4 Pro.

## Key Takeaways

- Domain decomposition for scalable parallelism
- Weighted Laplacian smoothing preserves volume
- Python bindings and Blender add-on
- Supports VTK, BGEO, PLY, XYZ, JSON input formats
- 296 stars, MIT license

## Related

- [[sph-surface-reconstruction]] — core technique
- [[marching-cubes]] — extraction algorithm

## Links

- Repository: https://github.com/InteractiveComputerGraphics/splashsurf
