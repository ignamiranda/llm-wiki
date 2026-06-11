---
title: "Domain Database (Quest Generation)"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, automated-planning, game-design, domain-modeling]
aliases: [quest-domain-database, quest-db, game-world-description]
summary: "A formal description of the game world used in genetic-algorithm-based quest generation, comprising objects, ground literals, semantic integrity constraints, planning operators, and tension mappings."
---

# Domain Database (Quest Generation)

## Definition / 定义

The Domain Database (DB) is the formal specification of a game world for the purpose of procedural quest generation. It comprises five elements: A (object-type pairs), B (ground literals describing world properties), Γ (semantic integrity constraints), Δ (STRIPS planning operators representing possible events), and T (operator-to-tension mappings). The DB is authored manually and is the primary input configuring what kinds of quests can be generated. The formalism was introduced in Lima's 2019 PhD thesis [[2019-11-01-lima-genetic-planning-quests]] and refined in the 2022 journal publication.

## Key Properties / 关键特性

- **A:** Objects with types (e.g., anne: character, johnhome: place, antidote2: item)
- **B:** Ground literals describing world state (e.g., alive(anne), at(john, johnhome))
- **Γ:** Six types of semantic integrity constraints (t, opp, u, r, qualif, motif)
- **Δ:** STRIPS planning operators (go, request, give, kill, cure, etc.)
- **T:** Tension effects per operator (e.g., kill: +, cure: -, go: =)
- Manual specification is time-consuming — automated extraction from existing game structures is an open research direction

## Examples / 示例

- Operator example: kill(CH0, CH1, IT0, PL0) — preconditions include alive(CH0), alive(CH1), has(CH0, IT0); effects include ¬alive(CH1)
- Tension mapping: T = {(kill, +), (save, -), (cure, -), (attack, +), (deliver, -), ...}

## Related Concepts / 相关概念

- [[semantic-integrity-constraints]] — the Γ component
- [[quest-genetic-algorithm]] — uses DB as input
- [[quest-motif]] — defined within DB's Γ constraints
- [[off-line-quest-generator]] — subsystem using DB
- [[2019-11-01-lima-genetic-planning-quests]] — foundational PhD thesis
- [[2026-06-11-branching-quests-genetic-planning]] — the journal paper

## References / 参考资料

- Lima, E.S. (2019). Procedural generation of quests for games using genetic algorithms and automated planning. PhD Thesis, PUC-Rio.
- Lima, E.S., Feijó, B. & Furtado, A.L. (2022). Procedural generation of branching quests for games. Entertainment Computing, 43, 100491.
