---
title: "Compile-Time Knowledge"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [ai, memory-systems, knowledge-management, architecture]
aliases: ["compile-time synthesis", "pre-built knowledge"]
summary: "An approach to AI knowledge management where thinking happens at information ingest time — the AI reads, synthesizes, and writes understanding into a knowledge base so that future queries require only retrieval, not re-synthesis."
---

# Compile-Time Knowledge

## Definition

A knowledge management paradigm where the AI does its cognitive work when information enters the system. The AI reads the source material, extracts key concepts, connects them to existing knowledge, flags contradictions, and writes the synthesis into a persistent store. Future queries against this store are lightweight — the thinking has already been done. This is the approach pioneered by the [[wiki-compile-pattern]].

## Key Properties

- Cognitive work happens at ingest time, not query time
- Pre-built synthesis enables fast, cheap queries
- Knowledge compounds as more sources are added
- Contradictions are surfaced at ingestion
- Requires editorial judgment calls from the AI
- Writing is the dominant AI activity

## Examples

Karpathy's LLM Wiki pattern: when a user drops a research paper into the wiki, the AI reads it, updates relevant pages, and connects it to existing knowledge. Next week, when the user asks a question, the AI reads the pre-built synthesis rather than re-processing all source documents.

## Related Concepts

- [[query-time-knowledge]] — the opposing approach
- [[memory-architecture-fork]] — the fundamental design choice
- [[wiki-compile-pattern]] — concrete implementation
- [[ai-as-writer]] — AI role in this paradigm

## References

- Karpathy, A. "LLM Wiki" — GitHub gist
