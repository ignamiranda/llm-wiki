---
title: "Branching Quest Generation"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, branching-narratives, genetic-algorithms, automated-planning, interactive-storytelling]
aliases: [nonlinear-quest-generation, branching-quests]
summary: "Procedural generation of quests with branching storylines where player choices lead to different narrative paths, combining automated planning with genetic algorithms guided by story arcs."
---

# Branching Quest Generation

## Definition / 定义

Branching quest generation is the procedural creation of quests with nonlinear storylines, where player choices at decision points lead to different narrative paths and outcomes. Unlike linear quest generation (which produces a fixed sequence of events), branching quest generation must maintain coherence across multiple possible plot variants while ensuring each branch is reachable through valid game actions. The approach by Lima, Feijó & Furtado (2022) combines automated planning with a genetic algorithm, representing quests as tree structures and using story arc fitness to guide evolution.

## Key Properties / 关键特性

- Quests represented as tree structures with branches encoding STRIPS planning problems
- Branches must be solvable by a planner to be valid (unreachable branches are removed)
- Story arc fitness evaluates how well all plot variants match a desired narrative template
- Crossover based on state compatibility (equal, sub, super types) between parent nodes
- Continuity factor rewards reuse of important terms across descendant branches
- Generated quests are assembled into a Game Tree forming the game's overall narrative

## Examples / 示例

- A quest where the player can either steal food, pay for it, or kill a zombie to earn it — each branch generates a different sequence of events validated by a planner
- Quest sequences where the outcome of one quest (e.g., which NPC survives) determines available branches in subsequent quests

## Related Concepts / 相关概念

- [[procedural-quest-generation]] — broader category including linear approaches
- [[quest-genetic-algorithm]] — the GA method used
- [[game-tree-narrative]] — how branching quests compose into a game
- [[story-arc-fitness]] — evaluating branching quest quality
- [[quest-structural-analysis]] — grammar-based approach (linear quests)
- [[tension-story-arc]] — narrative structure used in fitness
- [[2026-06-11-branching-quests-genetic-planning]] — the paper

## References / 参考资料

- Lima, E.S., Feijó, B. & Furtado, A.L. (2022). Procedural generation of branching quests for games. Entertainment Computing, 43, 100491.
