---
title: "Marching-Primitives — Shape Abstraction from SDF (CVPR 2023)"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [computer-vision, shape-abstraction, marching-cubes, sdf, cvpr, superquadrics]
summary: "A CVPR 2023 Highlight paper that extracts superquadric primitives from signed distance functions by marching through connected voxel regions."
---

# Marching-Primitives — Shape Abstraction from SDF (CVPR 2023)

## Summary

Marching-Primitives (CVPR 2023 Highlight) by Liu, Wu, Ruan & Chirikjian introduces a method for extracting superquadric geometric primitives directly from signed distance functions, enabling compact shape abstraction for physics simulation and robotic manipulation.

## Content

The algorithm iteratively grows superquadric primitives by analyzing voxel connectivity while marching through the SDF at different isovalues. For each connected volume of interest, it computes primitive parameters probabilistically to capture the local geometry. The MATLAB implementation (with planned Python version) demonstrates state-of-the-art accuracy on synthetic and real-world datasets.

## Key Takeaways

- Extracts superquadric primitives (not triangles) from SDF
- CVPR 2023 Highlight paper
- Applications in robotics, physics simulation, and shape analysis
- MATLAB implementation with SDF preprocessing script
- 147 stars, MIT license

## Related

- [[marching-cubes]] — inspiration for the marching-based approach
- [[weixiao-liu]] — lead author
- [[gregory-chirikjian]] — senior author

## Links

- Repository: https://github.com/ChirikjianLab/Marching-Primitives
- Paper: https://arxiv.org/abs/2303.13190
