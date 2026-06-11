---
title: "Dual Graph Map Representation"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, graph-theory, voronoi, map-representation]
aliases: [dual-graph-map]
summary: "A map representation that stores both the Voronoi diagram (polygon shapes) and its dual Delaunay triangulation (polygon adjacency) together, enabling efficient switching between shape rendering and adjacency/pathfinding."
source_url: "http://www-cs-students.stanford.edu/~amitp/game-programming/polygon-map-generation/"
source_hash: "B996558CD403FDD124ABCC155317B8BBDAF943366AEE3AF70521E0D7970D35D9"
---

# Dual Graph Map Representation

## Definition / 定义

A map data structure that simultaneously represents two related graphs: the Delaunay triangulation (nodes at polygon centers, edges for adjacency) and the Voronoi diagram (nodes at polygon corners, edges for shapes). Every edge in the Delaunay graph corresponds to exactly one edge in the Voronoi graph. Instead of storing them separately, each edge points to four nodes: two polygon centers and two polygon corners.

## Key Properties / 关键特性

- Every triangle in the Delaunay triangulation corresponds to a corner in the Voronoi diagram, and vice versa
- Polygon adjacency is determined via the Delaunay graph (useful for pathfinding, biome spreading)
- Polygon shapes are defined by the Voronoi graph (useful for rendering, river paths, elevation)
- Compact integer representations (e.g., Delaunator) can store the dual graph efficiently
- The two graphs define quadrilateral regions between polygon centers and corners, which constrain noisy edge rendering

## Examples / 示例

- Finding a river path: navigate the Voronoi corner graph following downhill slopes
- Pathfinding: use the Delaunay adjacency graph to move between polygon centers
- Rendering: use the Voronoi shape graph to draw polygon borders and fill colors
- Noisy edges: each Delaunay-Voronoi edge pair defines a quadrilateral that constrains noise

## Related Concepts / 相关概念

- [[voronoi-diagram-mapgen]] — the geometric structure being represented
- [[noisy-edges]] — rendering technique that depends on dual graph quadrilaterals
- [[2010-09-01-polygonal-map-generation]] — the article that introduced this combined representation for game maps

## References / 参考资料

- Amit Patel, "Polygonal Map Generation for Games", Red Blob Games, 2010
- Wikipedia: Delaunay triangulation, Graph theory
