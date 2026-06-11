---
title: "MarkovJuniorWeb"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [wfc, markov-junior, typescript, webassembly, procedural-generation, probabilistic-programming]
aliases: []
summary: "A browser-based TypeScript port of MarkovJunior with isometric rendering, .vox export, and experimental WebAssembly JIT compilation."
source_url: "https://github.com/Yuu6883/MarkovJuniorWeb"
source_hash: "9DF7F1E79608DD8F6BB3D9871B26A356F2DC95F3A2A062010E6CC2BD79ADA73D"
---

# MarkovJuniorWeb

## Definition

MarkovJuniorWeb is a browser-based TypeScript port of MarkovJunior, a probabilistic programming language created by Maxim Gumin (mxgmn) for procedural generation. It implements all features of the original including isometric rendering, .vox file export, and node tree visualization.

## Key Properties

- Full TypeScript port of MarkovJunior (C# original)
- Runs in browser and Node.js
- Isometric rendering
- .vox (Magica Voxel) export
- Node tree visualization
- Experimental AssemblyScript → WebAssembly JIT compiler for performance
- ~2x slower than original C# in JS; WASM version narrows the gap
- 199 GitHub stars

## Examples

All models from the original MarkovJunior repo are loadable. Includes SokobanLevel1, various dungeon, maze, and texture generation models.

## Related Concepts

- [[2026-06-11-wfc-implementations-survey]] — surveyed in the WFC survey article
- [[debroglie]] — another WFC implementation

## References

- https://github.com/Yuu6883/MarkovJuniorWeb
- https://yuu6883.github.io/MarkovJuniorWeb/