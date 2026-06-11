---
title: "Procedurally Generating History in Caves of Qud"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, caves-of-qud, history-generation, narrative-generation, replacement-grammar, gdc, jason-grinblat]
summary: "Jason Grinblat's GDC talk on Caves of Qud's procedural history generation system — covering historical entities, replacement grammars for text, causality, and narrative coherence."
source_url: "https://www.youtube.com/watch?v=H0sLa1y3BW4"
source_hash: "72D6E0D6937A4C2A8CE8A2DAC2D96AB8F257995B777205CB54AF0F50E87ED62E"
---

# Procedurally Generating History in Caves of Qud

## Summary

[[jason-grinblat]] presents Caves of Qud's procedural history generation system at GDC. The talk covers the model of historical entities (people, places, events), replacement grammars for text generation, techniques for causality and narrative coherence, and how generated histories create the game's distinctive lore that feels ancient and mythic.

## Content

The talk begins by defining history as "a continuous systematic narrative of past events relating to a particular people, country, period, person, etc." and then translates this into a generative model:

- **Historical entities model**: The system models entities (factions, sultans, locations, artifacts) and the relationships between them
- **Replacement grammars for text**: Context-free grammars that generate descriptive text from structured historical data, producing prose that varies while preserving underlying facts
- **Causality and coherence**: Ensuring generated histories maintain narrative cause-and-effect — events reference prior events, creating the illusion of a continuous timeline
- **Gospel generation**: Texts are generated with deliberate bias and interpretative gaps, making them feel like in-universe historical accounts rather than omniscient chronicles

The talk shows examples of generated sultan histories, shrine inscriptions, and faction histories that players discover while exploring the world.

## Key Takeaways

- Procedural history generation requires modeling entities and their relationships first, then generating text from that structure
- Replacement grammars provide a powerful middle ground between templating and full NLG
- Narrative coherence emerges from causal chains between generated events
- Historical bias and gaps make generated histories feel more authentic

## Related

- [[historical-rationalization]] — core technique for Caves of Qud's history generation
- [[jason-grinblat]] — presenter
- [[caves-of-qud]] — game discussed
- [[2026-06-11-jason-grinblat-procedural-history-caves-of-qud]] — related talk at Roguelike Celebration
- [[2026-06-11-end-to-end-procgen-caves-of-qud]] — broader architecture talk
