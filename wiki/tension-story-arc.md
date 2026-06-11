---
title: "Tension-Based Story Arc"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, narrative, storytelling, story-arcs]
aliases: [tension-arc, story-arc-tension]
summary: "A representation of narrative story arcs as sequences of tension changes — rise (+), fall (-), or maintain (=) — used as a target template in genetic-algorithm-based quest generation to evaluate plot quality."
---

# Tension-Based Story Arc

## Definition

A tension-based story arc represents narrative structure as a sequence of tension changes over discretized time. Each step can be rise (+), fall (-), or maintain (=), determined by how each event in a quest affects the overall tension level (defined in the Domain Database). The symbolic sequence can be converted to a numeric representation and scaled to standard intervals for comparison. The three-act structure (setup → confrontation → resolution) is one canonical example.

## Key Properties

- Symbolic notation: d_sym_arc = {s₁, s₂, ..., sₙ} where s ∈ {+, -, =}
- Numeric conversion: vᵢ = vᵢ₋₁ + 1 for +, vᵢ₋₁ - 1 for -, vᵢ₋₁ for =
- Scaled to standard intervals [1,10] time × [0,1] tension for comparison
- Three-act structure example: {+, +, +, -} (rising tension, then resolution)

## Examples

- Three-act arc: d_sym = {+, +, +, -} → d_num = {1, 2, 3, 2} → d_scaled = {0.33, 0.33, 0.66, 0.66, 0.66, 1.00, 1.00, 0.66, 0.66, 0.66}

## Related Concepts

- [[story-arc-fitness]] — uses tension story arcs for evaluation
- [[quest-genetic-algorithm]] — fitness evaluation in the GA
- [[domain-database-quest-gen]] — defines tension values for operators
- [[branching-quest-generation]] — broader context
- [[2026-06-11-branching-quests-genetic-planning]] — the paper

## References

- Lima, E.S., Feijó, B. & Furtado, A.L. (2022). Procedural generation of branching quests for games. Entertainment Computing, 43, 100491.
