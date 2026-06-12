---
title: "Open Brain Pattern"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [ai, knowledge-management, open-brain, pattern, database, supabase]
aliases: ["Open Brain approach", "structured memory pattern", "OB1 pattern"]
summary: "Nate B. Jones' structured database approach to AI memory using Supabase + pgvector + MCP server, where information is stored faithfully and synthesized fresh at query time, enabling multi-agent access and auditable provenance."
source_url: "https://github.com/NateBJones-Projects/OB1"
source_hash: "FF0E3623AA6CB3E789FB16FC79649C30CF42F01E063867CFD77D062BB6903B69"
---

# Open Brain Pattern

## Definition

A structured knowledge management approach created by [[nate-openbrain]] where information is stored faithfully in a Supabase (PostgreSQL + pgvector) database without pre-synthesis. Data is tagged, categorized, and made searchable, but the AI does not attempt to compile or connect it until a question is asked. At query time, the AI reads relevant entries and produces a fresh synthesis. This enables precise structured queries, multi-agent access, and auditable provenance.

## Key Properties

- Supabase (PostgreSQL + pgvector) as the durable structured store
- MCP server as the gateway for AI tool access
- AI acts as a reader — retrieves and synthesizes at query time
- Adding information is cheap and lazy (write a row, tag it, done)
- Complex queries cost token budget each time
- Supports multi-agent simultaneous read/write access
- Scales to thousands of entries across dozens of categories
- Provenance is clear — every claim traceable to source rows
- Extensible via extensions, recipes, and skills

### Ecosystem (OB1 Repository)

The OB1 GitHub repo (3.7k stars, 700 forks) provides:
- **Extensions**: Household Knowledge Base, Home Maintenance, Family Calendar, Meal Planning, Professional CRM, Job Hunt Pipeline
- **Recipes**: Import tools for ChatGPT, Perplexity, Obsidian, X/Twitter, Instagram, Google, Grok, Email
- **Skills**: Auto-Capture, Competitive Analysis, Research Synthesis, Meeting Synthesis, Financial Model Review, Deal Memo Drafting
- **Primitives**: Edge Functions, Remote MCP, RLS, Shared MCP Server
- **Dashboards**: SvelteKit and Next.js options

## Related Concepts

- [[query-time-knowledge]] — the underlying paradigm
- [[wiki-compile-pattern]] — the compile-time alternative
- [[hybrid-memory-architecture]] — combining both
- [[ai-as-reader]] — AI role in this pattern
- [[nate-openbrain]] — creator
- [[2026-06-11-claude-code-memory-systems]] — Level 6 in the Claude Code memory taxonomy

## References

- OB1 GitHub: https://github.com/NateBJones-Projects/OB1
- Substack: https://natesnewsletter.substack.com/
- Discord: https://discord.gg/Cgh9WJEkeG
