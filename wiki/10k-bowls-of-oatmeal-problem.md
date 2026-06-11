---
title: "10,000 Bowls of Oatmeal Problem"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, game-design, procedural-storytelling]
aliases: [bowls-of-oatmeal-problem, oatmeal-problem]
summary: "The phenomenon where mathematically unique procedural content feels perceptually identical — mathematical uniqueness does not equal perceptual uniqueness."
source_hash: "3B5A43067F4CBC72968D6E3AE05A66867AE9CE3FE498D4E94ED5E2897FD82F26"
---

# 10,000 Bowls of Oatmeal Problem

## Definition

The 10,000 Bowls of Oatmeal Problem, named by Kate Compton (Chapter 1) and explored further by Bruno Dias (Chapter 16), describes the phenomenon where a procedural generator produces mathematically unique outputs that all feel perceptually identical. It is the gap between *variety* (statistical uniqueness) and *diversity* (perceptual distinctiveness).

## Key Properties

- **Mathematical uniqueness ≠ perceptual uniqueness**: two outputs may differ in measurable ways while feeling like the same thing to a human
- **Scarcity of meaningful axes**: many generators create variety along shallow dimensions that don't change the felt experience
- **Amplified by grammars**: grammar-based generators (like Tracery) are especially prone because recursive rules produce surface variation without deep difference
- **Requires qualitative authoring**: solving the problem requires curating meaningful dimensions of variation rather than maximising raw output count

## Examples

- **Diablo's "new gaming experience every time"** — the marketing promise versus the reality of similar-feeling dungeon layouts
- **Borderlands' "17.5 million guns"** — statistical uniqueness in weapon stats that players perceive as the same few archetypes
- **Tracery poetry generation** — where every generated poem uses the same syntactic structure with different vocabulary fill-ins

## Related Concepts

- [[generative-methods-taxonomy]] — understanding which methods are most prone to the oatmeal problem
- [[procedural-descriptions-filter-stack]] — a technique for increasing perceptual diversity

## References

- [[2019-01-01-procedural-storytelling-in-game-design]] — source (Chapters 1 and 16)
