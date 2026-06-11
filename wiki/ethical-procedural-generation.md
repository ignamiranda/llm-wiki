---
title: "Ethical Procedural Generation"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, narrative-generation, ai-ethics, game-design]
aliases: []
summary: "A framework for ethical responsibility in procedural generator design — generators encode their creators' values and amplify them at scale."
source_hash: "3B5A43067F4CBC72968D6E3AE05A66867AE9CE3FE498D4E94ED5E2897FD82F26"
---

# Ethical Procedural Generation

## Definition

Ethical procedural generation, introduced by Dr. Michael Cook in Chapter 5, is a framework for understanding the ethical responsibility inherent in building procedural generators. Every generator encodes its creator's values, assumptions, and biases — whether consciously or unconsciously — and amplifies them at scale across every piece of content it produces.

## Key Properties

- **Generator as amplifier**: a generator multiplies its designer's intent (and biases) across every output instance, magnifying both good and harmful patterns
- **Accidental features**: unconscious biases encoded in generation rules produce systematic skew — e.g., generating only male NPCs because of pronoun defaults
- **Rule of thumb**: don't introduce distinctions that don't mean anything — if a generator differentiates on a dimension (gender, race, class), that dimension must carry intentional meaning
- **Banlists (Kazemi)**: explicitly blocking undesirable output categories is a legitimate (if blunt) ethical tool
- **The Tay problem**: generative systems that learn from user input can be poisoned by malicious users, raising questions of responsibility

## Examples

- **Meganethia** (Cook) — a critical game that exposes ethical dimensions of generator design through play
- **Spore creature editor** — unintentionally limiting creature morphology to bilaterally symmetric body plans encoded assumptions about biology
- **Generative naming systems** — accidentally reproducing racist or gendered naming conventions from training data

## Related Concepts

- [[procedural-storytelling]] — broader context for narrative generation ethics
- [[generative-methods-taxonomy]] — the technical toolkit that carries ethical implications

## References

- [[2019-01-01-procedural-storytelling-in-game-design]] — source (Chapter 5, Dr. Michael Cook)
