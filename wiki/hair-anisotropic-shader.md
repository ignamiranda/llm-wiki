---
title: "Anisotropic Hair Shader"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [graphics, shader, hair-rendering, unity]
aliases: []
summary: "A hair shading technique that simulates anisotropic reflection from cylindrical hair strands by multisampling the BRDF with cosine-weighted normal distribution."
---

# Anisotropic Hair Shader

## Definition

A technique for simulating anisotropic shading on surfaces made of many parallel cylinders (hair). Three variants: full multisample (50 BRDF samples per pixel with weighted normal fan), specular multisample (partial sampling), and approximation (emulates result without brute force). The weight function is the product of the cosine of the angle between original and modified normal (occlusion) times the cosine of the angle between modified normal and view (visibility). Based on Unity's Standard PBR shading model for lighting consistency.

## Key Properties

- Multisampled BRDF with cosine-weighted normal fan
- Preserves Unity Standard shader lighting consistency
- Weight function models strand occlusion and visibility
- Open source implementation

## Related Concepts

- [[rune-skovbo-johansen]] — author

## References

- Source: runevision blog
