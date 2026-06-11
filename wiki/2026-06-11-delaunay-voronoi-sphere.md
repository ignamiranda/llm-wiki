---
title: "Delaunay+Voronoi on a Sphere"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, voronoi, delaunay, sphere, planet-generation, computational-geometry]
summary: "Amit Patel's technical guide to computing Delaunay triangulation and Voronoi regions on a sphere using stereographic projection, Fibonacci sphere points, and centroid alternatives."
source_url: "https://www.redblobgames.com/x/1842-delaunay-voronoi-sphere/"
source_hash: "c8ce135df46612d6c6f73d8acf98448faef1cfd45ef094bdb11a60354975b8d6"
---

# Delaunay+Voronoi on a Sphere

## Summary
A detailed technical walkthrough for computing Delaunay triangulation and Voronoi regions on a spherical surface, built for ProcJam 2018. The key insight is using stereographic projection to adapt existing 2D Delaunay libraries for spherical coordinates, with a workaround for the south pole hole.

## Technical Approach

### Point Distribution
Uses a Fibonacci sphere algorithm (phyllotaxis) instead of subdivided icosahedra for evenly distributed points. Two algorithms are compared from the CGAFaq. Fibonacci spheres are simpler but have different patterns at the poles.

### Delaunay Triangulation
The clever approach: project 3D points on a sphere onto an infinite 2D plane via stereographic projection, run an unmodified 2D Delaunay library (Delaunator), then map results back to the sphere. This creates a hole at the south pole that must be stitched by adding a new point and connecting triangle edges.

### Voronoi Regions
Voronoi regions are formed from triangle circumcenters. However, the author recommends using centroids instead, as Voronoi edges can have zero or near-zero length, making them unsuitable for placing roads and rivers.

## Related
- [[spherical-voronoi]] — Core concept
- [[fibonacci-sphere]] — Point distribution algorithm
- [[voronoi-diagram-mapgen]] — 2D Voronoi foundation
- [[dual-graph-representation]] — Dual graph applies to spherical Voronoi too
- [[amit-patel]] — Author
