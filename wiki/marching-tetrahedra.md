---
title: "Marching Tetrahedra"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [marching-cubes, isosurface-extraction, mesh-generation, algorithm]
aliases: [marching-tetrahedron-algorithm]
summary: "An isosurface extraction algorithm that subdivides each cube into tetrahedra before triangulation, producing meshes that match voxel data better than marching cubes but with more vertices."
---

# Marching Tetrahedra

## Definition

Marching Tetrahedra is an isosurface extraction algorithm that splits each cubic cell into multiple tetrahedra before applying case-based triangulation. Unlike Marching Cubes (which operates on cube corners directly), the tetrahedral subdivision reduces or eliminates ambiguities in surface topology and produces meshes that more faithfully represent the underlying scalar field, at the cost of generating more vertices and triangles.

## Key Properties

- Subdivides each cube into 5, 6, or 24 tetrahedra before triangulation
- Eliminates ambiguous face configurations that plague standard Marching Cubes
- Produces more vertices per cell than Marching Cubes (~4x more)
- Better surface quality and topological correctness
- Higher computational and memory cost

## Related Concepts

- [[marching-cubes]] — the base algorithm; marching tetrahedra improves on its ambiguities
- [[transvoxel-algorithm]] — another marching-cubes variant for LOD transitions

## References

- Implemented in Scrawk's Marching-Cubes Unity project alongside the standard cubes algorithm
