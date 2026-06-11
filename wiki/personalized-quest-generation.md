---
title: "Personalized Quest Generation"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, personalization, rpg, player-modeling, nlp]
aliases: [player-adaptive-quest-gen, personalized-quests]
summary: "A procedural quest generation approach that adapts quest objectives, dialogue, difficulty, and rewards to individual player characteristics and preferences, typically using player state encoded in a knowledge graph."
---

# Personalized Quest Generation

## Definition

Personalized quest generation is the adaptation of procedurally generated quest content to individual player characteristics, preferences, and in-game history. Player state — including skill level, play style, narrative preferences, and past choices — is encoded in a structured representation (such as a knowledge graph) and used to condition the generation process, producing quests that are tailored to each player rather than one-size-fits-all.

## Key Properties

- **Player modeling**: Encodes player characteristics, preferences, and history
- **Adaptive difficulty**: Quest complexity and challenge scale to player skill
- **Narrative tailoring**: Dialogue tone, story hooks, and rewards match player preferences
- **KG-encoded state**: Player profile stored as nodes and edges in a knowledge graph
- **Requires structured + generative components**: Typically pairs KG reasoning with LM generation

## Examples

- DRAGN Town Quests uses a Neo4j knowledge graph to encode player state alongside world knowledge, conditioning the GPT-2 language model to generate personalized quest text

## Related Concepts

- [[knowledge-graph-quest-generation]] — provides the structured player model
- [[gpt2-quest-generation]] — generates personalized natural language
- [[dragn-town-quests]] — system implementing personalized generation
- [[procedural-quest-generation]] — broader field
- [[2023-04-19-dragn-town-quest-generation]] — paper describing this approach

## References

- Knapp, G., Ashby, T. & Fulda, N. (2023). Personalized Quest and Dialogue Generation in Role-Playing Games: A Knowledge Graph- and Language Model-based Approach. CHI 2023. DOI: 10.1145/3544548.3581441
