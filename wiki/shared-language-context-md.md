---
title: "Shared Language via CONTEXT.md"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [agent-skills, communication, documentation, domain-language]
aliases: ["context-md", "shared-language-doc", "ubiquitous-language-doc"]
summary: "A shared language document (CONTEXT.md) that establishes domain-specific terminology for AI coding agents, reducing verbosity and improving code naming consistency."
---

# Shared Language via CONTEXT.md

## Definition / 定义

The shared language pattern uses a `CONTEXT.md` file in the project root to document domain-specific terminology, establishing a ubiquitous language between the human developer and the AI coding agent. Instead of the agent using 20 words to describe a concept that has a specific name in the project, it uses the concise domain term. This drastically reduces token usage and ensures consistent naming across variables, functions, and files.

## Key Properties / 关键特性

- **Concise vocabulary** — Every important domain concept gets a single canonical term
- **Agent-accessible** — Placed at the project root where agents naturally read it
- **Evolving document** — Updated as new domain understanding emerges, often during [[grill-me-methodology]] sessions
- **Token efficiency** — Reduces agent output size by replacing verbose descriptions with precise terms

## Examples / 示例

Without CONTEXT.md: "There's a problem when a lesson inside a section of a course is made 'real' (i.e. given a spot in the file system)"

With CONTEXT.md: "There's a problem with the materialization cascade"

## Related Concepts / 相关概念

- [[grill-me-methodology]] — the grilling session that often surfaces and documents shared language
- [[agent-skills]] — composable skill files that use CONTEXT.md for context
- [[2026-06-11-mattpocock-skills]] — the repository that champions this pattern

## References / 参考资料

- [Example CONTEXT.md](https://github.com/mattpocock/course-video-manager/blob/main/CONTEXT.md)
