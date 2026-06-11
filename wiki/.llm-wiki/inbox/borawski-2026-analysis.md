# Source Analysis: Borawski et al. (2026) — arXiv:2604.25482

**Source**: arXiv:2604.25482 — "From World-Gen to Quest-Line: A Dependency-Driven Prompt Pipeline for Coherent RPG Generation"
**Authors**: Dominik Borawski, Marta Szulc, Robert Chudy, Małgorzata Giedrowicz, Piotr Mironowicz
**Year**: 2026
**Language**: en
**Confidence**: high

## Summary

The paper presents a dependency-aware, multi-stage prompt pipeline for procedural RPG content generation using LLMs. It addresses coherence, controllability, and structural consistency in LLM-based narrative generation by decomposing generation into sequential stages: world building, NPC creation, player character creation, campaign-level quest planning, and quest expansion. Each stage conditions on structured JSON outputs from previous stages, reducing narrative drift and hallucinations.

## Key Concepts

- **Dependency-driven prompt pipeline**: Multi-stage generation where each stage consumes structured output from prior stages
- **Structured intermediate representations**: JSON schemas enforced per stage as the data contract between stages
- **Sequential conditioning**: Each stage's LLM prompt includes the full context from previous stages as structured data
- **Narrative drift**: The tendency for LLM-generated narratives to lose coherence over long generations — mitigated by explicit schema enforcement
- **World-building → NPC creation → PC creation → quest planning → quest expansion**: The five-stage decomposition

## Connections to Existing Wiki

| Existing Page | Connection |
|---|---|
| [[procedural-quest-generation]] | This paper is a specific methodology within procedural quest generation |
| [[branching-quest-generation]] | Related approach to quest generation, though this paper uses LLMs not GAs |
| [[planning-approach-procgen]] | The pipeline is a top-down planning approach with explicit stage dependencies |
| [[npc-motivations]] | NPC creation stage in the pipeline would produce motivational data |
| [[quest-giver]] | NPC creation stage handles quest-giver NPCs |
| [[game-tree-narrative]] | Quest planning stage produces campaign-level narrative structures |
| [[layer-based-procedural-generation]] | Conceptual parallel: the prompt pipeline is a form of layer-based generation with sequential dependencies |
| [[2026-06-11-branching-quests-genetic-planning]] | Prior quest generation paper using different approach (GA + planning) |
| [[2011-03-01-procedural-quest-generator]] | Doran & Parberry's structural approach to quest generation |

## Novel Contributions

1. First paper to apply multi-stage dependency-aware prompt pipelines to RPG world generation
2. Concrete schema design for each stage's structured output
3. Empirical evaluation of coherence improvements over single-shot generation

## Gaps

- No existing wiki pages on LLM-based narrative generation or prompt pipeline techniques
- No existing person pages for any of the five authors
- No existing concept pages for dependency-driven prompting in game generation

## Suggested Actions

- [x] Create article page summarizing the paper
- [x] Create person pages for all five authors
- [x] Create concept page: dependency-driven-prompt-pipeline
- [x] Create concept page: structured-llm-quest-generation
- [x] Create concept page: multi-stage-rpg-generation
