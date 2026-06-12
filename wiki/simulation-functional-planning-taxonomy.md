---
title: "Simulation, Functional and Planning Approaches to Procedural Generation"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, taxonomy, world-generation]
aliases: []
summary: "A three-part taxonomy of procedural world generation approaches: simulation (process-based), functional (mathematical), and planning (top-down design)."
---

# Simulation, Functional and Planning Approaches to Procedural Generation

## Definition

Three distinct approaches to procedural world generation: (1) **Simulation** — physical or biological process simulation (erosion, cellular automata), produces the most natural results but is expensive and hard to chunk. (2) **Functional** — pure mathematical functions (Perlin noise, FBM), fastest and most chunk-friendly but provides no topological guarantees. (3) **Planning** — top-down level design (guaranteeing paths, connections, traversability), guarantees gameplay-relevant properties but is more complex. These approaches can be combined hierarchically.

## Key Properties

- Simulation: emergent, natural, expensive, hard to chunk
- Functional: mathematical, fast, chunkable, no guarantees
- Planning: top-down, guaranteed properties, design-driven

## Related Concepts

- [[planning-approach-procgen]] — existing concept
- [[functional-approach-procgen]] — existing concept
- [[generative-methods-taxonomy]] — broader taxonomy

## References

- Source: runevision blog
