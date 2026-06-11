---
title: "Story Arc Fitness Function"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, genetic-algorithms, fitness-function, story-arcs]
aliases: [arc-fitness, story-arc-evaluation]
summary: "A fitness function for genetic-algorithm-based quest generation that evaluates branching quest quality by comparing all possible plot variants' story arcs to a desired target arc using mean squared error after scaling."
---

# Story Arc Fitness Function

## Definition / 定义

The story arc fitness function evaluates the quality of a branching quest by measuring how well its possible plot variants match a desired story arc. For each plot variant, the story arc (derived from tension values assigned to each event operator) is compared to the target arc using mean squared error after scaling both to standard time interval [1,10] and tension interval [0,1]. The final fitness is the inverse of the average MSE across all variants, multiplied by assessment factors such as continuity.

## Key Properties / 关键特性

- Each operator has a tension effect (+, -, =) defined in T ⊆ DB
- Story arcs are scaled to [1,10] time × [0,1] tension for comparison
- MSE between scaled variant arc and scaled target arc measures deviation
- Final fitness = (1/m) × Σ(p_len / MSE(p_i, d)) × f₁ × f₂ × ... × f_k
- Supports multiple assessment factors: continuity, branch count, average plot length
- Lower MSE = better fit to desired story arc

## Examples / 示例

- For a branching quest p with 3 plot variants and target three-act arc d, the fitness calculation yielded 1068.66, incorporating both MSE values and a continuity factor of 3

## Related Concepts / 相关概念

- [[quest-genetic-algorithm]] — where fitness is used
- [[tension-story-arc]] — story arc representation
- [[semantic-integrity-constraints]] — recurrence importance feeds the continuity factor
- [[branching-quest-generation]] — broader context
- [[2026-06-11-branching-quests-genetic-planning]] — the paper

## References / 参考资料

- Lima, E.S., Feijó, B. & Furtado, A.L. (2022). Procedural generation of branching quests for games. Entertainment Computing, 43, 100491.
