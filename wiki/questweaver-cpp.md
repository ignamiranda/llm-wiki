---
title: "QuestWeaver (C++)"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, cpp, weighted-graphs, templates, serialization]
aliases: [cultrarius-questweaver, questweaver-cpp]
summary: "A C++ quest/story generation system using weighted graph search with template files and serialization, separating quest logic from data."
---

# QuestWeaver (C++)

## Definition

QuestWeaver is a C++ quest and story generation system by Cultrarius that generates narrative content using **weighted graph search** over template-defined quest structures. It separates quest logic from data via template files, supports **serialization** of generated quests, and uses weighted random selection to traverse its quest graph.

## Key Properties

- **Approach**: Weighted graph search over template-defined quest nodes
- **Language**: C++
- **Data-driven**: Quest logic defined in template files, separated from C++ code
- **Serialization**: Generated quests can be saved and loaded
- **License**: Unlicense (public domain)
- **Repository**: 68 stars, 473 commits
- **Maturity**: Largest and most active of the surveyed quest gen repos

## Related Concepts

- [[procedural-quest-generation]] — the broader field
- [[questgen-tiendil]] — Python graph-based quest generation (different graph approach)
- [[quest-structural-analysis]] — alternative grammar-based methodology
- [[procedural-quest-generator-rust]] — Rust template-based quest generation
- [[tracery-questgen]] — grammar-based approach (JS)

## References

- Repository: https://github.com/Cultrarius/QuestWeaver
