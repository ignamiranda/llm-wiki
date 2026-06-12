---
title: "Memory Architecture Fork"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [ai, knowledge-management, architecture, design-decision]
aliases: ["knowledge system fork"]
summary: "The fundamental design decision every AI knowledge system must make: does the AI do its hard thinking when information arrives (compile-time) or when a question is asked (query-time)?"
---

# Memory Architecture Fork

## Definition

The binary design choice that defines every AI-powered knowledge system: **when does the AI do the cognitive work?** At information ingest time ([[compile-time-knowledge]]) or at query time ([[query-time-knowledge]])? This decision cascades into every other design aspect — storage format, AI role, scalability characteristics, staleness behavior, and use case fit.

## Key Properties

- Every system must pick one side of the fork or the other, or build a hybrid
- The choice determines the AI's primary job: writer vs reader
- Compile-time gives pre-built understanding; query-time gives precise, auditable answers
- The fork is about trading off front-end cost (ingest) vs back-end cost (query)
- Staleness manifests differently on each side

## Examples

- [[wiki-compile-pattern]] (Karpathy) — compile-time side
- [[open-brain-pattern]] (Nate) — query-time side
- [[hybrid-memory-architecture]] — attempts to bridge both sides

## Related Concepts

- [[compile-time-knowledge]] — ingest-time synthesis
- [[query-time-knowledge]] — query-time synthesis
- [[ai-as-writer]] — role in compile-time
- [[ai-as-reader]] — role in query-time

## References

- Nate. "Karpathy Wiki vs Open Brain" — YouTube
