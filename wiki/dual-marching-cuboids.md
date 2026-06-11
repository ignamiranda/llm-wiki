---
title: "Dual Marching Cuboids"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [marching-cubes, dual-contouring, greedy-meshing, mesh-generation, algorithm]
aliases: []
summary: "A hybrid meshing algorithm combining greedy meshing with dual contouring, producing watertight meshes with adaptive polygon density using one vertex per merged cuboid."
---

# Dual Marching Cuboids

## Definition

Dual Marching Cuboids is a meshing algorithm by Andy Geers that combines greedy meshing with dual contouring principles. It merges adjacent voxels into rectangular cuboids (greedy meshing), then places one vertex per cuboid (dual approach) to construct a surface mesh. This produces significantly fewer polygons than standard Marching Cubes while maintaining watertightness, making it suitable for 3D printing from depth-map data.

## Key Properties

- Combines greedy meshing with dual contouring
- Single vertex per cuboid (not per voxel)
- Produces watertight meshes suitable for 3D printing
- Surface tracking avoids visiting empty voxels
- ~6x polygon reduction vs. Marching Cubes on typical depth-map geometry
- Axis information from depth maps guides the greedy expansion order

## Related Concepts

- [[greedy-meshing]] — base approach for merging voxels into cuboids
- [[marching-cubes]] — produces more polygons but higher quality

## References

- Repository: https://github.com/andygeers/DualMarchingCuboids
