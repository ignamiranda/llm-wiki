---
title: "Spherical Voronoi Diagrams"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, voronoi, sphere, computational-geometry, planet-generation]
aliases: [Voronoi on a sphere]
summary: "Voronoi diagrams computed on a spherical surface, typically used for procedural planet generation. Can be computed via stereographic projection onto a plane for use with standard 2D Delaunay libraries."
---

# Spherical Voronoi Diagrams

## Definition
Spherical Voronoi diagrams partition a sphere's surface into regions based on distance to a set of seed points, analogous to 2D Voronoi diagrams but on a curved surface.

## Construction Methods
- **Stereographic projection**: Project points from sphere to 2D plane, run standard Delaunay triangulation, map results back. Creates a hole at the projection antipode that must be stitched.
- **Fibonacci sphere + Delaunator**: Distribute points via Fibonacci algorithm, project via stereographic projection, compute Delaunay triangulation, derive Voronoi from triangle circumcenters.

## Key Properties
- The Delaunay triangulation on a sphere is equivalent to the convex hull of the points on the sphere
- Triangle circumcenters lie slightly inside the sphere; should be normalized to the surface
- Centroid-based alternatives avoid zero-length edges common in true Voronoi

## Related Concepts
- [[voronoi-diagram-mapgen]] — 2D Voronoi foundation
- [[fibonacci-sphere]] — Point distribution for spherical Voronoi
- [[dual-graph-representation]] — Dual graph concept extends to spheres

## References
- Amit Patel, "Mesh Generation on a Sphere", Red Blob Games — https://www.redblobgames.com/maps/mesh-generation-on-a-sphere/
- Carsten et al., "Spherical Voronoi Diagrams" — computational geometry literature
