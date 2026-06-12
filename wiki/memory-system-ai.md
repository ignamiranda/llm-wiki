---
title: "Memory System"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [llm, memory, agent, persistence, claude-code, memory-taxonomy]
aliases: ["AI memory system", "agent memory"]
summary: "A mechanism that persists information across agent sessions by writing to the filesystem, enabling the agent to recall preferences, conventions, and context from previous work."
---

# Memory System

## Definition

A mechanism that makes an [[Agent|agent]] [[stateful]] across [[Session|sessions]] by persisting information to the [[filesystem]] (or other storage) and reloading it at session start. Because the [[Model|model]] is permanently [[stateless]], any apparent memory is manufactured by the [[harness]] writing facts down and reading them back.

Memory systems typically store: user preferences, project conventions, architectural decisions, recurring patterns, and learned facts about the codebase. The simplest memory system is AGENTS.md — a file of standing instructions loaded into every session. More sophisticated systems use vector databases or structured files.

## Key Properties

- No state is ever stored in the model itself — all memory is external
- Memory files (AGENTS.md, MEMORY.md) are loaded as [[context-window|context]]
- Memory systems make the harness stateful across sessions
- [[Chromadb-ai-memory|ChromaDB AI Memory]] is an example of a vector-database-backed memory system

## Examples

"It remembered my preferences from yesterday — does that mean the model learned them?" — "No, the agent wrote them to a memory file and reloaded them at session start. The model itself saw nothing of yesterday."

## Related Concepts

- [[stateless]] — the model property that memory systems compensate for
- [[chromadb-ai-memory]] — a concrete memory system implementation
- [[AGENTS.md]] — the simplest form of memory
- [[handoff]] — cross-session context transfer
- [[2026-06-11-claude-code-memory-systems]] — a 6-level taxonomy of Claude Code memory systems

## References

- Matt Pocock, *Dictionary of AI Coding*, Section 6
