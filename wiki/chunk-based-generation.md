---
title: "Chunk-Based Generation"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, chunks, world-generation]
aliases: [chunk-based world generation]
summary: "A world generation approach where the world is divided into rectangular tiles (chunks) that are generated independently on the fly."
---

# Chunk-Based Generation

## Definition

Chunk-based generation divides an infinite (or large) world into rectangular tiles called chunks. Chunks are generated on the fly as needed (typically as the player moves) and destroyed/recycled when no longer needed. Popularized by Minecraft, this approach is the foundation of most infinite world generation systems. [[layerprocgen]] extends this concept by allowing different layers to have chunks of different sizes, and by enabling chunks to request data from other layers with padding.

## Key Properties

- All chunks in a given layer have the same size (width and height)
- Chunks are rectangular, minimum size is 1x1
- Generated on demand when depended on, destroyed when no longer depended on
- Stored in a [[rolling-grid]] data structure
- Layer-specific chunk sizes enable multi-scale generation

## Examples

- A TerrainLayer with 256x256 chunks for renderable terrain
- A RegionLayer with chunks covering 50+ areas each for top-down planning
- A LocationLayer with three internal levels for point generation and relaxation

## Related Concepts

- [[layer-based-procedural-generation]] — chunks are the unit within layers
- [[rolling-grid]] — data structure for chunk storage
- [[owned-within-bounds]] — pattern for chunk ownership of cross-boundary data
- [[effect-distance-and-padding]] — how chunks get context beyond their own bounds
- [[noise-based-terrain-generation]] — noise-based terrain can feed chunk-based generation systems
- [[infinite-terrain]] — locally-computed infinite terrain is chunk-compatible
- [[modifying-in-blocks]] — WFC-based lazy generation of unbounded tile configurations
- [[terrain-lod-stitching]] — terrain tiles with LOD use chunk-based generation as foundation
- [[2026-06-11-terrain3d]] — a Godot 3.5 implementation using terrain tiles as chunks with dynamic LOD

## References

- LayerProcGen documentation: Layers and Chunks
