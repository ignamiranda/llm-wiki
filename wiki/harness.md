---
title: "Harness"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [llm, agent, architecture, tooling]
aliases: ["agent harness", "LLM harness"]
summary: "The software layer around a language model that turns it into an agent — providing tools, system prompt, context management, permissions, and the agent loop."
---

# Harness

## Definition

Everything around the [[Model|model]] that turns it into an [[Agent|agent]]: [[Tool|tools]], [[system-prompt]], context-window management, permissions, hooks. Claude.ai and Claude Code run on the same model but behave differently because their harnesses differ.

The model itself only does one thing — take text in, produce text out. The harness supplies everything else: it assembles the [[context-window|context]] for each model provider request, executes tool calls, feeds [[Tool|tool results]] back in, stores the session history, manages permissions, and decides when to compact.

## Key Properties

- The agent loop — model proposes, harness executes, repeat — is run by the harness
- When behavior differs between products, the harness is often the variable, not the model
- Most agent configuration lives in the harness (AGENTS.md, permissions, hooks)
- Examples: Claude Code, Cursor, Codex CLI, Claude.ai (chat harness)

## Examples

"Same model, why is Claude Code editing files and Claude.ai just answering questions?" — "Different harnesses. Claude Code has filesystem tools, a different system prompt, and a permission layer."

## Related Concepts

- [[Agent]] — the model-plus-harness unit
- [[Tool]] — functions the harness exposes
- [[system-prompt]] — standing instructions in the harness
- [[model-provider]] — the harness sends requests to providers

## References

- Matt Pocock, *Dictionary of AI Coding*, Section 1
