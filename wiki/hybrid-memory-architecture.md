---
title: "Hybrid Memory Architecture"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [ai, knowledge-management, architecture, hybrid]
aliases: ["combined memory system"]
summary: "A memory architecture that combines a structured database as durable source of truth with a compiled wiki layer generated on demand for browsable, pre-synthesized understanding."
---

# Hybrid Memory Architecture

## Definition

A proposed architecture combining the strengths of [[compile-time-knowledge]] and [[query-time-knowledge]]. A structured database (like [[open-brain-pattern]]) serves as the authoritative, single source of truth — all new information goes there first. A wiki compilation agent runs on a schedule (daily, weekly, on-demand) that reads from the database, synthesizes across entries via AI, and produces wiki pages (like [[wiki-compile-pattern]]) as generated artifacts. The wiki is never edited directly, preventing error compounding.

## Key Properties

- Database is always authoritative; wiki is regenerated from it
- Wiki never drifts from reality — always rebuilt from ground truth
- Can filter by date, category, or confidence before synthesizing
- Wiki pages are browsable in Obsidian or any note app
- Supports both precise queries (database) and synthesized understanding (wiki)
- Multi-agent safe: all agents write to database, wiki is a read-only compilation

## Examples

Open Brain's "wiki compiler recipe": a composable workflow that queries relevant tables, synthesizes pages through AI, and writes output to a wiki directory. Can run on an automated schedule, improving each cycle as the underlying data grows.

## Related Concepts

- [[compile-time-knowledge]] — wiki compilation phase
- [[query-time-knowledge]] — database query phase
- [[wiki-compile-pattern]] — the compilation output format
- [[open-brain-pattern]] — the underlying structured store

## References

- Nate. "Karpathy Wiki vs Open Brain" — YouTube
