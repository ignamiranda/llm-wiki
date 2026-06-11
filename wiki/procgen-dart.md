---
title: "procgen (Dart Library)"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, dart, library, noise, voronoi, geometry]
aliases: [bramp-procgen]
summary: "A Dart package by Andrew Brampton providing a collection of procedural generation algorithms — Perlin noise, fractal noise, Poisson disk sampling, Delaunay triangulation, Voronoi diagrams, and 2D geometry operations."
---

# procgen (Dart Library)

## Definition

procgen is a Dart package that bundles fundamental procedural generation algorithms into a single library, including Perlin noise, layered fractal noise, Poisson disk sampling, Delaunay triangulation, Voronoi diagrams, and 2D geometry types with smoothing and offsetting operations. It is distributed via `dart pub add procgen` and licensed under BSD 2-Clause.

## Key Properties

- Language: Dart (primarily), with a Swift showcase viewer
- Repository: [bramp/procgen](https://github.com/bramp/procgen) on GitHub
- License: BSD 2-Clause
- Author: Andrew Brampton
- Inspired by: watabou's procedural generation work

## Examples

```dart
final noise = Perlin(rng: Random());
final fractal = LayeredNoise.fractal(rng: Random(), octaves: 5);
final samples = PoissonPattern(rng: Random(), width: 100, height: 100, distance: 5);
final voronoi = VoronoiPattern(seeds: samples.points, width: 100, height: 100);
```

## Related Concepts

- [[2026-06-11-procgen-dart-library]] — detailed article about the library
- [[chaikin-smoothing]] — smoothing algorithm included in the library
- [[2015-07-07-noise-terrain-maps]] — Perlin noise technique used by the library
- [[voronoi-diagram-mapgen]] — Voronoi technique used by the library

## References

- [GitHub repository — bramp/procgen](https://github.com/bramp/procgen)
