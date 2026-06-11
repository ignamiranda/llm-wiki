---
title: "procgen — Dart Procedural Generation Library"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, dart, perlin-noise, voronoi, delaunay, poisson-disk-sampling, geometry]
summary: "A Dart package by Andrew Brampton providing a collection of procedural generation algorithms — Perlin noise, layered fractal noise, Poisson disk sampling, Delaunay triangulation, Voronoi diagrams, and 2D geometry operations."
source_url: "https://github.com/bramp/procgen"
source_hash: "8ac8e75b89afb9b4e0a89d430e616f79eb4e35b625c54c56ade92c1d4f32ccc5"
---

# procgen — Dart Procedural Generation Library

## Summary

A Dart package that bundles fundamental procedural generation algorithms into a single library — noise generation (Perlin, fractal), spatial sampling (Poisson disk), triangulation (Delaunay, Voronoi), and 2D geometry types with smoothing and offsetting. Inspired by the procedural generation work of watabou.

## Content

The library is organized into three main categories:

**Noise** — Provides [[perlin-noise|Perlin Noise]] for smooth gradient noise, [[fractional-brownian-motion|Layered Fractal Noise]] for multi-octave detail via FBM, and Poisson disk sampling for blue-noise point distributions at a controlled minimum separation distance.

**Triangulation** — Implements [[delaunay-triangulation|Delaunay triangulation]], [[voronoi-diagram-mapgen|Voronoi diagrams]], and random Poisson Voronoi diagrams, enabling spatial partitioning and nearest-neighbor queries.

**Geometry** — Defines Point, Segment, Line, Polyline, and Polygon types with operations including [[chaikin-smoothing|Chaikin smoothing]], average smoothing, resampling, segment/line intersection detection, and polyline/polygon offsetting.

### Usage

```dart
dart pub add procgen

import 'package:procgen/procgen.dart';

void main() {
  // Perlin noise
  final noise = Perlin(rng: Random());

  // Fractal noise
  final fractal = LayeredNoise.fractal(rng: Random(), octaves: 5);

  // Poisson disk samples
  final samples = PoissonPattern(
    rng: Random(), width: 100, height: 100, distance: 5);

  // Voronoi pattern from samples
  final voronoi = VoronoiPattern(
    seeds: samples.points, width: 100, height: 100);

  // Smooth polygons via Chaikin's algorithm
  final polygons = voronoi.getRect(-50, -50, 200, 200);
  final smoothed = polygons.map((poly) => poly.chaikinSmooth());
}
```

## Key Takeaways

- Dart-native implementation — useful for Flutter/Dart game projects needing PG utilities
- Combines noise, sampling, triangulation, and geometry in one package
- Inspired by watabou's procedural generation work
- Licensed under BSD 2-Clause

## Related

- [[2015-07-07-noise-terrain-maps]] — underlying Perlin noise technique
- [[voronoi-diagram-mapgen]] — Voronoi generation used by the library
- [[2026-06-11-delaunay-voronoi-sphere]] — related Delaunay/Voronoi work
- [[procgen-dart]] — the library as a concept
- [[chaikin-smoothing]] — smoothing algorithm included in the library
