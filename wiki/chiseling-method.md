---
title: "Chiseling Method"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, wfc, connectivity, algorithm]
summary: "A method by Boris the Brave for generating connected structures with WFC by carving out (chiseling) the output from a solid block rather than building it up from tiles."
---

# Chiseling Method

## Definition

The chiseling method is an approach by Boris the Brave for generating connected structures with WFC. Instead of building up the output tile by tile, it starts from a solid block and "chisels away" material, ensuring the resulting structure remains connected. This avoids the common WFC problem of generating disconnected or non-navigable regions.

## Key Properties

- Guarantees connected output structures
- Works by removing tiles from a solid block rather than placing tiles in empty space
- Implemented in the DeBroglie library
- Addresses a common weakness of basic WFC: lack of global connectivity guarantees

## Related Concepts

- [[wave-function-collapse]] — the algorithm being extended
- [[boris-the-brave]] — creator of the method, author of DeBroglie
- [[constrained-synthesis-wfc]] — related approach for adding constraints to WFC

## References

- Boris the Brave, "Random Paths via Chiseling" — https://www.boristhebrave.com/2018/04/28/random-paths-via-chiseling
- Boris the Brave, "DeBroglie" library — https://boristhebrave.github.io/DeBroglie
