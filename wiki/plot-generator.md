---
title: "Plot Generator"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, narrative-generation, game-design, storytelling, plot]
aliases: [plot generation, automated plot, story generator]
summary: "An algorithmic system that generates narrative plots — sequences of causally or thematically connected events — as opposed to generating individual quests, dialog, or character personalities in isolation."
---

# Plot Generator

## Definition

A plot generator is a system that algorithmically produces narrative plots — structured sequences of events with causal, temporal, or thematic relationships. Unlike quest generators (which produce individual missions with goals and rewards) or dialog systems (which produce lines of character speech), plot generators aim to create the overarching narrative architecture: what happens, to whom, in what order, and why.

## Key Properties

- Generates event sequences, not isolated content
- Requires causal or thematic coherence between events
- Can operate at different levels of abstraction (high-level plot beats vs. detailed event sequences)
- Often combines with other systems (character generation, dialog, world simulation) to produce complete narratives
- Related to but distinct from quest generation (quests are player-facing goals; plots are narrative structures)

## Examples

- **Plot generation via planning** — using automated planning (e.g., STRIPS/PDDL) to generate event sequences satisfying narrative goals
- **Grammar-based plot generation** — using BNF grammars or Tracery to generate plot structures from templates
- **Tarot-based plot generation** — using tarot card spreads as plot structure templates (Ch 26 of Short & Adams 2019)
- **Dwarf Fortress legends mode** — generates world histories as an emergent byproduct of simulation, not from a dedicated plot generator

## Related Concepts

- [[procedural-storytelling]] — broader field
- [[procedural-quest-generation]] — related but distinct (quests vs. plots)
- [[emergent-narrative]] — contrasting approach (bottom-up vs. top-down plot generation)
- [[conan-quest-generator]] — planning-based narrative generation
- [[procedural-quest-generation]] — grammar-based quest generation

## References

- Short, T. X. & Adams, T. (Eds.). (2019). *Procedural Storytelling in Game Design*. CRC Press. — Chapter 23: Plot Generators
