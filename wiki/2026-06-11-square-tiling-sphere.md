---
title: "Square Tile Maps on a Sphere"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, sphere, cube-mapping, map-projection, game-development, computational-geometry]
summary: "Amit Patel's exploration of using a cube's six square faces as the basis for square tile maps on a sphere, covering gnomonic projection, area distortion, and coordinate systems for moving between cube faces."
source_url: "https://www.redblobgames.com/x/1938-square-tiling-of-sphere/"
source_hash: "a8eed21aea3604bf3bb4c8df84ee00f7c458b92fa9c9c2faa208e3017e24dacd"
---

# Square Tile Maps on a Sphere

## Summary
An exploration of using a cube (six square faces) as the geometric foundation for square tile maps on a sphere. Covers gnomonic projection from cube to sphere, area distortion issues, tangent adjustment for reducing distortion, a coordinate system for moving between cube faces, and a survey of academic literature on cube-to-sphere projections.

## Cube-to-Sphere Mapping
Each cube face is projected onto the sphere using the gnomonic projection (normalizing the position vector). This creates area distortion — face centers are enlarged more than edges. The tangent adjustment (using pi/4 * atan(w)) reduces this.

## Distortion Tradeoffs
Three desirable properties compete:
1. **Area**: All tiles cover equal surface area
2. **Aspect**: All tiles have equal width/height
3. **Angle**: All tiles meet at 90 degrees

No projection achieves all three. Google's S2 library offers tangent, quadratic, and linear methods — quadratic is the default.

## Coordinate System
Uses a (row, column, orientation) system for the six cube faces:
- Row 1 (equator): four faces with columns 0-3
- Rows 0 and 2 (poles): single face each
- Face transitions are handled by three cases: pole-to-equator, equator-to-equator, equator-to-pole

## Related
- [[2026-06-11-hexagon-tiling-sphere]] — Hexagon-based alternative
- [[2026-06-11-delaunay-voronoi-sphere]] — Voronoi-based alternative
- [[cube-sphere-projection]] — Core concept
- [[amit-patel]] — Author
