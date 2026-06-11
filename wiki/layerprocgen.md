---
title: "LayerProcGen"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, unity, csharp, framework, infinite-worlds]
summary: "A C# framework for layer-based infinite procedural generation that is deterministic, contextual, and multi-threaded, designed for Unity but usable in any C# engine."
source_url: "https://github.com/runevision/LayerProcGen/"
source_hash: "abf6a277a0b01f8aeb4a60a3c0dff4dfb99ad4af974001d1fcdaa397f3b00de5"
---

# LayerProcGen

## Summary

LayerProcGen is an open-source C# framework (MPL-2.0 licensed) for layer-based infinite procedural generation. Created by Rune Skovbo Johansen, it enables developers to build worlds that are infinite, deterministic, and contextual — where procedural operations seamlessly cross chunk boundaries. The framework divides generation into multiple layers with strict input/output separation and automatic dependency management. It powers the released game The Cluster and the in-development game The Big Forest.

## Content

LayerProcGen addresses a fundamental challenge in infinite procedural generation: how to generate seamless, contextual content on the fly while keeping results deterministic. Traditional chunk-based approaches (as popularized by Minecraft) use purely functional generation where each chunk is independent, which prevents context-dependent operations like blurring across chunk boundaries, pathfinding that crosses chunks, or point relaxation between neighboring chunks.

The framework's solution is a multi-layer architecture where:

- **Each layer handles one level of abstraction** — from coarse regional planning down to fine terrain detail
- **Chunks in one layer can request data from lower layers with padding** — giving them the context they need
- **Dependencies form a directed acyclic graph (DAG)** — ensuring deterministic, cycle-free generation
- **Internal layer levels** allow a single class to implement multiple layers at once
- **Top layer dependencies** serve as entry points, typically focused on the player position

Key architectural elements include the [[rolling-grid]] for chunk storage, the [[owned-within-bounds]] pattern for disambiguating overlapping chunk ownership, and [[effect-distance-and-padding]] for controlling how much context chunks receive.

The framework contrasts two approaches to procedural generation: the [[functional-approach-procgen]] (local, context-free, sandbox-oriented) and the [[planning-approach-procgen]] (top-down, intentional, enabling designed experiences even in infinite worlds). LayerProcGen is designed to enable the planning approach at scale.

## Key Takeaways

- Chunks in different layers can be orders of magnitude different in size, enabling both micro and macro planning
- Multi-threaded via Parallel.ForEach with automatic core scaling
- Pseudo-infinite (limited by 32-bit integer range)
- Determinism + contextual integrity achieved through strict layer separation and padded data requests
- The same framework supports both functional and planning-oriented generation styles

## Related

- [[rune-skovbo-johansen]] — creator of LayerProcGen
- [[layer-based-procedural-generation]] — the core methodology the framework implements
- [[contextual-generation]] — seamless cross-boundary generation
- [[deterministic-generation]] — reproducible chunk output
- [[chunk-based-generation]] — the unit of world division
- [[layer-dependencies]] — inter-layer data flow mechanism
- [[top-layer-dependencies]] — generation entry points
- [[planning-approach-procgen]] — what LayerProcGen enables at scale
- [[functional-approach-procgen]] — the alternative sandbox approach
