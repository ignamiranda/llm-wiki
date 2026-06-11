# GitHub Repositories Analysis — Open-Source Quest Generation Tools

**Date:** 2026-06-11
**Purpose:** Survey of 6 open-source GitHub repositories for procedural quest generation, documenting approaches, languages, maturity, and relationships.

## Repository Summary

| Repo | Stars | Language | Approach | License | Commits |
|------|-------|----------|----------|---------|---------|
| the-tale/questgen | 34 | Python | Directed graph + predicates | BSD-3-Clause | 68 |
| deanljohnson/Questify | 3 | JavaScript | Structural analysis (Doran & Parberry) | MIT | 76 |
| decrews/Procedural-Quest-Generator | 11 | C#/Unity | Structural analysis (Doran & Parberry) | — | — |
| lemilonkh/questgen | 10 | JavaScript | Tracery grammar expansion | MIT | — |
| m0nirul/procedural-quest-generator | 0 | Rust | Template + variable replacement | — | — |
| Cultrarius/QuestWeaver | 68 | C++ | Weighted graph search + templates | Unlicense | 473 |

## Approaches

### 1. Doran & Parberry Structural Analysis (3 repos)
- **deanljohnson/Questify** (JS) — direct implementation of the BNF grammar approach
- **decrews/Procedural-Quest-Generator** (C#/Unity) — Unity port with ScriptableObject data
- Both follow the motivation → strategy → atomic action hierarchy

### 2. Graph-Based (2 repos)
- **the-tale/questgen** (Python) — directed graph with predicate-annotated edges; supports nonlinear, nested quests
- **Cultrarius/QuestWeaver** (C++) — weighted graph search with template-defined nodes; most mature repo (473 commits)

### 3. Grammar/Template Expansion (3 repos)
- **lemilonkh/questgen** (JS) — Tracery context-free grammar
- **m0nirul/procedural-quest-generator** (Rust) — template + variable replacement + validation
- **Cultrarius/QuestWeaver** (C++) — also uses template files for quest data

## Key Observations

1. **Doran & Parberry's 2011 paper is the dominant influence** — 3 of 6 repos are direct implementations of their structural analysis.
2. **Graph representations are the most flexible** — both questgen (directed graph) and QuestWeaver (weighted graph) allow nonlinear structures beyond simple trees.
3. **Template/grammar approaches are the simplest** — Tracery (lemilonkh) and the Rust template system require minimal code but produce the least structured output.
4. **QuestWeaver is the most mature** — 68 stars, 473 commits, Unlicense, data-driven architecture with serialization.
5. **Questgen (the-tale) is the most novel** — predicate-annotated edges and event/constraint system go beyond the Doran & Parberry approach.
6. **No clear winner in approach** — different games have different needs (linear narrative vs. open-world flexibility vs. light quest decoration).

## Pages Created

- [[questgen-tiendil]] — the-tale/questgen
- [[questify-js]] — deanljohnson/Questify
- [[decrews-quest-generator]] — decrews/Procedural-Quest-Generator
- [[tracery-questgen]] — lemilonkh/questgen
- [[procedural-quest-generator-rust]] — m0nirul/procedural-quest-generator
- [[questweaver-cpp]] — Cultrarius/QuestWeaver
