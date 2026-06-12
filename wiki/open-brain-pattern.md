---
title: "Open Brain Pattern"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [ai, knowledge-management, open-brain, pattern, database]
aliases: ["Open Brain approach", "structured memory pattern"]
summary: "Nate's structured database approach to AI memory: store information faithfully in a SQL database, synthesize fresh answers at query time, enabling multi-agent access and precise structured queries."
---

# Open Brain Pattern

## Definition

A structured knowledge management approach where information is stored faithfully in a SQL database without pre-synthesis. Data is tagged, categorized, and made searchable, but the AI does not attempt to compile or connect it until a question is asked. At query time, the AI reads relevant entries and produces a fresh synthesis. This enables precise structured queries, multi-agent access, and auditable provenance.

## Key Properties

- SQL database as durable structured store
- AI acts as a reader — retrieves and synthesizes at query time
- Adding information is cheap and lazy (write a row, tag it, done)
- Complex queries cost token budget each time
- Supports multi-agent simultaneous read/write access
- Scales to thousands of entries across dozens of categories
- Provenance is clear — every claim traceable to source rows

## Examples

Open Brain: when a user adds meeting notes, articles, research findings, tasks, and contacts, they are stored in structured tables. A question like "Show me every competitor update from Q3" triggers the AI to search, read, and synthesize a fresh answer from the underlying data.

## Related Concepts

- [[query-time-knowledge]] — the underlying paradigm
- [[wiki-compile-pattern]] — the compile-time alternative
- [[hybrid-memory-architecture]] — combining both
- [[ai-as-reader]] — AI role in this pattern
- [[nate-openbrain]] — creator
- [[2026-06-11-claude-code-memory-systems]] — Level 6 in the Claude Code memory taxonomy

## References

- Nate. "Karpathy Wiki vs Open Brain" — YouTube
