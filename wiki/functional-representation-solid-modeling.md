---
title: "Functional Representation (F-Rep) Solid Modeling"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [solid-modeling, functional-representation, mesh-generation, procedural-modeling, computational-geometry]
aliases: [f-rep, f-rep-solid-modeling, functional-representation]
summary: "A solid modeling paradigm where 3D shapes are represented as mathematical functions f(x,y,z) rather than boundary representations, enabling watertight, manifold, hierarchical, and feature-preserving mesh generation."
---

# Functional Representation (F-Rep) Solid Modeling

## Definition

Functional Representation (F-Rep) is a solid modeling paradigm where 3D shapes are defined by mathematical functions f(x,y,z). The surface of the shape is the implicit surface where f(x,y,z) = 0 — the zero level set. Points where f(x,y,z) < 0 are inside the solid; points where f(x,y,z) > 0 are outside. F-rep unifies shape definition, transforms, and CSG operations under a single mathematical framework, enabling evaluation at arbitrary points without storing explicit geometry.

## Key Properties

- Shapes are functions, not meshes — infinite resolution in principle
- Surface is the zero level set of f(x,y,z)
- CSG operations become simple mathematical combinations: union = min(f,g), intersection = max(f,g), difference = max(f,-g)
- Transforms are function composition: move = f(x-dx, y-dy, z-dz)
- Produces watertight, manifold meshes when evaluated
- Hierarchical evaluation enables adaptive refinement
- Feature-preserving — sharp edges can be retained
- Well-suited for CAD, animation, and scientific visualization

## Examples

Basic shape definitions:
- Sphere: `f(x,y,z) = x² + y² + z² - r²`
- Box: `f(x,y,z) = max(|x|-w, |y|-h, |z|-d)`
- Cylinder: `f(x,y,z) = max(√(x²+z²) - r, |y| - h)`

libfive implements this paradigm as a practical modeling system — see [[libfive]].

## Related Concepts

- [[libfive]] — the primary practical implementation of f-rep solid modeling
- [[openscad]] — CSG/B-rep based modeling, a contrasting paradigm
- [[ilmola-generator]] — parametric mesh generation, a different approach to geometry creation
- [[mesh-generation]] — extracting discrete meshes from continuous representations
- [[solid-modeling]] — the broader field of computational solid geometry
- [[matthew-keeter]] — creator of the libfive f-rep system

## References

- [libfive: Functional Representation](https://libfive.com/)
- Pasko, A., et al. "Function representation in geometric modeling: concepts, implementation and applications." The Visual Computer (1995).
- [Matthew Keeter's blog on f-rep](https://www.mattkeeter.com/projects/)
