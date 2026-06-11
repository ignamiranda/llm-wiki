---
title: "TDD for AI Coding Agents"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [agent-skills, testing, tdd, red-green-refactor, feedback-loops]
aliases: ["tdd-agent-skill", "ai-tdd"]
summary: "A red-green-refactor test-driven development loop adapted for AI coding agents, providing consistent feedback through automated tests before and after implementation."
---

# TDD for AI Coding Agents

## Definition

An adaptation of classic test-driven development (TDD) for AI coding agents, structured as a red-green-refactor loop. The agent first writes a failing test (red), then implements the minimum code to make it pass (green), then refactors while keeping tests green. This gives the agent a consistent feedback signal about whether its code actually works, preventing the "flying blind" problem where agents produce code that looks correct but fails at runtime.

## Key Properties

- **Red-Green-Refactor** — Classic TDD cycle enforced through the skill workflow
- **Vertical slicing** — Features are built one test at a time, not all at once
- **Regression protection** — The test suite catches regressions from refactoring
- **AI-specific guidance** — Includes instructions on what makes good and bad tests for AI-generated code

## Related Concepts

- [[agent-skills]] — the composable skill framework this belongs to
- [[2026-06-11-mattpocock-skills]] — the repository containing the TDD skill
- [[codebase-improvement-skill]] — complementary skill for ongoing architecture health

## References

- [tdd SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md)
