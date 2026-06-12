# Ingest Analysis — AI Memory Systems Batch (9 sources)
**Batch hash:** BATCH-2026-06-11-AI-MEMORY
**Language detected:** en
**Analyzed:** 2026-06-11T20:30:00Z

## Source Summary

Batch of 9 sources covering AI memory systems for coding agents and personal knowledge management. Includes the original Karpathy LLM Wiki gist, the actual GitHub repos for memsearch (Zilliz), mempalace, OB1 (Open Brain), and mem0, plus detailed articles by John Conneely and Pavel Huryn on structured Claude Code memory, and commercial offerings (Recall, Simon Scrapes community).

## Source Hashes & Files

| Source | Hash | Raw File |
|--------|------|----------|
| skool.com/scrapes (Agentic Academy) | `5978B0F8...` | `.raw/01-skool-scrapes.txt` |
| Young Leaders in Tech #98 (John Conneely) | `20A0D91C...` | `.raw/02-youngleaders-claude-memory.txt` |
| Pavel Huryn Substack Note | `0C920A79...` | `.raw/03-pawel-huryn-memory-note.txt` |
| zilliztech/memsearch | `0FEED44E...` | `.raw/04-memsearch.txt` |
| MemPalace/mempalace | `0EE4C182...` | `.raw/05-mempalace.txt` |
| Karpathy LLM Wiki gist | `A6EF621F...` | `.raw/06-karpathy-llm-wiki-gist.txt` |
| recall.it | `38D60B3F...` | `.raw/07-recall.txt` |
| mem0.ai | `F7631460...` | `.raw/08-mem0.txt` |
| NateBJones-Projects/OB1 | `FF0E3623...` | `.raw/09-ob1-open-brain.txt` |

## Concepts to Create

| Concept | Action | Reason |
|---------|--------|--------|
| mem0 | create | New concept — YC-backed AI memory layer as a service, SOC 2/HIPAA compliant, cloud API |
| recall-knowledge-base | create | New concept — SaaS personal knowledge base with AI chat, summaries, spaced repetition |

## Concepts to Update

| Concept | Action | Reason |
|---------|--------|--------|
| memsearch | major update | Current page based on YouTube summary; actual repo has much more detail (4 platforms, 3-layer recall, Milvus shadow index, hybrid search BM25+vector+RRF, SHA-256 dedup, live watcher, Python API) |
| mem-palace | major update | Current page describes "AAAK symbolic format" which appears inaccurate — actual MemPalace uses verbatim markdown storage with ChromaDB backend. Needs contradiction flag. |
| open-brain-pattern | update | Add OB1 GitHub repo details (extensions, recipes, skills, Supabase+pgvector architecture) |
| memory-system-ai | minor update | Add references to new systems from this batch |

## Persons to Update

| Person | Action | Details |
|--------|--------|---------|
| pavel-huryn | major update | Date is wrong (shown as 2025, should be Feb 18, 2026). Need to add actual Substack note URL, mention follow-up on error logging/knowledge graduation. |
| john-connolly | major update | Current page is sparse (from YouTube summary). John Conneely (note spelling: currently "Connolly" but actual name is "Conneely") wrote a detailed Substack article (#98) with complete setup prompts, PreToolUse hook, PPID-based dedup, memory structure, team sharing via git. |
| nate-openbrain | update | Add OB1 GitHub repo URL, extension list, community contributions, Discord/Substack links |
| andrej-karpathy | minor update | Add "Created the LLM Wiki pattern" to contributions, link to the gist |

## Pages to Create

| Filename | Type | Title | Key Content |
|----------|------|-------|-------------|
| 2026-06-11-karpathy-llm-wiki-original-gist | article | Karpathy's Original LLM Wiki Gist | Summary of the canonical gist: three-layer architecture, operations (ingest/query/lint), indexing/logging, Obsidian integration tips |
| 2026-06-11-john-conneely-claude-memory-setup | article | How I Finally Sorted My Claude Code Memory — John Conneely | Full detailed article: structured memory system, PreToolUse hook, PPID-based dedup, auto-init, domain knowledge lifecycle |
| mem0 | concept | Mem0 | AI memory layer as a service, Memory Compression Engine, YC-backed, SOC 2/HIPAA |
| recall-knowledge-base | concept | Recall | SaaS knowledge base with AI chat, summaries, auto-tagging, spaced repetition quizzes, MCP/API access |

## Pages to Update

| Page | What Changed |
|------|-------------|
| memsearch.md | Major update: 4 platform support, 3-layer progressive recall, hybrid search (BM25+vector+RRF), SHA-256 dedup, live watcher, Python API, CLI reference, configuration options. Update source_url to GitHub. |
| mem-palace.md | Major rewrite needed: Actual MemPalace is ChromaDB-backed verbatim markdown storage with 96.6% R@5 on LongMemEval. Current page describes "AAAK symbolic format" which seems to conflate different tools. Flag contradiction. |
| open-brain-pattern.md | Minor update: add OB1 repo details — extensions (household, calendar, CRM, etc.), recipes, skills, community contributions. |
| pavel-huryn.md | Fix date (2025→2026). Add actual Substack URL and follow-up post reference. |
| john-connolly.md | Fix name spelling (Connolly→Conneely). Major content expansion with full system details. Update source_url to actual Substack article. |
| nate-openbrain.md | Update with OB1 GitHub URL, full extension list, community stats (3.7k stars, 700 forks). |

## Contradictions Detected

| Existing Page | New Claim | Conflict |
|---------------|-----------|----------|
| [[mem-palace]] | MemPalace stores conversations as verbatim markdown text with ChromaDB backend (wing→room→drawer hierarchy) | Current page says "Not markdown-readable: stored in AAAK symbolic format, not plain text" and references "mem-palace" as AAAK-based. The GitHub repo (55.4k stars) at `MemPalace/mempalace` uses plain markdown. May be describing a different tool with the same name. **Action: flag for user review** |

## Proposed Cross-Links

- [[memsearch]] ↔ [[mem0]] — competing/production memory services (self-hosted vs cloud)
- [[memsearch]] ↔ [[mempalace]] — both open-source memory systems with different approaches (Milvus vs ChromaDB)
- [[memsearch]] ↔ [[chromadb-ai-memory]] — related vector-DB-backed memory systems
- [[2026-06-11-karpathy-llm-wiki-original-gist]] ↔ [[andrej-karpathy]] — creator
- [[2026-06-11-karpathy-llm-wiki-original-gist]] ↔ [[wiki-compile-pattern]] — the pattern itself
- [[john-conneely]] ↔ [[pavel-huryn]] — connected work
- [[open-brain-pattern]] ↔ [[ob1-github]] — implementation reference
- [[mem0]] ↔ [[memory-system-ai]] — cloud memory system category
- [[recall-knowledge-base]] ↔ [[memory-system-ai]] — alternate approach (SaaS PKM)

## Items for User Review

- [ ] **Contradiction in mem-palace.md**: Does "Mem Palace" (AAAK) and "MemPalace" (ChromaDB/verbatim) refer to the same tool or different ones? The GitHub repo has 55.4k stars and uses plain markdown + ChromaDB, while the existing page describes AAAK symbolic format.
- [ ] **Simon Scrapes Agentic Academy**: This is a commercial community (1.5k members, $37/month) — not knowledge content suitable for the wiki. Skip or create a minimal note?
- [ ] **Recall, mem0, Karpathy gist**: These are new tools/concepts not yet in the wiki. Should all get their own pages or be integrated into existing pages?
- [ ] Proceed to Phase 2 after review?
