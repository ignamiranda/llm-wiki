---
title: "Simple Tiled Model (WFC)"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, tiles, constraint-satisfaction, wfc]
summary: "A WFC mode where tile adjacency constraints replace pixel pattern matching, enabling tile-based level generation with explicitly defined tile sets and symmetry classifications."
---

# Simple Tiled Model (WFC)

## Definition

The simple tiled model is the second primary mode of the Wave Function Collapse algorithm, where generation is driven by pre-defined tiles and their adjacency constraints rather than extracted pixel patterns. It is the simplest nontrivial case of WFC, corresponding to NxN=1x2, where propagation reduces to adjacency constraint propagation. The model is initialized with a list of tiles and their adjacency data rather than a sample bitmap.

## Key Properties

- Uses explicitly defined tilesets instead of pixel pattern extraction
- Propagation is adjacency constraint propagation (simpler than the overlapping model)
- Supports a tile symmetry system based on the dihedral group D4 to shorten adjacency enumeration
- Tilesets can be Wang (edge-labeled) or non-Wang (adjacency cannot be induced from edge labels)
- "Easy" tilesets never produce contradictions but also lack interesting global structure
- Can be extended to 3D with additional heuristic functions

## Examples

- Knot tileset (5 tiles, not easy — produces complex patterns)
- Circuit tileset (non-Wang — corners cannot be adjacent but can connect via Connection tiles)
- Townscaper's irregular grid tileset (Oskar Stålberg)
- 3D castle generation with voxel tilesets

## Related Concepts

- [[wave-function-collapse]] — the parent algorithm
- [[overlapping-model-wfc]] — the alternative WFC mode
- [[tile-symmetry-system-wfc]] — D4 symmetry classification
- [[markovjunior]] — 3D simple tiled model implementation
- [[entropy-heuristic-wfc]] — observation selection

## References

- Maxim Gumin, "WaveFunctionCollapse" — https://github.com/mxgmn/WaveFunctionCollapse
