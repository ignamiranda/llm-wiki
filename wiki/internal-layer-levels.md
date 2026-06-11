---
title: "Internal Layer Levels"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, layering, architecture, layerprocgen]
aliases: [layer levels]
summary: "A concept where a single layer class implements multiple layers at once, each at a different level of detail or abstraction."
---

# Internal Layer Levels

## Definition

Internal layer levels allow a single layer class to implement multiple layers at once. Each level within a layer operates at its own scale and serves a different stage in the generation pipeline for that layer. Levels within a layer count as separate nodes in the [[layer-dependencies]] directed acyclic graph. This is an optional but powerful feature for organizing multi-stage generation within a single conceptual layer.

## Key Properties

- A single class can implement multiple levels
- Each level has its own scale and role
- Levels within a layer count as separate DAG nodes
- Enables passing intermediate results between levels within the same class

## Examples

- In [[layerprocgen]]'s example, a LocationLayer has three internal levels: Level 0 generates random positions, Level 1 relaxes distances between them, Level 2 determines connections
- A GeoGridLayer could use internal levels for coarse then fine height data

## Related Concepts

- [[layer-based-procedural-generation]] — the architecture internal levels belong to
- [[layer-dependencies]] — levels are separate nodes in the dependency graph
- [[chunk-based-generation]] — each level still operates on chunks

## References

- LayerProcGen documentation: Internal Layer Levels
