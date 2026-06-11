---
title: "Game Tree (Narrative)"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, branching-narratives, game-design, narrative-structure]
aliases: [narrative-game-tree, quest-tree]
summary: "A tree structure representing a game's narrative where each node is a branching quest, and each quest's outcomes determine which quests can follow, enabling coherent sequences of branching narratives."
---

# Game Tree (Narrative)

## Definition

The Game Tree (Ω) is a hierarchical structure representing the complete narrative of a game as a tree of branching quests. Each node is a branching quest (ψᵢ), itself a tree structure. The number of final states (outcomes) of a quest determines the number of possible new quests that can follow it — each outcome becomes a child node. This structure ensures logical coherence between consecutive quests by propagating world state changes through the tree.

## Key Properties

- Each node = one branching quest (internally a tree of branches)
- Child quests are generated from the final states of parent quests
- World state changes from previous quests affect available options in future quests
- Height of the tree is a parameter (e.g., limited to 2 for playable prototypes)
- Supports hybrid trees mixing procedurally generated and human-designed quests

## Examples

- In the Lima et al. (2022) prototype, the game tree had 14 quests (3 human-designed, 11 AI-generated) with height 2, meaning players experienced two AI quests and one human quest per playthrough

## Related Concepts

- [[branching-quest-generation]] — quests that form the tree's nodes
- [[off-line-quest-generator]] — subsystem that generates quests for the game tree
- [[domain-database-quest-gen]] — defines the world whose state propagates through the tree
- [[2026-06-11-branching-quests-genetic-planning]] — the paper introducing this concept

## References

- Lima, E.S., Feijó, B. & Furtado, A.L. (2022). Procedural generation of branching quests for games. Entertainment Computing, 43, 100491.
