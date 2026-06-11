---
title: "Structured LLM Quest Generation"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, llm, prompt-pipeline, narrative-generation, rpg]
aliases: [llm-quest-generation, schema-driven-quest-generation]
summary: "A methodology for procedurally generating RPG quests using LLMs with structured intermediate representations, where quest content is produced through schema-constrained multi-stage prompting."
---

# Structured LLM Quest Generation

## Definition / 定义

Structured LLM quest generation is a methodology for producing RPG quest content using large language models guided by predefined schemas and intermediate representations. Rather than relying on single-shot prompts or free-form generation, this approach decomposes the quest creation process into stages (world building, NPC/PC creation, quest planning, quest expansion), each producing structured output (typically JSON) that feeds into subsequent stages. The schema enforcement ensures consistency, prevents contradictions, and enables scalable production of interconnected quest content.

## Key Properties / 关键特性

- **Schema-guided generation**: LLM outputs are constrained to predefined JSON schemas at each stage
- **Multi-stage decomposition**: Quest creation is split into focused sub-tasks with explicit dependencies
- **Cross-stage consistency**: Later stages reference structured data from earlier stages to maintain world coherence
- **Hallucination mitigation**: Structured dependencies constrain the LLM's output space, reducing fabricated content

## Examples / 示例

- [[2026-04-28-llm-prompt-pipeline-quest-gen]] — Borawski et al. (2026) demonstrate a five-stage pipeline producing coherent quest lines with branching points, NPC motivations, and world-consistent events

## Related Concepts / 相关概念

- [[dependency-driven-prompt-pipeline]] — the general prompting architecture this methodology uses
- [[multi-stage-rpg-generation]] — the broader RPG content generation pattern
- [[procedural-quest-generation]] — traditional (non-LLM) approaches to quest generation
- [[branching-quest-generation]] — alternative methodology for producing branching quests
- [[planning-approach-procgen]] — conceptual parallel in top-down generation
- [[npc-motivations]] — relevant to NPC schema design
- [[quest-giver]] — relevant to quest-NPC relationships
- [[game-tree-narrative]] — relevant to quest planning structures

## References / 参考资料

- Borawski, D., Szulc, M., Chudy, R., Giedrowicz, M., & Mironowicz, P. (2026). From World-Gen to Quest-Line: A Dependency-Driven Prompt Pipeline for Coherent RPG Generation. arXiv:2604.25482.
