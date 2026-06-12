---
title: "Query-Time Knowledge"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [ai, memory-systems, knowledge-management, architecture]
aliases: ["query-time synthesis", "fresh synthesis"]
summary: "An approach to AI knowledge management where thinking happens at query time — data is stored faithfully without synthesis, and the AI reads relevant entries and synthesizes fresh answers on demand."
---

# Query-Time Knowledge

## Definition

A knowledge management paradigm where information is stored faithfully with minimal transformation (tagging, categorization) and the AI does its cognitive work when a question is asked. The AI reads relevant entries from structured storage and produces a fresh synthesis on the fly. This is the approach used by the [[open-brain-pattern]].

## Key Properties

- Cognitive work happens at query time, not ingest time
- Fresh synthesis means answers reflect all available data
- Reading is the dominant AI activity
- Adding new information is cheap and lazy
- Provenance is clear — claims traceable to source data
- Complex queries may be expensive (AI processes each time)
- Supports multi-agent access and structured queries

## Examples

Open Brain: when a user adds a meeting note, it is stored as a row with tags. When the user later asks "Show me all pricing discussions from Q1," the AI searches the database, reads relevant entries, and synthesizes a fresh answer specific to that query.

## Related Concepts

- [[compile-time-knowledge]] — the opposing approach
- [[memory-architecture-fork]] — the fundamental design choice
- [[open-brain-pattern]] — concrete implementation
- [[ai-as-reader]] — AI role in this paradigm

## References

- Nate (Open Brain). "Karpathy Wiki vs Open Brain" — YouTube
