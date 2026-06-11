---
title: "Genetic Algorithm for Quest Generation"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, genetic-algorithms, automated-planning, evolutionary-computation]
aliases: [ga-quest-generation, quest-ga]
summary: "A genetic algorithm specialized for procedural quest generation, using tree-structured individuals representing branching quests, state-compatibility crossover, and story-arc-based fitness evaluation."
---

# Genetic Algorithm for Quest Generation

## Definition

A genetic algorithm designed for quest generation where each individual is a candidate branching quest encoded as a tree structure. Branches are STRIPS planning problems solved by a heuristic search planner (HSP2). The algorithm uses a novel crossover operator based on state compatibility between parent nodes (equal, sub, super types) and a fitness function measuring how well a quest's story arcs match a desired template. Control parameters include population size 100, elitism 2%, mutation probability 20%, and 100 generations. The algorithm was originally developed in Lima's 2019 PhD thesis [[2019-11-01-lima-genetic-planning-quests]] at PUC-Rio.

## Key Properties

- **Individual representation:** Tree with root (initial state), internal nodes (intermediate goals/states), leaf nodes (final goals), and branches (planning problems)
- **Crossover:** Three compatibility types — equal (uniform swap), sub (subset-to-superset), super (superset-to-subset)
- **Mutation:** Random add/remove of branches (20% probability)
- **Fitness:** Mean squared error between scaled story arcs of plot variants and desired story arc, multiplied by assessment factors (e.g., continuity)
- **Optimizations:** Parallel branch generation via thread pools; memoization of planning problem solutions
- **Convergence:** ~35 generations sufficient for optimal solutions

## Examples

- The Lima et al. (2022) prototype used this GA to generate 11 branching quests for a zombie survival RPG, with the three-act structure as desired story arc

## Related Concepts

- [[branching-quest-generation]] — what the GA produces
- [[story-arc-fitness]] — the fitness function
- [[semantic-integrity-constraints]] — guide branch generation
- [[tension-story-arc]] — narrative structure used in fitness
- [[domain-database-quest-gen]] — input defining the game world
- [[off-line-quest-generator]] — subsystem running the GA
- [[2019-11-01-lima-genetic-planning-quests]] — foundational PhD thesis
- [[2026-06-11-branching-quests-genetic-planning]] — the journal paper

## References

- Lima, E.S. (2019). Procedural generation of quests for games using genetic algorithms and automated planning. PhD Thesis, PUC-Rio.
- Lima, E.S., Feijó, B. & Furtado, A.L. (2022). Procedural generation of branching quests for games. Entertainment Computing, 43, 100491.
- Goldberg, D.E. (1989). Genetic Algorithms in Search, Optimization and Machine Learning.
