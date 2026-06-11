---
title: "Procedural Quest Generation"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, rpg, planning, npc]
aliases: [automated-quest-generation, quest-gen]
summary: "The algorithmic generation of quests for role-playing games, typically using structural analysis of human-authored quests, grammar-based expansion, or planning techniques."
---

# Procedural Quest Generation

## Definition / 定义

Procedural quest generation is the algorithmic creation of quest content for role-playing games without manual authoring. It is a subfield of procedural content generation (PCG) focused on narrative and task structures. A key challenge is that general planning (which quest generation reduces to) is NP-complete, making domain-specific constraints essential for practical generators.

## Key Properties / 关键特性

- Reduces to a planning problem: initial state + goal state + set of actions
- General planning is NP-complete (PSPACE-hard for non-trivial domains)
- Practical generators restrict the domain using observed structural patterns from human-authored quests
- Generators must ensure quests make sense in the current game state
- Generators need to know when to generate a quest (not just how)

## Approaches

- **Structural analysis + grammar** (Doran & Parberry 2011): derive BNF grammar from corpus of quests, expand trees from NPC motivation root
- **Key-lock structure** (Ashmore & Nitsche 2007): quests as sequences of locked doors and keys
- **Planning-based**: general planners but computationally expensive for real-time use
- **Genetic algorithm + planning for branching quests** (Lima, Feijó & Furtado 2022): combines automated planning with a genetic algorithm guided by story arcs to generate branching (nonlinear) quests, using tree-structured individuals, state-compatibility crossover, and story arc fitness

## Examples / 示例

- Doran & Parberry's Prolog-based generator starts with an NPC motivation, selects a strategy, and recursively expands a quest tree using production rules
- The generator produces both a terse action tree and a narrative with boilerplate NPC dialog

## Related Concepts / 相关概念

- [[npc-motivations]] — root taxonomy for grammar-based quest generation
- [[quest-structural-analysis]] — methodology for deriving quest structure
- [[quest-generator-prolog]] — a concrete implementation
- [[branching-quest-generation]] — nonlinear/GA+planning approach
- [[quest-genetic-algorithm]] — GA method for branching quests
- [[game-tree-narrative]] — narrative structure for branching quests
- [[2011-03-01-procedural-quest-generator]] — the paper describing the grammar-based approach
- [[ian-parberry]] — co-author (grammar-based approach)
- [[jonathan-doran]] — co-author (grammar-based approach)
- [[edirlei-soares-de-lima]] — lead author (GA+planning approach)
- [[bruno-feijo]] — co-author (GA+planning approach)
- [[antonio-l-furtado]] — co-author (GA+planning approach)
- [[2026-06-11-branching-quests-genetic-planning]] — the paper describing the GA+planning approach

## References / 参考资料

- Doran, J. & Parberry, I. (2011). A Prototype Quest Generator Based on a Structural Analysis of Quests from Four MMORPGs. Technical Report LARC-2011-02.
- Ashmore, C. & Nitsche, M. (2007). The Quest in a Generated World. Proc. DiGRA 2007.
- Lima, E.S., Feijó, B. & Furtado, A.L. (2022). Procedural generation of branching quests for games. Entertainment Computing, 43, 100491.
