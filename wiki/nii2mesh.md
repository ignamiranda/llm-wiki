---
title: "nii2mesh"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [medical-imaging, mesh-generation, marching-cubes, nifti, mri, neuroimaging]
aliases: [nifti-to-mesh]
summary: "A minimal C tool that converts NIfTI 3D voxel images to triangulated meshes using Marching Cubes, supporting multiple output formats and mesh simplification."
---

# nii2mesh

## Definition

nii2mesh is a lightweight, pure-C command-line tool that converts NIfTI format 3D medical images (MRI, CT) into triangulated meshes using an enhanced Marching Cubes algorithm (Lewiner et al.). It supports pre-smoothing, iso-surface thresholding, connected-component filtering, bubble filling, mesh simplification via quadric error metrics, and post-smoothing via Laplacian smoothing with volume preservation.

## Key Properties

- Written in pure C (no C++ dependencies)
- Supports GIfTI, MZ3, OBJ, PLY, FreeSurfer, STL, VTK output formats
- Enhanced Marching Cubes (Lewiner) or classic (Bloys) implementation
- Mesh simplification via Fast Quadric Mesh Simplification
- Adaptive reduction using smaller triangles in high-curvature regions
- WebAssembly compilation for browser-based demos
- Used in neuroimaging toolchains (MRIcroGL, Surfice)

## Related Concepts

- [[marching-cubes]] — core algorithm for voxel-to-mesh conversion
- [[meshreconstruction]] — related C++ marching cubes library

## References

- Repository: https://github.com/neurolabusc/nii2mesh
- Live demo: https://github.com/rordenlab/nii2meshWeb
