---
title: "Only Forwards Design"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
source_hash: "3B5A43067F4CBC72968D6E3AE05A66867AE9CE3FE498D4E94ED5E2897FD82F26"
tags: [procedural-generation, procedural-storytelling, narrative-generation, game-design, ink]
aliases: []
summary: "An architectural principle that prevents backtracking and dangling narrative loose ends at the system level — built into the Ink narrative language."
---

# Only Forwards Design

## Definition

Jon Ingold's architectural principle for interactive narrative that prevents backtracking and dangling narrative loose ends at the system level. Built into the Ink narrative language, it ensures that once a player passes a narrative point, they cannot return to alter it — eliminating the combinatorial explosion of branching narrative.

## Key Properties

- **Prevents backtracking architecturally** — The system simply does not allow the player to return to previous states
- **Paragraph labels as conditionals** — Labels in Ink are set-once, never-unset flags; once a paragraph has been visited, its content may change permanently
- **Location cruft avoidance** — Players cannot carry contradictory context between locations because they cannot revisit them with new knowledge
- **Knowledge webs** — Characters' knowledge about the world is tracked through set-once flags, enabling context-aware dialog

## Examples

Ingold's work on *80 Days* and *Heaven's Vault* uses only-forwards design to manage complex branching narratives without the exponential complexity of traditional choice trees.

## Related Concepts

- [[narrative-momentum]] — Only-forwards design maintains narrative momentum
- [[procedural-storytelling]] — An architectural approach for procedural narrative

## References

- [[2019-01-01-procedural-storytelling-in-game-design]] — source, Chapter 7 by Jon Ingold
