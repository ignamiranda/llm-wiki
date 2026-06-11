---
title: "Quest Motif"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, genetic-algorithms, narrative, constraints]
aliases: [goal-motif, quest-theme]
summary: "A semantic integrity constraint type that groups related predicates under a motif name, ensuring coherent goal generation across different branches of a branching quest by selecting goals sharing the same theme."
---

# Quest Motif

## Definition

A quest motif is a named grouping of related predicates in the semantic integrity constraints (Γ) of the Domain Database. When generating a branching quest, a motif is randomly selected, and only predicates sharing that motif are used to define goal states across all branches. This ensures that branches lead to related tasks (e.g., gathering an item) rather than unrelated ones (e.g., gathering an item in one branch and killing an enemy in another).

## Key Properties

- Defined in the motif field of semantic integrity constraints (Γ ⊆ DB)
- Randomly selected during initial population generation
- Filters allowed predicates for goal state generation
- Prevents incoherent branches with unrelated objectives
- Works together with quest-giver selection to define branch goal states

## Examples

- askitem motif: groups hasreceived(character, character, item) and knowfailedtoget(character, character, item) — both relate to requesting and obtaining items

## Related Concepts

- [[semantic-integrity-constraints]] — motif is one of six constraint types
- [[quest-genetic-algorithm]] — uses motif in individual generation
- [[quest-giver]] — selected alongside motif
- [[branching-quest-generation]] — broader context
- [[2026-06-11-branching-quests-genetic-planning]] — the paper

## References

- Lima, E.S., Feijó, B. & Furtado, A.L. (2022). Procedural generation of branching quests for games. Entertainment Computing, 43, 100491.
