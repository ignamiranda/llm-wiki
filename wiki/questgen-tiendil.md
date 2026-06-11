---
title: "questgen (the-tale/questgen)"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, python, directed-graphs, predicates]
aliases: [the-tale-questgen, questgen-python]
summary: "A Python library for automatic non-linear quest generation using directed graph representation with predicates, events, and constraints."
---

# questgen (the-tale/questgen)

## Definition

questgen is an open-source Python library for automatic non-linear quest generation by the [the-tale](https://github.com/the-tale) project. It represents quests as **directed graphs** with nodes connected by edges annotated with **predicates** — conditions that must be satisfied for the edge to be traversable. This enables nested, nonlinear quest structures with events and constraints, moving beyond simple linear or tree-shaped quests.

## Key Properties

- **Representation**: Directed graph with predicate-annotated edges
- **Nonlinear**: Supports branching and rejoining quest paths, not just trees
- **Nesting**: Quest states can contain sub-quests recursively
- **Events & Constraints**: Nodes can fire events and enforce pre/post conditions
- **Language**: Python
- **License**: BSD-3-Clause
- **Repository**: 34 stars, 68 commits

## Related Concepts

- [[procedural-quest-generation]] — the broader field
- [[quest-structural-analysis]] — alternative grammar-based approach
- [[quest-generator-prolog]] — earlier Prolog-based generator
- [[questify-js]] — JavaScript motivation-based generator
- [[decrews-quest-generator]] — C#/Unity implementation of Doran & Parberry

## References

- Repository: https://github.com/the-tale/questgen
