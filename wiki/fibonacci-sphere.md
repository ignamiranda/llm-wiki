---
title: "Fibonacci Sphere"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, sphere, point-distribution, algorithms, computational-geometry]
aliases: [spherical phyllotaxis, Fibonacci lattice sphere]
summary: "An algorithm for distributing points approximately evenly on a sphere's surface using the Fibonacci sequence, with a spiral pattern that avoids clustering at poles."
---

# Fibonacci Sphere

## Definition
The Fibonacci sphere algorithm distributes N points on a sphere's surface by spiraling from pole to pole using the golden angle. Each point is placed at a fixed increment in latitude and an azimuthal angle proportional to the golden ratio.

## Key Properties
- Even distribution: points are reasonably evenly spaced without the clustering that purely random placement produces
- Simple implementation: no subdivision or iteration required
- Pole patterns: the distribution at the poles differs from the mid-latitudes (unlike subdivided icosahedra)
- Not optimal: the Tammes problem studies optimal sphere packing, but Fibonacci is good enough for procedural generation

## Related Concepts
- [[spherical-voronoi]] — Uses Fibonacci sphere for seed points
- [[2026-06-11-delaunay-voronoi-sphere]] — Context of use
