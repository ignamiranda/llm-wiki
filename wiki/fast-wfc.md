---
title: "fast-wfc"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [wfc, wave-function-collapse, cpp, performance, procedural-generation]
aliases: []
summary: "A C++17 implementation of Wave Function Collapse focused on performance, achieving ~10x speedup over the original implementation."
source_url: "https://github.com/math-fehr/fast-wfc"
source_hash: "A4BBE0A73026A8F1384D2A16276AE1F613A4BDB8661659A314C76A090F636C38"
---

# fast-wfc

## Definition

fast-wfc is a C++17 implementation of Wave Function Collapse by Mathieu Fehr and Nathanaëlle Courant, optimized for performance. At time of release, it achieved approximately 10x speedup over the original C# implementation through efficient data structures and propagation algorithms.

## Key Properties

- Written in C++17 with CMake build system
- ~10x performance improvement over original WFC
- Rust bindings available via fastwfc-rs
- Overlapping model implementation
- MIT licensed, 435 GitHub stars

## Examples

Suitable for real-time procedural texture generation and game development contexts where WFC speed is critical. Example image samples from the original WFC repo are included.

## Related Concepts

- [[debroglie]] — C# WFC with backtracking
- [[2026-06-11-wfc-implementations-survey]] — surveyed in the WFC survey article

## References

- https://github.com/math-fehr/fast-wfc