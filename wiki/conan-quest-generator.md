---
title: "CONAN (Creation Of Novel Adventure Narrative)"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, automated-planning, multi-agent-planning, narrative-generation]
aliases: [CONAN engine, conan-procedural-quest-generation, Creation Of Novel Adventure Narrative]
summary: "A planning-based procedural quest generator that takes world descriptions as sets of facts and generates quests according to world state and character preferences."
---

# CONAN (Creation Of Novel Adventure Narrative)

## Definition / 定义

CONAN (Creation Of Novel Adventure Narrative) is a procedural quest generator that uses a planning approach to story generation. It accepts a formal world description — a set of facts about characters, locations, and items — and generates quests based on the current state of the world and the preferences of its characters. Quests are defined as sequences of actions that must be performed to achieve a goal, usually for a reward. Developed by Breault, Ouellet & Davies (2018), it is an open-source engine released under the MIT license.

## Key Properties / 关键特性

- **Planning-based**: generates quests from first principles using general planning, not grammar expansion or genetic algorithms
- **World-aware**: takes a formal world description as input (facts about characters, locations, items, relationships)
- **Character-driven**: character preferences influence which quests are generated
- **Evaluated against empirical data**: validated by comparing generated quest motivation distributions against Doran & Parberry's structural analysis of commercial MMORPG quests
- **Open source**: MIT-licensed, [repository on GitHub](https://github.com/science-of-imagination/conan-procedural-quest-generation)
- **Implementation**: primarily SAS (93.1%) with Python (6.9%) components

## Examples / 示例

- Given a world with an ailing villager, a healer NPC, and a rare herb location, CONAN can generate a "cure the villager" quest by planning the sequence: travel to herb location → acquire herb → return to healer → administer cure
- Given a world with warring factions, CONAN generates quests reflecting Protection or Conquest motivations depending on character preferences

## Related Concepts / 相关概念

- [[procedural-quest-generation]] — the broader field CONAN belongs to
- [[planning-approach-procgen]] — the planning-based generation methodology
- [[2018-08-19-conan-quest-generator]] — the paper describing the CONAN engine
- [[quest-structural-analysis]] — methodology used to evaluate CONAN's output
- [[npc-motivations]] — taxonomy used to classify CONAN's generated quests
- [[quest-generator-prolog]] — Doran & Parberry's grammar-based generator (contrasting approach)
- [[branching-quest-generation]] — Lima, Feijó & Furtado's GA+planning approach (contrasting approach)

## References / 参考资料

- Breault, V., Ouellet, S. & Davies, J. (2018). Let CONAN tell you a story: Procedural quest generation. arXiv:1808.06217.
- GitHub repository: https://github.com/science-of-imagination/conan-procedural-quest-generation
