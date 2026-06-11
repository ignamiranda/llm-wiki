---
title: "OpenSCAD — The Programmers Solid 3D CAD Modeller"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [cad, procedural-modeling, solid-modeling, openscad, 3d-modeling]
aliases: [openscad]
summary: "A free software application for creating solid 3D CAD objects through script-based modeling, available on Linux, Windows, and macOS."
source_url: "https://openscad.org/"
---

# OpenSCAD — The Programmers Solid 3D CAD Modeller

## Definition

OpenSCAD is a free software application for creating solid 3D CAD models using a declarative script-based approach. Unlike interactive modelers, OpenSCAD treats the model as a program — the user writes code describing geometric operations, and the application compiles it into a 3D shape. It is particularly popular in the open-source hardware, 3D printing, and maker communities.

## Key Properties

- Script-based (declarative) modeling language — models are defined as programs
- Constructive Solid Geometry (CSG) operations: union, difference, intersection
- Primitive shapes: cube, sphere, cylinder, polyhedron
- 2D-to-3D extrusion: linear_extrude, rotate_extrude
- Transformation operations: translate, rotate, scale, mirror, color
- Import/export: STL, OFF, DXF, SVG, CSG, AMF, 3MF
- Cross-platform: Linux, Windows, macOS
- Extensible via custom libraries and modules
- Large ecosystem of community-contributed libraries (e.g., BOSL2, MCAD)

## Examples

```openscad
// A simple gear-like shape
difference() {
    cylinder(r=10, h=5);
    for (i = [0:5]) {
        rotate([0, 0, i * 60])
            translate([7, 0, 0])
                cylinder(r=2, h=5);
    }
}
```

## Related Concepts

- [[libfive]] — functional representation (f-rep) approach to solid modeling, an alternative to CSG/B-rep
- [[ilmola-generator]] — mesh primitive generation library, lower-level than OpenSCAD
- [[functional-representation-solid-modeling]] — the mathematical paradigm behind libfive
- [[solid-modeling]] — the broader domain of computational solid geometry
- [[cad]] — computer-aided design, the application domain

## References

- [OpenSCAD Homepage](https://openscad.org/)
- [GitHub Repository](https://github.com/openscad/openscad)
- [OpenSCAD Documentation](https://en.wikibooks.org/wiki/OpenSCAD_User_Manual)
