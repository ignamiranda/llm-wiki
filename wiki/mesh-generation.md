---
title: "Mesh Generation"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [mesh-generation, computer-graphics, 3d-modeling, computational-geometry]
aliases: [meshing]
summary: "The process of generating a polygonal mesh from implicit surfaces (isosurfaces), point clouds, volumetric data, or parametric models for rendering, simulation, or 3D printing."
---

# Mesh Generation

## Definition

Mesh generation converts mathematical or sampled representations of 3D geometry into polygonal meshes (typically triangle or quad meshes) suitable for rendering, simulation, or fabrication. It encompasses techniques from computer graphics, computational geometry, and engineering simulation.

## Key Techniques

- [[marching-cubes]] — extracts meshes from voxel grids or implicit surfaces
- [[greedy-meshing]] — merges adjacent faces for polygon reduction in block-aligned geometry
- [[dual-marching-cuboids]] — greedy meshing with dual contouring for watertight results
- [[marching-tetrahedra]] — tetrahedral subdivision to resolve marching cubes ambiguities
- Dual Contouring — vertex placement at feature points for sharp edges

## Related Concepts

- [[solid-modeling]] — representation of solid geometry (B-rep, CSG, F-rep)
- [[sph-surface-reconstruction]] — mesh extraction from particle simulations
- [[functional-representation-solid-modeling]] — F-rep meshing pipeline
