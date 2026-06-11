---
title: "Hexagon Tiling of a Sphere"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, sphere, hexagon-tiling, game-development, map-projection]
summary: "Amit Patel's exploration of the challenges and possible solutions for wrapping hexagon tile maps on a sphere, including the twelve-pentagon problem and coordinate system workarounds."
source_url: "https://www.redblobgames.com/x/1640-hexagon-tiling-of-sphere/"
source_hash: "678d0b244c271f50d37546c49146a109b47db06c5fec28bedb7ff2888e5d50be"
---

# Hexagon Tiling of a Sphere

## Summary
An exploration of the fundamental challenge of placing hexagon tiles on a sphere: Euler's theorem forces twelve pentagons into any hexagon-based spherical tiling. Three coordinate system ideas are evaluated (two-level, convex limit, teleport regions), along with a flat rendering approach that hides the pentagons in unreachable zones.

## The Pentagon Problem
Due to Euler's formula for polyhedra (V - E + F = 2), any tiling of a sphere with primarily hexagonal faces will contain exactly twelve pentagons. These pentagons create discontinuities that must be hidden or worked around.

## Coordinate System Ideas
1. **Two-level**: Per-region local coordinates + region tracking. No local distortion but complex region crossings.
2. **Convex limit**: Single global coordinate clipped to icosahedron outline. Simple but locally distorted near poles.
3. **Teleport regions**: Single coordinate with teleport between valid regions. Hybrid approach with no local distortion in tropic zones.

## Flat Rendering
The demo implementation renders the four-region column around the player plus six neighboring regions, adjusting triangular regions near poles out of sight as the player moves. Players must stay away from the twelve pentagon zones.

## Related
- [[2026-06-11-square-tiling-sphere]] — Square tile alternative using cube
- [[2026-06-11-delaunay-voronoi-sphere]] — Voronoi-based alternative
- [[amit-patel]] — Author
