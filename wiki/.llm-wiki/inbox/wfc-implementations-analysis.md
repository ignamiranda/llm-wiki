# Ingest Analysis — WFC Implementations Survey (12 GitHub Repos)
**Source hashes:** `89411389E256BFE9934D184C24D17642D32349D1F7C473BA5F387D5019AEF8BC`, `CB9E6EB83E524FCEAC4B0E2FC82DBDA18A8C583A6CA623061123F8F5B0E9E903`, `A4BBE0A73026A8F1384D2A16276AE1F613A4BDB8661659A314C76A090F636C38`, `BB1D49C39FA120CAA3FFBAF947A3B962E10927CE21018374FE06452EE95AE252`, `EDA076B49DF261CCA0FC7377ADD7430B1AE0D525D6B578FCF19DFBE0261E81A2`, `9DF7F1E79608DD8F6BB3D9871B26A356F2DC95F3A2A062010E6CC2BD79ADA73D`, `8D4E29C3DDAE0A3A8C4E7B076E321CB85695BE092CE4F451261F78F78906CF22`, `103AE5ED509E03036F6DA2D52FDAE501153EE55716633D3AC49D1A12E722182F`, `8509C4C5645ACA60A9DDFA23FF010B991C98127B4CC782970D91E69B9E10A73A`, `F1D5AE9771439782900028A364E3FDAB25624FE0A42DF483260B771519EA7BA1`, `D0E84825CDD9E71BE132985B5D98579A7403E59B7B41D4A5D8D2FB91BD798203`, `68F7911DF763B724BCCDA20398747FF4F72FE3BCFBEAB8E84B1E2FDCC26AC5CC`
**Language detected:** en
**Analyzed:** 2026-06-11T10:00:00Z

## Source Summary

12 open-source GitHub repositories implementing or extending the Wave Function Collapse (WFC) algorithm. They span languages (C#, C++, Rust, Python, Go, GDScript, TypeScript), engines (Unity, Godot, Bevy), and extend WFC to arbitrary graphs, 3D voxels, hex grids, and constraint satisfaction. Star range: 62–515. Most are MIT-licensed.

## Concepts to Extract

| Concept | Action | Reason |
|---------|--------|--------|
| debroglie | create | Feature-rich C# WFC with backtracking, non-local constraints |
| fast-wfc | create | Performance-optimized C++17 WFC (10x speedup) |
| ghx-proc-gen | create | Rust WFC/Model Synthesis for Bevy with AC-4 solver |
| graph-wave-function-collapse | create | WFC on arbitrary graphs (not grids) |
| autolevel | create | Unity WFC level generator with editor tools |
| markov-junior-web | create | Browser-based MarkovJunior port |
| wfc-implementations-survey | create | Survey article covering all 12 repos |

## Persons to Create/Update

| Person | Action | Details |
|--------|--------|---------|
| boris-the-brave | create | Author of DeBroglie C# WFC library, writer of WFC/Model Synthesis articles |

## Pages to Create

| Filename | Type | Title | Key Content |
|----------|------|-------|-------------|
| 2026-06-11-wfc-implementations-survey | article | WFC Implementations Survey / WFC 实现概览 | Survey of 12 open-source WFC repos across languages and engines |
| debroglie | concept | DeBroglie | C# WFC library with backtracking, non-local constraints, 2D/3D/hex support |
| fast-wfc | concept | fast-wfc | C++17 performance-optimized WFC, 10x speedup over original |
| ghx-proc-gen | concept | ghx_proc_gen | Rust WFC/Model Synthesis library for Bevy engine, AC-4 solver |
| graph-wave-function-collapse | concept | Graph Wave Function Collapse (GWFC) | WFC extended to arbitrary graphs via subgraph isomorphism (VF2) |
| autolevel | concept | AutoLevel | Unity WFC-based procedural level generator with editor tools |
| markov-junior-web | concept | MarkovJuniorWeb | Browser-based TypeScript port of MarkovJunior with WebAssembly JIT |

## Contradictions Detected

None. The existing wiki covers noise-based terrain and LayerProcGen — unrelated to specific WFC implementations. No factual overlap to contradict.

## Proposed Cross-Links

- [[debroglie]] ↔ [[2026-06-11-wfc-implementations-survey]] — featured implementation
- [[fast-wfc]] ↔ [[2026-06-11-wfc-implementations-survey]] — featured implementation
- [[ghx-proc-gen]] ↔ [[2026-06-11-wfc-implementations-survey]] — featured implementation
- [[graph-wave-function-collapse]] ↔ [[2026-06-11-wfc-implementations-survey]] — featured implementation
- [[autolevel]] ↔ [[2026-06-11-wfc-implementations-survey]] — featured implementation
- [[debroglie]] ↔ [[boris-the-brave]] — created by
- [[markov-junior-web]] ↔ [[2026-06-11-wfc-implementations-survey]] — related implementation
- [[noise-based-terrain-generation]] ↔ [[2026-06-11-wfc-implementations-survey]] — related procgen technique

## Items for User Review

None — all sources are well-known open-source WFC implementations with clear README documentation.
