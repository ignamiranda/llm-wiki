---
title: "WFC Implementations Survey / WFC 实现概览"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [wfc, wave-function-collapse, procedural-generation, survey, implementations]
summary: "A survey of 12 open-source Wave Function Collapse implementations spanning C#, C++, Rust, Python, Go, GDScript, and TypeScript, across Unity, Godot, and Bevy engines."
source_url: ""
source_hash: "89411389,CB9E6EB8,A4BBE0A7,BB1D49C3,EDA076B4,9DF7F1E7,8D4E29C3,103AE5ED,8509C4C5,F1D5AE97,D0E84825,68F7911D"
---

# WFC Implementations Survey / WFC 实现概览

## Summary / 摘要

This article surveys 12 open-source implementations of the Wave Function Collapse (WFC) algorithm, originally created by Maxim Gumin (mxgmn). These implementations span 7 programming languages, 3 game engines, and extend WFC to arbitrary graphs, 3D voxels, hex grids, and general constraint satisfaction.

## Content / 内容

### DeBroglie (C#) — 515★

**Author:** BorisTheBrave  
**URL:** https://github.com/BorisTheBrave/DeBroglie  
**License:** MIT

DeBroglie is the most feature-complete WFC library in C#. Unlike the original implementation, it has full backtracking support, enabling it to solve arbitrarily complicated constraint sets. It supports non-local constraints (specifying properties beyond local adjacency), overlapping and tiled models, 2D tiles, hex grids, and 3D voxels. Extensive documentation at boristhebrave.github.io/DeBroglie/.

### godot-constraint-solving (GDScript) — 450★

**Author:** AlexeyBond  
**URL:** https://github.com/AlexeyBond/godot-constraint-solving  
**License:** MIT

A Godot 4 addon implementing WFC and a generic constraint satisfaction problem (CSP) solver. Features backtracking, multithreaded generation, and learning from example (inferring rules from a sample map). Supports TileMapLayer, TileMap (including hex), and GridMap. Includes a precondition API for combining WFC with other procgen algorithms (e.g., dungeon generation). Available in the Godot Asset Library.

### fast-wfc (C++) — 435★

**Authors:** Mathieu Fehr, Nathanaëlle Courant  
**URL:** https://github.com/math-fehr/fast-wfc  
**License:** MIT

A performance-focused C++17 WFC implementation that achieved ~10x speedup over the original at the time of release. Uses CMake build system. Includes Rust bindings (fastwfc-rs). Optimizations include efficient pattern storage and propagation.

### wfc (C) — 367★

**Author:** Krystian (krychu)  
**URL:** https://github.com/krychu/wfc  
**License:** MIT

Single-file C library implementing the overlapping WFC method with extensive optimizations. Generates a 128×128 image from 308 unique tiles in 371ms. Includes a command-line tool and Rust bindings (wfc-rs). Uses stb_image.h for file I/O. Pure C with no dependencies beyond stb.

### WfcMaze (C#) — 342★

**Author:** keijiro  
**URL:** https://github.com/keijiro/WfcMaze  
**License:** MIT

A Unity implementation of WFC focused on maze/procedural model generation. By keijiro, known for many Unity demos and experiments.

### MarkovJuniorWeb (TypeScript) — 199★

**Author:** Yuu6883  
**URL:** https://github.com/Yuu6883/MarkovJuniorWeb  
**License:** MIT

A browser-based TypeScript port of MarkovJunior (mxgmn's probabilistic programming language). Supports isometric rendering, .vox export, and node tree visualization. Includes an experimental MarkovJunior → AssemblyScript → WebAssembly JIT compiler. All models from the original repo are loadable.

### ghx_proc_gen (Rust) — 154★

**Author:** Gilles Henaux  
**URL:** https://github.com/Henauxg/ghx_proc_gen  
**License:** MIT/Apache-2.0

A Rust library for 2D & 3D procedural generation using Model Synthesis/WFC with AC-4 constraint propagation. Targets the Bevy engine via bevy_ghx_proc_gen. Features: socket-based adjacency, automatic model rotation variations, grid looping, observer pattern for incremental generation, and interactive generation (set_and_propagate). Well-documented with multiple examples (chessboard, pillars, canyon, tile-layers).

### AutoLevel (C#) — 148★

**Author:** Al-Asl  
**URL:** https://github.com/Al-Asl/AutoLevel  
**License:** MIT

A Unity WFC-based procedural level generator with editor tools. Features: weight, volume, and boundary constraints; block/big-block system; FBX export; multithreaded solver; layer support. Designed to be controllable and easy to use via Unity editor UI components (Level Builder, Block Repo, Block Asset).

### wfc_python (Python) — 141★

**Author:** Isaac Karth  
**URL:** https://github.com/ikarth/wfc_python  
**License:** MIT

A direct Python translation of mxgmn's original C# WFC implementation. Minimal optimization, intended as a reference/educational port. A newer re-implemented version exists at ikarth/wfc_2019f.

### wfc (Go) — 79★

**Author:** Shawn Ridgeway  
**URL:** https://github.com/shawnridgeway/wfc  
**License:** MIT

A Go port of WFC supporting both Overlapping Model (bitmap texture synthesis) and Simple Tiled Model (tile adjacency constraints). API includes Generate, Iterate, Render, Clear, and SetSeed. Based on kchapelier's JavaScript version.

### GraphWaveFunctionCollapse (Python) — 64★

**Author:** lamelizard  
**URL:** https://github.com/lamelizard/GraphWaveFunctionCollapse  
**License:** MIT

Extends WFC from grids to arbitrary graphs. Patterns are defined via a "local similarity graph" (GL) and extracted from a colored example graph (GI) using VF2 subgraph isomorphism. Output graph (GO) is colored using extracted patterns with constraint propagation. Includes a thesis (German) on the algorithm. Uses networkx and GraphML.

### wave-function-collapse (Python) — 62★

**Author:** Coac  
**URL:** https://github.com/Coac/wave-function-collapse  
**License:** MIT

A Python WFC implementation supporting 1D, 2D, and 3D samples. Supports Magica Voxel (.vox) files via py-vox-io and MIDI file generation. Clean modular architecture (cell, grid, pattern, propagator, wfc modules).

## Key Takeaways / 关键收获

- C# dominates WFC implementation ecosystem (DeBroglie, WfcMaze, AutoLevel) with Unity integration
- Rust is emerging as a new target (ghx_proc_gen for Bevy)
- The algorithm has been extended beyond grids to arbitrary graphs (GWFC)
- Backtracking is a key differentiator — most implementations give up on contradiction, DeBroglie and godot-constraint-solving retry
- Performance varies by 10x+ between implementations; fast-wfc and krychu/wfc lead on speed

## Related / 关联

- [[debroglie]] — C# WFC library with backtracking
- [[fast-wfc]] — Performance-optimized C++ WFC
- [[ghx-proc-gen]] — Rust WFC for Bevy
- [[graph-wave-function-collapse]] — WFC on arbitrary graphs
- [[autolevel]] — Unity WFC level generator
- [[markov-junior-web]] — Browser-based MarkovJunior
- [[noise-based-terrain-generation]] — related procgen technique
- [[layer-based-procedural-generation]] — related architecture technique