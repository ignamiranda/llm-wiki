---
title: "Creaking Gorge and The Cauldron"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [game-development, vr, unity, shader, level-design]
summary: "Development of two new Eye of the Temple areas — Creaking Gorge (vertical non-linear cliff area) and The Cauldron (lava-themed with custom world-space shader and fire propagation puzzles)."
source_url: "https://blog.runevision.com/2018/09/creaking-gorge-and-cauldron.html"
---

# Creaking Gorge and The Cauldron

## Summary
Development of two new Eye of the Temple areas — Creaking Gorge (vertical non-linear cliff area) and The Cauldron (lava-themed with custom world-space shader and fire propagation puzzles).

## Content
Two new areas developed for Eye of the Temple, a room-scale VR game. Creaking Gorge is a vertical non-linear level built around cliffs and platforms. The design leverages room-scale VR's natural spatial affordances, letting players navigate vertically by climbing and stepping between physical-platform-aligned geometry. The area's non-linearity means players can approach objectives from multiple angles, with multiple paths through the gorge.

The Cauldron is a lava-themed area centered on a custom world-space shader technique for lava rendering. Rather than using standard UV-based texture mapping, the shader performs texture lookups in world space, creating a consistent lava surface appearance regardless of mesh geometry. This allows lava to flow naturally across uneven terrain without visible seams or UV distortion.

Fire propagation serves as the area's core puzzle mechanic. Fire spreads between connected elements — when one flammable object ignites, nearby connected objects catch fire in sequence. Players must manipulate this propagation chain to solve puzzles, creating a mechanic where spatial adjacency and connectivity determine puzzle state changes.

## Key Takeaways
- World-space texture lookups for lava shader rendering
- Fire propagation as a puzzle mechanic in VR
- Vertical non-linear level design in a room-scale VR context

## Related
- [[rune-skovbo-johansen]] — author
