---
title: "DRAGN Town Quests"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, rpg, knowledge-graph, gpt2, neo4j, python]
aliases: [DRAGN-Town-Quests, dragn-town]
summary: "A hybrid quest generation system developed by BYU's DRAGN Lab combining a Neo4j knowledge graph with a fine-tuned GPT-2 language model, published at CHI 2023."
---

# DRAGN Town Quests

## Definition

DRAGN Town Quests is a hybrid procedural quest generation system built by Brigham Young University's DRAGN Lab. It combines a Neo4j knowledge graph for structured reasoning about quest coherence and player state with a GPT-2 language model fine-tuned on World of Warcraft quest text for natural language generation. The system produces personalized quests adapted to individual player characteristics.

## Key Properties

- **Hybrid architecture**: Knowledge graph (symbolic) + language model (neural)
- **Graph database**: Neo4j encodes characters, locations, items, objectives, and player state
- **Fine-tuned LM**: GPT-2 trained on WoW quest corpus for dialogue and description generation
- **Personalization**: Player characteristics and preferences encoded in the KG
- **Implementation**: Python/Jupyter Notebook, Hugging Face Transformers, Neo4j driver

## Examples

- The system can generate quests with varied objectives (fetch, kill, escort, deliver) with natural-language quest text and NPC dialogue personalized to the player's in-game profile

## Related Concepts

- [[knowledge-graph-quest-generation]] — the KG approach this system uses
- [[gpt2-quest-generation]] — the LM approach this system uses
- [[personalized-quest-generation]] — the personalization aspect
- [[procedural-quest-generation]] — broader research area
- [[2023-04-19-dragn-town-quest-generation]] — the paper describing this system
- [[dragn-lab]] — the lab that built it
- [[gregory-knapp]] — first author
- [[nancy-fulda]] — supervisor

## References

- Knapp, G., Ashby, T. & Fulda, N. (2023). Personalized Quest and Dialogue Generation in Role-Playing Games: A Knowledge Graph- and Language Model-based Approach. CHI 2023. DOI: 10.1145/3544548.3581441
- GitHub: DRAGNLabs/DRAGN-Town-Quests
