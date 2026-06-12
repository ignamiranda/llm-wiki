---
title: "I Made a Hair Shader"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [graphics, unity, shader, hair-rendering]
summary: "Three implementations of an anisotropic hair shader for Unity — full multisample, specular multisample, and approximation — using cosine-weighted BRDF sampling without special meshes or textures."
source_url: "https://blog.runevision.com/2025/10/i-made-hair-shader.html"
---

# I Made a Hair Shader

## Summary
Three implementations of an anisotropic hair shader for Unity — full multisample, specular multisample, and approximation — using cosine-weighted BRDF sampling without special meshes or textures.

## Content
The article presents anisotropic hair shading for Unity that works on standard sphere and capsule primitives with only a simple normal map, requiring no special hair mesh geometry or custom textures. The core insight is that hair anisotropy can be simulated by spreading surface normals across a 180-degree fan oriented along the hair direction, then evaluating the standard BRDF across these spread normals.

The full multisample variant runs Unity's PBR BRDF up to 50 times per pixel, with each sample using a slightly perturbed normal. The weight function combines the cosine of the modified normal angle with the cosine of the view angle, producing a natural anisotropic highlight that follows hair strands. The specular multisample variant applies the same technique only to the specular component, reducing cost while preserving the anisotropic specular appearance.

The approximation variant emulates the multisampled result without brute-force oversampling, deriving a closed-form expression that mimics the integrated BRDF across the normal fan. This makes it suitable for mobile or performance-constrained scenarios. The shader modifies Unity's Standard shading model, adding anisotropy parameters while keeping the familiar PBR workflow.

The implementation is open source on GitHub at github.com/runevision/HairShader. The technique draws inspiration from Thorsten Scheuermann's Hair Rendering paper (SIGGRAPH 2004) and earlier work on anisotropic BRDF approximation.

## Key Takeaways
- Three variants: full multisample, specular multisample, approximation
- Weight function uses product of two cosines for natural anisotropic appearance
- Open source release at github.com/runevision/HairShader
- Uses Unity's Standard shading model modified for anisotropy

## Related
- [[rune-skovbo-johansen]] — author
