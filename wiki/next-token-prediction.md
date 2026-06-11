---
title: "Next-Token Prediction"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [llm, inference, token, mechanism]
aliases: ["next token prediction", "autoregressive generation"]
summary: "The core mechanism of large language models — given a context, the model samples one next token at a time, building every output one token at a time."
---

# Next-Token Prediction

## Definition

The fundamental operation of a large language model: given a [[context-window|context]], the model computes a probability distribution over every token in its vocabulary, samples one [[Token|token]] from that distribution, appends it, and repeats. Every output — a sentence, a tool call, a thousand-line file — is built one token at a time. The model has no other mode of operation.

The model never checks whether a token is true before emitting it — only whether it is likely — which is the root of [[hallucination]]. Because each token is committed to sequentially, a confident-sounding opening sentence can steer the rest of the answer wrong.

## Key Properties

- Each step runs the full context through the parameters to produce probabilities
- Sampling introduces [[non-determinism]] — same prompt, different output
- Output speed is bounded by tokens-per-second generation rate
- Tool calls are just structured strings in the output stream, parsed by the [[harness]]

## Examples

A model generating a tool call: it doesn't "decide" to call a tool — it outputs the structured string `{"tool":"read","path":"file.ts"}` one token at a time, and the harness parses it.

## Related Concepts

- [[Token]] — the atomic unit of next-token prediction
- [[non-determinism]] — caused by the sampling step
- [[harness]] — orchestrates multiple predictions into agent behavior

## References

- Matt Pocock, *Dictionary of AI Coding*, Section 1
