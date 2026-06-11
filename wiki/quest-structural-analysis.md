---
title: "Quest Structural Analysis"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, rpg, structural-analysis, bnf, grammar]
aliases: [quest-grammar, quest-decomposition]
summary: "A methodology for analyzing RPG quests by decomposing them into a formal BNF grammar with NPC motivations, strategies, and atomic actions, derived from corpus analysis of ~3000 quests."
---

# Quest Structural Analysis

## Definition

Quest structural analysis is a methodology for decomposing RPG quests into a formal grammar. Developed by Doran & Parberry (2011), it analyzes quests at three levels: NPC motivation (why), strategy (approach), and atomic actions (what the player does). The resulting BNF grammar enables both the description of existing quests and the generation of new ones.

## Key Properties

- Based on corpus analysis of ~3000 quests from 4 MMORPGs
- Quests form trees: root = motivation, internal nodes = subquests, leaves = atomic actions
- Pre-order traversal of the tree gives the player's sequence of actions
- The grammar includes recursive rules enabling quests of arbitrary depth
- Each production rule has implicit preconditions and postconditions

## The Three Levels

1. **NPC Motivation** (9 types) — the root of the quest tree
2. **Strategy** (23+ verb-noun pairs) — how the NPC addresses the motivation
3. **Atomic Action** (20 types) — primitive player actions with defined pre/post conditions

## BNF Grammar Structure

```
<QUEST> ::= <Knowledge> | <Comfort> | <Reputation> | <Serenity> |
            <Protection> | <Conquest> | <Wealth> | <Ability> | <Equipment>
<Comfort> ::= <Obtain Luxuries>
<Obtain Luxuries> ::= <get> <goto> <give>
```

Non-terminal symbols expand via production rules (18 rules in the paper). Terminal symbols are atomic actions from Table 4.

## Related Concepts

- [[conan-quest-generator]] — evaluated its output against this structural analysis taxonomy
- [[npc-motivations]] — the root level of the analysis
- [[procedural-quest-generation]] — applies this analysis for generation
- [[quest-generator-prolog]] — implements generation using this grammar
- [[2011-03-01-procedural-quest-generator]] — the paper defining this methodology
- [[ian-parberry]] — co-author
- [[jonathan-doran]] — co-author

## References

- Doran, J. & Parberry, I. (2011). A Prototype Quest Generator Based on a Structural Analysis of Quests from Four MMORPGs. Technical Report LARC-2011-02.
