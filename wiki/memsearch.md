---
title: "MemSearch"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [claude-code, memory-systems, semantic-search, vector-database, plugin]
aliases: [zilliz-memsearch]
summary: "A Claude Code plugin by Zilliz that ports the OpenClaude memory architecture — chunking documents into semantic vectors and auto-injecting the top matches into every prompt via hooks."
source_url: "https://youtu.be/UHVFcUzAGlM"
source_hash: "f3624d705c6e04e2e7538ae9bf26cb817ebab58bc58a64cb6d04be83c6486c2e"
---

# MemSearch

## Definition

A Claude Code plugin by Zilliz (the team behind the Milvus vector database) that implements the OpenClaude memory architecture. It chunks documents into semantic vectors and uses a `user prompt submit` hook to auto-inject the top 3 semantically relevant matches into every prompt, enabling meaning-based retrieval rather than keyword search.

## Key Properties

- Based on the **OpenClaude 3-layer model**: memory.md (durable facts), daily notes (one per date), and dreaming (background promotion to long-term)
- Uses **semantic vectors** for retrieval — understands meaning, not just keywords
- **Hook-based injection**: top matches are automatically injected at query time via `user prompt submit` hook
- **Markdown-first**: all memory remains in readable plain markdown files
- Two-line install: `/plugin marketplace add zilliztech memsearch` then `plugin install memsearch`
- Supports `/memsearch` slash command for explicit recall

## Comparison with Claude Mem

| Feature | MemSearch | Claude Mem |
|---------|-----------|------------|
| Storage | Plain markdown | MCP-based storage |
| Retrieval | Auto-injected via hooks | Claude must call MCP tool |
| Readability | Human-readable files | Summaries/timelines |
| Extra features | — | Dashboard, team collab, cost tracking |

## Related Concepts

- [[memory-system-ai]] — category of AI memory
- [[mem-palace]] — Level 4 alternative (verbatim recall)
- [[context-rot]] — the problem it solves
- [[2026-06-11-claude-code-memory-systems]] — Level 3 in the taxonomy

## References

- "Every Claude Code Memory System Compared" — YouTube video
- Zilliz MemSearch GitHub repository
