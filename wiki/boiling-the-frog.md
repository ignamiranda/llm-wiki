---
title: "Boiling the Frog"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, narrative-generation, game-design, frostpunk, ethics]
aliases: []
summary: "A gradual normalization design pattern where incrementally escalating moral compromises appear as logical conclusions — used in Frostpunk to explore authoritarianism."
source_hash: "3B5A43067F4CBC72968D6E3AE05A66867AE9CE3FE498D4E94ED5E2897FD82F26"
---

# Boiling the Frog

## Definition

Boiling the Frog, articulated by Fijak and Stokalski of 11 Bit Studios in Chapter 19, is a design pattern where morally escalating choices are presented incrementally so that each step appears as a reasonable, almost inevitable response to circumstances. The pattern is named for the metaphor of a frog that will jump out of boiling water but stays in water that is gradually heated to boiling.

## Key Properties

- **Gradual law progression**: laws and policies are unlocked in sequence, each one slightly more extreme than the last, so no single step feels outrageous
- **Maslovian hierarchy for AI agents**: NPC needs are modelled in a hierarchy — survival first, then comfort, then social needs — creating natural justification for authoritarian policies
- **Hope vs discontent as 2D emotional space**: player manages two axes of population sentiment rather than a single morale bar, enabling nuanced trade-offs
- **Post-play reflection**: the endlog asks "Was it worth it?" — forcing players to confront the cumulative moral cost of their incremental decisions

## Examples

- **Frostpunk** — the progression from "Emergency Shift" (overtime) to "Extended Shifts" (14-hour days) to "Child Labour" to "Prison" to "New Order" (totalitarian police state), each step a rational response to the previous crisis
- **Papers, Please** — similarly gradual normalisation of authoritarian border control policies

## Related Concepts

- [[ethical-procedural-generation]] — ethical considerations in generator design that make such patterns possible

## References

- [[2019-01-01-procedural-storytelling-in-game-design]] — source (Chapter 19, Fijak & Stokalski)
