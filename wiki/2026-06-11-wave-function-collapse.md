---
title: Wave Function Collapse
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, constraint-satisfaction, texture-synthesis, algorithm]
summary: "An overview of the Wave Function Collapse algorithm \u2014 a constraint-based\
  \ texture synthesis method that generates locally similar outputs from example bitmaps,\
  \ popularized by Maxim Gumin's reference implementation."
source_url: https://github.com/mxgmn/WaveFunctionCollapse
source_hash: f3136128c2e9c51b7e695f8991730c2bde81f30f31bdf5d8fff36bd3fa7f5d3b
---


# Wave Function Collapse

## Summary

Wave Function Collapse (WFC) is a constraint-based texture synthesis algorithm that generates images locally similar to a given input bitmap. Inspired by quantum mechanics (specifically wave function collapse), it initializes the output in a superposition of all possible states and iteratively collapses regions into definite states while propagating adjacency constraints. The algorithm was popularized by Maxim Gumin's (mxgmn) open-source reference implementation, has been ported to dozens of languages and engines, and is widely used for procedural level generation in games.

## Content

### The Algorithm

WFC takes an input bitmap and produces an output that is locally similar, meaning:

- **(C1)** The output contains only NxN patterns of pixels present in the input.
- **(Weak C2)** The distribution of NxN patterns in the output approximates the distribution in the input.

The algorithm initializes the output in a completely unobserved state — each pixel value is in a superposition of all colors from the input, with real-number coefficients. It then enters the **observation-propagation cycle**:

1. **Observation**: The NxN region with the lowest Shannon entropy is selected and collapsed into a definite state according to its coefficients and the input pattern distribution.
2. **Propagation**: Information from the collapse propagates through the output using constraint propagation (AC-4 algorithm), reducing the set of possible patterns for neighboring regions.

The cycle repeats until all regions reach a definite state (success) or a contradiction occurs (all coefficients for a pixel become zero). Since the problem of determining whether a bitmap allows nontrivial satisfying bitmaps is NP-hard, contradictions cannot be entirely avoided, but they occur surprisingly rarely in practice.

### Two Models

WFC has two primary modes:

- **Overlapping Model**: Extracts NxN pixel patterns from the input and uses them as the basis for superposition states. Typical N=3.
- **Simple Tiled Model**: Uses pre-defined tiles with adjacency constraints instead of pixel patterns. The simplest case is NxN=1x2, equivalent to adjacency constraint propagation. Tiles are classified by symmetry type under the dihedral group D4 to shorten adjacency enumeration.

### Applications

WFC has been adopted across game development, graphics, and research:

- **Games**: Level generation in [[caves-of-qud]] (first commercial use, see [[2026-06-11-wfc-map-gen-caves-of-qud]]), Bad North, Dead Static Drive, Townscaper, and many smaller titles
- **3D Synthesis**: Voxel model generation using 5x5x5 and 5x5x2 blocks
- **Constrained Synthesis**: WFC supports user-specified constraints, enabling autocomplete of partially constructed levels
- **Research**: Papers on backtracking strategies, alternative heuristics, combination with VQ-VAE, information hiding in textures, and learning from positive/negative examples

### Related Work

WFC builds on prior work in texture synthesis and constraint satisfaction:

- **Texture Synthesis by Non-parametric Sampling** (Efros & Leung, 1999) — the broader field WFC belongs to
- **Model Synthesis** (Merrell, 2009) — adjacency constraints from example models, which WFC generalizes
- **AC-4** (Mohr & Henderson, 1986) — constraint propagation algorithm used in WFC
- **ConvChain** (mxgmn) — complementary algorithm that satisfies strong C2 but not C1
- **MarkovJunior** (mxgmn) — 3D simple tiled model with extensive tilesets

### Implementations

The reference implementation is C#/.NET. Notable ports include: C++ (fast-wfc), Python, Rust, Kotlin, Go, Java, Julia, JavaScript, Dart, Haxe, Clojure. Engine integrations exist for Unity, Unreal Engine 5, Godot 4, and Houdini.

## Key Takeaways

- WFC is a constraint-based (not noise/function-based) approach to procedural generation
- The algorithm is inherently NP-hard but practical for most use cases
- Two modes: overlapping model (pixel patterns) and simple tiled model (tile adjacencies)
- Widely adopted in game development for level generation, especially for tile-based games
- Supports constraints, enabling mixed-initiative design and integration with other generators

## Related

- [[wave-function-collapse]] — core concept definition
- [[overlapping-model-wfc]] — pixel pattern mode
- [[simple-tiled-model]] — tile adjacency mode
- [[entropy-heuristic-wfc]] — observation selection heuristic
- [[observation-propagation-cycle]] — core algorithm loop
- [[constraint-propagation-ac4]] — propagation algorithm
- [[model-synthesis]] — prior art by Paul Merrell
- [[maxim-gumin]] — creator of the reference implementation
- [[oskar-stalberg]] — Townscaper, Bad North, irregular grid WFC
- [[boris-the-brave]] — DeBroglie library, chiseling method
- [[layer-based-procedural-generation]] — alternative paradigm (contrast)
