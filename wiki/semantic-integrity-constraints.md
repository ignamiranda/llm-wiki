---
title: "Semantic Integrity Constraints"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, genetic-algorithms, constraints, automated-planning]
aliases: [integrity-constraints-quest-gen]
summary: "A set of six constraint types (t, opp, u, r, qualif, motif) used in genetic-algorithm-based quest generation to ensure generated branches respect the logical structure of the game world and produce coherent quests."
---

# Semantic Integrity Constraints

## Definition / 定义

Semantic integrity constraints (Γ) are a set of rules in the Domain Database that guide branch generation in the quest genetic algorithm. Each constraint is a 5-tuple γ = ⟨pred, (u₁r₁t₁, ..., uₙrₙtₙ), opp, qualif, motif⟩ attached to a predicate symbol, defining six types of semantic restrictions: variable types, opposite/contradictory relations, existential uniqueness, recurrence importance, qualification types, and goal motifs. These constraints ensure generated branches respect the logical structure of the game world.

## Key Properties / 关键特性

Six constraint types:
1. **t (variable types):** Required object type for each predicate term (e.g., cured must have a character term)
2. **opp (opposite/contradictory):** Opposite predicate (e.g., healthy ↔ infected); both cannot hold simultaneously
3. **u (existential uniqueness):** A term can appear only once (e.g., a character at only one place)
4. **r (recurrence importance):** Marks terms whose recurrence across descendant branches contributes to the continuity factor in fitness
5. **qualif (qualification):** Whether a predicate can be dynamically added to initial state (initial) or goal state (goal) without logical inconsistency
6. **motif (goal motif):** Groups related predicates under a motif name for coherent goal generation

## Examples / 示例

- γ = (at, (character, ∃! place), null, initial, null) — a character can only be at one place; at predicates can be added to initial states
- γ = (request, (character, character, ?item, place), null, null, null) — item term recurrence contributes to continuity
- γ = (hasreceived, (character, character, ∃!item), null, null, askitem) — hasreceived is part of the askitem motif

## Related Concepts / 相关概念

- [[domain-database-quest-gen]] — where constraints are defined
- [[quest-genetic-algorithm]] — uses constraints in branch generation
- [[quest-motif]] — the motif constraint type
- [[branching-quest-generation]] — broader context
- [[2026-06-11-branching-quests-genetic-planning]] — the paper

## References / 参考资料

- Lima, E.S., Feijó, B. & Furtado, A.L. (2022). Procedural generation of branching quests for games. Entertainment Computing, 43, 100491.
