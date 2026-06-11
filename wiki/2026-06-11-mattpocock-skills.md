---
title: "Matt Pocock's Agent Skills Repository"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [agent-skills, ai-coding, software-engineering, best-practices, claude-code]
summary: "Matt Pocock's open-source collection of composable agent skills that package software engineering best practices into reusable workflows for AI coding agents like Claude Code and Codex."
source_url: "https://github.com/mattpocock/skills/"
source_hash: "3e6cd8e8655a4e7ae1a16a608b0b038c47e99714974ee09d5f52f9ac13aef14c"
---

# Matt Pocock's Agent Skills Repository

## Summary

The `mattpocock/skills` repository provides ~18 composable agent skills for AI coding agents (Claude Code, Codex, etc.), packaged as declarative SKILL.md files with accompanying workflows. The skills address four common failure modes of AI-assisted development: misalignment between human and agent, excessive verbosity, lack of feedback loops, and accelerated software entropy. Skills are organized into Engineering (10), Productivity (5), and Misc (4) categories, each implementing a specific best practice from software engineering.

## Content

### Philosophy

The repository is grounded in pragmatism rather than "vibe coding." It rejects monolithic process-takeover approaches (GSD, BMAD, Spec-Kit) in favor of small, hackable, composable skills that give the developer control. Each skill is designed to work with any model and is built on decades of engineering experience codified into repeatable practices.

### Four Failure Modes

**1. Misalignment** — The most common failure mode: the agent builds something different from what was wanted. Fixed by [[grill-me-methodology]] (grilling sessions where the agent interviews the user before starting work).

**2. Verbosity** — Agents use 20 words where 1 will do. Fixed by [[shared-language-context-md]] — a `CONTEXT.md` document establishing ubiquitous language, plus ADRs for architectural decisions.

**3. No Feedback Loops** — Without feedback on produced code, agents fly blind. Fixed by [[tdd-agent-skill]] (red-green-refactor TDD) and a dedicated diagnose skill for debugging.

**4. Software Entropy** — AI accelerates code complexity. Fixed by `improve-codebase-architecture` — a skill that systematically deepens codebase design.

### Skill Categories

**Engineering**: diagnose, grill-with-docs, triage, improve-codebase-architecture, setup-matt-pocock-skills, tdd, to-issues, to-prd, zoom-out, prototype

**Productivity**: caveman (ultra-compressed communication), grill-me, handoff, teach, write-a-skill

**Misc**: git-guardrails-claude-code, migrate-to-shoehorn, scaffold-exercises, setup-pre-commit

### Setup

```bash
npx skills@latest add mattpocock/skills
```

Select desired skills and agents, then run `/setup-matt-pocock-skills` to configure the issue tracker and triage labels.

## Key Takeaways

- The most critical skill is aligning with the agent before starting work ([[grill-me-methodology]])
- A shared language document ([[shared-language-context-md]]) dramatically reduces token usage and improves code consistency
- TDD with red-green-refactor provides essential feedback loops for AI-generated code
- Codebase architecture deteriorates faster with AI assistance — systematic improvement skills are necessary
- Skills should be small, composable, and hackable rather than monolithic process frameworks

## Related

- [[matt-pocock]] — author of the skills repository
- [[agent-skills]] — the concept of composable declarative skills for coding agents
- [[2026-06-11-anthropic-skills-repo]] — Anthropic's reference repository of Agent Skills
- [[grill-me-methodology]] — the grilling interview pattern for agent alignment
- [[shared-language-context-md]] — ubiquitous language via CONTEXT.md
- [[tdd-agent-skill]] — TDD adapted for AI-assisted development
- [[codebase-improvement-skill]] — systematic architecture improvement for AI-developed code
