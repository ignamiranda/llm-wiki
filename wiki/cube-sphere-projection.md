---
title: "Cube-to-Sphere Projection"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, sphere, cube-mapping, map-projection, computational-geometry]
aliases: [cube map projection, gnomonic cube projection]
summary: "A method for mapping a cube's surface onto a sphere by normalizing position vectors, used as a geometric foundation for square tile maps on spherical worlds."
---

# Cube-to-Sphere Projection

## Definition
Cube-to-sphere projection maps the six faces of a cube onto a sphere by normalizing each point's position vector (gnomonic projection). This creates six square face regions on the sphere, enabling the use of square tiles for spherical game maps.

## Distortion Properties
Three competing properties cannot all be optimized:
- **Area**: all tiles cover equal surface area
- **Aspect**: all tiles have the same width-to-height ratio
- **Angle**: all tile corners meet at 90 degrees

Common adjustments include tangent (pi/4 * atan(w)), quadratic (Google S2 default), and linear methods.

## Key Properties
- Eight singularities at cube vertices (90-degree distortion each)
- Face centers are enlarged more than edges (area distortion)
- Tangent adjustment reduces area distortion at cost of angle preservation

## Related Concepts
- [[2026-06-11-square-tiling-sphere]] — Primary implementation
- [[2026-06-11-hexagon-tiling-sphere]] — Hexagon-based alternative

## References
- Google S2 Geometry library — quadratic projection used for planet-scale geometry
- "Cube-to-Sphere Gnomonic Projection" — computational geometry reference
