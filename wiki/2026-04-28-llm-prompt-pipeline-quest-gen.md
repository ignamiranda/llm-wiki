---
title: "From World-Gen to Quest-Line: A Dependency-Driven Prompt Pipeline for Coherent RPG Generation"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, rpg, llm, prompt-pipeline, narrative-generation, world-building]
summary: "Borawski et al. (2026) propose a dependency-aware multi-stage LLM prompt pipeline for RPG content generation, decomposing the process into world building, NPC/PC creation, quest planning, and quest expansion — each stage conditioning on structured JSON from prior stages."
---

# From World-Gen to Quest-Line: A Dependency-Driven Prompt Pipeline for Coherent RPG Generation

## Summary

Borawski et al. (2026) present a dependency-aware, multi-stage prompt pipeline for procedural RPG content generation using LLMs. The approach decomposes generation into five sequential stages — world building, NPC creation, player character creation, campaign-level quest planning, and quest expansion — each conditioning on structured JSON outputs from previous stages. By enforcing schemas and explicit data flow, the pipeline reduces narrative drift, limits hallucinations, and supports scalable creation of interconnected narrative elements.

## Content

### The Problem

LLMs show strong potential for narrative generation but struggle with coherence, controllability, and structural consistency when generating complex, multi-layered RPG worlds. Single-shot prompts produce incoherent or contradictory outputs, and naive sequential prompting lacks the dependency management needed for consistent world-building.

### The Approach: Dependency-Driven Prompt Pipeline

The paper models narrative dependencies through **structured intermediate representations** — each stage produces a well-defined JSON schema that serves as input to subsequent stages. The pipeline's five stages are:

1. **World Building** — Generates the setting, geography, factions, history, and global lore as a structured JSON document.
2. **Non-Player Character Creation** — Conditioned on the world document, generates NPCs with roles, motivations, relationships, and dialog styles.
3. **Player Character Creation** — Also conditioned on the world, generates the player character's background, abilities, and starting situation.
4. **Campaign-Level Quest Planning** — Uses the world, NPCs, and PC data to produce a high-level quest arc with branching points and dependencies.
5. **Quest Expansion** — Expands each quest node into detailed gameplay: objectives, encounters, rewards, dialog, failure states.

### Key Mechanisms

- **Schema enforcement**: Each stage's LLM output is constrained to a predefined JSON schema, ensuring parseable, structured data for the next stage.
- **Sequential conditioning**: Prompts include the full structured output of all previous stages, giving the LLM complete context.
- **Narrative drift mitigation**: By decomposing generation into focused stages with explicit data contracts, the pipeline prevents the drift that plagues long single-shot generations.
- **Hallucination reduction**: Structured dependencies make it harder for the model to contradict established facts.

### Relationship to Prior Work

The paper situates itself within [[procedural-quest-generation]] research, drawing on the structural analysis tradition of [[quest-structural-analysis]] but shifting from rule-based or GA-based approaches to LLM-driven generation. It shares the top-down decomposition philosophy of [[planning-approach-procgen]] and the dependency management concerns seen in [[layer-based-procedural-generation]].

## Key Takeaways

- Multi-stage prompt pipelines with structured intermediate representations improve LLM narrative coherence in RPG generation
- The five-stage decomposition (world → NPCs → PC → quest plan → quest expansion) provides a reusable template for RPG content generation
- Schema enforcement is a practical mechanism for reducing hallucinations and narrative drift
- The [[dependency-driven-prompt-pipeline]] concept generalises beyond games to any domain requiring coherent multi-stage generation

## Related

- [[procedural-quest-generation]] — broader context for this work
- [[branching-quest-generation]] — alternative approach to quest generation
- [[dependency-driven-prompt-pipeline]] — core concept introduced by this paper
- [[structured-llm-quest-generation]] — the specific methodology
- [[multi-stage-rpg-generation]] — the architectural pattern
- [[planning-approach-procgen]] — conceptual parallel in top-down generation
- [[layer-based-procedural-generation]] — conceptual parallel in dependency management
- [[npc-motivations]] — relevant to the NPC creation stage
- [[quest-giver]] — relevant to NPC-quest relationships
- [[game-tree-narrative]] — relevant to quest planning structures
- [[2026-06-11-branching-quests-genetic-planning]] — prior quest generation paper
- [[2011-03-01-procedural-quest-generator]] — earlier structural quest analysis
