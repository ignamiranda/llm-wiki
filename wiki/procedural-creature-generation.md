---
title: "Procedural Creature Generation"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, game-development, animation, creatures]
aliases: []
summary: "The algorithmic generation of quadruped mammal anatomies using parametrized bone structures and extruded rectangle geometry, developed by Rune Skovbo Johansen for The Big Forest."
---

# Procedural Creature Generation

## Definition

An approach to generating forest creatures (foxes, bears, deer, etc.) with plausible anatomy using a multi-segment extruded rectangle system. 503 low-level parameters (bone lengths, rotations, thicknesses) reduced to 106 high-level parameters (bulkiness, tallness, head length, etc.). Gradient descent silhouette fitting accelerates example creature creation. A failed PCA approach demonstrated that automated parametrization does not produce meaningful parameters. Requires further refinement — random parameter values still produce invalid creatures.

## Key Properties

- Extruded rectangle mesh representation
- 106 high-level parameters control 503 low-level parameters
- Manual parametrization required (PCA and ML do not produce meaningful parameters)
- Gradient descent silhouette fitting assists example creation

## Related Concepts

- [[rune-skovbo-johansen]] — author
- [[silhouette-gradient-descent-fitting]] — supporting technique

## References

- Source: runevision blog
