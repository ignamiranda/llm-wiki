---
title: "Blender Geometry Nodes"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, blender, geometry-nodes, procedural-modeling]
aliases: [geometry-nodes, GN]
summary: "A node-based system in Blender for procedural and non-destructive geometry creation and modification, integrated since Blender 3.0."
---

# Blender Geometry Nodes

## Definition

Geometry Nodes is a visual node-graph system integrated into Blender (3.0+) for procedural and non-destructive modeling. It allows creating, modifying, and combining geometry through a node-based interface without writing code, providing an alternative to traditional modifier stacks and scripting workflows.

## Key Properties

- **Node-based visual programming** — geometry flows through a directed acyclic graph of operations
- **Non-destructive workflow** — the original geometry is never modified; the node graph defines a live procedural operation
- **Fields** — lazy-evaluated functions on geometry domains (points, faces, edges) enabling per-element variation
- **Attributes** — named data layers on geometry (position, normal, custom float/vector/color data) that can be read and written
- **Instances** — efficient reuse of geometry references without duplication, supporting instance-level attributes
- **Baking** — stores geometry node evaluation results to disk, decoupling the result from the node tree
- **Node-based tools** — Geometry Node trees can be registered as tools in the 3D viewport, extending Blender's tool system with procedural logic

## Examples

- Procedural terrain generation with noise-based height displacement
- Parametric building generation (windows, walls, roofs driven by input parameters)
- Scatter objects (trees, rocks) on a surface using density masks
- Procedural plant/vegetation generation
- Custom modifiers for complex deformations (twist, taper, bend)

## Related Concepts

- [[houdini-procedural-asset-pipeline|Houdini]] — comparable node-based procedural system, but with PDG pipeline automation and broader industry adoption in game asset pipelines
- [[unity-procedural-mesh-resources]] — Unity ecosystem for procedural mesh generation (code-based rather than node-based)
- [[wave-function-collapse]] — constraint-based procedural technique that can be used alongside or as input to Geometry Nodes

## References

- [Blender Geometry Nodes Manual](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/index.html)
