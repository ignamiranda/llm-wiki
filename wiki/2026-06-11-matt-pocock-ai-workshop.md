---
title: "Matt Pocock's AI Software Engineering Workshop"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [ai, software-engineering, llm, smart-zone, compaction, agent-skills, workshop]
summary: "Matt Pocock's workshop on practical AI-assisted software engineering, covering the Smart Zone / Dumb Zone concept, compaction vs clearing, session lifecycle, agent skills, and the grill-me skill pattern for requirements alignment."
source_url: https://www.youtube.com/watch?v=-QFHIoCo-Ko
source_hash: D0142EF408B901707C8E5BDDD7E985DE345E58F18BCC6CE61AA59F1535334FF4
---

# Matt Pocock's AI Software Engineering Workshop

## Summary

Matt Pocock delivers a hands-on workshop on working effectively with AI coding agents. Core themes: the Smart Zone / Dumb Zone concept (Dex Hardy) where LLM quality degrades as context fills, the Memento-like statelessness of LLMs requiring careful context management, compaction vs clearing strategies, the Ralph Wiggum iterative development pattern, the grill-me skill for requirements alignment, and a critique of the specs-to-code / vibe coding movement.

## Content

### Smart Zone / Dumb Zone

Dex Hardy's concept: LLMs have a "smart zone" (fresh context, optimal performance) and a "dumb zone" (degraded quality as context fills). Every token added scales attention relationships quadratically — roughly 100K tokens is the practical limit before degradation sets in, regardless of the model's maximum context window. Work must be sized to fit within the smart zone.

### The Memento Problem

LLMs are stateless — every session starts from zero (like the movie Memento). This is actually an advantage: the system prompt is always the same, enabling reproducible behavior. The recommended approach is to clear rather than compact, maintaining a consistent starting state.

### Compaction vs Clearing

Two strategies for context management:
- **Clearing**: Delete everything and return to the system prompt. Gives consistent, reproducible starting state.
- **Compaction**: Summarize the session into a compact history. Preserves context but at reduced fidelity.

Pocock prefers clearing for consistency, despite many developers favoring compaction.

### Session Stages

Every AI coding session follows a predictable lifecycle:
1. **System prompt** — minimal foundational context (keep as small as possible)
2. **Exploration** — agent learns the codebase
3. **Implementation** — the actual coding work
4. **Testing** — verification and feedback loops

### Ralph Wiggum Pattern

An iterative development pattern where instead of multi-phase plans, you specify the end goal (PRD) and instruct the AI to "make a small change that gets us closer." The loop continues until the goal is met. Named after Ralph Wiggum's "I'm in danger" meme — the pattern of repeatedly making small progress.

### Grill Me Skill

The grill-me skill is an agent skill pattern for requirements gathering. Before any implementation, the AI grills the developer on the spec, uncovering misalignment and clarifying scope. This prevents the silent assumption gap that plagues the "specs to code" approach. Key steps: load the skill, pass the client brief, let the AI ask clarifying questions.

### Against Specs-to-Code

Pocock argues against the "specs-to-code" / vibe coding movement where developers write specs and let AI generate code without understanding the output. The code is your battleground — you must maintain a handle on it. Specs-to-code fails because it treats code as an opaque output rather than a shared artifact to be shaped.

## Key Takeaways

- Size tasks to fit within the smart zone (~100K tokens max)
- Prefer clearing over compaction for consistent agent behavior
- Use the grill-me skill before any implementation to surface misalignment
- Break large tasks into smart-zone-sized chunks via the Ralph Wiggum pattern
- Monitor token count to know when you're approaching the dumb zone
- Code is your battleground — don't delegate understanding of it

## Related

- [[smart-zone-dumb-zone]] — LLM quality degradation
- [[attention-degradation]] — related phenomenon
- [[compaction-vs-clearing]] — context management
- [[compaction]] — existing concept
- [[handoff]] — related context transfer
- [[ralph-wiggum-pattern]] — iterative development
- [[session-stages]] — AI session lifecycle
- [[grill-me-skill]] — requirements alignment skill
- [[specs-to-code-criticism]] — against vibe coding
- [[token-awareness]] — monitoring token usage
- [[matt-pocock]] — workshop presenter
- [[dex-hardy]] — smart zone concept creator
- [[agent-skills]] — skill framework
