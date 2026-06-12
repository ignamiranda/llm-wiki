---
title: "Karpathy's Original LLM Wiki Gist"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [llm-wiki, karpathy, knowledge-management, personal-knowledge-base]
source_url: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
source_hash: "A6EF621F32A2022EA09802F791ED73C1DB35997AC1C364271D06EEB6EE1421AD"
summary: "Andrej Karpathy's canonical gist (April 4, 2026) describing the LLM Wiki pattern — a three-layer architecture for building persistent, interlinked knowledge bases using LLMs as the maintainer."
---

# Karpathy's Original LLM Wiki Gist

## Summary

Andrej Karpathy's foundational gist describing the LLM Wiki pattern — a structured approach to building persistent knowledge bases where LLMs handle the maintenance burden that causes humans to abandon wikis. The core insight: instead of re-retrieving raw documents at every query (RAG), the LLM incrementally builds and maintains a structured, interlinked collection of markdown files that compounds knowledge over time.

## Content

### Three-Layer Architecture

1. **Raw sources** — curated, immutable source documents (articles, papers, images). The LLM reads but never modifies.
2. **The wiki** — LLM-generated markdown files: summaries, entity pages, concept pages, cross-references. The LLM owns this layer entirely.
3. **The schema** — a configuration document (CLAUDE.md or AGENTS.md) defining wiki structure, conventions, and workflows.

### Operations

- **Ingest**: Drop a source, LLM reads it → discusses with user → writes summary page → updates index → updates related entity/concept pages → logs the change. A single source may touch 10-15 pages.
- **Query**: Ask questions against the wiki. LLM searches index → reads relevant pages → synthesizes answer with citations. Answers can be filed back as new pages to compound knowledge.
- **Lint**: Health-check the wiki for contradictions, stale claims, orphan pages, missing cross-references.

### Indexing

- **index.md** — content-oriented catalog of every page with one-line summaries, organized by category
- **log.md** — chronological, append-only record of ingests, queries, and lint passes

### Tools & Tips

- Obsidian as IDE, LLM as programmer, wiki as codebase
- Obsidian Web Clipper to convert articles to markdown
- Marp for slide decks from wiki content
- Dataview for queries over page frontmatter
- Git for version history, branching, collaboration
- qmd (optional) for local search with hybrid BM25/vector

### Why This Works

The tedious part of maintaining a knowledge base is bookkeeping — updating cross-references, keeping summaries current, noting contradictions. LLMs don't get bored and can touch 15 files in one pass. The human curates sources and asks good questions; the LLM does everything else.

## Key Takeaways

- Knowledge is compiled once and kept current, not re-derived on every query
- The wiki is a persistent, compounding artifact that gets richer with every source
- Related in spirit to Vannevar Bush's Memex (1945) — associative trails between documents
- All details are modular and customizable per domain

## Related

- [[andrej-karpathy]] — creator
- [[wiki-compile-pattern]] — the compile-time pattern this embodies
- [[2026-06-11-karpathy-wiki-vs-open-brain]] — comparison with Open Brain
- [[memory-system-ai]] — category of AI memory system
