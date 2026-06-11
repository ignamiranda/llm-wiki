---
title: "Quest-Giver"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, npc, game-design, narrative]
aliases: [quest-giver-npc, dispatcher-role]
summary: "The NPC character that offers a quest to players, provides information, and rewards completion — corresponding to Propp's dispatcher character role in narrative theory."
---

# Quest-Giver

## Definition / 定义

The quest-giver is the most essential NPC in role-playing and adventure games' quest structures (Howard, 2008). This character offers the quest to players, gives them information on how to proceed, and provides rewards upon completion. In the quest genetic algorithm by Lima, Feijó & Furtado (2022), the quest-giver is randomly selected from all characters in the game world during individual generation, and its identity serves as the main character for goal state predicates across all branches.

## Key Properties / 关键特性

- Corresponds to the dispatcher role in Propp's morphology of folktales
- Randomly selected from available characters during initial population generation
- Used as the main character for all goal state predicates in a quest's branches
- Reinforces coherence by grounding all branch goals to the same NPC motivation
- Also serves as the reward provider upon quest completion

## Examples / 示例

- In the Lima et al. (2022) zombie survival RPG, Anne frequently acts as quest-giver, requesting antidotes, food, or escorts from the player character John

## Related Concepts / 相关概念

- [[branching-quest-generation]] — uses quest-giver selection
- [[quest-motif]] — quest-giver + motif define goal generation
- [[quest-genetic-algorithm]] — selection step in initial population
- [[2026-06-11-branching-quests-genetic-planning]] — the paper
- [[npc-motivations]] — related NPC taxonomy

## References / 参考资料

- Lima, E.S., Feijó, B. & Furtado, A.L. (2022). Procedural generation of branching quests for games. Entertainment Computing, 43, 100491.
- Howard, J. (2008). Quests: Design, Theory, and History in Games and Narratives.
- Propp, V. (1968). Morphology of the Folktale.
