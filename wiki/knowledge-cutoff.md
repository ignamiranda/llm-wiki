---
title: "Knowledge Cutoff"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [llm, knowledge, training, limitations]
aliases: ["training cutoff", "data cutoff"]
summary: "The point in time after which a language model has no training data — it has never seen library versions, APIs, or events from after that date."
---

# Knowledge Cutoff

## Definition

The point in time after which a [[Model|model]] has no training data. [[Training]] ends at a specific date, so the model has not seen the library version you upgraded to last month, the CVE disclosed last week, or the API you shipped yesterday. This is distinct from forgetting — the model literally was never exposed to that information.

Everything the model knows from training is [[parametric-knowledge|parametric knowledge]], and the knowledge cutoff is its temporal boundary.

## Key Properties

- Every model has a knowledge cutoff; it is a fundamental limitation, not a bug
- The fix is never "teach the model" — it is putting current material into [[context-window|context]]
- The cutoff date is usually published by the [[model-provider]]
- Does not affect [[contextual knowledge]] provided in the prompt

## Examples

"Can the model use the latest React 19 APIs?" — "Only if the cutoff date is after React 19's release. Otherwise, load the relevant docs into context."

## Related Concepts

- [[parametric-knowledge]] — what the cutoff bounds
- [[contextual knowledge]] — information you provide to work around the cutoff
- [[Training]] — the process that ends at the cutoff
- [[model-provider]] — publishes cutoff dates

## References

- Matt Pocock, *Dictionary of AI Coding*, Section 4
