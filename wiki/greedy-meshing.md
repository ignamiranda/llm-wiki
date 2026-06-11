---
title: "Greedy Meshing"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [marching-cubes, mesh-generation, optimization, voxel, geometry]
aliases: [greedy-voxel-meshing]
summary: "A mesh optimization technique that merges adjacent voxel faces into larger polygons by greedily expanding in each dimension, drastically reducing polygon counts for block-aligned geometry."
---

# Greedy Meshing

## Definition

Greedy Meshing is a mesh simplification technique for voxel-based geometry that combines adjacent voxel faces into larger rectangular polygons. Starting from an unvisited cell, it greedily expands in one direction as far as possible, then expands the resulting strip in a perpendicular direction, marking visited cells along the way. This produces complex interlocking patterns of rectangular blocks with far fewer polygons than naively meshing each voxel individually.

## Key Properties

- Reduces polygon count by orders of magnitude for block-aligned geometry
- Produces rectangular cuboids rather than individual voxel faces
- Works best on geometry with large flat regions
- Expansion order affects the resulting mesh topology
- Suitable for Minecraft-style voxel worlds
- Can be extended to arbitrary meshes via [[dual-marching-cuboids]]

## Related Concepts

- [[dual-marching-cuboids]] — extends greedy meshing with dual contouring for smooth surfaces
- [[marching-cubes]] — produces higher-quality surfaces but more polygons

## References

- Andy Geers' DualMarchingCuboids: https://github.com/andygeers/DualMarchingCuboids
