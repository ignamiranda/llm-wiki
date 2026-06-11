---
title: "ghx_proc_gen"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [wfc, wave-function-collapse, rust, bevy, procedural-generation, model-synthesis]
aliases: []
summary: "A Rust library for 2D & 3D procedural generation with Model Synthesis/WFC using AC-4 constraint propagation, available for the Bevy engine."
source_url: "https://github.com/Henauxg/ghx_proc_gen"
source_hash: "8D4E29C3DDAE0A3A8C4E7B076E321CB85695BE092CE4F451261F78F78906CF22"
---

# ghx_proc_gen

## Definition

ghx_proc_gen is a Rust library for 2D and 3D procedural generation using Model Synthesis (also known as Wave Function Collapse), created by Gilles Henaux. It uses an AC-4 constraint solver and is designed for grid-based generation (terrain, structures). It integrates with the Bevy engine via the bevy_ghx_proc_gen crate.

## Key Properties

- AC-4 constraint propagation algorithm
- 2D (Cartesian2D) and 3D (Cartesian3D) grid support
- Socket-based adjacency constraint system
- Automatic model rotation variations
- Grid loop/wrapping on any axis
- Observer pattern for incremental generation
- Interactive generation via set_and_propagate
- Cargo features: models-names, debug-traces, bevy, reflect
- Dual-licensed MIT/Apache-2.0, 154 GitHub stars

## Examples

- Chessboard pattern generation (quickstart)
- Unicode terrain display in terminal
- Bevy examples: pillars, tile-layers, canyon with animated windmills

## Related Concepts

- [[debroglie]] — C# WFC library cited as inspiration
- [[fast-wfc]] — performance WFC in C++
- [[2026-06-11-wfc-implementations-survey]] — surveyed in the WFC survey article
- [[noise-based-terrain-generation]] — related procgen technique

## References

- https://github.com/Henauxg/ghx_proc_gen
- https://docs.rs/ghx_proc_gen