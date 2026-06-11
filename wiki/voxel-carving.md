---
title: "Voxel Carving"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [computer-vision, 3d-reconstruction, voxel, silhouette, shape-from-silhouette]
aliases: [visual-hull, shape-from-silhouette, space-carving]
summary: "A 3D reconstruction technique that carves away voxels inconsistent with 2D silhouette images from multiple viewpoints, recovering the visual hull of an object."
---

# Voxel Carving

## Definition

Voxel Carving (also called Shape from Silhouette or Visual Hull reconstruction) is a 3D reconstruction method that starts with a bounding volume of voxels and iteratively removes (carves away) voxels that project outside the silhouette of the object in any input image. Advanced variants use Truncated Signed Distance Function (TSDF) fusion to combine depth information from multiple views, producing smooth surfaces that can be extracted via Marching Cubes.

## Key Properties

- Input: 2D silhouettes/binary masks and camera parameters
- Output: 3D voxel model or triangle mesh
- TSDF fusion variant produces smooth, watertight surfaces
- Computationally efficient for GPU implementation
- Cannot reconstruct concavities not visible in silhouettes

## Related Concepts

- [[kinect-fusion]] — real-time TSDF fusion approach
- [[marching-cubes]] — used for mesh extraction from voxel/TSDF representation

## References

- Vacancy library: https://github.com/unclearness/vacancy
