---
title: "Differentiable Marching Cubes"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [marching-cubes, differentiable-rendering, gradient-based-optimization, 3d-reconstruction, deep-learning]
aliases: [diffmc, differentiable-isosurface]
summary: "A GPU-accelerated, differentiable implementation of Marching Cubes and Dual Marching Cubes that enables gradient backpropagation through the mesh extraction step for deep learning pipelines."
---

# Differentiable Marching Cubes

## Definition

Differentiable Marching Cubes (DiffMC) and Differentiable Dual Marching Cubes (DiffDMC) are CUDA-accelerated implementations of isosurface extraction that support automatic gradient backpropagation. Unlike standard marching cubes (which is a discrete, non-differentiable operation), these implementations allow gradients to flow from mesh vertices back to the SDF values, enabling end-to-end deep learning for shape reconstruction, texture optimization, and material estimation from images.

## Key Properties

- Implemented in CUDA with PyTorch integration
- Supports both standard Marching Cubes and Dual Marching Cubes
- Optional learnable grid deformation
- Produces watertight manifold meshes
- Significantly faster than DMTet and FlexiCubes (2-6x speedup)
- Lower VRAM consumption than competing methods
- Supports batch training and checkpointing

## Related Concepts

- [[marching-cubes]] — base algorithm made differentiable
- [[dual-marching-cubes]] — dual variant also supported

## References

- DISO library: https://github.com/SarahWeiii/diso
- Paper: Wei et al., "Neumanifold" (WACV 2025)
