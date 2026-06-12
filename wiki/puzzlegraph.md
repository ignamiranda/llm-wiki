---
title: "PuzzleGraph"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [game-design, puzzle, tool, graph-theory]
aliases: [puzzle-graph]
summary: "An open-source tool by Rune Skovbo Johansen for analyzing and visualizing puzzle state spaces using graph theory, helping designers understand solution paths and dead ends."
---

# PuzzleGraph

## Definition

PuzzleGraph is an open-source Unity tool (MPL 2.0) for puzzle design that visualizes the complete state space of discrete puzzles. Supports gates, toggles, pressure plates, boulders, one-way edges, and hazards. Uses BFS and DFS search to build a graph of all reachable states from the initial state, with spring-based force-directed layout.

## Key Properties

- Separates puzzle design (static) from state (dynamic)
- BFS state space exploration
- Spring-force graph layout
- Open source (MPL 2.0)

## Related Concepts

- [[rune-skovbo-johansen]] — creator
- [[game-progression-dependency-graph]] — related graph-based design

## References

- Source: runevision blog
