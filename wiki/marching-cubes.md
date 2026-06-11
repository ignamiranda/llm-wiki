---
title: "Marching Cubes"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [marching-cubes, isosurface-extraction, mesh-generation, algorithm, computer-graphics]
aliases: [mc-algorithm, lorensen-cline]
summary: "A computer graphics algorithm for extracting a polygonal mesh from a three-dimensional scalar field (voxel grid) by processing each cube independently with 15 base case patterns."
---

# Marching Cubes

## Definition

Marching Cubes, introduced by Lorensen and Cline in 1987, is a fundamental isosurface extraction algorithm that converts a three-dimensional scalar field (voxel grid) into a triangle mesh. It processes each cubic cell independently: for each of the 8 corners, it classifies the corner as inside or outside the isosurface, creating one of 256 possible configurations that reduce via symmetry to 15 base cases. Each case defines a triangulation pattern, producing a watertight manifold surface.

## Key Properties

- First published: Lorensen & Cline, "Marching Cubes: A High Resolution 3D Surface Construction Algorithm" (SIGGRAPH 1987)
- Operates on regular 3D voxel grids with scalar values at each vertex
- 15 canonical triangulation patterns (256 configurations via rotation/mirror symmetry)
- Produces watertight, manifold meshes suitable for rendering and 3D printing
- Ambiguous face configurations can cause topological holes — resolved by Marching Tetrahedra
- O(1) per cell; total complexity O(n^3) for an n×n×n grid
- GPU-parallelizable: each cube is independent, ideal for compute shaders

## Variants

- [[marching-tetrahedra]] — subdivides cubes into tetrahedra to eliminate face ambiguities
- [[transvoxel-algorithm]] — Eric Lengyel's extension for seamless LOD transitions between chunks
- [[dual-marching-cuboids]] — greedy meshing hybrid, producing fewer polygons via merged cuboids
- [[differentiable-marching-cubes]] — CUDA-accelerated variant with gradient backpropagation for deep learning
- Dual Marching Cubes — places vertices at dual grid positions for better feature preservation

## Related Concepts

- [[greedy-meshing]] — mesh optimization merging adjacent faces; fewer polygons but blockier
- [[kinect-fusion]] — real-time TSDF fusion pipeline using Marching Cubes for mesh extraction
- [[voxel-carving]] — 3D reconstruction from silhouettes, with Marching Cubes for final mesh extraction
- [[sph-surface-reconstruction]] — extracts surfaces from particle simulations
- [[terrain-lod-stitching]] — LOD transition techniques for chunk-based terrain meshing

## References

- Lorensen, W. E. & Cline, H. E. (1987). "Marching Cubes: A High Resolution 3D Surface Construction Algorithm." SIGGRAPH '87.
- Lengyel, E. "Transvoxel Algorithm." Game Engine Gems.
- Bourke, P. "Polygonising a Scalar Field." http://paulbourke.net/geometry/polygonise/
