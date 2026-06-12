---
title: "2024 Retrospective"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [game-development, procedural-generation, retrospective]
summary: "Yearly reflection: LayerProcGen released as open source, The Cluster finally released after 21 years, progress on The Big Forest's procedural creatures, and music releases."
source_url: "https://blog.runevision.com/2025/01/2024-retrospective.html"
---

# 2024 Retrospective

## Summary

Two of four yearly goals accomplished: LayerProcGen released as open source in May 2024, and The Cluster finally saw release after 21 years. Terrain generation saw major performance improvements through the Burst compiler. Work on procedural creatures for The Big Forest occupied the latter half of the year. The Fractal Dithering technique presentation slipped to January 2025.

## Content

LayerProcGen was released as open source in May 2024, with community ports quickly emerging — Sythelux Rikd created a Godot port and Oli Scherer contributed a Rust port. The Cluster was released for free on Itch.io after 21 years of on-and-off development, marking a major milestone.

Terrain generation work yielded significant technical progress. The Burst compiler provided a dramatic speedup for procedural generation. Multi-resolution terrain chunks were implemented with a skirt-based solution to eliminate LOD cracks, solving a long-standing visual artifact problem.

Procedural creature generation for The Big Forest became the primary focus in the second half of 2024, building on the terrain systems developed earlier. The Fractal Dithering technique, intended for a conference presentation, was not completed in time but was delivered in January 2025.

Additional accomplishments included scanning 42 pages of childhood paper game drawings as archival material, and receiving a brief mention in a Game Maker's Toolkit video.

## Key Takeaways

- LayerProcGen ported to Godot by Sythelux Rikd, Rust by Oli Scherer
- Multi-resolution terrain chunks with skirt-based crack fixing
- Burst compiler radically sped up terrain generation

## Related

- [[rune-skovbo-johansen]] — author
- [[layerprocgen]] — released open source
- [[procedural-creature-generation]] — progress
