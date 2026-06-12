---
title: "Sugiyama Layered Graph Drawing"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [graph-theory, visualization, algorithm]
aliases: []
summary: "A class of algorithms for drawing directed acyclic graphs in a layered hierarchical layout, also known as layered graph drawing."
---

# Sugiyama Layered Graph Drawing

## Definition

An algorithm family with four phases: (1) **Layer assignment** — assign nodes to horizontal layers. (2) **Crossing reduction** — reorder nodes within layers to minimize edge crossings. (3) **Coordinate assignment** — assign x-coordinates within layers. (4) **Edge routing** — draw edges with bends. Rune Skovbo Johansen improved his implementation with techniques from papers on scalable DAG drawing with gates and ports, bilayer cross counting, and fast k-level graph layout.

## Key Properties

- Hierarchical layered layout for DAGs
- Four-phase processing pipeline
- Minimizes edge crossings
- Supports gates and ports

## Related Concepts

- [[game-progression-dependency-graph]] — visualization context

## References

- Source: runevision blog
