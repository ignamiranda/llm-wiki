---
title: "Codebase Architecture Improvement"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [agent-skills, architecture, refactoring, technical-debt, code-quality]
aliases: ["improve-codebase-architecture", "architecture-improvement-skill"]
summary: "A systematic agent skill for identifying and resolving architectural deepening opportunities in a codebase, informed by the domain language in CONTEXT.md and documented decisions in ADRs."
---

# Codebase Architecture Improvement

## Definition

A structured agent workflow for rescuing codebases from accelerated entropy caused by AI-assisted development. The skill analyzes the codebase for "deepening opportunities" — places where the architecture can be improved by consolidating tightly-coupled modules, making the codebase more testable, and improving AI-navigability. It uses the project's [[shared-language-context-md]] (CONTEXT.md) and Architecture Decision Records (ADRs) as context.

## Key Properties

- **Domain-informed** — Uses CONTEXT.md to understand the domain model before suggesting changes
- **ADR-aware** — Considers documented architectural decisions to avoid contradicting past choices
- **Entropy countermeasure** — Specifically designed to counteract the rapid complexity growth from AI-generated code
- **Incremental improvement** — Recommends running every few days rather than as a one-time fix

## Related Concepts

- [[agent-skills]] — the composable skill framework
- [[shared-language-context-md]] — domain language context used by this skill
- [[tdd-agent-skill]] — provides the test safety net for refactoring
- [[2026-06-11-mattpocock-skills]] — the repository containing this skill

## References

- [improve-codebase-architecture SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/improve-codebase-architecture/SKILL.md)
