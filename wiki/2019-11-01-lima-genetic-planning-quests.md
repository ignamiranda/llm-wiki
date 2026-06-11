---
title: "Procedural Generation of Quests for Games Using Genetic Algorithms and Automated Planning — Lima (2019)"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, genetic-algorithms, automated-planning, phd-thesis, interactive-storytelling]
source_url: "https://www.inf.puc-rio.br/wordpress/wp-content/uploads/2019/11/196293.pdf"
summary: "Lima's 2019 PhD thesis at PUC-Rio presents the foundational method combining genetic algorithms with automated planning (STRIPS/HSP2) for procedural quest generation, including the Domain Database formalism, semantic integrity constraints, tree-structured genetic algorithm with state-compatibility crossover, and story arc fitness function."
---

# Procedural Generation of Quests for Games Using Genetic Algorithms and Automated Planning — Lima (2019)

## Summary / 摘要

This PhD thesis by Edirlei Soares de Lima at PUC-Rio (advised by Bruno Feijó and Antonio L. Furtado) establishes the core method for procedural quest generation using genetic algorithms and automated planning. It introduces the Domain Database formalism for describing game worlds, semantic integrity constraints for coherent branch generation, a tree-structured genetic algorithm with state-compatibility crossover, and the story arc fitness function. This work is the foundation for the subsequent journal publication [[2026-06-11-branching-quests-genetic-planning|Lima, Feijó & Furtado (2022)]].

## Content / 内容

### Core Method

The thesis presents a two-subsystem architecture:

- **Offline Quest Generator (OQG):** Runs a genetic algorithm during preprocessing to generate branching quests. Each quest is represented as a tree where branches are STRIPS planning problems solved by the HSP2 heuristic search planner.
- **Game Manager (GM):** Handles real-time quest execution during gameplay, selecting from pre-generated quests based on player actions.

### Formal Components

1. **Domain Database (DB):** A 5-tuple ⟨A, B, Γ, Δ, T⟩ where A describes objects with types, B contains ground literals, Γ defines semantic integrity constraints, Δ specifies STRIPS planning operators, and T maps operators to tension effects.

2. **Semantic Integrity Constraints (Γ):** Six constraint types (t, opp, u, r, qualif, motif) ensuring generated branches respect game world logic.

3. **Genetic Algorithm:** Tree-structured individuals with:
   - Root (initial state S₀), internal nodes (intermediate goals/states), leaf nodes (final goals/states)
   - Crossover based on state compatibility (equal, sub, super types)
   - Mutation via random add/remove of branches (20% probability)
   - Population 100, elitism 2%, 100 generations

4. **Story Arc Fitness:** Compares plot variants' story arcs to a desired template using MSE after scaling.

### Relationship to the 2022 Paper

The 2022 Entertainment Computing paper [[2026-06-11-branching-quests-genetic-planning]] is a condensed journal version. The thesis contains:
- More comprehensive theoretical exposition of the genetic algorithm design
- Additional experimental results and convergence analysis
- Full system architecture and formalism documentation
- The Turing Test evaluation was added to the 2022 paper

### Related Conference Version

A shorter version was also presented at SBGames 2019:
- Lima, E.S., Feijó, B. & Furtado, A.L. (2019). Procedural generation of quests for games using genetic algorithms and automated planning. *2019 18th Brazilian Symposium on Computer Games and Digital Entertainment (SBGames)*, pp. 5-8.

## Key Takeaways / 关键收获

- Foundational PhD thesis establishing GA + automated planning for quest generation
- Introduces Domain Database, semantic integrity constraints, and story arc fitness
- All components reused and extended in the 2022 journal publication
- Demonstrates convergence within ~35 generations (consistent with 2022 results)

## Related / 关联

- [[2026-06-11-branching-quests-genetic-planning]] — journal version (2022)
- [[branching-quest-generation]] — core concept
- [[quest-genetic-algorithm]] — the GA method
- [[game-tree-narrative]] — narrative structure
- [[story-arc-fitness]] — evaluation method
- [[semantic-integrity-constraints]] — constraints
- [[domain-database-quest-gen]] — game world description
- [[off-line-quest-generator]] — subsystem
- [[quest-motif]] — goal coherence
- [[edirlei-soares-de-lima]] — author
- [[bruno-feijo]] — advisor/co-author
- [[antonio-l-furtado]] — advisor/co-author
