---
title: "MoravaEngine — Multi-API 2D/3D Graphics Engine"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [graphics-engine, opengl, vulkan, directx, marching-cubes, cpp, voxel, procedural-generation]
summary: "A C++ 2D/3D graphics engine supporting OpenGL 4.5+, Vulkan 1.2, and DirectX 11, with marching cubes as one of many implemented CG techniques."
---

# MoravaEngine — Multi-API 2D/3D Graphics Engine

## Summary

MoravaEngine by Dusan Trajko is a multi-API C++ graphics engine supporting OpenGL 4.5+, Vulkan 1.2, and DirectX 11. It serves as a sandbox for experimenting with CG techniques including Marching Cubes, PBR, IBL, SSAO, physics, and procedural generation.

## Content

The engine includes a comprehensive set of rendering techniques: Phong lighting, PBR, IBL, shadow mapping, SSAO, particle systems, instanced rendering, post-processing, and skeletal animation. Marching Cubes is implemented as one technique for voxel-based volume rendering. Built with a Hazel-like architecture, CMake build system, and imgui-based editor.

## Key Takeaways

- Supports 3 graphics APIs: OpenGL 4.5+, Vulkan 1.2, DirectX 11
- Experimentation sandbox with 20+ CG techniques
- 309 stars, Apache-2.0 license
- 1,959 commits, actively developed

## Related

- [[marching-cubes]] — one of the implemented techniques
- [[procedural-quest-generation]] — related procedural generation focus

## Links

- Repository: https://github.com/dtrajko/MoravaEngine
