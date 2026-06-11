---
title: "Unity Procedural Mesh and Texture Resources"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, unity, procedural-modeling, game-assets]
aliases: [voxelboy-resources, procedural-mesh-unity]
summary: "A curated list of tutorials and open-source repositories for procedural mesh and texture generation in Unity, compiled by VoxelBoy for the Dublin Unity User Group."
---

# Unity Procedural Mesh and Texture Resources

## Definition

A curated GitHub repository by VoxelBoy compiling tutorials, libraries, and tools for generating procedural meshes and textures within the Unity game engine. Originally prepared for a Dublin Unity User Group (DUUG) talk titled "Procedural meshes and textures in Unity."

## Key Resources

### Tutorials

- **Catlike Coding** — comprehensive tutorial series covering procedural grids, noise, and mesh generation
- **Jayelinda's "Modelling by Numbers"** — multi-part guide to procedural mesh construction
- **ScrawkBlog** — tutorials on procedural mesh generation and noise
- **Nick Jensen** — procedural curved mesh generation in Unity
- **Unity Documentation** — official guide to generating mesh geometry procedurally

### Open-Source Repositories

- **ProceduralToolkit** (Syomus) — comprehensive C# toolkit for procedural generation
- **LibNoise for Unity** (ricardojmendez) — port of the LibNoise library for coherent noise generation
- **Unity Accidental Noise** (miketucker) — noise generation library for Unity
- **Noise Shaders** (keijiro) — GPU-based noise generation via shaders

## Key Properties

- **Code-driven** — unlike node-based systems (Blender Geometry Nodes, Houdini), Unity procedural generation is primarily done through C# scripting
- **Mesh API** — Unity's `Mesh` class allows direct vertex/triangle/index buffer construction at runtime
- **Community-driven** — the listed resources represent the broader Unity procedural generation ecosystem, including [[autolevel]] (WFC), [[layerprocgen]] (infinite world generation), and [[debroglie]] (WFC)

## Related Concepts

- [[blender-geometry-nodes]] — node-based alternative to code-driven procedural meshes
- [[houdini-procedural-asset-pipeline]] — Houdini PDG pipeline for game assets (complementary DCC-driven approach)
- [[autolevel]] — Unity editor-integrated WFC level generator
- [[debroglie]] — C# WFC library usable in Unity
- [[layerprocgen]] — Unity C# framework for layer-based procedural generation

## References

- [Resources-for-Procedural-Mesh-and-Texture-Generation](https://github.com/VoxelBoy/Resources-for-Procedural-Mesh-and-Texture-Generation) — GitHub repository
