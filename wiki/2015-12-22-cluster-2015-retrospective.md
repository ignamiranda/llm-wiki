---
title: "The Cluster 2015 Retrospective"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [game-development, procedural-generation, the-cluster, ai]
summary: "Annual retrospective on The Cluster — an exploration-platformer with procedurally generated worlds, covering playtesting results, behaviour tree AI, pathfinding, dialogue systems, and world-structure communication."
source_url: "https://blog.runevision.com/2015/12/the-cluster-2015-retrospective.html"
---

# The Cluster 2015 Retrospective

## Summary
Annual retrospective on The Cluster — an exploration-platformer with procedurally generated worlds, covering playtesting results, behaviour tree AI, pathfinding, dialogue systems, and world-structure communication.

## Content
This 2015 retrospective covers progress on The Cluster, an exploration-platformer with procedurally generated worlds. Enemy combat was implemented using behaviour trees, providing modular and reusable AI logic for enemy decision-making. The AI pathfinding system enables enemies to navigate procedurally generated terrain, accounting for the non-uniform geometry that procedural generation produces.

A dialogue system was added for NPC interactions, and in-world road signs were introduced to help players understand the structure of procedurally generated worlds. Since procedural levels lack the designed landmarks of hand-crafted worlds, signs provide critical orientation and wayfinding information. A map screen and travel tubes (shortcuts between distant locations) further aid navigation.

A central theme of the retrospective is the challenge of making procedurally generated worlds feel intentional and designed rather than random. The article examines playtesting feedback and how each system — AI, pathfinding, dialogue, signs, and shortcuts — contributes to player comprehension and enjoyment of the generated world.

## Key Takeaways
- Behaviour trees for enemy AI in a procedural platformer
- Road signs help players understand procedurally generated world structure
- Travel tubes create shortcut connections in non-linear worlds

## Related
- [[rune-skovbo-johansen]] — author
- [[the-cluster]] — game reference
