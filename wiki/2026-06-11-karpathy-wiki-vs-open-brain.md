---
title: "Karpathy Wiki vs Open Brain — Two Memory Architectures"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [ai, memory-systems, knowledge-management, llm-wiki, open-brain, compile-time, query-time]
summary: "Nate compares Andrej Karpathy's LLM Wiki pattern (compile-time synthesis, file-based) with Open Brain (query-time synthesis, structured database), proposing a hybrid model combining both approaches."
source_url: https://www.youtube.com/watch?v=dxq7WtWxi44
source_hash: 038F3058CAD3EA44BDF9259D759CD57472F28C3A5ACA37BFD330430183FC48CC
---

# Karpathy Wiki vs Open Brain — Two Memory Architectures

## Summary

A detailed comparison between two AI memory architectures: Karpathy's LLM Wiki pattern (compile-time, file-based, AI-as-writer) and Open Brain (query-time, structured database, AI-as-reader). The video argues that the fundamental design choice is when the AI does its hard thinking — at information ingest time (Wiki) or at query time (Open Brain). Both systems share principles (user-owned data, human-as-curator, intentional structure) but excel at different use cases. A hybrid model is proposed where Open Brain serves as the authoritative structured store and a wiki layer is generated as a compiled view on demand.

## Content

### The Compile-Time vs Query-Time Fork

The core distinction between the two approaches is a fundamental architectural decision: **when does the AI do the hard thinking?** Every knowledge system with an AI at its core must answer this question.

- **Karpathy's Wiki (compile-time)**: When a new source arrives, the AI actively works against it — extracts concepts, cross-references, flags contradictions, and writes understanding into the wiki. The hard work happens at ingest. Afterward, browsing the wiki requires virtually no AI work — it's pure retrieval.

- **Open Brain (query-time)**: When new information arrives, it is stored faithfully with tags and categorization but no synthesis. The hard work happens when a question is asked — the AI reads relevant entries, synthesizes fresh, and produces an answer on the fly.

### AI Job Description

- **AI as Writer (Wiki)**: The AI's primary job is maintaining documents — reading raw material, synthesizing, writing, linking, cross-referencing, indexing. It makes editorial judgments about importance and connections.

- **AI as Reader (Open Brain)**: The AI's primary job is answering questions by pulling from structured data and producing precise, fresh synthesis based on all available detail.

### Strengths by Use Case

**Wiki wins when:**
- Deep research mode (reading 10+ papers on a topic over weeks)
- Personal knowledge evolution over months
- Value is in connections between sources
- Solo researcher scenario
- Zero infrastructure, running in 30 minutes

**Open Brain wins when:**
- Precise structured queries ("Show me every meeting note from Q1 where pricing was discussed")
- Multi-agent access (multiple AI tools reading/writing same data)
- High volume (thousands of entries across dozens of categories)
- Team/org usage with conflicting perspectives
- Operational data (project status, deal flow, competitive positioning)

### The Hybrid Model

The proposed hybrid architecture keeps Open Brain as the permanent, authoritative structured store. A wiki compiler recipe runs on a schedule (daily, weekly, on-demand) that reads from the database, synthesizes across entries via AI, and produces wiki pages as generated artifacts. This gives both precise query capability and browsable compiled understanding.

### Breaking Points

- **Wiki breakage at scale**: Multi-agent conflicts, team usage, knowledge drift from neglected synthesis
- **Open Brain breakage at scale**: Synthesis quality varies, no browsable artifact, contradictions are silent
- **Wiki staleness**: Looks like confident misinformation (prose that reads well but is wrong)
- **Database staleness**: Looks like ignorance (gaps in data, old facts still true)

## Key Takeaways

- The fundamental fork in memory architecture is compile-time vs query-time knowledge synthesis
- Wiki excels at deep research and connection-building; Open Brain excels at precise queries and scale
- A hybrid approach combines both: structured data as source of truth, wiki as compiled view
- Staleness looks different in each system — confident prose vs visible gaps
- Multi-agent access fundamentally requires structured storage

## Related

- [[compile-time-knowledge]] — knowledge compiled at ingest time
- [[query-time-knowledge]] — knowledge synthesized at query time
- [[memory-architecture-fork]] — the fundamental design choice
- [[wiki-compile-pattern]] — Karpathy's approach
- [[open-brain-pattern]] — Nate's approach
- [[hybrid-memory-architecture]] — combining both
- [[ai-as-writer]] — AI role in compile-time systems
- [[ai-as-reader]] — AI role in query-time systems
- [[knowledge-contradiction-preservation]] — preserving vs smoothing contradictions
- [[andrej-karpathy]] — creator of the wiki pattern
- [[nate-openbrain]] — creator of Open Brain
