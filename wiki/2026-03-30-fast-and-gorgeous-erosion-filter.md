---
title: "Fast and Gorgeous Erosion Filter — Rune Skovbo Johansen (2026)"
type: article
language: en
created: 2026-03-30
modified: 2026-06-11
tags: [procedural-generation, terrain, erosion, noise, shadertoy, directional-noise]
source_url: "https://blog.runevision.com/2026/03/fast-and-gorgeous-erosion-filter.html"
source_hash: "98524c25a93c23bc1c62a8cfdadc4ab61059f0ccfde490c8ed8f2f292ab76e6d"
summary: "Rune Skovbo Johansen presents a non-simulated erosion filter technique that produces branching gullies and ridges via gradient-aligned stripe noise, with improvements over the original technique by Clay John and Fewes."
---

# Fast and Gorgeous Erosion Filter — Rune Skovbo Johansen (2026)

## Summary

A blog post and companion YouTube video by [[rune-skovbo-johansen]] describing a non-simulated terrain erosion filter technique. The technique produces branching gullies and ridges using a special kind of directional noise where every point can be evaluated in isolation — making it fast, GPU-friendly, and trivial to generate in chunks. The post covers the original technique by [[clay-john]] (2018), its refinement by [[felix-westin|Felix Westin (Fewes)]] (2023), and Johansen's own significant evolutions (2025-2026) including stacked fading, normalized gullies, and straight gullies.

## Content

### Background

In 2018, [[clay-john|Clay John]] posted a Shadertoy called *Eroded Terrain Noise* — a noise function that looked like eroded terrain with branching structure, runnable in a single-pass pixel shader. In 2023, [[felix-westin|Felix Westin (Fewes)]] posted a refined version with improved presentation. Johansen's work (2025-2026) addresses derivative inconsistencies, adds intuitive parameters, and introduces several new techniques.

### The Basic Idea

Given a height function with gradient (direction and steepness of steepest ascent), stripes are added along the gradient direction to produce gullies and ridges. The sides of these gullies add their own gradients, enabling multi-octave layering where smaller gullies branch at angles from larger ones.

Generating gradient-aligned stripes requires dividing the pattern into cells, each with its own pivot point, and blending neighboring cells' stripes together. The stripes are extruded sine waves; blending unaligned sine waves produces a new sine wave with smaller amplitude.

### Peaks and Valleys

Two approaches handle the problem of zero-gradient at peaks and valleys:

- **Frequency approach** (original): Stripe frequency is proportional to slope — stripes become infinitely thick at zero slope, so peaks/valleys always land on ridges. Produces bulges at valleys.
- **Fade approach** (Johansen's innovation): Stripe widths stay consistent but stripes fade out where steepness approaches zero, fading towards a target value that transitions from black at valleys to white at peaks.

### Derivate Correction

Johansen found that the original technique had multiple derivative inconsistencies (missing frequency-rule and amplitude-rule corrections) that mostly cancelled out at default parameters but made the technique fragile when parameters were changed. Fixing these made the technique more predictable and usable with intuitive parameters like `EROSION_SCALE` and `EROSION_SLOPE_POWER`.

### Stacked Fading

Each octave updates the fade target and mask to prevent smaller gullies from appearing on ridges/creases of larger gullies. The combi-mask restricts subsequent octaves to steeper slopes, controlled by a detail parameter.

### Normalized Gullies

Since cosine/sine pairs from blended cell stripes can be treated as points on a unit circle, the interpolated result can be normalized back to radius 1 for consistent gully magnitude. Partial normalization (threshold at 0.5) avoids spiky artifacts.

### Straight Gullies

By faking the gully slope as a sign function (as if gullies were extruded triangle waves rather than sine waves), smaller gullies branch cleanly from larger ones instead of curling at the ends. The resulting discontinuities are fully faded away by the mask.

### Ridge Map and Water Drainage

The fade target doubles as a ridge map — ridges and creases in white/black. This enables drawing dendritic drainage lines at the bottom of gullies, though unbroken lines are not guaranteed.

### Edge Rounding

Separate controls for rounding of ridges and creases, achieved by chaining a variable-size ease-in function onto the mask shaping function.

## Key Takeaways

- Non-simulated erosion filter that evaluates each point in isolation — fast, GPU-friendly, chunk-friendly
- Three evolutions: Clay John (2018 original), Fewes (2023 visual polish), Johansen (2025-2026 fundamental improvements)
- Key techniques: stacked fading, normalized gullies, straight gullies, Phacelle Noise extraction
- Code released under Mozilla Public License v2

## Related

- [[erosion-filter-technique]] — the core technique
- [[phacelle-noise]] — directional noise extracted from the filter
- [[clay-john]] — original creator of the eroded terrain noise
- [[felix-westin]] — refined the technique visually
- [[rune-skovbo-johansen]] — author of this article and significant improvements
- [[layerprocgen]] — another procedural generation framework by the same author
