---
title: "Offline Quest Generator"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, genetic-algorithms, system-architecture]
aliases: [oqq, offline-quest-gen]
summary: "A preprocessing subsystem that runs the quest generation genetic algorithm offline, producing the full set of branching quests for a game before runtime, which are then executed by the Game Manager during gameplay."
---

# Offline Quest Generator

## Definition / 定义

The Offline Quest Generator (OQG) is the preprocessing subsystem of the quest generation architecture by Lima, Feijó & Furtado (2022). It runs the genetic algorithm during a setup phase (before gameplay), generating the complete set of branching quests that will populate the Game Tree. The OQG includes a Genetic Algorithm module implementing evolutionary operators and a Quest Planner module (HSP2) that validates generated branches by solving their STRIPS planning problems.

## Key Properties / 关键特性

- Runs entirely in preprocessing — no runtime generation overhead
- Uses Domain Database as input to define the game world
- Produces the Game Tree structure for the Game Manager
- Supports an interactive mode: designer-created quests can be mixed with generated ones
- Generated quests are stored and selected by the Game Manager based on player actions

## Related Concepts / 相关概念

- [[quest-genetic-algorithm]] — core algorithm run by OQG
- [[game-tree-narrative]] — the output structure
- [[domain-database-quest-gen]] — input defining the world
- [[quest-giver]] — selection happens in OQG
- [[quest-motif]] — motif selection happens in OQG
- [[2026-06-11-branching-quests-genetic-planning]] — the paper

## References / 参考资料

- Lima, E.S., Feijó, B. & Furtado, A.L. (2022). Procedural generation of branching quests for games. Entertainment Computing, 43, 100491.
