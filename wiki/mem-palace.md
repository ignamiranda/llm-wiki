---
title: "Mem Palace"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [claude-code, memory-systems, rag, verbatim-recall, llm]
aliases: [memory-palace]
summary: "A RAG-based Claude Code memory system that stores conversations verbatim using a memory palace indexing metaphor (wings, rooms, closets, drawers) with AAAK symbolic language for fast scanning."
source_url: "https://youtu.be/UHVFcUzAGlM"
source_hash: "f3624d705c6e04e2e7538ae9bf26cb817ebab58bc58a64cb6d04be83c6486c2e"
---

# Mem Palace

## Definition

A Claude Code memory system implementing proper RAG (Retrieval-Augmented Generation) for verbatim word-for-word recall. Uses an ancient memory palace metaphor — wings (people/projects), rooms (sessions/threads), closets (topics/bundles), and drawers (verbatim text) — to organize conversation data, with an **AAAK symbolic index** that an LLM can scan at a glance (~42ms retrieval).

## Key Properties

- **Verbatim storage**: no summarization, nothing gets lost
- **Memory palace structure**: wing → room → closet → drawer hierarchy
- **AAAK index**: a dense symbolic dialect the LLM scans in a single pass for fast lookups
- **Dual database**: SQL database for entities/relationships + ChromaDB vector database for searchable chunks
- **Background hooks**: silent indexing on session end and pre-compaction
- **Mining**: can retrospectively index past sessions
- **Single command install**: creates `.mem-palace/` folder with palace structure, registers hooks

## Trade-offs

- **Not markdown-readable**: stored in AAAK symbolic format, not plain text
- **Highest benchmarks**: reportedly the highest scoring memory system in published benchmarks
- **Local-only**: all data stored locally, not accessible across tools

## Related Concepts

- [[memsearch]] — Level 3 alternative (semantic search, markdown-readable)
- [[memory-system-ai]] — broader AI memory category
- [[context-rot]] — the problem it solves
- [[2026-06-11-claude-code-memory-systems]] — Level 4 in the taxonomy
- [[mempalace]] — separate open-source project (55.4k stars) with similar name using verbatim markdown + ChromaDB

## References

- "Every Claude Code Memory System Compared" — YouTube video
- mempalaceofficial.com
