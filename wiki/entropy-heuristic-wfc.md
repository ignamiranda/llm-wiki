---
title: "Minimal Entropy Heuristic (WFC)"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, wfc, heuristics, entropy]
summary: "The observation heuristic used in WFC where the NxN region with the lowest Shannon entropy is selected for collapse, producing organic-looking results by mimicking human drawing behavior."
---

# Minimal Entropy Heuristic (WFC)

## Definition / 定义

The minimal entropy heuristic is the strategy used in WFC's observation step to select which NxN region to collapse next. It chooses the region with the lowest nonzero Shannon entropy — the region with the fewest viable remaining patterns. This mimics how humans approach constrained drawing: filling in the most constrained areas first before tackling freer regions.

## Key Properties / 关键特性

- Selects the wave element with minimal nonzero entropy for observation
- Removes directional bias that would otherwise appear in generated results
- Works on irregular grids, not just rectangular grids
- Well-suited for pre-constrained problems
- Produces visually organic results — a key reason WFC is enjoyable to watch

## Examples / 示例

- WFC generates more natural-looking results than sequential scanline ordering
- In Townscaper, Oskar Stålberg uses a custom observation heuristic that avoids local minima on irregular grids
- In Bad North, observation selects tiles that preserve navigability at each step

## Related Concepts / 相关概念

- [[wave-function-collapse]] — the parent algorithm
- [[observation-propagation-cycle]] — the core loop that uses this heuristic
- [[overlapping-model-wfc]] — uses this heuristic for pattern selection

## References / 参考资料

- Maxim Gumin, "WaveFunctionCollapse" — https://github.com/mxgmn/WaveFunctionCollapse
