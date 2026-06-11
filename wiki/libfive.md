---
title: "libfive — Functional Representation Solid Modeling"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [libfive, solid-modeling, functional-representation, mesh-generation, procedural-modeling, cad]
aliases: [libfive-studio]
summary: "Infrastructure for solid modeling using functional representations (f-reps), including a C++ library with C API, Guile Scheme and Python bindings, and a Studio GUI application."
source_url: "https://libfive.com/"
---

# libfive — Functional Representation Solid Modeling

## Definition

libfive is an infrastructure for solid modeling based on functional representations (f-reps), created by Matthew Keeter. Instead of storing geometry as boundary meshes, shapes are defined as mathematical functions f(x,y,z) where the surface is the zero level set. libfive compiles these functions into watertight, manifold, hierarchical, feature-preserving triangle meshes. It includes a shared library (C++ with C API), a standard library of shapes and transforms, language bindings for Guile Scheme and Python, and a Studio GUI application.

## Key Properties

- F-rep core — shapes are mathematical functions, not polygonal meshes
- Produces watertight, manifold, feature-preserving triangle meshes
- Hierarchical evaluation for performance
- Standard library: primitives (sphere, box, cylinder, etc.), transforms (move, scale, rotate), CSG (union, difference, intersection)
- Language bindings: Guile Scheme, Python
- Studio GUI: interactive visualization and modeling
- Created by Matthew Keeter
- MPL/GPL licensed (dual licensing)
- 2,431 commits, 1.6k GitHub stars

## Examples

Using the C API to create and evaluate a shape:

```c
// Create a sphere of radius 1
libfive_shape* sphere = libfive_sphere(1.0);
// Move it
libfive_shape* moved = libfive_move(sphere, 1.0, 0.0, 0.0);
// Evaluate to mesh
libfive_mesh* mesh = libfive_mesh_eval(moved, 0.1);
```

## Related Concepts

- [[functional-representation-solid-modeling]] — the core mathematical paradigm behind libfive
- [[openscad]] — CSG/B-rep based solid modeling, a different paradigm
- [[ilmola-generator]] — mesh primitive generation, lower-level output
- [[matthew-keeter]] — creator of libfive
- [[mesh-generation]] — the process of creating triangle meshes from models
- [[solid-modeling]] — the broader field

## References

- [libfive Homepage](https://libfive.com/)
- [GitHub Repository](https://github.com/libfive/libfive)
- [Matthew Keeter's personal site](https://www.mattkeeter.com/)
