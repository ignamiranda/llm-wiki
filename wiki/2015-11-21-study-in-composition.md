---
title: "A Study in Composition"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, graphics, l-systems, color-palette, art]
summary: "A procedural generation jam entry creating landscape compositions that evoke different moods through L-system trees, HSV color palettes, and cinematographic camera cuts."
source_url: "https://blog.runevision.com/2015/11/a-study-in-composition.html"
---

# A Study in Composition

## Summary
A procedural generation jam entry creating landscape compositions that evoke different moods through L-system trees, HSV color palettes, and cinematographic camera cuts.

## Content
Created as an entry for the Exile Game Jam and the Procedural Generation Jam, this project generates landscape compositions intended to evoke specific moods. L-systems drive procedural tree generation, creating varied tree morphologies from a small set of production rules. Tree placement uses multi-frequency noise to produce natural-looking distribution patterns — higher-frequency noise creates local clusters while lower-frequency noise controls broader density variation across the landscape.

Color palettes are generated in HSV space using complementary and triad color schemes to establish mood. The HSV approach allows intuitive control over hue relationships while varying saturation and value independently, producing cohesive palette families from simple seed parameters. Warm palettes evoke sunset or autumn moods; cool palettes evoke serene or melancholic atmospheres.

The presentation layer includes automatic camera cuts that follow cinematographic principles — varying shot distances, angles, and compositions to create a cinematic sequence rather than a static render. The source code was released under the MIT license. The project was a collaboration with Morten Nobel-Jørgensen, Andreas Frostholm, and Tim Garbos.

## Key Takeaways
- L-systems for procedural tree generation
- HSV color palettes (complementary/triad) for mood setting
- Multi-frequency noise for organic tree distribution
- Automatic camera cuts for cinematic presentation

## Related
- [[rune-skovbo-johansen]] — author
