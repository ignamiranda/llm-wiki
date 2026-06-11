---
title: "Wave Function Collapse (WFC)"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, constraint-satisfaction, texture-synthesis, algorithm]
source_hash: "f3136128c2e9c51b7e695f8991730c2bde81f30f31bdf5d8fff36bd3fa7f5d3b"
summary: "A constraint-based texture synthesis algorithm that generates outputs locally similar to an input bitmap by iteratively collapsing superposition states and propagating adjacency constraints."
---

# Wave Function Collapse (WFC)

## Definition / 定义

Wave Function Collapse (WFC) is an algorithm for procedural generation that synthesizes images or tilemaps that are locally similar to a given input example. It frames generation as a constraint satisfaction problem: the output must contain only NxN patterns present in the input (condition C1), with a distribution approximating the input's distribution (weak condition C2). The algorithm borrows terminology from quantum mechanics — the output starts in a superposition of all possible states and iteratively "collapses" regions to definite states.

## Key Properties / 关键特性

- **Constraint-based**: Unlike noise or function-based generators, WFC works by enforcing local pattern constraints derived from an example
- **NP-hard**: Determining whether a bitmap admits nontrivial satisfying bitmaps is NP-hard, so the algorithm can fail with contradictions
- **Two modes**: The overlapping model (pixel pattern matching) and the simple tiled model (tile adjacency constraints)
- **Observation-propagation cycle**: Alternates between collapsing uncertain regions and propagating constraints
- **Entropy heuristic**: Selects the region with lowest Shannon entropy for collapse, which produces organic-looking results
- **Constraint support**: Can incorporate user-specified constraints, enabling mixed-initiative design

## Examples / 示例

- Generating brick wall textures that retain correct brick alignment (where simpler texture synthesis fails)
- Procedural level generation in Bad North, Caves of Qud, and Townscaper
- Autocompleting a partially constructed level from a human designer's starting layout
- 3D voxel structure generation using 5x5x5 blocks
- Encoding QR-code-like information inside WFC tilings (Lefebvre et al.)

## Related Concepts / 相关概念

- [[2026-06-11-wave-function-collapse]] — overview article on the algorithm
- [[overlapping-model-wfc]] — pixel-pattern-based mode
- [[simple-tiled-model]] — tile-adjacency-based mode
- [[entropy-heuristic-wfc]] — the observation selection strategy
- [[observation-propagation-cycle]] — the core algorithm loop
- [[constraint-propagation-ac4]] — the AC-4 algorithm used for constraint propagation
- [[model-synthesis]] — Paul Merrell's prior work WFC generalizes
- [[convchain]] — complementary algorithm (satisfies C2 but not C1)
- [[markovjunior]] — extends WFC to 3D with extensive tilesets
- [[maxim-gumin]] — creator of the reference implementation

## References / 参考资料

- Maxim Gumin, "WaveFunctionCollapse" — https://github.com/mxgmn/WaveFunctionCollapse
- Paul C. Merrell, "Model Synthesis" (2009) — http://graphics.stanford.edu/~pmerrell/thesis.pdf
- Alan K. Mackworth, "Consistency in Networks of Relations" (1977)
- Roger Mohr & Thomas C. Henderson, "AC-4" (1986)
