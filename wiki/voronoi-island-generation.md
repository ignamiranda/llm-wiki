---
title: "Voronoi Island Generation"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, islands, voronoi, geography]
aliases: [voronoi-coastline]
summary: "The process of defining coastlines and islands on a Voronoi polygon map by assigning land and water to corners, then propagating to polygons."
source_url: "http://www-cs-students.stanford.edu/~amitp/game-programming/polygon-map-generation/"
source_hash: "B996558CD403FDD124ABCC155317B8BBDAF943366AEE3AF70521E0D7970D35D9"
---

# Voronoi Island Generation

## Definition / 定义

The process of creating island landmasses on a Voronoi polygon map. A shape function (radial sine waves, noise function, user drawing, or any other source) assigns land or water to each polygon corner. Polygons inherit their land/water status from the fraction of their corners that are land. Flood fill from the map border distinguishes oceans (connected to border) from lakes (surrounded by land).

## Key Properties / 关键特性

- Land/water is first assigned to corners (Voronoi vertices), then polygons inherit by corner fraction
- The coastline is all edges where land and water polygons meet
- Flood fill distinguishes ocean (connected to map border) from lakes (enclosed by land)
- Any shape function can be used: mathematical (radial sine waves), noise-based, user-drawn, or even scanned physical objects
- The dual graph introduces edge cases — a polygon with mixed water/land corners requires experimentation to resolve
- The "elevation after oceans" approach defines coastline first, then computes elevation as distance from coast

## Examples / 示例

- A radial sine wave island generator produces roughly circular islands with frilly coastlines
- Perlin noise can create more organic continental shapes
- mapgen4 lets users draw their own island outlines
- Other projects have used pizza box stains, cloud photos, or torn paper as island shapes

## Related Concepts / 相关概念

- [[voronoi-diagram-mapgen]] — the underlying polygon structure
- [[elevation-from-coast-distance]] — elevation is computed after coastlines are defined
- [[dual-graph-representation]] — handles the polygon/corner land-water propagation
- [[2010-09-01-polygonal-map-generation]] — the article describing this technique

## References / 参考资料

- Amit Patel, "Polygonal Map Generation for Games", Red Blob Games, 2010
