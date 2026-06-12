---
title: "Knowledge Contradiction Preservation"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [ai, knowledge-management, contradiction, data-integrity]
aliases: ["contradiction preservation", "tension preservation"]
summary: "The practice of preserving contradictory facts in a knowledge system rather than resolving them, because the tension between conflicting claims is itself valuable strategic signal."
---

# Knowledge Contradiction Preservation

## Definition

A design principle in knowledge management where contradictory information is preserved rather than synthesized away. When two sources make conflicting claims, the gap between them is potentially the most valuable signal in the knowledge base. For example, engineering saying a build takes 12 weeks while sales promised 8 — the gap itself is the problem leadership needs to see. A well-meaning wiki might smooth this into a single "10 week" narrative, destroying the signal.

## Key Properties

- Contradictions are strategic signals, not bugs
- Compile-time systems surface contradictions at ingest (if prompted)
- Query-time systems require explicit contradiction checking
- Synthesized narratives can hide critical misalignment
- Raw data preserves tension that synthesis erases

## Related Concepts

- [[compile-time-knowledge]] — may surface contradictions at ingest
- [[query-time-knowledge]] — requires audit to surface contradictions
- [[wiki-compile-pattern]] — risks smoothing contradictions away

## References

- Nate. "Karpathy Wiki vs Open Brain" — YouTube
