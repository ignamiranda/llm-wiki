---
title: "Procedural History in Caves of Qud — Jason Grinblat at Roguelike Celebration"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, caves-of-qud, history-generation, narrative-generation, sultan, roguelike-celebration, jason-grinblat]
summary: "Jason Grinblat's Roguelike Celebration talk on Caves of Qud's procedural history system, structured around five generated sultan histories, covering history-driven world generation and design constraints."
source_url: "https://www.youtube.com/watch?v=ClGAApZYIvI"
source_hash: "7D8F18AE25DD4384337154EDF3102FEBA1BAF96AC1C067EA58182CDDBB76892B"
---

# Procedural History in Caves of Qud — Jason Grinblat at Roguelike Celebration

## Summary

[[jason-grinblat]] presents at Roguelike Celebration on Caves of Qud's procedural history system. The talk is structured around five generated sultan histories from different playthroughs, showing how the history system feeds into world generation — shrines, holy sites, and locations from the generated history are instantiated as explorable places in the game world.

## Content

The talk covers Caves of Qud's approach to making generated history feel authentic and embedded:

- **Sultan system**: The history is centered around sultans — ancient leaders with archetypal epithets and domains (e.g., "Sultan of Rust", "Sultan of Glass"). Each sultan has a domain that influences the kinds of events and locations generated
- **History-driven world generation**: Locations mentioned in generated history (shrines, tombs, hermitages) are physically instantiated in the game world as explorable places, creating a direct link between lore and gameplay
- **Replacement grammars**: Text generation using context-free grammars that produce varied prose from structured historical data
- **Design constraints**: Limiting the historical scope to sultan dynasties focuses the generation and makes output manageable
- **Apophenia as feature**: The fragmentary, biased nature of generated histories encourages players to fill gaps with their own interpretation

## Key Takeaways

- Generated history becomes more compelling when it physically manifests in the game world
- Centering history around specific entity types (sultans) provides structure for generation
- Fragmentary, biased histories encourage player interpretation and engagement
- The design constraint of "sultan-centric history" makes generation tractable while producing rich results

## Related

- [[historical-rationalization]] — core technique
- [[jason-grinblat]] — presenter
- [[caves-of-qud]] — game discussed
- [[2026-06-11-procedurally-generating-history-caves-of-qud]] — related GDC talk
- [[2026-06-11-end-to-end-procgen-caves-of-qud]] — broader architecture talk
