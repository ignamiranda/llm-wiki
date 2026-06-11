---
title: "Procedural Generation of Branching Quests for Games — Lima, Feijó & Furtado (2022)"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, genetic-algorithms, automated-planning, branching-narratives, interactive-storytelling]
source_url: "https://www.sciencedirect.com/science/article/pii/S1875952122000155"
source_hash: "4D0ADE1E8FF12A0EEEB2983012C0718C5995414C3F7F548A84B02148867860B0"
summary: "Lima, Feijó & Furtado (2022) present a novel method combining automated planning with a genetic algorithm guided by story arcs to generate coherent branching quests for dynamic game worlds, evaluated via a Turing Test showing players cannot distinguish AI-generated quests from human-designed ones."
---

# Procedural Generation of Branching Quests for Games — Lima, Feijó & Furtado (2022)

## Summary / 摘要

This paper presents a quest generation method combining automated planning with a genetic algorithm guided by story arcs to produce coherent branching quests for interactive game worlds. Quests are modeled as tree structures where branches represent different story paths. The genetic algorithm uses state-compatibility crossover (equal, sub, super types) and a fitness function comparing story arcs to a desired template via MSE. A Turing Test with 38 players achieved 48.68% accuracy — statistically indistinguishable from human-designed quests.

## Content / 内容

### Core Method

The system architecture comprises two subsystems:
- **Offline Quest Generator (OQG)**: Runs the genetic algorithm in preprocessing, generating quests via automated planning
- **Game Manager (GM)**: Handles real-time quest execution during gameplay

Quests are represented as tree structures within a **Game Tree (Ω)** — a higher-level tree where each node is a branching quest, and each quest's final states determine which quests can follow.

### Genetic Algorithm Design

**Individual representation:** Each candidate quest is a tree where:
- Root = initial state (S₀)
- Internal nodes = intermediate goal states (Gᵢ) and intermediate states (Sᵢ)
- Leaf nodes = final goals and final states
- Branches (Eᵢ) = pairs of nodes (Sⱼ, Gᵢ) plus an edge comprising a sequence of events

Each branch is encoded as a STRIPS planning problem: Eᵢ = ⟨F, Sⱼ, Gᵢ, O⟩

**Initial population:** Generated in three steps: quest-giver selection, quest motif selection, and tree structure generation. Branches use the HSP2 heuristic search planner to generate storylines.

**Crossover:** Based on state compatibility between parent nodes — three types:
1. **Equal type** (P₁Sᵢ = P₂Sⱼ): branches swap uniformly
2. **Sub type** (P₁Sᵢ ⊂ P₂Sⱼ): branches from subset propagate to superset with 50% probability
3. **Super type** (P₁Sᵢ ⊃ P₂Sⱼ): reverse of sub type

**Mutation:** Random add/remove of branches with 20% probability.

**Fitness function:** Compares story arcs of all plot variants to a desired story arc (e.g., three-act structure) using mean squared error after scaling both arcs to [1,10] time × [0,1] tension intervals. Includes a continuity factor rewarding term recurrence across descendant branches.

**Control parameters:** Population 100, elitism 2%, mutation 20%, 100 generations.

### Optimizations

- Parallel branch generation using thread pools
- Memoization of planning problem solutions via hash table caching

### Evaluation

**Technical evaluation (30 runs):**
- Genetic algorithm converges within ~35 generations
- Optimized version >3× faster than base (90.87s vs 307.32s for initial population)

**Turing Test (38 players, 114 data points):**
- 48.68% overall accuracy — essentially indistinguishable from random guessing (50%)
- Machine quests correctly identified: 34/76 (44.7%)
- Human quests correctly identified: 20/38 (52.6%)

### Limitations

- Domain Database specification is manual and time-consuming
- Planning is EXPSPACE-complete — performance depends on game world complexity
- No rigorous user study on overall game experience impact yet
- Game implementation must handle all story variants consistently

## Key Takeaways / 关键收获

- First method combining genetic algorithms + automated planning specifically for branching (nonlinear) quest generation
- Tree-structured individuals with state-compatibility crossover are a novel contribution
- Story arc fitness enables guided generation toward desired narrative structures
- Turing Test shows AI-generated branching quests are indistinguishable from professional human-designed quests
- Main practical barrier: manual authoring of the Domain Database

## Related / 关联

- [[branching-quest-generation]] — core concept
- [[quest-genetic-algorithm]] — the GA approach
- [[game-tree-narrative]] — overall narrative structure
- [[story-arc-fitness]] — evaluation method
- [[semantic-integrity-constraints]] — constraints guiding generation
- [[tension-story-arc]] — story arc representation
- [[domain-database-quest-gen]] — game world description
- [[quest-giver]] — NPC role
- [[quest-motif]] — goal coherence
- [[off-line-quest-generator]] — subsystem
- [[procedural-quest-generation]] — broader context
- [[edirlei-soares-de-lima]] — lead author
- [[bruno-feijo]] — co-author
- [[antonio-l-furtado]] — co-author
