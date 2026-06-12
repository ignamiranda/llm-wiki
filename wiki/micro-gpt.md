---
title: "Micro GPT"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [ai, llm, education, minimal-implementation, python]
aliases: ["microGPT"]
summary: "Andrej Karpathy's 200-line minimal implementation of GPT training in Python, distilling the algorithm to its bare essence by stripping away all efficiency-related complexity."
---

# Micro GPT

## Definition

The latest iteration of Andrej Karpathy's decade-long project to boil LLM training to its absolute minimum — 200 lines of Python including comments. It demonstrates that the core algorithm of neural network training for language models is conceptually simple: neural network architecture (~50 lines), forward/backward pass with auto grad engine (~100 lines), Adam optimizer (~10 lines), and training loop. All the complexity in production implementations comes from efficiency requirements (CUDA, distributed training, data loading).

## Key Properties

- 200 lines of Python, fully readable
- No dependencies beyond standard Python libraries
- Every line is about algorithm, not performance
- Self-contained training loop from scratch
- Educational: designed to be understood, not deployed
- Represents the essence of Karpathy's teaching philosophy

## Related Concepts

- [[ai-education-paradigm]] — shift from teaching humans to teaching agents
- [[andrej-karpathy]] — creator

## References

- Karpathy, A. "microGPT" — GitHub
- Karpathy, A. "No Priors Podcast" — YouTube
