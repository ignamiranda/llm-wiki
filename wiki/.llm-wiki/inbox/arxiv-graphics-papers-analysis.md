---
title: "Analysis of arXiv Papers on Procedural Graphics Asset Generation"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, game-assets, computer-graphics, procedural-modeling, systematic-review]
aliases: []
summary: "Analysis of four recent arXiv papers covering procedural graphical asset generation from systematic review through Infinigen ecosystem to ProcFunc library."
---

# Analysis of arXiv Papers on Procedural Graphics Asset Generation

## Source 1: arXiv:2311.10129 — Intelligent Generation of Graphical Game Assets

**Authors:** Kaisei Fukaya, Damon Daylamani-Zad, Harry Agius (Nov 2023)

**Type:** Systematic literature review (200 papers)

**Key contributions:**
- Systematic review of 200 papers on procedural generation of graphical game assets
- Covers clouds, buildings, vegetation, terrains, water, textures
- Proposes a conceptual framework for PCG asset generation
- Taxonomizes approaches by asset type, generation technique, evaluation method

**Relevance:** Provides a broad landscape view of the field that the other three papers build upon.

---

## Source 2: arXiv:2505.10755 — Infinigen-Articulated

**Authors:** Abhishek Joshi et al. (15 co-authors, May 2025)

**Type:** Toolkit/System paper

**Key contributions:**
- Infinigen-Articulated: toolkit for procedurally generated articulated assets
- 18 common articulated object categories
- Blender-based generators with export pipeline to robotics simulators
- Targets robotics simulation gap — most PCG assets are static

**Relevance:** Extends [[infinigen-procedural-scenes]] into articulated/robotics domain.

---

## Source 3: arXiv:2406.11824 — Infinigen Indoors

**Authors:** Alexander Raistrick et al. (12 co-authors, CVPR 2024)

**Type:** System paper (CVPR 2024)

**Key contributions:**
- Infinigen Indoors: Blender-based procedural generator for indoor scenes
- Extends [[infinigen-procedural-scenes]] with indoor assets (furniture, architecture, appliances)
- Constraint-based arrangement system with domain-specific language
- Open source under BSD license

**Relevance:** Bridges natural scenes (original Infinigen) to indoor environments.

---

## Source 4: arXiv:2604.26943 — ProcFunc

**Authors:** Alexander Raistrick et al. (11 co-authors, Apr 2026)

**Type:** Library/Tool paper

**Key contributions:**
- [[procfunclib]]: Python library for Blender-based procedural 3D generation
- Streamlines creating, combining, analyzing procedural generation code
- VLMs can use it for code editing
- New indoor room generator included

**Relevance:** Provides a higher-level abstraction layer for building procedural generators in Blender.

---

## Cross-Cutting Themes

| Theme | Papers | Notes |
|-------|--------|-------|
| Blender as platform | 2, 3, 4 | All systems use Blender as the generation engine |
| Procedural asset pipeline | 1, 2, 3, 4 | From survey to specific implementations |
| Robotics simulation | 2 | Articulated assets for robotics |
| Indoor/outdoor | 3 | Extending outdoor PCG to indoor |
| Code-level abstraction | 4 | Making PCG more accessible to VLMs and humans |

## New Tags to Register

- `articulated-assets` — procedural generation of objects with joints/articulation
- `indoor-scenes` — procedural generation of indoor environments
- `robotics-simulation` — assets or scenes for robotics simulators
- `3d-generation` — general 3D procedural content generation
- `infinigen` — the Infinigen procedural generation ecosystem
- `blender` — Blender-based generation tools
- `systematic-review` — literature survey papers
- `game-assets` — graphical game asset generation
- `procedural-modeling` — 3D procedural modeling techniques
- `cvpr` — CVPR conference publications

## Related Wiki Pages to Create

- [[2023-11-16-graphical-asset-generation-survey]] — Fukaya review
- [[2025-05-15-infinigen-articulated]] — Joshi Infinigen-Articulated
- [[2024-06-17-infinigen-indoors]] — Raistrick Infinigen Indoors
- [[2026-04-29-procfunc]] — Raistrick ProcFunc
- [[infinigen-procedural-scenes]] — Infinigen umbrella concept
- [[procfunclib]] — ProcFunc library concept
- Person pages for key authors
