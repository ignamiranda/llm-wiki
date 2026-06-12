---
title: "Face-Weighted Normals"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [graphics, 3d-modeling, vertex-normals, rendering]
aliases: []
summary: "A technique for calculating vertex normals by averaging the normals of adjacent faces weighted by each face's surface area, producing smooth beveled edges while preserving flat surfaces."
---

# Face-Weighted Normals

## Definition

Vertex normals computed as a weighted average of adjacent face normals, with weights proportional to face area (area-weighted) or face angle (angle-weighted). The area-weighted approach naturally produces smoother transitions at bevels and prevents artifacts at T-junctions.

## Key Properties

- Weights each face's contribution by its surface area
- Preserves hard edges via threshold angle
- Implementable as asset post-processing pipeline

## Related Concepts

- [[mesh-generation]] — related
- [[rune-skovbo-johansen]] — author

## References

- Source: runevision blog
