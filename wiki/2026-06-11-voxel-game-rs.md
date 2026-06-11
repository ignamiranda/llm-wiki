---
title: "voxel-game-rs — Bevy Voxel Game with WGSL Compute Shaders"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [marching-cubes, rust, bevy, wgsl, compute-shader, voxel, game-development]
summary: "A voxel game demo in Rust using Bevy ECS with Marching Cubes implemented as a WGSL compute shader for ~1ms chunk generation."
---

# voxel-game-rs — Bevy Voxel Game with WGSL Compute Shaders

## Summary

voxel-game-rs by qhdwight is a Rust/Bevy voxel game demo implementing Marching Cubes entirely in GPU compute shaders (WGSL), achieving ~1ms generation for 32x32x32 chunks on i9 + 1080 Ti hardware.

## Content

Uses the Bevy game engine with ECS architecture and the Rapier physics plugin. The Marching Cubes compute shader polygonizes a scalar field entirely on the GPU. Features Source engine-inspired movement (air strafing, bunny hopping).

## Key Takeaways

- Full compute shader Marching Cubes in WGSL
- Bevy ECS + Rapier physics integration
- ~1ms per 32x32x32 chunk
- 111 stars, GPL-3.0

## Related

- [[marching-cubes]] — core algorithm
- [[2026-06-11-scrawk-marching-cubes-gpu]] — related Unity GPU implementation
- [[isosurface]] — related Rust library

## Links

- Repository: https://github.com/qhdwight/voxel-game-rs
