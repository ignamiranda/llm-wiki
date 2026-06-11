---
title: "Dependency-Driven Prompt Pipeline"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, llm, prompt-pipeline, narrative-generation, quest-generation]
aliases: [dependency-aware-prompt-pipeline, structured-prompt-pipeline]
summary: "A multi-stage LLM prompting approach where each stage produces structured intermediate representations that serve as conditioned input to subsequent stages, reducing narrative drift and hallucinations."
---

# Dependency-Driven Prompt Pipeline

## Definition

A dependency-driven prompt pipeline is a multi-stage LLM generation architecture where the output of each stage is a structured intermediate representation (typically JSON) that informs and constrains subsequent stages. By decomposing complex generation tasks into focused sub-tasks with explicit data contracts between them, the pipeline mitigates narrative drift, limits hallucinations, and maintains coherence across long or complex generations.

## Key Properties

- **Sequential conditioning**: Each stage's prompt includes structured output from all prior stages
- **Schema enforcement**: Intermediate outputs conform to predefined schemas, ensuring parseability and type safety
- **Narrative drift mitigation**: Focused per-stage prompts prevent the loss of coherence typical of long single-shot generations
- **Reusability**: Stages can be independently modified, replaced, or reordered

## Examples

- [[2026-04-28-llm-prompt-pipeline-quest-gen]] — Borawski et al. (2026) apply a five-stage pipeline to RPG generation: world building → NPC creation → PC creation → quest planning → quest expansion
- Technical report generation: data collection → analysis → outline → draft → review, each stage consuming JSON from the prior

## Related Concepts

- [[structured-llm-quest-generation]] — specific application of this pattern to quest generation
- [[multi-stage-rpg-generation]] — the architectural pattern for RPG content
- [[planning-approach-procgen]] — top-down decomposition philosophy
- [[layer-based-procedural-generation]] — parallel concept in non-LLM generation where layers have dependencies
- [[procedural-quest-generation]] — broader context
- [[2026-04-28-llm-prompt-pipeline-quest-gen]] — paper introducing this concept to the wiki

## References

- Borawski, D., Szulc, M., Chudy, R., Giedrowicz, M., & Mironowicz, P. (2026). From World-Gen to Quest-Line: A Dependency-Driven Prompt Pipeline for Coherent RPG Generation. arXiv:2604.25482.
