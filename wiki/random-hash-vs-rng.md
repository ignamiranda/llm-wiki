---
title: "Random Hash Functions vs Random Number Generators"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, random-numbers, hash-functions]
aliases: []
summary: "The distinction between hash functions and random number generators for procedural generation: hash functions produce uncorrelated outputs from different seeds, while RNGs with seeded sequences show correlated patterns."
---

# Random Hash Functions vs Random Number Generators

## Definition

A key insight for procedural generation: using RNGs with different seeds for different coordinates produces correlated outputs, visible as stripe patterns in visualization. Hash functions like xxHash produce truly uncorrelated outputs for different inputs without sequential state. xxHash is recommended for procedural generation because it takes single integers directly without byte conversion overhead. MurmurHash3, MD5, Wang Hash, and PcgHash are alternatives. The two can be combined: hash for coordinate-to-seed mapping, RNG for sequence generation from that seed.

## Key Properties

- RNG with different seeds produces correlated outputs
- Hash functions produce uncorrelated outputs per input
- xxHash optimized for procedural generation use
- Combined approach: hash → seed → RNG sequence

## Related Concepts

- [[deterministic-generation]] — related
- [[rune-skovbo-johansen]] — author

## References

- Source: runevision blog
