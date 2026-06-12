---
title: "AI Session Stages"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [ai, software-engineering, workflow, session-management]
aliases: ["session lifecycle", "coding session stages"]
summary: "The four predictable stages of an AI-assisted coding session: system prompt setup, codebase exploration, implementation, and testing."
---

# AI Session Stages

## Definition

The four-stage lifecycle of an effective AI coding session as described by Matt Pocock:

1. **System Prompt** — The foundational context that is always present. Should be as small as possible — large system prompts push the session directly into the [[smart-zone-dumb-zone|dumb zone]] before any work begins.
2. **Exploration** — The AI agent explores the codebase, reading relevant files and understanding the existing architecture.
3. **Implementation** — The actual coding work: writing, modifying, and refactoring code.
4. **Testing** — Verification, feedback loops, and validation.

## Key Properties

- System prompt should be minimal to maximize smart zone capacity
- Exploration and testing are often undervalued compared to implementation
- Each stage consumes context window budget
- Understanding the current stage helps decide when to [[compaction-vs-clearing|clear or compact]]
- The cycle can be repeated: testing → clearing → new session for next feature

## Related Concepts

- [[smart-zone-dumb-zone]] — context budget awareness
- [[compaction-vs-clearing]] — transitioning between sessions
- [[token-awareness]] — monitoring stage progression

## References

- Pocock, M. "AI Software Engineering Workshop" — YouTube
