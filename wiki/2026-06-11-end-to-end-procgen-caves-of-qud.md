---
title: "End-to-End Procedural Generation in Caves of Qud"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, caves-of-qud, freehold-games, game-development, chunk-based-generation, gdc]
summary: "Jason Grinblat and Brian Butler present an architectural case study for composing multiple procedural generation techniques into large-scale generative systems, using Caves of Qud's village generation as an example."
source_url: "https://www.youtube.com/watch?v=jV-DZqdKlnE"
source_hash: "79DA2A87EDF2D0D098B184A248FDC91A3438F24AEACB5E753C0408A0E11FFC55"
---

# End-to-End Procedural Generation in Caves of Qud

## Summary

In this GDC talk, [[jason-grinblat]] and [[brian-butler]] walk through the architecture of Caves of Qud's large-scale procedural generation systems. They frame the problem as "how do you compose multiple procgen techniques to build large-scale generative systems?" — something beyond looking up a single algorithm tutorial. The case study focuses on village generation, showing how noise, L-systems, Markov chains, WFC, and grammar-based generation are composed into a unified pipeline.

## Content

The talk is structured around the design and implementation of Caves of Qud's village generation system. Key architectural patterns include:

- **Chunky procgen**: Dividing generation into discrete composable chunks rather than monolithic algorithms
- **Technique composition**: Combining noise maps for terrain, L-systems for vegetation, WFC for buildings, Markov chains for names, and replacement grammars for history
- **Village-as-system**: Each village is the product of multiple interacting generation passes rather than a single algorithm
- **Design context first**: Understanding what the generated content needs to communicate before choosing techniques

The talk covers the full pipeline from high-level design decisions down to implementation details, with live demos of the generation system in action.

## Key Takeaways

- Large-scale procedural generation is primarily an *architectural* challenge, not an algorithmic one
- Compose techniques rather than finding a single "magic bullet" algorithm
- Design context should drive technique selection
- Chunky decomposition makes complex generative systems tractable

## Related

- [[caves-of-qud]] — game discussed
- [[jason-grinblat]] — co-presenter
- [[brian-butler]] — co-presenter
- [[2026-06-11-wfc-map-gen-caves-of-qud]] — related talk on WFC map generation in Caves of Qud
- [[2026-06-11-procedurally-generating-history-caves-of-qud]] — related talk on history generation
- [[procedural-generation]] — broader topic
- [[wave-function-collapse]] — one technique used in the pipeline
