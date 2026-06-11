---
title: "Overlapping Model (WFC)"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, texture-synthesis, wfc]
summary: "A WFC mode where NxN pixel patterns are extracted from the input bitmap and used as the basis for superposition states, enabling synthesis directly from example images."
---

# Overlapping Model (WFC)

## Definition

The overlapping model is one of two primary modes of the Wave Function Collapse algorithm. It extracts all NxN patterns of pixels from the input bitmap and uses them to define the superposition states of each region in the output. Each element of the output "wave" represents a superposition of these patterns with boolean coefficients, where a false coefficient means the pattern is forbidden and true means it is not yet forbidden.

## Key Properties

- Directly works from example images without manual tile definition
- Typical pattern size is N=3
- Pattern data can be augmented with rotations and reflections
- The output wave element state is a superposition of NxN patterns (boolean coefficients), while pixel states are superpositions of colors (real coefficients)
- Contradictions arise when all patterns for a region become forbidden
- The model can be augmented with additional heuristics (height, density, curvature) for higher-dimensional synthesis

## Examples

- Generating brick wall textures from a small sample
- Synthesizing pixel art level segments from example tilesets
- 3D voxel generation using 5x5x5 and 5x5x2 block patterns

## Related Concepts

- [[wave-function-collapse]] — the parent algorithm
- [[simple-tiled-model]] — the alternative WFC mode
- [[entropy-heuristic-wfc]] — observation selection
- [[observation-propagation-cycle]] — core loop

## References

- Maxim Gumin, "WaveFunctionCollapse" — https://github.com/mxgmn/WaveFunctionCollapse
