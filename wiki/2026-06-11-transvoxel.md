---
title: "Transvoxel Algorithm — Reference Data Tables"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [marching-cubes, transvoxel, level-of-detail, voxel, cpp]
summary: "Eric Lengyel's official reference implementation of the Transvoxel Algorithm data tables in C++."
---

# Transvoxel Algorithm — Reference Data Tables

## Summary

Eric Lengyel's Transvoxel repository hosts the official C++ data tables for the Transvoxel Algorithm, which extends Marching Cubes with seamless LOD transitions between voxel blocks at different resolutions.

## Content

The repository contains a single C++ file (Transvoxel.cpp) with the complete set of lookup tables for the Transvoxel Algorithm. These tables handle the ~512 transition cell configurations needed to create watertight seams between high-resolution and low-resolution voxel regions. The algorithm is described in Lengyel's "Game Engine Gems" series and on transvoxel.org.

## Key Takeaways

- Official reference data tables (C++)
- Enables crack-free LOD transitions in voxel terrain
- 84 stars, MIT license

## Related

- [[transvoxel-algorithm]] — concept page
- [[marching-cubes]] — base algorithm
- [[eric-lengyel]] — creator

## Links

- Repository: https://github.com/EricLengyel/Transvoxel
- Website: https://transvoxel.org
