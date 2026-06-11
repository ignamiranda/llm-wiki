---
title: "Let CONAN tell you a story: Procedural quest generation"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, automated-planning, multi-agent-planning, narrative-generation, ai]
source_url: "https://arxiv.org/abs/1808.06217"
source_hash: "conan-1808.06217"
summary: "Breault, Ouellet & Davies (2018) propose CONAN — a planning-based procedural quest generator that takes world descriptions as sets of facts and generates quests according to world state and character preferences, evaluated against the Doran & Parberry structural quest taxonomy."
---

# Let CONAN tell you a story: Procedural quest generation

## Summary / 摘要

This paper presents CONAN (Creation Of Novel Adventure Narrative), a procedural quest generator that uses a planning approach to story generation. The engine accepts a world description represented as a set of facts — including characters, locations, and items — and generates quests based on the state of the world and the preferences of characters. Quests are evaluated through classification of their underlying motivations by analyzing the sequences of actions required to complete them. Compared against [[quest-structural-analysis]] of commercial video game quests, CONAN was found to successfully replicate the quest structures found in human-authored games.

## Content / 内容

### The CONAN Engine

CONAN frames quest generation as a planning problem: given an initial world state and a set of possible actions, find a sequence of actions that achieves a goal state while satisfying character preferences. The engine is designed as a multi-agent planning system where characters (agents) have preferences that influence which quests are generated and how they unfold.

The engine takes as input:
- **World description**: facts about characters, locations, items, and their relationships
- **Character preferences**: what each character values or desires
- **Goal specification**: what constitutes a completed quest

### Planning Approach

Unlike the grammar-based approach of Doran & Parberry ([[2011-03-01-procedural-quest-generator]]) which expands quests from [[npc-motivations]] using BNF production rules, CONAN uses general planning techniques to construct quests from first principles. This allows it to adapt to arbitrary world states rather than following pre-defined templates.

### Evaluation Methodology

CONAN's output was evaluated by classifying generated quests according to the 9-category NPC motivation taxonomy ([[npc-motivations]]) from Doran & Parberry's structural analysis. The action sequences of generated quests were analyzed to determine which motivation category they fell into, and these distributions were compared against the distributions observed in commercial MMORPGs.

### Results

The engine was found to be capable of replicating the quest structures found in commercial video game quests. The comparison against human structural quest analysis showed that CONAN could produce quests with similar motivation distributions to those seen in games like World of Warcraft, demonstrating that planning-based generation can produce structurally authentic quest content.

### Relation to Other Approaches

CONAN represents a distinct approach in the [[procedural-quest-generation]] landscape:
- **Grammar-based** (Doran & Parberry 2011): expand from NPC motivations using BNF rules
- **GA+Planning** (Lima, Feijó & Furtado 2022): genetic algorithm combined with planning for branching quests
- **CONAN** (Breault, Ouellet & Davies 2018): pure planning approach with character preferences

CONAN's planning approach occupies a middle ground — more flexible than grammar-based templates but computationally lighter than evolving populations of branching quest trees.

## Key Takeaways / 关键收获

- CONAN uses a planning-based approach (not grammar or GA) for procedural quest generation
- World descriptions are formalized as sets of facts about characters, locations, and items
- Character preferences influence quest generation
- CONAN successfully replicates quest structures found in commercial MMORPGs
- The engine is open-source under MIT license, implemented primarily in SAS with Python components

## Related / 关联

- [[conan-quest-generator]] — the CONAN engine concept page
- [[procedural-quest-generation]] — broader field
- [[planning-approach-procgen]] — planning-based generation methodology
- [[quest-structural-analysis]] — methodology used for evaluation
- [[npc-motivations]] — taxonomy used to classify generated quests
- [[2011-03-01-procedural-quest-generator]] — Doran & Parberry's grammar-based approach (evaluation baseline)
- [[2026-06-11-branching-quests-genetic-planning]] — Lima, Feijó & Furtado's GA+planning approach
- [[vincent-breault]] — lead author
- [[sebastien-ouellet]] — co-author
- [[jim-davies]] — co-author
