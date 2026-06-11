---
title: "Attention Degradation"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [llm, context, attention, failure-modes]
aliases: ["context degradation", "lost in the middle", "dumb zone"]
summary: "The phenomenon where a language model's output quality declines in long sessions as the context window fills, because the model's attention dilutes across too many tokens and early content gets buried."
---

# Attention Degradation

## Definition

The decay in output quality as a [[Session|session]] grows long and the [[context-window]] fills. The [[Model|model]]'s [[Attention|attention]] budget is finite — every [[Token|token]] in the window competes for it. As the window accumulates tool results, file contents, and conversation history, the model has less effective attention per token. Content near the middle of the window is especially affected (the "lost in the middle" phenomenon).

This is why long sessions drift into the "dumb zone": the model appears to forget instructions given earlier, repeats reasoning already established, or misses details it previously handled correctly. The model has not changed — the signal-to-noise ratio in its context has degraded.

## Key Properties

- Not a memory issue — everything is still in the window, but buried
- The fix is curation: [[compaction]], [[handoff]], or [[clearing|clearing]]
- Early content (system prompt, first messages) is usually preserved — middle content is most affected
- Degradation is gradual, not a hard cliff at a specific token count

## Examples

An agent that was following conventions precisely in turn 5 starts making inconsistent choices in turn 40 — it needs a compaction or handoff, not re-explanation.

## Related Concepts

- [[context-window]] — where degradation occurs
- [[compaction]] — technique to combat degradation
- [[handoff]] — transfer to a fresh context when degraded
- [[Session]] — the unit that accumulates and degrades

## References

- Matt Pocock, *Dictionary of AI Coding*, Section 4
