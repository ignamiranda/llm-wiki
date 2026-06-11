---
title: "Non-Determinism"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [llm, inference, token, behavior]
aliases: ["nondeterminism", "output variability"]
summary: "The property that the same LLM input can produce different output on different runs, due to the sampling step in next-token prediction and provider-side serving variation."
---

# Non-Determinism

## Definition

The same input to a language model can produce different output. Running a model twice with identical [[context-window|context]] may yield two different answers — sometimes a single word, sometimes a completely different approach. This is a built-in property of [[next-token prediction]], not a bug layered on top.

During [[Inference|inference]], the model produces a probability distribution over possible next [[Token|tokens]] and one is sampled from it. Sampling intentionally includes randomness — always picking the most likely token produces repetitive, lower-quality text. Provider-side serving adds more variation: requests are batched on shared hardware, and tiny floating-point differences between batches can tip a close call between two tokens.

## Key Properties

- Expect a bell curve of results on the same task — most within range, but real tails exist
- A bad attempt is one draw from the distribution; retrying is a legitimate strategy
- Verification matters more than with deterministic tools — [[automated-checks|automated check]] must catch bad draws
- Do not over-narrativize: a string of bad runs is usually the distribution, not a model update

## Examples

"Claude has been awful today. Did they ship a worse version?" — "Probably not. Non-determinism means you'll have good and bad days on the same task. Try again tomorrow."

## Related Concepts

- [[next-token prediction]] — the mechanism that produces non-determinism
- [[Inference]] — the phase where non-determinism occurs
- [[Token]] — the unit of prediction

## References

- Matt Pocock, *Dictionary of AI Coding*, Section 1
