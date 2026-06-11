---
title: "GPT-2 Quest Generation"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, gpt2, nlp, language-model, fine-tuning, rpg]
aliases: [gpt2-quest-gen, lm-quest-generation]
summary: "The use of a fine-tuned GPT-2 language model to generate quest dialogue, descriptions, and narrative text, typically conditioned on structured knowledge from a knowledge graph."
---

# GPT-2 Quest Generation

## Definition / 定义

GPT-2 quest generation is the use of OpenAI's GPT-2 language model, fine-tuned on a corpus of quest text (e.g., World of Warcraft quest data), to generate natural language components of procedurally generated quests — including quest descriptions, NPC dialogue, and narrative text. The language model is typically conditioned on structured information from a knowledge graph to ensure the generated text remains coherent with the game world state.

## Key Properties / 关键特性

- **Fine-tuned**: Base GPT-2 adapted to quest-specific language via additional training on quest text corpora
- **Natural language**: Produces human-readable quest text, dialogue, and descriptions
- **Conditioned generation**: Output guided by structured inputs (e.g., knowledge graph subgraphs)
- **Limited coherence**: Pure LM approaches may generate inconsistent text; requires KG or other constraints

## Examples / 示例

- DRAGN Town Quests fine-tunes GPT-2 on World of Warcraft quest text, using a Neo4j knowledge graph to condition the LM output for coherent quest generation

## Related Concepts / 相关概念

- [[knowledge-graph-quest-generation]] — provides structure to guide LM output
- [[dragn-town-quests]] — system combining GPT-2 with KG
- [[personalized-quest-generation]] — LM enables varied dialogue per player
- [[procedural-quest-generation]] — broader field
- [[2023-04-19-dragn-town-quest-generation]] — paper describing this approach

## References / 参考资料

- Knapp, G., Ashby, T. & Fulda, N. (2023). Personalized Quest and Dialogue Generation in Role-Playing Games: A Knowledge Graph- and Language Model-based Approach. CHI 2023. DOI: 10.1145/3544548.3581441
