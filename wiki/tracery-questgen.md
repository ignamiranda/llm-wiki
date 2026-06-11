---
title: "Tracery Quest Generator (lemilonkh/questgen)"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, javascript, tracery, grammar, rpg]
aliases: [lemilonkh-questgen, tracery-quest-gen]
summary: "A JavaScript procedural quest generator using Tracery grammar to produce random quest descriptions for RPGs from grammar.json templates."
---

# Tracery Quest Generator (lemilonkh/questgen)

## Definition / 定义

A JavaScript procedural quest generator by lemilonkh that uses **Tracery** — a context-free grammar expansion library — to produce random quest descriptions for role-playing games. It defines quest structures, NPC names, locations, objectives, and rewards as grammar rules in a `grammar.json` file, then expands them into human-readable quest text.

## Key Properties / 关键特性

- **Approach**: Grammar-based generation using Tracery (context-free grammar)
- **Language**: JavaScript
- **Configuration**: `grammar.json` template file with all expansion rules
- **Output**: Random quest descriptions (text)
- **License**: MIT
- **Repository**: 10 stars
- **Design philosophy**: Minimal and focused — simply defines a grammar and expands it

## Related Concepts / 相关概念

- [[procedural-quest-generation]] — the broader field
- [[quest-structural-analysis]] — a more formal BNF grammar methodology
- [[quest-generator-prolog]] — different grammar-based approach (Prolog)
- [[questify-js]] — another JavaScript quest generator (motivation-based)

## References / 参考资料

- Repository: https://github.com/lemilonkh/questgen
- Tracery: https://github.com/galaxykate/tracery
