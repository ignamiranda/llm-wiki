---
title: "Questify (JS)"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, javascript, structural-analysis, npc]
aliases: [deanljohnson-questify, questify-js]
summary: "A JavaScript procedural quest generator implementing Doran & Parberry's structural analysis approach with motivations, strategies, and atomic actions."
---

# Questify (JS)

## Definition

Questify is a JavaScript procedural quest generator by Dean L. Johnson that directly implements the **quest structural analysis** methodology of Doran & Parberry (2011). It structures generation around the three-level hierarchy — **NPC motivations** (root), **strategies** (approaches), and **atomic actions** (leaves) — and produces quest action trees as output.

## Key Properties

- **Approach**: Based on Doran & Parberry's BNF grammar formalism
- **Language**: JavaScript (Node.js)
- **Output**: Quest action trees with NPC dialog boilerplate
- **License**: MIT
- **Repository**: 3 stars, 76 commits
- **Maturity**: Moderate development history with 76 commits

## Related Concepts

- [[quest-structural-analysis]] — the underlying methodology
- [[npc-motivations]] — root taxonomy used for generation
- [[procedural-quest-generation]] — the broader field
- [[quest-generator-prolog]] — the original Prolog implementation of the same approach
- [[decrews-quest-generator]] — C#/Unity port of the same algorithm
- [[ian-parberry]] — co-author of the structural analysis paper
- [[jonathan-doran]] — co-author of the structural analysis paper

## References

- Repository: https://github.com/deanljohnson/Questify
- Doran, J. & Parberry, I. (2011). A Prototype Quest Generator Based on a Structural Analysis of Quests from Four MMORPGs.
