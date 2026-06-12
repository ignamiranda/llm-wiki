---
title: "Hash Functions for Procedural Generation"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, hash-functions, random-numbers]
aliases: []
summary: "The use of fast hash functions (especially xxHash) in procedural generation for repeatable, uncorrelated pseudo-random values from coordinate inputs."
---

# Hash Functions for Procedural Generation

## Definition

Hash functions map arbitrary input to an apparently random value deterministically. In procedural generation, this enables: (1) repeatable values for any coordinate without sequential state, (2) uncorrelated outputs from different inputs (unlike seeded RNGs), and (3) single-int-input methods common in GPU and CPU procgen. xxHash is recommended due to no byte conversion needed for integers, single-int-input methods, and excellent distribution. Alternatives include MurmurHash3, Wang Hash, and PCG Hash. Often combined with traditional RNGs (hash for seeding, RNG for sequences).

## Key Properties

- Deterministic: same input always produces same output
- Uncorrelated outputs for different inputs
- No sequential state required
- xxHash optimized for procgen use

## Related Concepts

- [[random-hash-vs-rng]] — broader comparison
- [[deterministic-generation]] — related
- [[rune-skovbo-johansen]] — author

## References

- Source: runevision blog
