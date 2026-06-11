---
title: "Parametric Knowledge"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [llm, knowledge, training, inference]
aliases: ["parametric memory", "baked-in knowledge"]
summary: "Facts a language model can recite from its training data, stored in its parameters — as opposed to contextual knowledge provided in the prompt."
---

# Parametric Knowledge

## Definition

Facts the [[Model|model]] can recite from training, like a standard library API — stored in the [[Parameters|parameters]], not retrieved from anywhere. This is [[parametric knowledge|parametric knowledge]]: information compressed into the model's weights during [[Training|training]] as a side effect of improving [[next-token prediction]].

The model has no database of facts inside it — just billions of numbers arranged so the calculation tends to produce useful output. Anything the model "knows" from training is parametric knowledge.

## Key Properties

- Bounded by the [[knowledge-cutoff]] — the model has not seen anything after training ended
- Cannot be updated without retraining
- Contrasts with contextual knowledge, which is provided in the [[context-window]]
- When the model does not know your codebase, the fix is to put it in context, not to "teach" the model

## Examples

"Can we fine-tune it on our codebase?" — "That would update the parameters — different model afterwards. For one project it's almost always cheaper to load the codebase as context."

## Related Concepts

- [[knowledge-cutoff]] — the temporal boundary of parametric knowledge
- [[contextual knowledge]] — information provided in the prompt
- [[Training]] — how parametric knowledge is created
- [[Parameters]] — where parametric knowledge is stored

## References

- Matt Pocock, *Dictionary of AI Coding*, Section 4
