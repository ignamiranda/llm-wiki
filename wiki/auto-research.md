---
title: "Auto Research"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [ai, research, automation, experimentation]
aliases: ["closed-loop research", "AI-driven research"]
summary: "A closed-loop AI-driven research system where an AI agent generates hypotheses, runs experiments, checks results, and iterates autonomously — applicable to domains where candidate generation is expensive but verification is cheap."
---

# Auto Research

## Definition

A system where AI autonomously drives the research cycle: generate candidate solutions, run experiments, evaluate results, and iterate. The key enabling property is asymmetric effort — generating candidates is expensive but verifying them is cheap. This enables at-home distributed research ([[open-ground]]) where untrusted workers contribute compute cycles and a trusted pool performs verification.

## Key Properties

- AI generates and tests hypotheses autonomously
- Works where verification is cheaper than generation
- Enables distributed, untrusted collaboration
- Applicable to code optimization, protein folding, materials science
- Leaderboard-based incentive structure

## Examples

Karpathy's auto research for LLM training: agents try to find code that trains a model to low validation loss. A candidate commit can be cheaply verified by running a training loop. 10,000 ideas might be tried, but only verification of the best ones is needed.

## Related Concepts

- [[open-ground]] — distributed research collaboration
- [[andrej-karpathy]] — proponent

## References

- Karpathy, A. "No Priors Podcast" — YouTube
