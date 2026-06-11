---
title: "Personalized Quest and Dialogue Generation in Role-Playing Games: A Knowledge Graph- and Language Model-based Approach"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, rpg, knowledge-graph, gpt2, neo4j, nlp, personalization, chi-2023]
summary: "Knapp, Ashby & Fulda (CHI 2023) present a hybrid approach to personalized quest generation combining a Neo4j knowledge graph with a GPT-2 language model fine-tuned on World of Warcraft quest data."
source_url: "https://doi.org/10.1145/3544548.3581441"
---

# Personalized Quest and Dialogue Generation in Role-Playing Games: A Knowledge Graph- and Language Model-based Approach

## Summary

Published at ACM CHI 2023 by Brigham Young University's DRAGN Lab, this paper presents a hybrid architecture for procedural quest generation that combines a Neo4j knowledge graph with a GPT-2 language model fine-tuned on World of Warcraft quest text. The knowledge graph provides structured reasoning about quest coherence, while the language model generates natural language dialogue and descriptions. The system produces personalized quests adapted to individual player characteristics, representing a departure from prior grammar-based or planning-only approaches.

## Content

### Hybrid Architecture

The system integrates two components:

1. **Neo4j Knowledge Graph**: Encodes semantic relationships between quest elements — characters, locations, items, objectives, and player state. The KG enables logical reasoning about quest coherence, ensures generated quests maintain internal consistency, and encodes player preferences for personalization.

2. **GPT-2 (Fine-tuned)**: A pretrained language model fine-tuned on a corpus of World of Warcraft quest text. The LM generates natural language dialogue, quest descriptions, and narrative text. The knowledge graph conditions or constrains the LM output to maintain coherence with the game world state.

### Personalization

Quests are tailored to individual players by encoding player characteristics and preferences within the knowledge graph. The system can adapt quest objectives, dialogue tone, difficulty, and rewards based on the player profile.

### Relationship to Prior Work

This work extends the broader field of [[procedural-quest-generation]] by introducing a neural language model component alongside structured knowledge representation. Prior approaches such as Doran & Parberry's [[2011-03-01-procedural-quest-generator]] used grammar-based expansion with Prolog, while Lima et al.'s [[2026-06-11-branching-quests-genetic-planning]] combined planning with genetic algorithms. The KG+LM approach represents a third paradigm: symbolic reasoning for structure plus neural generation for natural language.

## Key Takeaways

- First published approach combining knowledge graphs with fine-tuned LMs for quest generation (as of CHI 2023)
- Knowledge graphs provide structured coherence guarantees lacking in pure LM approaches
- Personalization is achieved through player state encoded in the KG
- Demonstrates viability of hybrid symbolic-neural architectures for narrative generation
- Implemented in Python/Jupyter Notebook with Neo4j and Hugging Face Transformers

## Related

- [[dragn-town-quests]] — the project and codebase
- [[dragn-lab]] — the research lab
- [[knowledge-graph-quest-generation]] — KG approach to quest generation
- [[gpt2-quest-generation]] — using GPT-2 for quests
- [[personalized-quest-generation]] — player-adaptive quest generation
- [[procedural-quest-generation]] — broader field
- [[gregory-knapp]] — first author
- [[nancy-fulda]] — supervisor
