---
title: "DeBroglie"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [wfc, wave-function-collapse, csharp, unity, procedural-generation, backtracking]
aliases: []
summary: "A C# library implementing the Wave Function Collapse algorithm with backtracking support, non-local constraints, and 2D/3D/hex grid support."
source_url: "https://github.com/BorisTheBrave/DeBroglie"
source_hash: "89411389E256BFE9934D184C24D17642D32349D1F7C473BA5F387D5019AEF8BC"
---

# DeBroglie

## Definition / 定义

DeBroglie is a C# library implementing the Wave Function Collapse algorithm, created by BorisTheBrave. Unlike the original WFC implementation, DeBroglie has full backtracking support, allowing it to solve arbitrarily complicated constraint sets. It supports overlapping and tiled models, non-local constraints, 2D tiles, hex grids, and 3D voxels.

## Key Properties / 关键特性

- Full backtracking support — does not immediately give up on contradiction
- Non-local constraints — specify properties beyond local adjacency
- Overlapping and Simple Tiled model implementations
- 2D tiles, hex grids, and 3D voxels
- Tiled editor integration via DeBroglie.Tiled
- Extensive documentation and articles at boristhebrave.github.io/DeBroglie/
- 515 GitHub stars, MIT licensed

## Examples / 示例

Used for generating tilemaps, textures, and 3D voxel structures in C#/.NET projects. The backtracking makes it suitable for puzzles and constrained generation where the original WFC would fail.

## Related Concepts / 相关概念

- [[fast-wfc]] — performance-focused WFC in C++
- [[ghx-proc-gen]] — Rust WFC for Bevy engine
- [[graph-wave-function-collapse]] — WFC on arbitrary graphs
- [[2026-06-11-wfc-implementations-survey]] — surveyed in the WFC survey article

## References / 参考资料

- https://github.com/BorisTheBrave/DeBroglie
- https://boristhebrave.github.io/DeBroglie/