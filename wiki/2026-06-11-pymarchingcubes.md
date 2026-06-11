---
title: "PyMarchingCubes — Python Marching Cubes with Color Interpolation"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [marching-cubes, python, color-interpolation, tsdf, binary-smoothing]
summary: "A Python/C++ library for marching cubes with color interpolation, TSDF edge subsampling, and binary array smoothing, forked from PyMCubes."
---

# PyMarchingCubes — Python Marching Cubes with Color Interpolation

## Summary

PyMarchingCubes (by Justus Thies) is a fork of PyMCubes with an improved marching cubes implementation that fixes triangulation errors, adds color interpolation, and introduces edge subsampling for TSDF volumes.

## Content

The library extends PyMCubes with: (1) a corrected marching cubes implementation fixing oversized triangles, (2) `marching_cubes_color` for vertex color interpolation from RGB volumes, (3) `marching_cubes_super_sampling` for edge subsampling in truncated SDFs, and (4) `mcubes.smooth` for smoothing binary arrays before extraction. Supports OBJ, OFF, and Collada DAE export with vertex colors.

## Key Takeaways

- Improved triangulation over original PyMCubes
- Color interpolation from RGB volumes
- Edge subsampling for TSDF zero-crossing accuracy
- Binary array smoothing for segmentation masks
- 190 stars, BSD-3-Clause

## Related

- [[marching-cubes]] — core algorithm
- [[justus-thies]] — creator

## Links

- Repository: https://github.com/JustusThies/PyMarchingCubes
