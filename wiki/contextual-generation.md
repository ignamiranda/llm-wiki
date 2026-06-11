---
title: "Contextual Generation"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, determinism, chunk-boundaries]
aliases: [contextual procedural generation]
summary: "Procedural generation where operations produce seamless results across chunk boundaries while remaining deterministic."
---

# Contextual Generation

## Definition

Contextual generation means having two traits simultaneously: (1) determinism — the same chunk always generates the same result regardless of generation order, and (2) integrity — the output of chunks is continuous and seamless, as if all chunks had been generated simultaneously. In [[layer-based-procedural-generation]], this is achieved by supplying chunks with sufficient context from lower layers through padding.

## Key Properties

- Enables operations that cross chunk boundaries: blurring, point relaxation, pathfinding
- Determinism achieved through strict input/output separation between layers
- Integrity achieved through effect distance and padding — each chunk gets context beyond its own bounds
- The "owned within bounds" pattern resolves ownership of overlap areas

## Examples

- Natural-looking paths generated via pathfinding that seamlessly cross chunk boundaries
- Distance relaxation between random points in neighboring chunks
- Kernel-based filters (blurring) applied across chunk boundaries
- In [[layerprocgen]], a CultivationLayer can pathfind across multiple chunks because it collects terrain data from GeoGridLayer with padding

## Related Concepts

- [[deterministic-generation]] — the determinism half of contextual generation
- [[effect-distance-and-padding]] — mechanism for providing context beyond chunk bounds
- [[owned-within-bounds]] — disambiguating ownership of cross-chunk data
- [[layer-based-procedural-generation]] — the architecture that enables contextual generation

## References

- LayerProcGen documentation: Contextual Generation
