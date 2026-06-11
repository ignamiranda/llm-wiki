---
title: "Observation-Propagation Cycle (WFC)"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, wfc, algorithm]
summary: "The core loop of the Wave Function Collapse algorithm that alternates between collapsing uncertain regions into definite states and propagating the resulting constraint information through the output."
---

# Observation-Propagation Cycle (WFC)

## Definition / 定义

The observation-propagation cycle is the iterative core of the Wave Function Collapse algorithm. It alternates between two phases until the output is fully determined or a contradiction is reached. In the observation step, the region with lowest Shannon entropy is collapsed to a definite state. In the propagation step, this new information propagates through the output, reducing the set of possible patterns for neighboring regions via constraint propagation.

## Key Properties / 关键特性

- **Observation**: Select the NxN region with minimal nonzero entropy; collapse it to a definite state based on pattern coefficients and input distribution
- **Propagation**: Use the AC-4 constraint propagation algorithm to reduce coefficients in neighboring regions
- Continues until all elements are either fully observed (one nonzero coefficient) or contradictory (all coefficients zero)
- If a contradiction occurs, the algorithm terminates without producing output
- The cycle is inspired by the quantum mechanics concept of wave function collapse, though WFC uses real-valued coefficients, not complex

## Examples / 示例

- In pixel art synthesis: collapse a 3x3 region → propagate constraints to all overlapping 3x3 regions → repeat
- In tilemap generation: collapse a tile → propagate adjacency constraints to neighbors → repeat

## Related Concepts / 相关概念

- [[wave-function-collapse]] — the parent algorithm
- [[entropy-heuristic-wfc]] — the observation selection strategy
- [[constraint-propagation-ac4]] — the propagation algorithm
- [[overlapping-model-wfc]] — uses this cycle with pattern superposition
- [[simple-tiled-model]] — uses this cycle with adjacency constraints

## References / 参考资料

- Maxim Gumin, "WaveFunctionCollapse" — https://github.com/mxgmn/WaveFunctionCollapse
