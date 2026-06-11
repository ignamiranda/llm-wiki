---
title: "Solid Modeling"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [solid-modeling, cad, 3d-modeling, computational-geometry]
aliases: [solid-modelling]
summary: "The branch of 3D modeling dealing with unambiguous, watertight representations of solid objects for CAD, engineering, and manufacturing."
---

# Solid Modeling

## Definition

Solid modeling is a branch of 3D modeling focused on creating complete, unambiguous representations of solid objects — every point in space is classified as inside, outside, or on the surface. Unlike surface modeling (which only represents boundaries), solid models are mathematically watertight, enabling CSG operations, mass property calculations, and manufacturing simulation.

## Representations

- **Constructive Solid Geometry (CSG)** — shapes built from boolean operations on primitives
- **Boundary Representation (B-rep)** — surfaces defined by topological elements (faces, edges, vertices)
- **Functional Representation (F-Rep)** — shapes as mathematical functions f(x,y,z) → zero level set
- **Voxel/SDF representation** — discretized signed distance fields on a grid

## Related Concepts

- [[functional-representation-solid-modeling]] — F-Rep approach to solid modeling
- [[cad]] — computer-aided design using solid modeling techniques
- [[mesh-generation]] — converting solid representations to polygonal meshes
- [[libfive]] — F-Rep solid modeling infrastructure
- [[openscad]] — script-based CSG solid modeler
