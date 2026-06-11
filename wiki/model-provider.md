---
title: "Model Provider"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [llm, infrastructure, inference]
aliases: ["provider", "LLM provider", "API provider"]
summary: "The service that hosts and runs a language model for inference — typically a remote API (Anthropic, OpenAI, Google) or local runtime (Ollama, llama.cpp)."
---

# Model Provider

## Definition

Whatever serves a [[Model|model]] for [[Inference|inference]]. Usually a remote service (Anthropic, OpenAI, Google), but can also be local — Ollama, LM Studio, llama.cpp running on your own machine. The [[harness]] doesn't run the model itself; it asks a provider to.

The provider owns the machinery: the [[Parameters|parameters]] live on its hardware, and every model provider request is the harness sending [[Token|tokens]] over the network and getting predictions back. The provider is the source of rate limits, degraded capacity, and outages — not the model or the harness.

## Key Properties

- Sets commercial terms: per-token pricing, [[prefix-cache]] discounts, model availability
- Provider and model maker can be different companies (Bedrock, Vertex, OpenRouter serve others' models)
- Local providers (Ollama, llama.cpp) trade capability for control and zero per-token cost
- Provider status page is the first place to check when an agent stalls or errors

## Examples

"Can we run this offline for the air-gapped client?" — "Swap the model provider to Ollama or llama.cpp on their box. The harness doesn't care, it just hits a different endpoint."

## Related Concepts

- [[harness]] — interfaces with the provider
- [[Inference]] — what the provider runs
- [[prefix-cache]] — provider-side optimization
- [[model-provider-request|model provider request]] — the unit of interaction

## References

- Matt Pocock, *Dictionary of AI Coding*, Section 1
