---
title: "Model Synthesis"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, constraint-satisfaction, algorithm]
summary: "Paul Merrell's 2009 algorithm for generating larger models from examples by deriving adjacency constraints between tiles and using AC-3 constraint propagation."
---

# Model Synthesis

## Definition

Model Synthesis is Paul Merrell's 2009 algorithm that generates larger models from example models by deriving adjacency constraints between tiles and synthesizing new configurations using the AC-3 constraint propagation algorithm. Wave Function Collapse generalizes Merrell's approach by working with NxN overlapping patterns of tiles rather than individual tiles, introducing the lowest entropy heuristic to remove directional bias, and implementing a tile symmetry system.

## Key Properties

- Derives adjacency constraints between tiles from example models
- Uses AC-3 (rather than WFC's AC-4) for constraint propagation
- Introduced the method of incrementally modifying the model in parts to reduce failure rate
- WFC generalizes this approach to work with NxN overlapping patterns instead of individual tiles
- Merrell's method has a directional bias that WFC's entropy heuristic removes

## Related Concepts

- [[wave-function-collapse]] — WFC generalizes Model Synthesis
- [[constraint-propagation-ac4]] — WFC uses AC-4 instead of AC-3
- [[entropy-heuristic-wfc]] — removes the directional bias in Merrell's approach
- [[tile-symmetry-system-wfc]] — reduces input sizes for adjacency data
- [[modifying-in-blocks]] — Merrell's technique for incremental modification

## References

- Paul C. Merrell, "Model Synthesis" (2009) — http://graphics.stanford.edu/~pmerrell/thesis.pdf
- Paul Merrell, Model Synthesis page — https://paulmerrell.org/model-synthesis/
