---
title: "A Prototype Quest Generator Based on a Structural Analysis of Quests from Four MMORPGs"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, rpg, mmorpg, npc, planning, prolog, structural-analysis]
summary: "Doran & Parberry (2011) analyze ~3000 quests from four MMORPGs to derive a common BNF grammar for quest structure, then build a Prolog-based procedural quest generator."
source_url: "https://ianparberry.com/techreports/LARC-2011-02.pdf"
source_hash: "36142B04C75B15030ADDE49CDF5B03C6D0C44C27035DC8C1B7533898E51E5F3D"
---

# A Prototype Quest Generator Based on a Structural Analysis of Quests from Four MMORPGs

## Summary / 摘要

An analysis of approximately 3000 quests from Eve Online, World of Warcraft, Everquest, and Vanguard: Saga of Heroes reveals that RPG quests share a common underlying structure expressible as a formal grammar. The authors identify 9 distinct NPC motivations, 20 atomic actions, and a BNF production rule system that can describe any quest from the dataset. A prototype procedural quest generator written in Prolog (with a Java applet front-end) uses this grammar to produce complex, multi-leveled quests, leveraging Prolog's automatic backtracking to handle the combinatorial search.

## Content / 内容

### Motivation and Approach

The paper addresses the intractability of general planning for quest generation by observing that human-authored quests are far more structurally constrained than the full space of possible quests. By analyzing quests from existing games, the authors derive a restricted planning domain that is tractable while still producing believable content.

### Structural Analysis

Quests decompose into three levels:
1. **NPC Motivations** — 9 categories (Knowledge, Comfort, Reputation, Serenity, Protection, Conquest, Wealth, Ability, Equipment) that drive why an NPC assigns a quest
2. **Strategies** — 23+ verb-noun pairs (e.g., "kill pests", "steal supplies") specific to each motivation, each expanding to a sequence of 1-6 actions
3. **Atomic Actions** — 20 primitive actions (goto, kill, give, take, listen, report, spy, etc.) with defined preconditions and postconditions

Actions form trees where non-terminal nodes are subquests and leaves are atomic actions. Pre-order traversal gives the player's action sequence. The grammar uses BNF with recursive rules (Table 5 in the paper), enabling quests of arbitrary depth and complexity.

### NPC Motivations

The 9 motivations (Table 1) with their observed distribution across the dataset:

| Motivation | Description | Percent |
|------------|-------------|---------|
| Knowledge | Information known to a character | 18.3% |
| Comfort | Physical comfort | 1.6% |
| Reputation | How others perceive a character | 6.5% |
| Serenity | Peace of mind | 13.7% |
| Protection | Security against threats | 18.2% |
| Conquest | Desire to prevail over enemies | 20.2% |
| Wealth | Economic power | 2.0% |
| Ability | Character skills | 1.1% |
| Equipment | Usable assets | 18.5% |

### Quest Generator

The generator is written in **Prolog** with a **Java applet** front-end. It starts from a randomly chosen NPC motivation and expands the quest tree using the production rules. Prolog's built-in backtracking automatically handles dead ends — if a branch cannot be expanded given the current game state, the generator abandons it and tries alternatives. The seed 0 uses system time for unpredictable results; other seeds reproduce specific quests.

Output consists of a terse action tree and a narrative with simple boilerplate NPC dialog.

### Related Work Context

The paper distinguishes itself from prior quest classification work by Sullivan, Ashmore & Nitsche (key-lock structure), Jill Walker (exploration/combat binary), and Dickey (classification without generation). It frames quest generation as a restricted planning problem — NP-complete in general, but made tractable through domain-specific constraints derived from observed quest structure.

## Key Takeaways / 关键收获

- Human-authored quests share more structural commonality than expected — authors unconsciously follow patterns
- 9 NPC motivations provide a natural taxonomy for driving procedural quest generation
- BNF grammars can express quest structure with recursive subquest nesting
- Prolog's backtracking is a natural fit for tree-expansion quest generation
- The structural approach avoids the NP-complete general planning problem by restricting the domain to observed patterns

## Related / 关联

- [[npc-motivations]] — the 9-category taxonomy defined in this paper
- [[procedural-quest-generation]] — the broader concept this paper implements
- [[quest-structural-analysis]] — the BNF grammar methodology
- [[quest-generator-prolog]] — the Prolog-based prototype
- [[ian-parberry]] — co-author
- [[jonathan-doran]] — co-author
