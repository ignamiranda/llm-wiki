---
title: "Downhill River Generation"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, rivers, hydrology, voronoi]
aliases: [steepest-descent-rivers]
summary: "A river generation technique where rivers start at random mountain corners and follow the steepest downhill slope through the Voronoi corner graph until reaching the ocean."
source_url: "http://www-cs-students.stanford.edu/~amitp/game-programming/polygon-map-generation/"
source_hash: "B996558CD403FDD124ABCC155317B8BBDAF943366AEE3AF70521E0D7970D35D9"
---

# Downhill River Generation

## Definition / 定义

A river generation algorithm for polygon-based maps that places river sources at random high-elevation (mountain) corner nodes, then follows the steepest downhill direction from each corner to the next until reaching the ocean. Downhill vectors are computed from the elevation differences between adjacent corners.

## Key Properties / 关键特性

- Rivers flow through the Voronoi corner graph rather than polygon centers, producing more natural-looking paths
- Multiple rivers merge when they share downstream segments; combined flow is summed
- Rendered river width is proportional to the square root of accumulated flow
- Lake polygons have flat elevation, so rivers naturally flow into and out of lakes at edges
- Requires monotonic elevation (no local minima) to guarantee all rivers reach the ocean
- Elevation defined as distance from coast ensures monotonicity without needing lake-filling or channel-carving algorithms

## Examples / 示例

- Starting at a mountain ridge, a river flows downhill through multiple polygon corners, widening as tributaries join
- Multiple mountain-top sources produce a branching river network
- Rivers naturally form valleys with adjacent lakes at their edges

## Related Concepts / 相关概念

- [[elevation-from-coast-distance]] — elevation model that guarantees downhill paths reach the ocean
- [[voronoi-diagram-mapgen]] — the corner graph that rivers traverse
- [[2010-09-01-polygonal-map-generation]] — the article that described this technique

## References / 参考资料

- Amit Patel, "Polygonal Map Generation for Games", Red Blob Games, 2010
