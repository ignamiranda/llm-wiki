---
title: "Silhouette Gradient Descent Fitting"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, optimization, 3d-modeling]
aliases: []
summary: "A technique using gradient descent optimization with signed distance field (SDF) silhouette comparison to fit procedural model parameters to match reference 3D meshes."
---

# Silhouette Gradient Descent Fitting

## Definition

Method: capture silhouettes of a reference model from multiple angles once, then at each gradient descent step compare procedural model silhouettes against the reference using SDF-based distance measurement. The penalty function sums SDF distances at border pixels across all angles. Used by Rune Skovbo Johansen to fit procedural creature parameters to animal reference models, particularly effective for leg and neck lengths. The Adam optimizer did not perform as well as basic gradient descent.

## Key Properties

- Multi-angle silhouette comparison
- SDF-based distance measurement for smooth gradients
- Works with implicit parameter spaces (no training data needed)
- May not capture fine details (ears, horns)

## Related Concepts

- [[rune-skovbo-johansen]] — author
- [[procedural-creature-generation]] — application context

## References

- Source: runevision blog
