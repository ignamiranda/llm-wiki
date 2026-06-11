---
title: "Dual Marching Cuboids — Greedy Dual Contouring for Depth Maps"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [marching-cubes, dual-contouring, greedy-meshing, mesh-generation, ios, swift]
summary: "A Swift implementation of the Dual Marching Cuboids algorithm combining greedy meshing with dual contouring for watertight 3D printable meshes from depth map data."
---

# Dual Marching Cuboids — Greedy Dual Contouring for Depth Maps

## Summary

Dual Marching Cuboids by Andy Geers is a Swift implementation of an algorithm that combines greedy meshing with dual contouring, producing watertight meshes with dramatically reduced polygon counts for depth-map-based 3D reconstruction.

## Content

The algorithm uses surface tracking to find seed cells, greedy merging of adjacent voxels into cuboids, and dual contouring to place one vertex per cuboid for triangulation. It handles the "single-sided" geometry characteristic of depth maps, produces watertight meshes for 3D printing, and achieves ~6x polygon reduction vs. Marching Cubes. Includes detailed documentation explaining the background of Marching Cubes, octrees, surface tracking, dual methods, and greedy meshing.

## Key Takeaways

- Novel combination of greedy meshing + dual contouring
- Watertight output suitable for 3D printing
- ~6x fewer polygons than standard Marching Cubes
- Detailed educational documentation
- Powers the Little Buildings iOS app
- 92 stars, MIT license

## Related

- [[dual-marching-cuboids]] — concept page
- [[greedy-meshing]] — foundational technique
- [[marching-cubes]] — comparison baseline
- [[andy-geers]] — creator

## Links

- Repository: https://github.com/andygeers/DualMarchingCuboids
