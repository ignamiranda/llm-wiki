---
title: "Marching Cubes Terrain (Eldemarkki) — Unity Job System Implementation"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [marching-cubes, unity, terrain-generation, job-system, burst-compiler, voxel]
summary: "A Unity Marching Cubes terrain implementation using the Job System and Burst Compiler for performance, featuring procedural infinite worlds and heightmap import."
---

# Marching Cubes Terrain (Eldemarkki) — Unity Job System Implementation

## Summary

Eldemarkki's Marching-Cubes-Terrain is a Unity implementation using the Job System and Burst Compiler for multithreaded terrain generation. It supports real-time terrain editing, procedural infinite worlds, and heightmap-based terrain import.

## Content

The project implements Marching Cubes with Unity's C# Job System for parallel chunk generation, achieving significant performance gains over naive CPU approaches. Features include real-time sculpting (add/remove terrain with smoothing via Ctrl+click), procedural infinite world generation with noise-based density, and black-and-white heightmap import for creating custom terrain shapes.

## Key Takeaways

- Uses Unity Job System + Burst Compiler for parallel chunk generation
- Supports procedural infinite worlds or heightmap-based terrain
- Real-time terrain editing with additive/subtractive sculpting
- Archived by owner (Feb 2026, read-only)
- Based on Paul Bourke's Marching Cubes reference implementation

## Related

- [[marching-cubes]] — core algorithm
- [[2026-06-11-scrawk-marching-cubes]] — another Unity marching cubes implementation
- [[2026-06-11-javier-garzo-marching-cubes]] — related Unity voxel engine

## Links

- Repository: https://github.com/Eldemarkki/Marching-Cubes-Terrain
