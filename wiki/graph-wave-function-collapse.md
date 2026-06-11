---
title: "Graph Wave Function Collapse (GWFC)"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [wfc, wave-function-collapse, graph-algorithms, procedural-generation, python]
aliases: [graph-wfc, gwfc]
summary: "An extension of Wave Function Collapse from grid structures to arbitrary graphs, using subgraph isomorphism (VF2) to extract and apply patterns."
source_url: "https://github.com/lamelizard/GraphWaveFunctionCollapse"
source_hash: "D0E84825CDD9E71BE132985B5D98579A7403E59B7B41D4A5D8D2FB91BD798203"
---

# Graph Wave Function Collapse (GWFC)

## Definition / 定义

Graph Wave Function Collapse (GWFC) extends the WFC algorithm from regular grid structures to arbitrary graphs. Patterns are defined via a "local similarity graph" (GL) and extracted from a colored example graph (GI) using VF2 subgraph isomorphism. The target output graph (GO) is then colored using the extracted patterns with constraint propagation.

## Key Properties / 关键特性

- Generalizes WFC from grids to any graph structure
- Uses VF2 algorithm (via networkx) for subgraph isomorphism
- Multiple local similarity graphs (GLs) supported
- Shannon entropy-based pattern selection
- Constraint propagation removes impossible color assignments
- Input/output via GraphML format
- Written in Python 3.x, pip-installable (graphwfc)
- Includes a thesis (German) on the algorithm
- MIT licensed, 64 GitHub stars

## Examples / 示例

- Generating colored trees, hexagonal grids, and custom graph structures
- Can simulate standard grid-based WFC by constructing appropriate GL graphs
- Example models: beach, starcave, city

## Related Concepts / 相关概念

- [[debroglie]] — grid-based WFC in C#
- [[2026-06-11-wfc-implementations-survey]] — surveyed in the WFC survey article
- [[layer-based-procedural-generation]] — alternative procgen architecture

## References / 参考资料

- https://github.com/lamelizard/GraphWaveFunctionCollapse
- https://lamelizard.github.io/GraphWaveFunctionCollapse/graphwfc.html