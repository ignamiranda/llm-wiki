---
title: "Generative Methods Taxonomy"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, generative-methods, game-design, procedural-storytelling]
aliases: []
summary: "Kate Compton's classification of six fundamental approaches to building procedural generators: distribution, parametric, tile-based, grammars, constraint solvers, and agents/simulations."
source_hash: "3B5A43067F4CBC72968D6E3AE05A66867AE9CE3FE498D4E94ED5E2897FD82F26"
---

# Generative Methods Taxonomy

## Definition

The generative methods taxonomy, introduced by Dr. Kate Compton in Chapter 1, classifies procedural generators into six fundamental approaches. Each method represents a different way to encode creative possibility space into algorithmic rules, ranging from simple weighted randomness to complex multi-agent simulations.

## Key Properties

- **Distribution**: weighted randomness, deck shuffling, and probability tables — the simplest approach, often surprisingly effective
- **Parametric**: numerical tweaks along defined axes — adjusting sliders for hill height, river width, tree density
- **Tile-based**: modular chunks assembled in combinations — hand-authored building blocks that fit together (e.g., tile maps)
- **Grammars**: recursive expansion rules — starting from a seed symbol and repeatedly applying replacement rules (e.g., Tracery)
- **Constraint solvers**: brute force or AI search — define what valid output looks like and search for solutions (e.g., Wave Function Collapse)
- **Agents/Simulations**: steering behaviours, boids, genetic algorithms, cellular automata — emergent results from many small entities following local rules

## Examples

- **Tracery** (Compton) — grammar-based generation for story and dialog
- **Spore** — agents/simulation for creature movement and ecosystem behaviour
- **Diablo** loot system — distribution-based rarity tables
- **Spelunky** — tile-based level chunk assembly
- **Wave Function Collapse** — constraint solver for image and level generation

## Related Concepts

- [[artist-in-a-box]] — an approach that often combines multiple methods to simulate human artistry
- [[10k-bowls-of-oatmeal-problem]] — a key pitfall regardless of which method is chosen
- [[tracery]] — a popular grammar-based generator in this taxonomy

## References

- [[2019-01-01-procedural-storytelling-in-game-design]] — source (Chapter 1, Dr. Kate Compton)
