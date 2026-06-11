---
title: "Context Window"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [llm, context, token, architecture]
aliases: ["context", "window", "LLM context window"]
summary: "The finite token sequence a language model sees on each request — the only surface through which the model perceives anything. Everything in the window competes for space and attention."
---

# Context Window

## Definition

Everything the [[Model|model]] sees on each model provider request. Finite, model-specific, and the only surface through which the model perceives anything. It is a single sequence of [[Token|tokens]]: the [[system-prompt]], the conversation so far, every tool result the [[harness]] has fed back in.

If something is in that sequence, the model can use it; if it is not, the model does not know it exists. Anything outside the window must be brought in, usually via a tool call, before it can affect anything.

## Key Properties

- Finite — fills up as the session progresses, eventually forcing [[compaction]] or clearing
- Everything in the window competes — loading unnecessary content reduces space for what matters
- The window is working state, not persisted memory — it does not carry across sessions
- Size varies by model (typically 8K–200K tokens)

## Examples

"Can I just paste the whole monorepo into the prompt?" — "The context window is 200k tokens — that's maybe a fifth of the repo. Pick the files the task touches."

## Related Concepts

- [[attention-degradation]] — what happens as the window fills
- [[compaction]] — technique to shrink what the window carries
- [[handoff]] — transferring work when the window is full
- [[Token]] — the unit the window is measured in

## References

- Matt Pocock, *Dictionary of AI Coding*, Section 2
