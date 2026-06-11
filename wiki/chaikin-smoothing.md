---
title: "Chaikin Smoothing"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, geometry, smoothing, algorithm]
aliases: [chaikin-corner-cutting]
summary: "A corner-cutting algorithm for smoothing polylines and polygons by iteratively replacing each vertex with two new points at fractional positions along adjacent edges."
---

# Chaikin Smoothing

## Definition

Chaikin smoothing (also known as Chaikin's corner-cutting algorithm) is a technique for smoothing polylines and polygons by iteratively replacing each vertex with two new points positioned at fractional distances (typically 1/4 and 3/4) along the adjacent edges. After each pass, the number of vertices doubles and the shape becomes progressively smoother, converging to a quadratic B-spline.

## Key Properties

- Each iteration: each vertex is replaced by two points at 25% and 75% along each incident edge
- Doubles vertex count per pass
- Converges to a quadratic B-spline curve in the limit
- Preserves the convex hull of the original shape
- Works on both open polylines and closed polygons

## Examples

```dart
// From the procgen Dart library
final smoothed = polygons.map((poly) => poly.chaikinSmooth());
```

## Related Concepts

- [[2026-06-11-procgen-dart-library]] — Dart library that includes Chaikin smoothing
- [[procgen-dart]] — the parent library
- [[voronoi-diagram-mapgen]] — Voronoi polygons are common targets for Chaikin smoothing

## References

- [GitHub — bramp/procgen](https://github.com/bramp/procgen)
