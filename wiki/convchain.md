---
title: "ConvChain"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, texture-synthesis, algorithm]
summary: "A related algorithm by Maxim Gumin that satisfies the strong version of condition C2 (exact pattern distribution matching) but does not guarantee C1 (only using input patterns)."
---

# ConvChain

## Definition

ConvChain is an algorithm by Maxim Gumin (mxgmn) that satisfies the strong version of condition C2 — the limit distribution of NxN patterns in its outputs is exactly the same as the distributions in the input. However, it does not satisfy condition C1 — it often produces noticeable local defects. This makes ConvChain complementary to WFC: running ConvChain first produces a well-sampled configuration, then running WFC corrects local defects, analogous to combining Monte-Carlo optimization with gradient descent.

## Key Properties

- Satisfies strong C2 (exact pattern distribution matching)
- Fails C1 (produces noticeable defects)
- Recommended as a pre-processing step before WFC
- Part of a family of related algorithms by mxgmn

## Related Concepts

- [[wave-function-collapse]] — complementary algorithm
- [[maxim-gumin]] — creator

## References

- Maxim Gumin, "ConvChain" — https://github.com/mxgmn/ConvChain
