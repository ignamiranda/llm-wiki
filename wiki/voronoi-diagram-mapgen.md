---
title: "Voronoi Diagrams for Map Generation"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, voronoi, map-generation, geometry]
aliases: [voronoi-map]
summary: "Using Voronoi diagrams as the underlying geometric structure for procedural map generation, providing irregular polygon shapes instead of uniform tile grids."
source_url: "http://www-cs-students.stanford.edu/~amitp/game-programming/polygon-map-generation/"
source_hash: "B996558CD403FDD124ABCC155317B8BBDAF943366AEE3AF70521E0D7970D35D9"
---

# Voronoi Diagrams for Map Generation

## Definition / 定义

A technique for procedural map generation that uses Voronoi polygons as the fundamental spatial subdivision instead of square or hexagonal grids. Random seed points are distributed across the map, and each point becomes a polygon containing all area closer to that point than to any other. The resulting irregular polygons form distinct player-recognizable areas useful for gameplay mechanics.

## Key Properties / 关键特性

- Produces irregular polygon shapes and sizes rather than uniform tiles
- Random point distribution creates "clumpy" distributions; Lloyd relaxation or Poisson disc sampling produces more even distributions
- The dual Delaunay triangulation provides adjacency information for pathfinding and neighborhood queries
- Polygon corners serve as a second graph for shape-based operations (rivers, elevation, rendering)
- Typical implementations use 200–8000 polygons depending on detail needs

## Examples / 示例

- Island maps where each polygon is a distinct zone with its own elevation, biome, and gameplay properties
- Realm of the Mad God used Voronoi-based maps where elevation corresponds to difficulty, with players starting on beaches and progressing to mountaintop boss fights
- Fantasy map generators (Azgaar's, donjon) use Voronoi diagrams for continent and region subdivision

## Related Concepts / 相关概念

- [[lloyd-relaxation]] — algorithm to even out Voronoi polygon distribution
- [[dual-graph-representation]] — storing Voronoi and Delaunay graphs together
- [[2010-09-01-polygonal-map-generation]] — the seminal article on this technique
- [[layer-based-procedural-generation]] — alternative approach using layered chunk generation
- [[chunk-based-generation]] — alternative approach using rectangular tile chunks

## References / 参考资料

- Amit Patel, "Polygonal Map Generation for Games", Red Blob Games, 2010
- Wikipedia: Voronoi diagram, Delaunay triangulation
