---
title: "Procedural Descriptions Filter Stack"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
source_hash: "3B5A43067F4CBC72968D6E3AE05A66867AE9CE3FE498D4E94ED5E2897FD82F26"
tags: [procedural-generation, procedural-storytelling, narrative-generation, game-design, text-generation]
aliases: []
summary: "A filter-based architecture for procedural text generation that negotiates between a grammar and a world model to balance the oatmeal problem and the brutalist building problem."
---

# Procedural Descriptions Filter Stack

## Definition

Bruno Dias's filter-based architecture for procedural text generation, used in *Voyageur*. The system negotiates between a grammar (what can be said) and a world model (what is true) through a stack of filters that transform, select, and polish generated descriptions.

## Key Properties

- **Filter stack** — A pipeline of filters: mismatch → dryness → full bonus → unmentioned → tweak → lensing → bias, each handling a specific transformation
- **Salience scoring and culling** — Not all generated details are included; the system scores items by relevance and discards low-salience content
- **Reincorporation vs seeded model** — The system can seed generation with specific details to ensure earlier events are referenced later
- **Guardrails / hardcoded tweaks** — Rare but important phrases are hardcoded to prevent the grammar from producing nonsensical output for edge cases

## Examples

In *Voyageur*, the player travels between procedurally generated planets. Each planet's description is built through the filter stack, combining world-model facts (atmosphere, life forms, resources) with grammatical templates and filtered through salience and style.

## Related Concepts

- [[10k-bowls-of-oatmeal-problem]] — The filter stack addresses the oatmeal problem (generating endless bland variations)
- [[procedural-storytelling]] — Procedural descriptions support procedural storytelling

## References

- [[2019-01-01-procedural-storytelling-in-game-design]] — source, Chapter 16 by Bruno Dias
