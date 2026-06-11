---
title: "Infinigen Indoors — Photorealistic Indoor Scenes using Procedural Generation"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, indoor-scenes, blender, infinigen, procedural-modeling, cvpr]
summary: "Raistrick et al. (CVPR 2024) present Infinigen Indoors, a Blender-based procedural generator for photorealistic indoor scenes with constraint-based arrangement."
source_url: "https://arxiv.org/abs/2406.11824"
---

# Infinigen Indoors — Photorealistic Indoor Scenes using Procedural Generation

## Summary

Raistrick et al. (CVPR 2024) extend the [[infinigen-procedural-scenes]] ecosystem with Infinigen Indoors, a Blender-based procedural generator of photorealistic indoor scenes. It introduces indoor assets (furniture, architectural elements, appliances) and a constraint-based arrangement system with a domain-specific language for specifying room layouts. Open source under BSD license.

## Content

Infinigen Indoors addresses the gap in photorealistic indoor scene generation by extending the outdoor-focused [[infinigen-procedural-scenes]] with:

- **Indoor asset generators**: Furniture (tables, chairs, shelves, beds, cabinets), architectural elements (walls, floors, doors, windows), appliances (refrigerators, ovens, sinks)
- **Constraint-based arrangement system**: A domain-specific language for specifying spatial relationships and layout rules
- **Room type specialization**: Generators tuned for bedrooms, kitchens, living rooms, bathrooms, etc.
- **Photorealism**: Leverages Blender's Cycles renderer with physically based materials and lighting

The constraint system uses a declarative approach where users specify high-level layout constraints (e.g., "bed against wall," "table near window") which the solver arranges procedurally.

Accepted at CVPR 2024. Open source under BSD license.

## Key Takeaways

- Extends Infinigen from outdoor natural scenes to indoor environments
- Constraint-based arrangement DSL for room layout specification
- Photorealistic rendering quality with Blender Cycles
- CVPR 2024 publication
- BSD open source license

## Related

- [[infinigen-procedural-scenes]] — parent ecosystem, originally focused on natural outdoor scenes
- [[2025-05-15-infinigen-articulated]] — articulated assets, complementary to indoor static assets
- [[procfunclib]] — ProcFunc provides higher-level abstraction for similar Blender generators
- [[2023-11-16-graphical-asset-generation-survey]] — survey context for indoor scene PCG
- [[alexander-raistrick]] — first author
