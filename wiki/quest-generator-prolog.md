---
title: "Prolog Quest Generator (Doran & Parberry)"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, prolog, java, backtracking, npc]
aliases: [doran-parberry-quest-generator, LARC-2011-02-generator]
summary: "A prototype procedural quest generator written in Prolog with a Java applet front-end, using BNF grammar expansion and automatic backtracking to produce complex RPG quests."
---

# Prolog Quest Generator (Doran & Parberry)

## Definition

A prototype procedural quest generator described in Doran & Parberry (2011), written in **Prolog** with a **Java applet** front-end. It generates RPG quests by expanding a BNF grammar tree starting from a randomly chosen NPC motivation, using Prolog's built-in backtracking to handle dead ends during expansion.

## Key Properties

- **Language**: Prolog (generation engine) + Java (front-end applet)
- **Input**: NPC motivation + random seed
- **Output**: Action tree (terse) + narrative with NPC dialog (boilerplate)
- Seed 0 = system time (unpredictable); other seeds = reproducible quests
- Uses Prolog's automatic backtracking: if a tree branch cannot expand given game state, tries alternative rules

## How It Works

1. Accept an NPC motivation (e.g., Knowledge, Protection)
2. Consult strategy table for that motivation, select one
3. Expand strategy into action sequence (may include non-terminals)
4. Recursively replace non-terminals using production rules
5. Choice between alternate rules depends on assumed player knowledge and game state
6. If alternatives remain, pick randomly
7. Assign specific details (item names, NPC names, locations) during expansion

## Related Concepts

- [[npc-motivations]] — root of the generation tree
- [[procedural-quest-generation]] — the broader field
- [[quest-structural-analysis]] — the grammar methodology
- [[2011-03-01-procedural-quest-generator]] — the paper describing this generator
- [[ian-parberry]] — co-author
- [[jonathan-doran]] — co-author

## References

- Doran, J. & Parberry, I. (2011). A Prototype Quest Generator Based on a Structural Analysis of Quests from Four MMORPGs. Technical Report LARC-2011-02.
- Generator online (archived): http://www.eng.unt.edu/ian/research/quests/
