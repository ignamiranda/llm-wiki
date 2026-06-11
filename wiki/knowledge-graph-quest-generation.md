---
title: "Knowledge Graph Quest Generation"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, knowledge-graph, neo4j, rpg, nlp]
aliases: [kg-quest-generation, graph-based-quest-gen]
summary: "A procedural quest generation approach that uses a knowledge graph (typically Neo4j) to encode semantic relationships between quest elements for coherent quest structuring and personalization."
---

# Knowledge Graph Quest Generation

## Definition / 定义

Knowledge graph quest generation is a procedural quest generation approach that uses a structured knowledge graph — typically implemented with a graph database like Neo4j — to encode semantic relationships between quest elements: characters, locations, items, objectives, and player state. The knowledge graph enables logical reasoning about quest coherence, ensures generated content maintains internal consistency, and supports personalization by encoding player characteristics within the graph.

## Key Properties / 关键特性

- **Structured semantics**: Relations between entities (character `located_at` location, item `needed_for` objective) enable reasoning
- **Coherence guarantees**: The graph enforces logical consistency that pure language models lack
- **Personalization**: Player state and preferences encoded as graph nodes and edges
- **Composable**: Can be paired with language models for natural language generation
- **Queryable**: SPARQL-like queries (Cypher in Neo4j) can retrieve relevant subgraphs for generation

## Examples / 示例

- DRAGN Town Quests uses a Neo4j knowledge graph to structure quest elements and condition the GPT-2 language model output

## Related Concepts / 相关概念

- [[dragn-town-quests]] — system implementing this approach
- [[gpt2-quest-generation]] — complementary LM approach
- [[personalized-quest-generation]] — enabled by KG player-state encoding
- [[procedural-quest-generation]] — broader field
- [[2023-04-19-dragn-town-quest-generation]] — paper describing this approach

## References / 参考资料

- Knapp, G., Ashby, T. & Fulda, N. (2023). Personalized Quest and Dialogue Generation in Role-Playing Games: A Knowledge Graph- and Language Model-based Approach. CHI 2023. DOI: 10.1145/3544548.3581441
