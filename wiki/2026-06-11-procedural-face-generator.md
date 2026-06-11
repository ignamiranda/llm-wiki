---
title: "Procedural Face Generator"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, computer-graphics, faces, parameterization, red-blob-games]
summary: "Amit Patel's experimental procedural face generator using a five-dimensional hypercube parameter space for cartoon face expressions, inspired by Scott McCloud's Making Comics."
source_url: "https://www.redblobgames.com/x/1845-face-generator/"
source_hash: "3e66b66a16b7b85bb882e69c687b50f41c3c9e018a4dbb1d1a1c876448912aba"
---

# Procedural Face Generator

## Summary
An experimental tool for procedurally generating simple cartoon faces using a five-dimensional hypercube parameter space. Started in 2011 (ActionScript/Flash) and ported to JavaScript/Canvas in 2015, with a 2018 update. The mouth shape parameters (m, p, q, r, s) produce a variety of expressions with the constraint m+p+q ≥ 0.

## Parameter Space
- **Mouth**: Five parameters forming a hypercube with one constraint
- **Asymmetry**: (skew, rotate) parameters for asymmetric mouth shapes
- **Eyebrows**: (browLift, browAngle) controls

## Influences
- Scott McCloud's Making Comics (expression interpolation, page 85)
- Nicky Case's Parable of the Polygons
- Red Blob Games logo face (since 1987)

## Related
- [[procedural-face-generation]] — Core concept
- [[amit-patel]] — Author
