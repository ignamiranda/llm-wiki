---
title: ChromaDB AI Memory / ChromaDB AI
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [chromadb, persistent-memory, vector-database, ai-agents, mcp, recall, retrieval]
aliases:
- chromadb-memory
- chromadb-agent-memory
summary: A persistent memory system for AI coding agents backed by ChromaDB, implementing
  multi-strategy recall with vector search, BM25, temporal decay, and reciprocal rank
  fusion.
---


# ChromaDB AI Memory

## Definition

ChromaDB AI Memory is a persistent context system for AI coding agents that uses ChromaDB (a SQLite-backed local vector database) to store and retrieve session data across runs. It implements multi-strategy recall combining vector similarity search, BM25 keyword matching, temporal freshness decay, and reciprocal rank fusion (RRF) to surface the most relevant context.

## Key Properties

- **Multi-strategy recall** — vector search (ChromaDB) + BM25 + temporal + RRF merged results
- **Freshness decay** — exponential recency blending with 30-day half-life; old memories fade over time
- **Claim verification** — `verify_file_path` MCP tool validates file paths from old memory before the agent acts on them
- **Session management** — explicit continue via `continue_session`; no guessing which session to resume
- **9 MCP tools** — store_context, search_context, get_session_summary, multi_search_context, consolidate_memories, list_sessions, continue_session, save_message, verify_file_path
- **3-layer capture** — structured data capture with auto-save wrapper on exit
- **Local-only** — all data at `~/.shokunin/memory/`, no cloud, no telemetry

## Examples

- After an agent works on a project, the session is saved to ChromaDB. On the next start, the agent can `continue_session <id>` to restore full context.
- Search across all past memory: `python ~/.shokunin/scripts/chroma-helper.py recall "docker deployment"`
- Memory test suite and healthcheck scripts validate all components.

## Related Concepts

- [[shokunin]] — the ecosystem that packages this memory system
- [[agent-skills]] — memory as a cross-cutting capability for agents
- MCP (Model Context Protocol) — the protocol through which memory tools are exposed
- [[claude-skills-plugin]] — alternative approach to agent capability distribution

## References

- Part of the [[shokunin]] ecosystem (source: https://github.com/EliasOulkadi/shokunin)
- Described in [[2026-06-11-shokunin]]
