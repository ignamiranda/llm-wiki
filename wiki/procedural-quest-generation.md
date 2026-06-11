---
title: "Procedural Quest Generation"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, rpg, planning, npc]
aliases: [automated-quest-generation, quest-gen]
summary: "The algorithmic generation of quests for role-playing games, using structural analysis, grammar-based expansion, planning, genetic algorithms, knowledge graphs, or language models."
---

# Procedural Quest Generation

## Definition

Procedural quest generation is the algorithmic creation of quest content for role-playing games without manual authoring. It is a subfield of procedural content generation (PCG) focused on narrative and task structures. A key challenge is that general planning (which quest generation reduces to) is NP-complete, making domain-specific constraints essential for practical generators.

## Key Properties

- Reduces to a planning problem: initial state + goal state + set of actions
- General planning is NP-complete (PSPACE-hard for non-trivial domains)
- Practical generators restrict the domain using observed structural patterns from human-authored quests
- Generators must ensure quests make sense in the current game state
- Generators need to know when to generate a quest (not just how)

## Approaches

- **Structural analysis + grammar** (Doran & Parberry 2011): derive BNF grammar from corpus of quests, expand trees from NPC motivation root
- **Key-lock structure** (Ashmore & Nitsche 2007): quests as sequences of locked doors and keys
- **Planning-based**: general planners but computationally expensive for real-time use
- **Planning with character preferences** (Breault, Ouellet & Davies 2018): [[conan-quest-generator|CONAN]] uses a planning engine that takes world descriptions as facts and generates quests driven by character preferences, validated against Doran & Parberry's structural taxonomy
- **Genetic algorithm + planning for branching quests** (Lima, Feijó & Furtado 2022): combines automated planning with a genetic algorithm guided by story arcs to generate branching (nonlinear) quests, using tree-structured individuals, state-compatibility crossover, and story arc fitness
- **Sequence generation for text-adventure games** (Ammanabrolu et al. 2019): frames quest generation as action sequence generation, using Markov models and LSTM-based neural models trained on recipe data to produce cooking quests in interactive fiction
- **Knowledge graph + language model** (Knapp, Ashby & Fulda 2023): combines a Neo4j knowledge graph with a fine-tuned GPT-2 language model for structured reasoning plus natural language generation, enabling player-personalized quests

## Examples

- Doran & Parberry's Prolog-based generator starts with an NPC motivation, selects a strategy, and recursively expands a quest tree using production rules
- The generator produces both a terse action tree and a narrative with boilerplate NPC dialog
- The [[dragn-town-quests]] system uses a Neo4j knowledge graph to condition GPT-2 output for personalized quest generation

## Related Concepts

- [[conan-quest-generator]] — planning-based quest generator with character preferences
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
- [[text-adventure-quest-generation]] — quest generation for interactive fiction
- [[markov-quest-model]] — Markov approach to quest generation
- [[neural-quest-model]] — LSTM-based neural approach to quest generation
- [[2019-09-13-text-adventure-quest-generation]] — the paper describing sequence-generation approaches
- [[prithviraj-ammanabrolu]] — first author (sequence-generation approach)
- [[mark-riedl]] — senior author (sequence-generation approach)
- [[dragn-town-quests]] — KG+LM hybrid approach
- [[knowledge-graph-quest-generation]] — KG approach to quest generation
- [[gpt2-quest-generation]] — LM approach to quest generation
- [[personalized-quest-generation]] — player-adaptive approach
- [[2023-04-19-dragn-town-quest-generation]] — the paper describing the KG+LM approach
- [[gregory-knapp]] — first author (KG+LM approach)
- [[nancy-fulda]] — senior author (KG+LM approach)
- [[dragn-lab]] — research lab

## References

- Doran, J. & Parberry, I. (2011). A Prototype Quest Generator Based on a Structural Analysis of Quests from Four MMORPGs. Technical Report LARC-2011-02.
- Ashmore, C. & Nitsche, M. (2007). The Quest in a Generated World. Proc. DiGRA 2007.
- Lima, E.S., Feijó, B. & Furtado, A.L. (2022). Procedural generation of branching quests for games. Entertainment Computing, 43, 100491.
- Breault, V., Ouellet, S. & Davies, J. (2018). Let CONAN tell you a story: Procedural quest generation. arXiv:1808.06217.
- Knapp, G., Ashby, T. & Fulda, N. (2023). Personalized Quest and Dialogue Generation in Role-Playing Games: A Knowledge Graph- and Language Model-based Approach. CHI 2023. DOI: 10.1145/3544548.3581441.
