---
title: "NPC Motivations"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [rpg, npc, quest-generation, procedural-generation, motivation]
aliases: [non-player-character-motivations]
summary: "A 9-category taxonomy of NPC motivations (Knowledge, Comfort, Reputation, Serenity, Protection, Conquest, Wealth, Ability, Equipment) derived from structural analysis of ~3000 MMORPG quests by Doran & Parberry."
---

# NPC Motivations

## Definition / 定义

NPC motivations are a 9-category taxonomy proposed by Doran & Parberry (2011) to describe the underlying reasons why non-player characters assign quests to players in role-playing games. Each quest maps to exactly one motivation, which determines the set of strategies the NPC can use and constrains the quest's structure. The taxonomy was derived from structural analysis of approximately 3000 quests from Eve Online, World of Warcraft, Everquest, and Vanguard: Saga of Heroes.

## The 9 Motivations

| Motivation | Description | Observed Frequency |
|------------|-------------|-------------------|
| Knowledge | Information known to a character | 18.3% |
| Comfort | Physical comfort | 1.6% |
| Reputation | How others perceive a character | 6.5% |
| Serenity | Peace of mind | 13.7% |
| Protection | Security against threats | 18.2% |
| Conquest | Desire to prevail over enemies | 20.2% |
| Wealth | Economic power | 2.0% |
| Ability | Character skills | 1.1% |
| Equipment | Usable assets | 18.5% |

Distribution is non-uniform; the authors suggest designers can shift distributions over time to affect game flavor.

## Key Properties / 关键特性

- Each NPC's motivation is expected to change as game events unfold
- Each motivation maps to 1-7 specific strategies (verb-noun pairs like "kill pests", "rescue NPC")
- The motivation determines the root of the quest tree, which is then expanded recursively
- Motivations are essential for making procedurally generated quests appear intentional rather than random

## Examples / 示例

- A **Protection**-motivated NPC asks the player to cure an ailing NPC (the "Cure for Lempeck Hargrin" quest from Everquest uses the Treat or Repair strategy)
- A **Knowledge**-motivated NPC asks the player to spy on a goblin (generated example in the paper)

## Related Concepts / 相关概念

- [[procedural-quest-generation]] — uses NPC motivations as the root of quest generation
- [[quest-structural-analysis]] — the methodology that identified these motivations
- [[conan-quest-generator]] — used this taxonomy to evaluate its generated quests against commercial games
- [[2011-03-01-procedural-quest-generator]] — the paper defining this taxonomy
- [[ian-parberry]] — co-author
- [[jonathan-doran]] — co-author

## References / 参考资料

- Doran, J. & Parberry, I. (2011). A Prototype Quest Generator Based on a Structural Analysis of Quests from Four MMORPGs. Technical Report LARC-2011-02.
