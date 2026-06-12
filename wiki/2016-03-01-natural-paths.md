---
title: "Creating Natural Paths on Terrains Using Pathfinding"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, pathfinding, terrain, a-star]
summary: "Using A*-like pathfinding on implicit coordinate grids with non-linear slope penalties to create natural-looking winding paths across procedural terrain, avoiding steep shortcuts."
source_url: "https://blog.runevision.com/2016/03/note-on-creating-natural-paths-in.html"
---

# Creating Natural Paths on Terrains Using Pathfinding

## Summary
Using A*-like pathfinding on implicit coordinate grids with non-linear slope penalties to create natural-looking winding paths across procedural terrain, avoiding steep shortcuts.

## Content
The core technique uses A*-like pathfinding on an implicit coordinate grid to generate trails across procedural terrain. Rather than storing a graph data structure, the grid is computed on the fly from terrain height data, keeping memory usage independent of world size. Pathfinding moves in 16 directions (8 cardinal + 8 diagonal) for smooth path angles.

The key innovation is penalizing slope steepness non-linearly — squaring the slope cost rather than using a linear penalty. This prevents pathfinding from taking steep shortcuts that a human would avoid. A gentle slope costs almost nothing, but a steep slope becomes prohibitively expensive, forcing the path to follow contours and take longer winding routes around steep areas. A parameter study compares power values of 1.5, 2.0, and 3.0 with various multipliers.

The technique was later integrated into the LayerProcGen framework for procedural world generation. Additional refinement includes terrain flattening along the generated path — adjacent terrain is gently graded to create a natural-looking trail surface rather than leaving the path as a purely abstract route.

## Key Takeaways
- Squaring the slope cost produces natural winding paths
- Implicit coordinate graph avoids storing graph data structure
- 16-direction movement provides smooth path angles
- Integrated into LayerProcGen framework

## Related
- [[rune-skovbo-johansen]] — author
- [[layerprocgen]] — implements this technique
- [[infinite-terrain]] — context
