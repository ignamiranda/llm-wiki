---
title: Connected Component Pathfinding
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [pathfinding, a-star, flood-fill, procedural-generation, game-development, optimization]
aliases: [connected-component-index, walkable-region-pathfinding]
summary: "A pathfinding optimization technique that tracks connected walkable regions via flood-fill indices, enabling agents to skip failed A* queries by checking component connectivity first."
---

# Connected Component Pathfinding

## Definition

Connected component pathfinding is an optimization for A* on dynamic maps where the environment changes frequently. Walkable tiles are grouped into connected components (regions reachable by walking). Each component gets a unique index maintained via flood-fill updates when the map changes. Agents check component indices before pathfinding — if start and goal share the same component number, A* will succeed; if not, the path is impossible and can be skipped entirely.

## Key Properties

- Eliminates nearly all failed A* calls on dynamic maps — agents query component numbers instead of running and failing pathfinding
- Components are updated incrementally: when a wall is built or water cuts an area, a flood fill re-indexes the affected region
- Maintained per movement type (e.g., walking only) — flying creatures may not have specialized indices
- Avoids complex overlay structures (e.g., jump point search, rectangular overlays) that are expensive to maintain on rapidly changing maps
- Trade-off: memory and update cost per movement type limits how many movement modalities can be tracked

## Examples

Dwarf Fortress uses A* with connected component pathfinding. When water cuts the fortress in half, a flood fill from one side re-indexes half the fortress to a new component number. Dwarves check component numbers; if numbers match, A* will succeed. Flying creatures fall back to the walking index — they lack specialized flying-component pathfinding, though short-range flood fills give them some combat advantages.

## Related Concepts

- [[2021-12-31-dwarf-fortress-development]] — describes DF's implementation
- [[2019-06-03-dwarf-fortress-development-gamasutra]] — context on DF's simulation system

## References

- Stack Overflow Blog: "700,000 lines of code, 20 years, and one developer: How Dwarf Fortress is built" (2021)
