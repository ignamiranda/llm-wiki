---
title: "Every Claude Code Memory System Compared"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [claude-code, memory-systems, ai-agents, knowledge-management, context, rag]
summary: "A comprehensive walkthrough of 6 levels of Claude Code memory systems — from native claude.md and memory.md through enhanced hooks, semantic search, verbatim recall, knowledge bases, and cross-tool architectures."
source_url: "https://youtu.be/UHVFcUzAGlM"
source_hash: "f3624d705c6e04e2e7538ae9bf26cb817ebab58bc58a64cb6d04be83c6486c2e"
---

# Every Claude Code Memory System Compared

## Summary

A survey of six levels of memory systems for Claude Code, each solving harder context retrieval problems. Level 1 covers native built-in memory ([[claude-md]], memory.md, the unreleased [[kairos]] daemon). Level 2 adds structured hooks and cross-project memory sharing ([[john-connolly]]'s system based on [[pavel-huryn]]'s pattern). Level 3 introduces semantic vector search via [[memsearch]] (Zilliz/OpenClaude). Level 4 enables verbatim word-for-word recall via [[mem-palace]] (RAG with memory palace indexing). Level 5 covers knowledge bases (Karpathy's LLM Wiki, Recall, LightRAG). Level 6 enables cross-tool memory ([[open-brain-pattern]], Mem0).

## Content

### Core Insight

Every memory system answers the same question: when you give Claude Code a task, how does it pull the right context at the right time? The differences come down to two variables:

1. **Storage mechanism** — where memory lives (markdown files, vector databases, SQL, cloud services)
2. **Retrieval stage** — how Claude accesses it (auto-injected at session start, searched on demand, injected via hooks at query time)

### Level 1 — Native Claude Code Memory

The built-in memory that ships with Claude Code:

- **[[claude-md]]** — A plain markdown file in the project folder storing rules, brand info, coding style. Always loaded into every session. Should stay under **200 lines** to avoid [[context-rot]] (degraded recall as context grows). External files referenced from claude.md are loaded only when needed.
- **Auto Memory (memory.md)** — Per-project memory structure using an index file (`memory.md`) that points to separate files for specific topics. Created automatically by the `/memory` command. Follows the same principle: treat memory.md as an index, not a dump.
- **[[kairos]]** — An unreleased Anthropic system (found in leaked Claude Code source) described as an "always-on daemon that watches your project continuously, decides what's worth remembering, and consolidates old notes while you sleep."

### Level 2 — Enhanced Structure + Hooks

Developed by [[john-connolly]] based on [[pavel-huryn]]'s concept, this level improves reliability of memory injection:

- Structured memory system at `.claude/memory/` with `general.md` (cross-project facts), `domain/topic/` files (domain-specific knowledge), and `tools/` files (tool configs)
- A **session start hook** auto-injects the memory.md index at the start of every session
- Potential for **team sharing** — syncing domain files between teammates

The key workflow: (1) paste a setup prompt into Claude Code, (2) run "reorganize memory" to consolidate files, (3) install a pre-tool hook in `settings.json` for auto-injection.

### Level 3 — Semantic Search (MemSearch)

As memory scales beyond a handful of files, keyword search breaks down. Level 3 solves this with [[memsearch]], a plugin by Zilliz based on the OpenClaude memory architecture:

- **OpenClaude's 3-layer model**: (a) `memory.md` for durable long-term facts loaded every session, (b) daily notes (one file per date, with today+yesterday auto-loaded, older notes on disk), (c) **dreaming** — a background process that scores daily notes and promotes recurring patterns to long-term memory
- **MemSearch plugin**: chunks documents into semantic vectors, uses a hook (`user prompt submit`) to auto-inject the top 3 semantic matches into every prompt
- **Markdown-first**: all memory remains in readable plain markdown

**Alternative: Claude Mem** — an MCP-based plugin with a dashboard, team collaboration, cost tracking, and privacy labels. However, MCP means Claude must actively decide to search (vs. auto-injection), and it stores summaries rather than verbatim markdown.

### Level 4 — Verbatim Recall (Mem Palace)

For exact word-for-word recall of past decisions, [[mem-palace]] implements a proper RAG system:

- **Memory Palace metaphor**: knowledge organized in wings (people/projects), rooms (sessions/threads), closets (topics), and drawers (verbatim text)
- **AAAK symbolic index** — a dense symbolic dialect an LLM can scan at a glance. The model scans thousands of drawers in a single pass (~42ms retrieval)
- **Two databases**: SQL database tracking entities and relationships, ChromaDB vector database storing searchable conversation chunks
- **Background hooks**: stores and indexes information silently on session end and pre-compaction
- **Mining**: can retrospectively index past sessions
- **Trade-off**: not markdown-readable (stored in symbolic index format), but offers highest benchmark scores for memory systems

### Level 5 — Knowledge Bases

Not about remembering conversations, but building interconnected knowledge bases:

- **Karpathy's LLM Wiki** — compile-time knowledge pattern: drop raw sources in `.raw/`, Claude reads and writes structured wiki pages in plain markdown. Best for deep research on specific topics where interconnections matter.
- **Recall** — hosted service (browser extension + AI chat) that does the LLM Wiki pattern as a managed service. Trade-offs: no data ownership (rent vs. own), built for content consumption not operational memory, has pricing.
- **LightRAG** — enterprise-grade knowledge graph with entity extraction and dual-level retrieval. Overkill for most use cases.

### Level 6 — Cross-Tool Memory

For users who work across multiple AI tools (Claude Code, ChatGPT, Cursor, etc.) and need shared memory:

- **[[open-brain-pattern]] (Nate Jones)** — Own your memory in a Postgres database (Supabase, ~$0.10-0.30/mo). One `thoughts` table with text, embedding vector, tags, and timestamp. An MCP server connects Claude Code to Supabase edge functions, and every AI tool queries through the same API. Downsides: complex setup (30-45 min), external database latency, data not local.
- **Mem0** — Hosted cross-tool memory layer (100k+ developers). Faster setup (under a minute), production-ready, but data lives on their servers vs. self-hosted Postgres.

## Key Takeaways

- Most users should stop at Level 2 (enhanced hooks + structured memory)
- Level 3 (MemSearch) is needed when memory files exceed what keyword search can handle
- Level 4 (Mem Palace) is for verbatim conversation recall
- Levels 5-6 serve specialized needs (deep research, cross-tool memory)
- Levels stack — you can run 1+2+3 together
- Keep [[claude-md]] under 200 lines; use external files referenced by the index

## Related

- [[memory-system-ai]] — general concept of AI memory systems
- [[context-rot]] — the problem these systems solve
- [[claude-md]] — native project-level instructions
- [[kairos]] — Anthropic's unreleased memory daemon
- [[memsearch]] — Zilliz semantic search plugin
- [[mem-palace]] — verbatim RAG with memory palace indexing
- [[open-brain-pattern]] — cross-tool memory architecture
- [[nate-openbrain]] — creator of Open Brain
- [[john-connolly]] — enhanced memory hooks
- [[pavel-huryn]] — structured memory pattern originator
