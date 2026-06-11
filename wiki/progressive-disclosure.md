---
title: "Progressive Disclosure"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [llm, documentation, context, efficiency]
aliases: ["gradual context loading"]
summary: "A documentation and prompting strategy that reveals information to an AI agent gradually — only loading detailed instructions and context when the agent reaches the point where it needs them."
---

# Progressive Disclosure

## Definition

A documentation and prompting strategy that reveals information to an [[Agent|agent]] gradually, rather than loading everything at session start. Instead of a massive AGENTS.md file describing every convention, the agent starts with a high-level index and only loads detailed instructions when it reaches the relevant task.

This conserves the [[context-window]] — the agent burns [[Token|tokens]] on what it needs right now, not on instructions for tasks it will not reach for another 30 turns. The technique is fundamental to working in bounded context windows with large codebases or complex projects.

## Key Properties

- Reduces token waste from irrelevant instructions
- Requires a structured index pointing to detailed files
- The agent reads the index first, then loads only what the current task needs
- Essential for keeping sessions focused and avoiding [[attention-degradation]]

## Examples

A project's AGENTS.md might just list: "See docs/agents/standards.md for code style, docs/agents/architecture.md for patterns." The agent loads those files only when the task requires them.

## Related Concepts

- [[context-window]] — the finite resource progressive disclosure conserves
- [[attention-degradation]] — what progressive disclosure helps prevent
- [[AGENTS.md]] — the top-level file that uses progressive disclosure
- [[compaction]] — related technique for managing context

## References

- Matt Pocock, *Dictionary of AI Coding*, Section 6
