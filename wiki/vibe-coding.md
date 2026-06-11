---
title: "Vibe Coding"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [ai-coding, methodology, workflow]
aliases: ["vibe-driven development"]
summary: "A prompt-driven development style where the developer describes what they want in natural language and the AI agent implements it, often with minimal review of the generated code."
---

# Vibe Coding

## Definition

A prompt-driven development style where the developer describes what they want in natural language and the [[Agent|agent]] implements it. The name captures the feel: the developer describes the "vibe" of what they want rather than specifying exact implementation details, accepting the agent's output with minimal review.

The term gained popularity in 2025 as AI coding agents became capable of generating substantial working code from natural language descriptions. It is contrasted with more structured approaches like [[tdd-agent-skill|TDD for AI agents]] or [[grill-me-methodology|grilling sessions]].

## Key Properties

- Trade-off: high velocity for low precision
- Works best for prototypes, UI components, and well-understood patterns
- Risk: subtle bugs and architectural drift from insufficient review
- [[automated-checks|Automated checks]] are especially important in this mode

## Examples

"Just make me a responsive navbar with a hamburger menu" — the agent generates the code with minimal specification.

## Related Concepts

- [[Agent]] — the entity that does the vibe coding
- [[grill-me-methodology]] — the opposite approach (structured alignment first)
- [[tdd-agent-skill]] — structured alternative with feedback loops
- [[automated-checks|automated check]] — essential safety net when vibe coding

## References

- Matt Pocock, *Dictionary of AI Coding*, Section 7
