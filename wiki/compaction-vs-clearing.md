---
title: "Compaction vs Clearing"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [ai, software-engineering, context-management, workflow]
aliases: ["clear vs compact"]
summary: "Two strategies for managing LLM context window: clearing (delete everything and return to system prompt) for consistent reproducibility, or compaction (summarize session history) for preserving progress."
---

# Compaction vs Clearing

## Definition

Two competing strategies for managing the [[context-window]] when it becomes degraded. **Clearing** deletes all accumulated context and returns the session to its initial system prompt state — the model "forgets" everything but starts fresh with full capability. **Compaction** summarizes the session history into a compact form that is fed back into the context window — preserving progress but at the cost of reduced fidelity and potential for the model to continue in the dumb zone.

## Key Properties

- Clearing: consistent starting state every time; model behaves like Memento (always the same)
- Compaction: preserves what was learned but risks carrying degraded signal
- Clearing is safer for reproducible, reliable behavior
- Compaction is preferred by many developers for convenience
- Matt Pocock recommends clearing over compaction
- [[handoff]] is a form of compaction with session transfer

## Examples

A developer working on a complex feature: after 50 turns, the AI starts forgetting earlier instructions. Option A: clear the session and start fresh (losing all intermediate context). Option B: compact the session into a summary of what was built and what remains.

## Related Concepts

- [[compaction]] — existing concept for context summarization
- [[handoff]] — full context transfer to new session
- [[attention-degradation]] — what both strategies address
- [[smart-zone-dumb-zone]] — why context management matters
- [[token-awareness]] — knowing when to act

## References

- Pocock, M. "AI Software Engineering Workshop" — YouTube
