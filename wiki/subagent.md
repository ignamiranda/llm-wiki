---
title: "Subagent"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [llm, agent, architecture, delegation]
aliases: ["child agent", "delegated agent"]
summary: "A secondary agent spawned by a primary agent to execute a specific subtask, returning its result to the parent — a delegation pattern for parallel or specialized work."
---

# Subagent

## Definition

A secondary [[Agent|agent]] spawned by a primary agent to execute a specific subtask. The parent agent defines the goal, hands off context, and receives the result. Subagents enable parallel work (multiple subagents running different tasks) and specialization (a code-review subagent, a testing subagent).

Subagents are a [[harness]]-level concept — the harness manages spawning, context transfer, and result collection. Each subagent runs its own [[Session|session]] with its own [[context-window]], which avoids [[attention-degradation]] on the parent session.

## Key Properties

- Each subagent runs an independent session with its own context window
- Enables parallelism — multiple subagents can work simultaneously
- Requires [[handoff]]-style context transfer to the subagent
- Subagents can have different [[system-prompt|system prompts]] and [[Tool|tools]]

## Examples

A migration agent might spawn subagents: one to analyze the codebase structure, one to plan the migration, and one to execute the changes — each with specialized instructions.

## Related Concepts

- [[Agent]] — the parent unit
- [[handoff]] — how context is transferred to subagents
- [[harness]] — manages subagent lifecycle
- [[Session]] — each subagent has its own session

## References

- Matt Pocock, *Dictionary of AI Coding*, Section 6
