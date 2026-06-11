---
title: "Procedural Generation of Articulated Simulation-Ready Assets — Infinigen-Articulated"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, articulated-assets, robotics-simulation, blender, infinigen, procedural-modeling]
summary: "Joshi et al. (2025) introduce Infinigen-Articulated — a Blender-based toolkit for procedurally generating articulated assets across 18 categories for robotics simulation."
source_url: "https://arxiv.org/abs/2505.10755"
---

# Procedural Generation of Articulated Simulation-Ready Assets — Infinigen-Articulated

## Summary

Joshi et al. (2025) introduce Infinigen-Articulated, a procedural generation toolkit built on [[infinigen-procedural-scenes]] for creating articulated (jointed) assets for robotics simulation. It covers 18 common articulated object categories with Blender-based generators and a pipeline for exporting to robotics simulators.

## Content

Infinigen-Articulated extends the [[infinigen-procedural-scenes]] ecosystem to address the robotics simulation need for articulated assets — objects with movable parts (drawers, doors, hinges, joints). Most procedural generation systems produce static geometry; this system generates fully rigged, simulation-ready articulated objects.

Key features:
- **18 categories** including cabinets, drawers, doors, laptops, scissors, pliers, and other common articulated mechanisms
- **Blender-based generation** using geometry nodes and Python scripting
- **Constraint system** for valid articulation ranges and joint limits
- **Export pipeline** to multiple robotics simulators (MuJoCo, Isaac Sim, PyBullet)
- **Randomized parameters** for visual and geometric variation within categories

The toolkit is designed to bridge the sim-to-real gap by providing diverse, procedurally generated articulated assets for training and evaluating robotic manipulation policies.

## Key Takeaways

- First systematic procedural generator for articulated (non-static) assets
- 18 categories of articulated objects with full joint rigging
- Integrates with the [[infinigen-procedural-scenes]] ecosystem
- Export to major robotics simulators
- Addresses the static-asset limitation of prior PCG work

## Related

- [[infinigen-procedural-scenes]] — parent ecosystem
- [[2024-06-17-infinigen-indoors]] — indoor scenes, complementary asset domain
- [[procfunclib]] — ProcFunc provides abstraction layer for similar Blender generators
- [[2023-11-16-graphical-asset-generation-survey]] — survey identifies the gap this fills
- [[alexander-raistrick]] — co-author, also leads Infinigen Indoors and ProcFunc
- [[karhan-kayan]] — co-author, contributed articulated asset generators
