---
title: "A Primer on Repeatable Random Numbers"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, random-numbers, hash-functions, rng]
summary: "A comprehensive guide comparing random number generators vs random hash functions for procedural generation, explaining why hashes (especially xxHash) avoid correlated pattern artifacts that seeded RNGs produce."
source_url: "https://blog.runevision.com/2015/01/primer-on-repeatable-random-numbers.html"
---

# A Primer on Repeatable Random Numbers

## Summary
A comprehensive guide comparing random number generators vs random hash functions for procedural generation, explaining why hashes (especially xxHash) avoid correlated pattern artifacts that seeded RNGs produce.

## Content

A common approach in procedural generation is to seed a random number generator per chunk or per object, then use that RNG for deterministic generation. However, this produces correlated outputs when visualized: coordinate plots reveal visible patterns linking nearby seeds, and statistical tests (such as the ENT test suite) confirm the correlation. The underlying issue is that RNGs are designed for sequential uncorrelated outputs from a single seed, not for uncorrelated outputs across different seeds.

Hash functions solve this problem. A good hash produces completely uncorrelated output for different inputs, making it ideal for turning a coordinate or seed into deterministic pseudo-random values. The article evaluates several hash functions for procedural generation: MurmurHash3, MD5, Wang Hash, and PcgHash by Adam Smith. It recommends xxHash as particularly well-suited — it accepts single-integer inputs without byte conversions, which is a common bottleneck in procedural generation pipelines where coordinates need to be hashed millions of times per frame.

The article also discusses combining hashes with traditional RNGs: use a hash to derive a seed per chunk, then use a conventional RNG for sequential rolls within that chunk. This hybrid approach gives the best of both worlds — uncorrelated per-chunk seeds from the hash, and fast sequential generation from the RNG. An appendix covers continuous noise functions (Perlin and Simplex noise), which are a different class of function that produces smooth interpolated values rather than random-looking outputs.

## Key Takeaways
- RNGs with different seeds produce correlated outputs visible in patterns
- Hash functions produce uncorrelated outputs from different seeds
- xxHash recommended for procedural generation
- Combine hashes + RNGs for different use cases

## Related
- [[rune-skovbo-johansen]] — author
- [[deterministic-generation]] — related concept
