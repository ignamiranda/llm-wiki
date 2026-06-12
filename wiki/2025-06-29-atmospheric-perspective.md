---
title: "Notes on Atmospheric Perspective and Distant Mountains"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [graphics, game-development, atmospheric-scattering, rendering, fog]
summary: "Observations from Japan on how distant mountains transition from deep blue to pale blue with distance, limitations of single-color fog in games, and resources for physically-based atmospheric scattering."
source_url: "https://blog.runevision.com/2025/06/notes-on-atmospheric-perspective-and.html"
---

# Notes on Atmospheric Perspective and Distant Mountains

## Summary
Observations from Japan on how distant mountains transition from deep blue to pale blue with distance, limitations of single-color fog in games, and resources for physically-based atmospheric scattering.

## Content
Field observations of Rayleigh and Mie scattering in Japan form the basis of this article. The key visual insight is that mountains transition from deep blue in mid-distance to pale, desaturated blue in the far distance — the same phenomenon that makes the horizon paler than the sky directly overhead. This occurs because there is progressively more air between the viewer and each receding mountain layer, scattering more short-wavelength (blue) light into the view path.

The article critiques the common game development trick of using single-color fog to simulate atmospheric perspective. A single fog color cannot accurately represent this depth-dependent color shift because distant objects do not uniformly approach a single fog color — they first become deep blue, then fade toward pale blue. The approximation breaks down noticeably in scenes with multiple depth layers of terrain.

Several resources for physically-based atmospheric scattering are discussed. Inigo Quilez's per-channel fog technique uses different density exponents for each color channel, producing a more convincing approximation. Unreal Engine's Sky Atmosphere Component and Unity HDRP's Physically Based Sky provide full physically based solutions. Bruneton and Neyret's Precomputed Atmospheric Scattering paper remains the canonical reference for real-time atmospheric rendering.

## Key Takeaways
- Atmospheric scattering causes mountains to go from deep blue to pale blue with distance, not towards a single color
- The fog trick (single-color fog) cannot accurately represent this
- Per-channel fog with different exponents can approximate it
- Physically based solutions exist in Unreal (Sky Atmosphere) and Unity HDRP

## Related
- [[rune-skovbo-johansen]] — author
