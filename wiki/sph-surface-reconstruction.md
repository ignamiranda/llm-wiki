---
title: "SPH Surface Reconstruction"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [sph, fluid-simulation, surface-reconstruction, marching-cubes, particle-system]
aliases: [sph-mesh-reconstruction, particle-surface-reconstruction]
summary: "The process of generating a triangle mesh surface from SPH (Smoothed Particle Hydrodynamics) fluid simulation particle data, typically using Marching Cubes on a reconstructed density field."
---

# SPH Surface Reconstruction

## Definition

SPH Surface Reconstruction converts particle data from Smoothed Particle Hydrodynamics fluid simulations into a closed triangle mesh suitable for rendering. The approach computes a density field on a background grid using SPH kernel interpolation over neighbor particles, then extracts the fluid surface as an isosurface using Marching Cubes. The result eliminates the "ball pit" look of raw particles and produces renderable fluid surfaces.

## Key Properties

- Uses SPH kernel interpolation to reconstruct a continuous density field
- Marching Cubes extracts the surface at a chosen density threshold
- Domain decomposition (subdomain grids) enables parallel processing of large simulations
- Weighted Laplacian smoothing removes bumpy artifacts while preserving volume
- Handles millions of particles in seconds
- Supports attribute interpolation (normals, velocities) onto the mesh surface

## Related Concepts

- [[marching-cubes]] — core extraction algorithm
- [[greedy-meshing]] — alternative approach for mesh simplification

## References

- splashsurf: https://github.com/InteractiveComputerGraphics/splashsurf
