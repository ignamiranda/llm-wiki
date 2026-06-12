---
title: "Slope Penalty Pathfinding"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, pathfinding, terrain, a-star]
aliases: []
summary: "A pathfinding technique using non-linear slope penalties to generate natural-looking winding paths across terrain, avoiding steep shortcuts."
---

# Slope Penalty Pathfinding

## Definition

A modification of A* pathfinding on implicit coordinate graphs where the cost of traversing a slope is squared rather than linear. This prevents the pathfinder from taking steep shortcuts and produces human-like paths that follow terrain contours. Uses 16-direction movement for smooth path angles. A parameter study shows power values of 2.0–3.0 produce natural results depending on terrain characteristics. Implemented in the LayerProcGen framework.

## Key Properties

- Non-linear slope cost (squared)
- Implicit graph (no stored graph structure)
- 16-direction movement
- Produces paths that follow contours like human trails

## Related Concepts

- [[layerprocgen]] — implementing framework
- [[rune-skovbo-johansen]] — author

## References

- Source: runevision blog
