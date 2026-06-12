---
title: "Graph Rewrite Rules for Procedural Generation"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, graph-theory, algorithm]
aliases: []
summary: "A technique using simple graph rewrite rules applied iteratively to generate directed acyclic dependency graphs with controlled branching factor."
---

# Graph Rewrite Rules for Procedural Generation

## Definition

A method: start with a simple graph (e.g., two connected nodes). Repeatedly apply a rewrite rule that splits an edge by inserting a new node, connecting it to both original nodes. This produces DAGs where each node (except start and end) has exactly 1–2 incoming and 1–2 outgoing edges. The branching factor is controlled by which edges are selected for splitting. Inspired by Dormans Joris' thesis "Engineering Emergence". Used by Rune Skovbo Johansen for procedurally generating game progression dependency graphs.

## Key Properties

- Simple edge-splitting rewrite rule
- Produces balanced DAGs
- In and out edges of 1 or 2
- Controlled branching factor

## Related Concepts

- [[game-progression-dependency-graph]] — application
- [[rune-skovbo-johansen]] — author

## References

- Source: runevision blog
