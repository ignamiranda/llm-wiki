---
title: "MemPalace"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [memory-systems, ai-agents, chromadb, verbatim-recall, open-source]
aliases: [mempalace-github, mempalace-chromadb]
summary: "A local-first, open-source AI memory system using verbatim markdown storage with a pluggable ChromaDB backend, achieving 96.6% R@5 raw on LongMemEval with zero API calls."
source_url: "https://github.com/MemPalace/mempalace"
source_hash: "0EE4C1828DE1BB9A5554C8CA83E5349FD8CA468B6CD263119C1F96F58B03FE7A"
---

# MemPalace

## Definition

MemPalace is an open-source (MIT, 55.4k+ stars) local-first AI memory system that stores conversation history as verbatim text and retrieves it with semantic search. It does not summarize, extract, or paraphrase. The index is structured — people and projects become *wings*, topics become *rooms*, and original content lives in *drawers* — so searches can be scoped rather than run against a flat corpus.

## Key Properties

- **Verbatim storage**: stores full conversation text without summarization or paraphrasing
- **Pluggable backend**: ChromaDB (default), sqlite_exact, Qdrant (REST), pgvector (Postgres)
- **96.6% R@5 raw on LongMemEval** — no API key, no cloud, no LLM required
- **Hybrid v4**: 98.4% R@5 with keyword + temporal boosting (tuned on held-out set)
- **+LLM rerank**: >=99% with any capable model (Claude Haiku, Sonnet, minimax-m2.7)
- **Knowledge graph**: temporal entity-relationship graph with validity windows, backed by local SQLite
- **29 MCP tools** covering palace reads/writes, knowledge graph ops, drawer management, agent diaries
- **Auto-save hooks** for Claude Code, Codex CLI, and Cursor IDE
- **Multiple embedding models**: embeddinggemma-300m (multilingual, 100+ languages) or all-MiniLM-L6-v2
- **Agents**: each specialist agent gets its own wing and diary in the palace, discoverable at runtime
- **Docker support**: CPU and GPU (CUDA) images available

## Benchmarks

| Benchmark | Metric | Score | Notes |
|-----------|--------|-------|-------|
| LongMemEval (raw) | R@5 | 96.6% | No LLM, no heuristics |
| LongMemEval (hybrid v4) | R@5 | 98.4% | Held-out 450q |
| LongMemEval (+LLM rerank) | R@5 | >=99% | Any capable model |
| LoCoMo (raw) | R@10 | 60.3% | 1,986 questions |
| LoCoMo (hybrid v5) | R@10 | 88.9% | Same set |
| ConvoMem (all categories) | Avg recall | 92.9% | 50 per category |
| MemBench (ACL 2025) | R@5 | 80.3% | 8,500 items |

## Related Concepts

- [[memsearch]] — alternative with Milvus backend
- [[chromadb-ai-memory]] — ChromaDB-based memory system
- [[memory-system-ai]] — general AI memory category
- [[mem0]] — cloud-based alternative

## References

- GitHub: https://github.com/MemPalace/mempalace
- Docs: https://mempalaceofficial.com
