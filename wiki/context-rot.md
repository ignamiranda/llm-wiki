---
title: "Context Rot"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [llm, context, attention, failure-modes, memory-systems]
aliases: [context-window-degradation]
summary: "The degradation of an LLM's ability to recall loaded information as the amount of context in the window increases, causing buried content to become effectively invisible."
source_url: "https://youtu.be/UHVFcUzAGlM"
source_hash: "f3624d705c6e04e2e7538ae9bf26cb817ebab58bc58a64cb6d04be83c6486c2e"
---

# Context Rot

## Definition

Context rot is the inability for AI language models to reliably recall 100% of the information loaded into their context window as the amount of context increases. Early content gets buried, attention dilates across too many tokens, and the model effectively forgets information that was explicitly provided.

## Key Properties

- Caused by attention dilution across too many tokens, not by limits of context window size
- Early-positioned content is most affected (recency bias in attention)
- Worsens linearly (or worse) with total context volume, not just with file count
- Affects both system-level instructions (like [[claude-md]]) and conversation history
- Primary motivation for structured memory systems that avoid dumping everything into a single file

## Mitigation Strategies

- Keep [[claude-md]] under 200 lines — reference external files rather than inlining content
- Use memory index files that point to separate documents (Level 1-2 systems)
- Use semantic search to retrieve only relevant context at query time (Level 3-4 systems)
- Use compile-time knowledge systems (Level 5) to pre-synthesize information

## Related Concepts

- [[memory-system-ai]] — systems designed to solve context rot
- [[claude-md]] — primary file affected by context rot
- [[2026-06-11-claude-code-memory-systems]] — survey of solutions to context rot

## References

- "Every Claude Code Memory System Compared" — YouTube video by [unknown creator]
