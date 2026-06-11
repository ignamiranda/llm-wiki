---
title: "Procedural Dialog"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
source_hash: "3B5A43067F4CBC72968D6E3AE05A66867AE9CE3FE498D4E94ED5E2897FD82F26"
tags: [procedural-generation, procedural-storytelling, narrative-generation, dialog-systems, game-development]
aliases: []
summary: "A rule-matching dialog engine where increasingly specific rules override general ones, powered by a unified context dictionary of all game state — used in Left 4 Dead."
---

# Procedural Dialog

## Definition

Elan Ruskin's procedural dialog system for Left 4 Dead uses a rule-matching engine where increasingly specific rules override general ones, powered by a unified context dictionary containing all game state. The system enables characters to comment on nearly any situation with contextually appropriate dialog.

## Key Properties

- **Rule-matching with most-specific wins** — General dialog rules are overridden by more specific ones when their conditions are met
- **Context dictionary** — A flat key-value store of all game state that rules query against
- **Character memory** — Persistent state that enables running gags and callbacks across a session
- **Follow-up events** — Characters can respond to each other's lines, creating natural-feeling repartee
- **Additive design** — New rules are added without removing old ones; specificity naturally suppresses outdated lines

## Examples

In Left 4 Dead, characters comment on specific zombies, player actions, level events, and each other's behavior. Running gags emerge from the memory system — a character might reference something said earlier in the campaign.

## Related Concepts

- [[procedural-storytelling]] — Procedural dialog is a form of procedural storytelling

## References

- [[2019-01-01-procedural-storytelling-in-game-design]] — source, Chapter 25 by Elan Ruskin
