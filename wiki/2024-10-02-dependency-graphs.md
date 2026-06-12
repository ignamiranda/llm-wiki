---
title: "Procedural Game Progression Dependency Graphs"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, game-design, graph-theory, progression, the-big-forest]
summary: "Development of a system that procedurally generates game progression dependency graphs and spatial graphs simultaneously, creating fully playable game levels with gates, keys, creatures, and clues."
source_url: "https://blog.runevision.com/2024/10/procedural-game-progression-dependency.html"
---

# Procedural Game Progression Dependency Graphs

## Summary
Development of a system that procedurally generates game progression dependency graphs and spatial graphs simultaneously, creating fully playable game levels with gates, keys, creatures, and clues.

## Content

The system started with simple tree structures for game progression, then evolved into directed acyclic graphs (DAGs) using a graph rewrite rule approach. A single rewrite rule is applied to random edges in the graph until the desired number of nodes is reached, with constraints ensuring each node has in-edges and out-edges of either 1 or 2. This produces balanced progression graphs where no node is a bottleneck and the branching factor stays controlled.

A key insight was the dual graph approach: the dependency graph (which rooms/objectives must be completed before others) and the spatial graph (the physical layout of rooms in the world) are generated simultaneously from the same data structure. A locked gate's key is a direct dependency in the dependency graph, but can be physically located far away in the spatial graph — the player must explore to find it, even though they know what they're looking for.

For visualization, the system uses Sugiyama-style layered graph drawing with improvements adapted from academic papers. The generated prototypes produce fully playable game levels with gates, keys, creatures, and clues, demonstrating that procedural progression can create meaningful gameplay. Limitations remain: the iconographic gameplay style needs better 3D creature models to be visually compelling. The work draws on Gareth Rees's analysis of Ocarina of Time's puzzle structure, Ron Gilbert's dependency charts, Squidi's puzzle trees, and Dormans Joris's thesis on Engineering Emergence.

## Key Takeaways
- Graph rewrite rules generate balanced DAGs with controlled branching factor
- Dual dependency/spatial graph generation from same data
- Sugiyama layered graph drawing for visualization
- Prototyped playable game levels with diverse puzzle mechanics

## Related
- [[rune-skovbo-johansen]] — author
- [[game-progression-dependency-graph]] — new concept
- [[quest-procedural-generation]] — related
