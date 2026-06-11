---
title: "ilmola/generator — Procedural Geometry Generation Library"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, procedural-modeling, geometry, mesh-generation, cpp]
aliases: [generator-cpp, ilmola-generator]
summary: "A C++11 library for procedurally generating meshes of geometric primitives (spheres, boxes, cones, cylinders, torus, teapot, etc.) with a nestable modifier system and SVG/OBJ export."
source_url: "https://github.com/ilmola/generator"
---

# ilmola/generator — Procedural Geometry Generation Library

## Definition

A C++11 procedural geometry generation library by ilmola that generates mesh data for geometric primitives at runtime. It is not a graphics library — it produces raw vertex data that can be consumed by any rendering pipeline. The library uses a right-handed coordinate system with double precision and supports an extensible modifier system for transforming generated geometry.

## Key Properties

- C++11, header-only or compiled, depends on GML math library
- Right-handed coordinate system, double precision floating point
- Supports primitives: sphere, box, cone, cylinder, torus, disk, teapot, and more
- Modifier chain architecture — modifiers like translate, rotate, scale, merge, subdivide, extrude, lathe, and spherify can be nested
- SVG preview output for 2D visualization
- OBJ export for 3D mesh interchange
- LGPL-2.1 licensed

## Examples

Embedding the library to generate a sphere mesh with subdivision:

```cpp
#include <generator/Sphere.hpp>
#include <generator/Subdivide.hpp>

auto sphere = generator::Sphere(1.0, 32, 24);
auto subdivided = generator::Subdivide(sphere, 2);
// Iterate over vertices and triangles
for (const auto& tri : subdivided.triangles()) { /* ... */ }
```

## Related Concepts

- [[openscad]] — script-based CSG CAD modeler, different paradigm (B-rep vs mesh gen)
- [[libfive]] — functional representation solid modeling, a more mathematical approach
- [[functional-representation-solid-modeling]] — the f-rep paradigm used by libfive
- [[mesh-generation]] — the broader category of algorithmic mesh creation
- [[matthew-keeter]] — creator of libfive

## References

- [GitHub Repository](https://github.com/ilmola/generator)
- License: LGPL-2.1
