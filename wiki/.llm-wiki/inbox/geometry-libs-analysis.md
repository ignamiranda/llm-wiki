# Geometry Libraries Analysis

**Date:** 2026-06-11
**Sources:** ilmola/generator, OpenSCAD, libfive

## Summary

Three distinct approaches to procedural geometry/solid modeling: a mesh primitive generator (ilmola/generator), a script-based CSG CAD modeller (OpenSCAD), and an f-rep solid modeling infrastructure (libfive). Each occupies a different niche in the procedural geometry landscape.

## Source 1: ilmola/generator

- **URL:** https://github.com/ilmola/generator
- **License:** LGPL-2.1
- **Language:** C++11
- **Stars:** 240, Forks: 28, Commits: 75
- **Category:** Procedural mesh generation library (not a renderer or CAD tool)
- **Key features:**
  - Generates meshes of geometric primitives (sphere, box, cone, cylinder, torus, teapot, etc.)
  - Right-handed coordinate system, double precision
  - Modifier system (translate, rotate, scale, merge, subdivide, extrude, lathe, spherify) — nestable
  - SVG preview, OBJ export
  - Depends on GML math library
  - LGPL-2.1 licensed

## Source 2: OpenSCAD

- **URL:** https://openscad.org/
- **License:** Free software (GPL)
- **Category:** Programmers Solid 3D CAD Modeller
- **Key features:**
  - Script-based (declarative) modeling
  - CSG operations (union, difference, intersection)
  - Cross-platform (Linux, Windows, macOS)
  - Extensible via libraries
  - Primitive shapes and 2D-to-3D extrusion
  - Large ecosystem of community libraries

## Source 3: libfive

- **URLs:** https://github.com/libfive/libfive, https://libfive.com/
- **License:** MPL/GPL
- **Language:** C++ (with C API), Guile Scheme and Python bindings
- **Stars:** 1.6k, Forks: 176, Commits: 2,431
- **Category:** Functional representation (f-rep) solid modeling infrastructure
- **Key features:**
  - F-rep based modeling — shapes defined as mathematical functions f(x,y,z)
  - Produces watertight, manifold, hierarchical, feature-preserving triangle meshes
  - Standard library of shapes, transforms, CSG operations
  - Studio GUI application
  - Creator: Matthew Keeter

## Relationships & Distinctions

| Axis | ilmola/generator | OpenSCAD | libfive |
|------|-----------------|----------|---------|
| Core paradigm | Parametric mesh generation | CSG/B-rep via scripting | Functional representation |
| Output | Raw vertex data (meshes) | Solid 3D models (STL, etc.) | Watertight triangle meshes |
| Programming | C++ library (to embed) | Declarative scripting language | C++ library + bindings |
| Modifier model | Nestable modifier chain | CSG operations in script | Shape composition via math |
| Target user | Game devs, C++ programmers | Makers, engineers, hobbyists | Researchers, advanced CAD |
| Maturity | Small (75 commits) | Very mature | Mature (2.4k commits) |

## Links to Create

- [[ilmola-generator]] — concept page for the generator library
- [[openscad]] — concept page for OpenSCAD
- [[libfive]] — concept page for libfive
- [[functional-representation-solid-modeling]] — concept page for f-rep
- [[matthew-keeter]] — person page for libfive creator
