---
title: "Procedural Creature Progress 2021–2024"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, game-development, animation, creatures, the-big-forest]
summary: "Rune's progress on procedural mammal generation (503 low-level params→106 high-level params) and procedural animation for The Big Forest, including gradient descent silhouette fitting, inverse kinematics overhaul, and reference animation analysis."
source_url: "https://blog.runevision.com/2025/01/procedural-creature-progress-2021-2024.html"
---

# Procedural Creature Progress 2021–2024

## Summary
Rune's progress on procedural mammal generation (503 low-level params→106 high-level params) and procedural animation for The Big Forest, including gradient descent silhouette fitting, inverse kinematics overhaul, and reference animation analysis.

## Content

The procedural creature model system began with extruded rectangle primitives and grew to 11 example creatures built through automatic extraction from skinned reference meshes. An early attempt at PCA-based parametrization failed — while PCA reduced dimensionality, the resulting parameters were not semantically meaningful, making it impossible to deliberately tweak creature anatomy in intuitive ways.

The breakthrough came from shifting to manually designed high-level parameters that control 503 low-level parameters through a structured mapping. To accelerate example creation, Rune built a gradient descent fitting tool: it compares a procedural model's silhouette against a reference 3D mesh's silhouette from multiple angles using signed distance fields (SDFs), then minimizes the silhouette difference to automatically find parameter values that match the reference. This makes it practical to create new creature examples without manual parameter tweaking.

On the animation side, the system uses an FK/IK kinematic approach with no physics simulation, inherited from the 2009 Locomotion System. Rune analyzed reference animation data by plotting foot lift height against stride distance, revealing gait patterns that informed improved leg timing. The IK algorithm was overhauled to handle foot rotation internally rather than as a post-process, producing more natural foot placement on uneven terrain. The result is a substantial improvement over the original system, though creature animation remains a work in progress.

## Key Takeaways
- 503 low-level → 106 high-level parameters for creature anatomy
- PCA failed to produce meaningful parameters
- Gradient descent + SDF silhouette fitting accelerates example creation
- Reference animation analysis reveals gait patterns (foot lift vs stride distance)
- IK overhaul with integrated foot rotation

## Related
- [[rune-skovbo-johansen]] — author
- [[procedural-creature-generation]] — new concept
- [[procedural-animation-locomotion-system]] — new concept
- [[silhouette-gradient-descent-fitting]] — new concept
