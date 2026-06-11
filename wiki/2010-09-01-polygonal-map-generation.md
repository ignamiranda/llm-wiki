---
title: "Polygonal Map Generation for Games"
type: article
language: en
created: 2010-09-01
modified: 2026-06-11
tags: [procedural-generation, voronoi, map-generation, game-development]
summary: "Amit Patel's guide to generating game maps using Voronoi polygons instead of square or hexagonal grids, covering the full pipeline from polygon generation to rendering."
source_url: "http://www-cs-students.stanford.edu/~amitp/game-programming/polygon-map-generation/"
source_hash: "B996558CD403FDD124ABCC155317B8BBDAF943366AEE3AF70521E0D7970D35D9"
status: archived
---

# Polygonal Map Generation for Games

## Summary

A comprehensive guide to procedural map generation using Voronoi diagrams rather than traditional tile grids. The pipeline produces island maps with coastlines, mountains, rivers, lakes, biomes, and noisy-edge rendering. The approach prioritizes gameplay constraints over realism — elevation monotonically increases from coast to mountain peak, rivers always flow downhill to the ocean, and biomes are determined by elevation (temperature proxy) and moisture.

## Content

The generation pipeline consists of these stages:

**Polygons:** Random points are distributed across the map and converted to Voronoi polygons. Lloyd relaxation (2 iterations) evens out polygon sizes. A barycentric dual mesh can be used instead for more uniform corner spacing.

**Map Representation:** Two dual graphs are stored together — the Delaunay triangulation (polygon centers, adjacency) and the Voronoi diagram (polygon corners, shapes). Every edge stores four nodes: two polygon centers and two corners, enabling seamless switching between the two representations.

**Islands:** Coastlines are drawn using any shape function (radial sine waves, noise, user-drawn). Corners are assigned land/water, then polygons inherit land/water from their corner fractions. Flood fill distinguishes oceans (connected to border) from lakes.

**Elevation:** Set as distance from the coast, with lake polygons skipped to keep valleys flat. Elevations are redistributed to match a desired distribution (more low-elevation land than mountains). The downhill direction from any corner always leads to the ocean, eliminating local minima.

**Rivers:** Random mountain corners are chosen as sources. The river follows the steepest downhill slope corner-to-corner until reaching the ocean. Multiple rivers merge downstream, with rendered width proportional to the square root of flow.

**Moisture:** Defined as decreasing distance from fresh water (rivers and lakes). Moisture is redistributed to a uniform distribution for roughly equal dry/wet area.

**Biomes:** Uses the Whittaker diagram — biome depends on elevation (temperature) and moisture. Ocean, lake/ice/marsh, and beach are determined first, then land biomes from the elevation-moisture grid (snow, tundra, taiga, shrubland, grassland, desert, various forests).

**Noisy Edges:** Polygon borders are replaced with noisy lines constrained to stay within quadrilateral regions defined by the dual graph structure, preventing lines from crossing.

**Rendering:** Additional techniques include noise textures for visual variety, per-pixel biome interpolation, and coordinate distortion for less polygon-like appearance.

## Key Takeaways

- Voronoi diagrams provide irregular polygon shapes with distinct player-recognizable areas useful for gameplay (towns, quests, territories, landmarks)
- The dual graph representation (Voronoi + Delaunay stored together) enables both shape rendering and adjacency/pathfinding
- "Elevation after oceans" approach (distance from coast) guarantees monotonic elevation and eliminates local minima
- Gameplay constraints should drive generation decisions, not realism — the article explicitly chose volcano-island geometry for Realm of the Mad God
- Noisy edges hide the underlying polygon structure while preserving it for game mechanics

## Related

- [[voronoi-diagram-mapgen]] — the core geometric structure
- [[lloyd-relaxation]] — algorithm for evening out polygon distribution
- [[dual-graph-representation]] — storing Voronoi and Delaunay graphs together
- [[downhill-river-generation]] — river generation via steepest descent
- [[noisy-edges]] — hiding polygon structure with constrained noise
- [[whittaker-diagram-biomes]] — biome classification by elevation and moisture
- [[elevation-from-coast-distance]] — defining elevation as distance from coastline
- [[amit-patel]] — author
- [[layer-based-procedural-generation]] — alternative approach to procedural generation
- [[2015-07-07-noise-terrain-maps]] — earlier noise-based terrain tutorial by the same author
