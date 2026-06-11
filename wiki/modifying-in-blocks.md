---
title: "Modifying in Blocks"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, wfc, lazy-generation, infinite-worlds]
summary: "Paul Merrell's technique for generating unbounded tile configurations by incrementally modifying the model in blocks, adapted by Boris the Brave and Marian Kleineberg for lazy infinite WFC generation."
---

# Modifying in Blocks

## Definition

Modifying in blocks is a technique introduced by Paul Merrell for incrementally modifying a generated model in parts to reduce the failure rate of Model Synthesis / WFC. Boris the Brave later applied this technique to the lazy generation of unbounded tile configurations, and Marian Kleineberg implemented it in his infinite city generator based on WFC.

## Key Properties

- Allows lazy (on-demand) generation of tiles in an unbounded world
- Reduces failure rate compared to generating large regions at once
- Enables infinite WFC worlds by regenerating only affected blocks when the generation focus moves
- Adapted from Merrell's original model synthesis work

## Related Concepts

- [[wave-function-collapse]] — the algorithm being extended
- [[model-synthesis]] — Merrell's original work this technique comes from
- [[boris-the-brave]] — adapted the technique for lazy generation
- [[chunk-based-generation]] — related concept for infinite world generation
- [[infinite-terrain]] — compare with noise-based infinite terrain approaches

## References

- Boris the Brave, "Infinite Modifying in Blocks" — https://www.boristhebrave.com/2021/11/08/infinite-modifying-in-blocks/
- Marian Kleineberg, "Infinite WFC" — https://marian42.de/article/infinite-wfc
