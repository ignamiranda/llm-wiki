---
title: "Houdini Procedural Asset Pipeline"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, houdini, procedural-modeling, game-assets]
aliases: [houdini-pdg-pipeline, PDG-pipeline]
summary: "A Houdini-based automated pipeline for procedural game asset generation, using PDG to orchestrate geometry generation, texturing, and UV unwrapping across multiple tools."
---

# Houdini Procedural Asset Pipeline

## Definition

A Houdini-based automated pipeline for generating procedural game assets, centered on the Procedural Dependency Graph (PDG) introduced in Houdini 17. PDG orchestrates geometry generation in Houdini, procedural texturing via Substance Designer (using the Substance Automation Toolkit), and UV unwrapping through RizomUV — all within a single dependency-driven graph that can execute in parallel across multiple machines or threads.

## Key Properties

- **PDG (Procedural Dependency Graph)** — a task-graph system for defining pipeline workflows; nodes represent work items (geometry generation, texture baking, exporting) connected by data dependencies
- **Cross-tool orchestration** — PDG can launch external processes, enabling integration of Substance Automation Toolkit (headless Substance Designer) and RizomUV (command-line UV unwrapping)
- **Parallel execution** — work items can run across multiple threads or network-rendered across a farm, similar to render-farm workflows
- **Parametric variation** — Houdini's native proceduralism generates infinite controlled variations of base assets (e.g., rocks, cliffs) through exposed parameters
- **COPs limited to baking** — Houdini's Compositing Operators are used only for baking texture maps (normal, curvature, position, bent normal) as input to Substance Designer, not for full texturing

## Examples

- Gatis Kurzemnieks' rock/cliff generation pipeline: Houdini generates rock geometry → COPs bake surface maps → Substance Designer generates final textures → RizomUV unwraps → PDG exports to Unity
- Large-scale natural environment generation with hundreds of unique rock formations
- Automated asset variant generation for game levels (different art directions, LODs, or biome variations)

## Related Concepts

- [[blender-geometry-nodes]] — comparable node-based procedural modeling system, but without PDG-level pipeline orchestration
- [[unity-procedural-mesh-resources]] — Unity ecosystem for code-driven procedural generation, complementary to Houdini's DCC-based approach
- [[2019-12-12-houdini-procedural-assets]] — Tutorial series documenting this pipeline in practice
- [[gatis-kurzemnieks]] — Creator of the documented pipeline implementation

## References

- [Creating procedural game assets with Houdini — Part 1](https://www.rendereverything.com/game_assets_with_houdini_1/) by Gatis Kurzemnieks
