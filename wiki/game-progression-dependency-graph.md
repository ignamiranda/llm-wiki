---
title: "Game Progression Dependency Graph"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, game-design, graph-theory, progression]
aliases: [dependency-graph, progression-graph, lock-and-key-graph]
summary: "A graph structure representing non-linear game progression where nodes are locations or objectives and edges represent dependency relationships (e.g., key required for door)."
---

# Game Progression Dependency Graph

## Definition

A directed acyclic graph (DAG) where nodes represent game locations, abilities, or items, and edges represent dependency relationships — node A must be completed or obtained before node B is accessible. Central to designing any non-linear game, from Metroidvania ability gates to RPG quests to puzzle locks and keys. Independently rediscovered by many game developers under different names.

Can be generated procedurally using graph rewrite rules or layered drawing algorithms. When combined with a spatial graph, enables full procedural level generation with meaningful progression.

## Key Properties

- Directed acyclic graph structure
- Nodes represent locks, keys, abilities, or locations
- Can be procedurally generated via rewrite rules
- Branching factor determines player freedom

## Related Concepts

- [[quest-procedural-generation]] — related domain
- [[branching-quest-generation]] — similar structure

## References

- Source: runevision blog
