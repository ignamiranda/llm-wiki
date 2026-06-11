---
title: "Constrained Synthesis (WFC)"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, wfc, constraints, mixed-initiative]
summary: "WFC's ability to incorporate user-specified constraints, enabling autocomplete-style mixed-initiative design where the algorithm fills in parts of a partially constructed output."
---

# Constrained Synthesis (WFC)

## Definition / 定义

Constrained synthesis refers to WFC's support for user-specified constraints alongside the pattern-matching or tile-adjacency constraints derived from the input. This allows WFC to autocomplete partially constructed outputs, where a human designer places some tiles or regions manually and the algorithm fills in the rest while respecting both the example-derived constraints and the user's fixed placements.

## Key Properties / 关键特性

- WFC can easily combine with other generative algorithms or manual creation
- Enables mixed-initiative design workflows
- Particularly useful for game level design where designers want to sketch layouts and have WFC complete them
- User constraints are treated as pre-collapsed regions that propagate through the normal cycle

## Examples / 示例

- Autocompleting a dungeon level started by a human level designer
- Combining WFC with constructive procedural generation methods (as in Caves of Qud)
- A designer places rooms and corridors, WFC fills in wall decorations and details

## Related Concepts / 相关概念

- [[wave-function-collapse]] — the parent algorithm
- [[observation-propagation-cycle]] — the user's fixed tiles are pre-collapsed states that propagate
- [[layer-based-procedural-generation]] — alternative approach to combining generation passes

## References / 参考资料

- Maxim Gumin, "WaveFunctionCollapse" — https://github.com/mxgmn/WaveFunctionCollapse
