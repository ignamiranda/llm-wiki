---
title: "Tile Symmetry System (WFC)"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, wfc, tiles, symmetry]
summary: "A system classifying tiles by their symmetry type under the dihedral group D4, used to shorten adjacency enumeration in the simple tiled model."
---

# Tile Symmetry System (WFC)

## Definition / 定义

The tile symmetry system is a classification scheme used in WFC's simple tiled model where each tile is assigned a symmetry type based on its behavior under the dihedral group D4 (the symmetry group of a square — rotations and reflections). Tiles with the same symmetry type as their assigned letters have isomorphic D4 actions, allowing adjacency pairs to be enumerated only up to symmetry, dramatically shortening adjacency lists for tilesets with many symmetrical tiles.

## Key Properties / 关键特性

- Based on the dihedral group D4 (8 elements: 4 rotations × reflection)
- Tiles are assigned letters corresponding to their symmetry type
- Adjacency pairs are enumerated only up to symmetry equivalence
- Even tiles with non-symmetrical drawings can be treated as symmetrical by the system
- Particularly effective for tilesets with many symmetrical tiles (e.g., Summer tileset)

## Related Concepts / 相关概念

- [[simple-tiled-model]] — the model this system serves
- [[wave-function-collapse]] — the parent algorithm

## References / 参考资料

- Maxim Gumin, "WaveFunctionCollapse" — https://github.com/mxgmn/WaveFunctionCollapse
- Nick Nenov, visual guide to the tile symmetry system — https://www.dropbox.com/s/zeiat1w8zre9ro8/Knots%20breakdown.png?dl=0
