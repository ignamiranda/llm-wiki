---
title: "Wiki Compile Pattern"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [ai, knowledge-management, llm-wiki, karpathy, pattern]
aliases: ["Karpathy wiki pattern", "LLM compile pattern"]
summary: "Andrej Karpathy's approach to persistent AI knowledge: compile knowledge from sources into interlinked wiki pages once, keep it current, never re-derive from scratch."
---

# Wiki Compile Pattern

## Definition

Andrej Karpathy's knowledge management pattern where an AI agent reads source documents, extracts key concepts and connections, and writes them into a set of interlinked wiki pages. The knowledge is "compiled once and kept current" — subsequent queries read the compiled understanding rather than re-processing raw sources. The system uses text files and folders as its storage medium, deliberately simple.

## Key Properties

- AI acts as a writer/editor — makes editorial decisions about content and connections
- Uses flat files (markdown) organized in folders — "file over app"
- Sources are kept as immutable raw material alongside compiled pages
- Each new source triggers active integration with existing knowledge
- Best suited for solo researchers working on complex, evolving topics
- Optimal scale: ~100 to ~10,000 high-signal documents

## Examples

Karpathy's personal setup: AI agent on one side, Obsidian note-taking app on the other. The agent edits wiki pages based on conversations, and Karpathy browses results in real time via graph view.

## Related Concepts

- [[compile-time-knowledge]] — the underlying paradigm
- [[open-brain-pattern]] — the query-time alternative
- [[hybrid-memory-architecture]] — combining both
- [[andrej-karpathy]] — creator

## References

- Karpathy, A. "LLM Wiki" — GitHub gist
- Nate. "Karpathy Wiki vs Open Brain" — YouTube
