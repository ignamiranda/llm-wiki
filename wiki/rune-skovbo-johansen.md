---
title: "Rune Skovbo Johansen"
type: person
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, game-development, unity, erosion, noise, shadertoy, vr, animation]
aliases: [runevision]
summary: "Creator of the LayerProcGen framework and erosion filter technique; indie game developer behind Eye of the Temple, The Cluster, and The Big Forest."
---

# Rune Skovbo Johansen

## Bio

Rune Skovbo Johansen (also known as runevision) is a game developer and creator of the LayerProcGen framework for layer-based infinite procedural generation. He shipped the VR game Eye of the Temple (2021, PCVR and Quest 2), released The Cluster (2024) after 21 years of on-and-off development, and is working on The Big Forest. He worked at Unity Technologies from 2008–2020 (company grew from ~20 to 3000+). His work focuses on enabling contextual, deterministic procedural generation in infinite game worlds, particularly using the planning approach rather than the purely functional approach common in sandbox-style games.

## Key Contributions

- Created [[layerprocgen]] — an open-source C# framework for layer-based procedural generation
- Published research and techniques on natural path generation through terrain using cost-based pathfinding
- Demonstrated top-down planning in infinite worlds through the game The Cluster
- Developed the [[erosion-filter-technique]] — a non-simulated terrain erosion filter using gradient-aligned stripe noise (2025-2026)
- Extracted [[phacelle-noise]] — a standalone directional noise function from the erosion filter (2026)
- Developed semi-procedural [[procedural-animation-locomotion-system]] for character locomotion (Master's thesis 2009, GDC 2009 lecture)
- Created [[procedural-creature-generation]] system with gradient descent silhouette fitting for The Big Forest
- Built [[puzzlegraph]] — an open-source puzzle state space visualization tool
- Created procedural [[hair-anisotropic-shader]] for Unity, released as open source
- Developed a [[face-weighted-normals]] vertex normal calculation technique for automatic smooth edges
- Published game design analysis on [[game-progression-dependency-graph]]s and designing for mystery
- Competed in Google AI Challenge (ants), ranked 22nd worldwide

## Related Work

- [[layerprocgen]] — primary creation
- [[layer-based-procedural-generation]] — the core methodology advanced by his work
- [[contextual-generation]] — key concept in his framework
- [[erosion-filter-technique]] — non-simulated erosion filter
- [[phacelle-noise]] — directional noise extracted from erosion filter
- [[2026-03-30-fast-and-gorgeous-erosion-filter]] — companion article and video
- [[procedural-animation-locomotion-system]] — semi-procedural animation system
- [[procedural-creature-generation]] — procedural mammal generation
- [[silhouette-gradient-descent-fitting]] — fitting procedural models to references
- [[puzzlegraph]] — puzzle state space visualization
- [[hair-anisotropic-shader]] — hair rendering technique
- [[face-weighted-normals]] — vertex normal calculation
- [[game-progression-dependency-graph]] — procedural progression design
- [[slope-penalty-pathfinding]] — natural path generation
- [[amit-patel]] — fellow tutorial author on procedural generation techniques

## Links

- [GitHub: runevision](https://github.com/runevision)
- [Blog: Rune Vision](https://blog.runevision.com/)
- [The Cluster](https://runevision.com/multimedia/thecluster/)
- [The Big Forest](https://runevision.com/multimedia/thebigforest/)
