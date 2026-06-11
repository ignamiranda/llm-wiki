---
title: "Narrative Momentum"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, narrative-generation, procedural-storytelling, game-design, ink, narrative-design]
aliases: []
summary: "The feeling that things are always happening and progressing in a story — defined as importance × rate of change — achieved through architectural principles like Only Forwards Design and knowledge modelling."
source_hash: "3B5A43067F4CBC72968D6E3AE05A66867AE9CE3FE498D4E94ED5E2897FD82F26"
---

# Narrative Momentum

## Definition

Narrative momentum, defined by Jon Ingold of inkle in Chapter 7, is the feeling that things are always happening and progressing in a story. Ingold formalises it as a product of *importance* × *rate of change* — a story event must matter to the player and the rate of meaningful change must be sustained. Momentum is achieved through architectural principles in the Ink scripting language rather than through content volume.

## Key Properties

- **Only Forwards Design**: narrative structure that prevents backtracking and revisiting past choices, forcing constant forward movement
- **Weave Structure**: always-dropping-downwards flow of narrative knots and stitches, preventing the player from retreating to earlier story states
- **Knowledge as acyclic directed graph**: player knowledge is modelled as a DAG where acquiring new information opens new branches but never allows returning to prior states of ignorance
- **Rule One (continuity)** and **Rule Two (momentum)**: two architectural rules that together ensure the story feels coherent and perpetually progressing

## Examples

- **80 Days** (inkle) — globe-trotting narrative where each city visit generates unique events and the clock never stops
- **Heaven's Vault** (inkle) — archaeological narrative where discovered knowledge permanently changes available dialog and cannot be undiscovered
- **Overboard!** (inkle) — detective story where every conversation moves the timeline forward and locks off missed opportunities

## Related Concepts

- [[only-forwards-design]] — the core architectural principle behind narrative momentum
- [[procedural-storytelling]] — the broader context of algorithmic narrative
- [[ink-weave-structure]] — the specific Ink implementation of momentum-preserving narrative flow

## References

- [[2019-01-01-procedural-storytelling-in-game-design]] — source (Chapter 7, Jon Ingold)
