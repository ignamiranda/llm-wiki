---
title: "Rolling Grid"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, data-structure, chunks, layerprocgen]
aliases: []
summary: "A moving-grid data structure used by LayerProcGen layers to store and manage chunks as the generation focus moves through the world."
---

# Rolling Grid

## Definition

A RollingGrid is the data structure each layer in [[layerprocgen]] uses to store its chunks. It maintains a grid of chunks that moves (rolls) as the generation focus shifts — when the player moves and new chunks are needed, old chunks are recycled. The grid size can be optionally configured in the layer base class constructor. The rolling grid is automatically managed by the `ChunkBasedDataLayer` base class.

## Key Properties

- Automatically handled by the layer base class
- Grid can be optionally sized in the layer constructor
- Chunks are created and destroyed as dependencies change
- Efficiently handles the moving window of active chunks around the player

## Examples

- Each layer in LayerProcGen has its own RollingGrid instance
- ExampleLayer with no custom grid size uses the default rolling grid
- A layer handling very large-scale planning might use a smaller grid with larger chunks

## Related Concepts

- [[chunk-based-generation]] — chunks are what the rolling grid stores
- [[layer-based-procedural-generation]] — rolling grid is a core implementation detail

## References

- LayerProcGen documentation: Layers and Chunks
