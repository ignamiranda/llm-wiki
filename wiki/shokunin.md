---
title: Shokunin
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [agent-skills, ai-engineering, opencode, chromadb, mcp-server, skill-development,
  persistent-memory, ci-cd]
aliases:
- shokunin-ecosystem
summary: An open-source ecosystem of 62 CI-validated AI agent engineering skills with
  ChromaDB persistent memory and MCP servers, supporting multiple AI coding runtimes.
---


# Shokunin

## Definition

Shokunin (, Japanese for "artisan") is an open-source ecosystem by [[elias-oulkadi]] that bundles 62 engineering skills, ChromaDB-based persistent memory, and MCP servers into a single-command install for AI coding agents. Skills are organized across 10 domains and are CI-validated for frontmatter, workflow structure, error handling, and cited sources. The ecosystem is runtime-agnostic with native support for OpenCode, Claude Code, Cursor, Windsurf, Cline, and Continue.dev.

## Key Properties

- **62 skills** across 10 engineering domains (infrastructure, backend, frontend, mobile, quality, content, documents, productivity, AI agents, system)
- **CI-validated** — every skill checked for frontmatter, workflow, error handling, and sources on push
- **ChromaDB memory** — persistent context with multi-strategy recall (vector + BM25 + temporal + RRF)
- **9 MCP tools** — store_context, search_context, multi_search_context, session management, verify_file_path
- **Declarative self-updates** — manifest-driven with drift detection
- **Multi-runtime** — OpenCode (native), Claude Code (MCP), Cursor/Windsurf/Cline/Continue.dev (rules)
- **Freshness decay** — exponential recency blending with 30-day half-life
- **Zero-install ChromaDB** — SQLite-backed local vector database

## Examples

- A Docker skill with 1,422 words including a multi-stage Node.js template, BuildKit cache optimization, distroless base images, and CVE scanning.
- An auth skill referencing OWASP directly with production checklists and anti-patterns.
- A database skill with real EXPLAIN ANALYZE output integrated into the prompt.
- Frontend skills incorporating Emil Kowalski patterns (Sonner, Vaul), Paul Bakaus principles (Impeccable), and Leon Lin variance engines (Taste).

## Related Concepts

- [[agent-skills]] — the general framework for AI agent skills; Shokunin is a concrete large-scale implementation
- [[claude-skills-plugin]] — plugin marketplace; Shokunin is broader, covering 6 runtimes
- [[skill-file-format]] — SKILL.md conventions used by all Shokunin skills
- [[chromadb-ai-memory]] — the memory subsystem within Shokunin
- [[2026-06-11-shokunin]] — article with full source attribution and overview
- [[2026-06-11-mattpocock-skills]] — comparable skill ecosystem with different scope
- [[2026-06-11-anthropic-skills-repo]] — comparable skill ecosystem by Anthropic

## References

- Source: https://github.com/EliasOulkadi/shokunin
- Linked from [[2026-06-11-shokunin]]
