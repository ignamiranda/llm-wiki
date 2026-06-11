---
title: "Contradiction Winnowing"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, game-design, procedural-characters, state-of-decay-2]
aliases: []
summary: "A tag-based system for generating believable procedural characters by progressively eliminating conflicting trait combinations — used in State of Decay 2."
source_hash: "3B5A43067F4CBC72968D6E3AE05A66867AE9CE3FE498D4E94ED5E2897FD82F26"
---

# Contradiction Winnowing

## Definition

Contradiction winnowing, described by Card, Tjernø, and Bozarth in Chapter 22 (State of Decay 2), is a tag-based character generation technique that produces believable procedural characters by progressively eliminating conflicting trait combinations. Instead of generating a character and checking validity, the system builds the character from a constraint-satisfaction perspective, narrowing the possibility space at each step.

## Key Properties

- **Trait tag system with mutual exclusion rules**: each trait carries tags that define which other traits it is compatible with
- **Hierarchical tag tree**: traits are organised in a hierarchy where parent tags enforce constraints on all children
- **Applies to all character features**: the constraint system governs not just personality traits but appearance, backstory, skills, and voice lines
- **Constraining last choice can cause dead-end failures**: if the final trait to assign has no valid options given previous choices, the generation must restart or backtrack

## Examples

- **State of Decay 2** survivor generation — characters with the "Veteran" tag cannot be paired with "Coward"; a character who "Lost a Loved One" cannot also have "Large Family" (contradictory backstories)
- **Dwarf Fortress** personality generation — analogous constraint systems that prevent a dwarf from being both "utterly content" and "enraged"

## Related Concepts

- [[dramatic-play]] — character generation feeds into dramatic role-playing opportunities
- [[procedural-storytelling]] — the broader narrative context for character generation

## References

- [[2019-01-01-procedural-storytelling-in-game-design]] — source (Chapter 22, Card, Tjernø & Bozarth)
