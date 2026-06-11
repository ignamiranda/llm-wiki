---
title: "Dictionary of AI Coding — Matt Pocock"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [ai-coding, glossary, llm, agent-skills, software-engineering]
summary: "Matt Pocock's comprehensive glossary of 60+ AI coding terms across 7 sections, translating jargon into plain English."
source_url: "https://github.com/mattpocock/dictionary-of-ai-coding"
source_hash: "DB754B6B740B8D314DA3F128049512F33371AA02EC8AF7F9EA23FC4C35307140"
---

# Dictionary of AI Coding — Matt Pocock

## Summary

Matt Pocock's **Dictionary of AI Coding** is a comprehensive glossary of 60+ AI coding terms organized into 7 sections, each term explained in plain English with usage examples. The dictionary covers the full stack of AI-assisted software development: model internals, session mechanics, tooling, failure modes, handoff patterns, memory systems, and workflow patterns. Each term includes a definition, a usage dialogue, and cross-references to related terms.

## Content

### Section 1 — The Model

Terms covering the foundational mechanics of large language models: [[AI]], [[model-provider|Model]], [[Parameters]], [[Training]], [[Inference]], [[Token]], [[next-token-prediction]], [[non-determinism]], [[model-provider]], [[harness]], model provider request, [[input-tokens|input tokens]], [[output-tokens|output tokens]], [[prefix-cache]], [[cache-tokens|cache tokens]].

Key theme: The model is [[stateless]] — it does [[next-token-prediction]] and nothing else. Everything that feels like an agent working is the [[harness]] orchestrating many predictions.

### Section 2 — Sessions, Context Windows & Turns

Terms about the interaction structure: [[stateless]], [[context]], [[context-window]], [[stateful]], [[agent]], [[system-prompt]], session, turn.

Key theme: The [[context-window]] is finite and everything in it competes for the model's [[attention-budget|attention budget]]. Sessions fill up and must be compacted or cleared.

### Section 3 — Tools & Environment

Terms about how agents perceive and act on the world: environment, filesystem, tool, tool call, tool result, MCP, permission request, permission mode, agent mode, [[sandbox]].

Key theme: The agent only sees the environment through tool results — its picture is a collection of snapshots.

### Section 4 — Failure Modes

Terms about what goes wrong: sycophancy, [[hallucination]], [[parametric-knowledge]], [[knowledge-cutoff]], contextual knowledge, attention relationship, attention budget, [[attention-degradation]], smart zone.

Key theme: Most failures trace back to context — the relevant fact was never loaded, or was buried under attention degradation.

### Section 5 — Handoffs

Terms about cross-session work: clearing, [[handoff]], primary source, secondary source, handoff artifact, spec, ticket, [[compaction]], autocompact.

Key theme: One task per session keeps context relevant. Handoffs and compaction bridge across sessions.

### Section 6 — Memory and Steering

Terms about making agents remember and follow direction: [[memory-system-ai|memory system]], AGENTS.md, [[progressive-disclosure]], context pointer, [[skill]], [[subagent]].

Key theme: The model can't learn — anything that must persist has to be written to the environment.

### Section 7 — Patterns of Work

Terms about development methodology: human-in-the-loop, AFK, automated check, automated review, human review, [[vibe-coding]], design concept, [[grill-me-methodology|grilling]], prototyping, DX, [[agent-experience-ax|AX]].

Key theme: Verification matters more with non-deterministic tools — automated checks catch bad draws from the distribution.

## Key Takeaways

- The term "AI" is a moving label, not a fixed technology — precise language sharpens diagnosis
- The model is stateless; all apparent continuity is manufactured by the harness re-feeding context
- Context engineering — curating what goes into the context window — is the most impactful skill in AI coding
- Cost scales with input tokens (history re-sent on every request) and output tokens (generated one at a time)
- Long sessions degrade due to attention degradation; compaction and handoffs are the fixes
- Verification and automated checks are essential when tools are non-deterministic

## Related

- [[matt-pocock]] — author of the dictionary
- [[2026-06-11-mattpocock-skills]] — his agent skills repository
- [[agent-skills]] — the concept of composable declarative skills
- [[grill-me-methodology]] — grilling pattern defined in Section 7
- [[skill-file-format]] — SKILL.md file format used by agent skills
