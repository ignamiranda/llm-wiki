---
title: "MemSearch"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [claude-code, memory-systems, semantic-search, vector-database, plugin, milvus]
aliases: [zilliz-memsearch]
summary: "A cross-platform semantic memory layer for AI coding agents by Zilliz, backed by Markdown (source of truth) and Milvus (shadow index), supporting Claude Code, OpenClaw, OpenCode, and Codex CLI."
source_url: "https://github.com/zilliztech/memsearch"
source_hash: "0FEED44EF088B9B44608E8EC55B4927C51CC9FE30FD64ACE22D67238A8308BF0"
---

# MemSearch

## Definition

A cross-platform semantic memory system for AI coding agents developed by Zilliz (the team behind the Milvus vector database). MemSearch uses Markdown files as the immutable source of truth and Milvus as a rebuildable shadow index for vector search. It supports Claude Code, OpenClaw, OpenCode, and Codex CLI, enabling unified memory across all tools.

## Key Properties

- **Cross-platform**: plugins for Claude Code, OpenClaw, OpenCode, and Codex CLI
- **Markdown as source of truth**: memories are plain `.md` files — human-readable, editable, version-controllable
- **Milvus shadow index**: Milvus (or Zilliz Cloud) is a derived, rebuildable cache — never the primary store
- **3-layer progressive recall**: L1 search (semantic) → L2 expand (full section) → L3 parse-transcript (raw dialogue)
- **Hybrid search**: dense vector (ONNX bge-m3) + BM25 sparse + RRF reranking
- **SHA-256 content dedup**: unchanged content is skipped during indexing
- **Live file watcher**: `memsearch watch` auto-indexes file changes in real time
- **PLuggable embedding**: ONNX bge-m3 (default, local CPU), OpenAI, Ollama, and more
- **Milvus backends**: Milvus Lite (zero-config, default), Zilliz Cloud (managed, free tier), self-hosted Milvus server
- **Python API**: `MemSearch` class with `index()`, `search()`, `watch()`, `compact()`
- **CLI**: `memsearch index`, `search`, `expand`, `watch`, `compact`, `stats`, `reset`, `config`

### 3-Layer Progressive Recall

```
L1: memsearch search "batch size"    → ranked chunks
L2: memsearch expand <chunk_hash>    → full .md section  
L3: parse-transcript <session.jsonl> → raw dialogue
```

### Architecture

```
Plugins (Claude Code, OpenClaw, OpenCode, Codex CLI)
        ↕
memsearch CLI / Python API (index, search, watch, compact)
        ↕
Core: Chunker → Embedder → Milvus
        ↕
Markdown Files (Source of Truth)
```

### Configuration

Embedding defaults to ONNX bge-m3 (local CPU, ~558 MB, downloaded on first launch). Switching to OpenAI or Ollama is a single config command. Milvus defaults to Milvus Lite (single SQLite-like file); switching to Zilliz Cloud or self-hosted Milvus is also a single config change.

## Related Concepts

- [[mempalace]] — alternative memory system using ChromaDB backend
- [[mem0]] — cloud-based alternative (API service)
- [[memory-system-ai]] — general AI memory category
- [[chromadb-ai-memory]] — ChromaDB-backed memory approach
- [[2026-06-11-claude-code-memory-systems]] — Level 3 in the Claude Code memory taxonomy

## References

- GitHub: https://github.com/zilliztech/memsearch
- Docs: https://zilliztech.github.io/memsearch/
- 2k+ stars, 364+ commits, MIT license
