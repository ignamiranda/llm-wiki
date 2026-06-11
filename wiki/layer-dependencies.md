---
title: "Layer Dependencies"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, dependencies, architecture, layerprocgen]
aliases: [inter-layer dependencies]
summary: "The mechanism in layer-based generation by which chunks in one layer request and receive data from other layers."
---

# Layer Dependencies

## Definition

Layer dependencies define how layers relate to each other in [[layer-based-procedural-generation]]. A chunk in one layer (the "user") can request data from another layer (the "provider") within specified world-space bounds. The provider layer calculates which of its chunks overlap those bounds, ensures they exist (generating them if needed), and returns their data. Dependencies are specified once in a layer's constructor with a fixed padding value.

## Key Properties

- User-provider relationship: a chunk uses data from another layer's chunks
- Padding must be specified as the maximum any chunk of the user layer might request
- Before a user chunk is generated, all provider chunks within its bounds + padding are generated first
- This is recursive — providers' own dependencies are resolved first
- Dependencies form a [[deterministic-generation | directed acyclic graph (DAG)]] — no cycles allowed
- Runtime errors are logged if a data request exceeds the configured padding

## Examples

- A CultivationLayer depends on GeoGridLayer with Point(16, 16) padding for terrain height data used in pathfinding
- A LandscapeLayer depends on both LocationLayer and CultivationLayer for location positions and path splines
- Top layer dependencies are the root entry points — they specify which layers to generate and where

## Related Concepts

- [[top-layer-dependencies]] — root-level dependencies that kick off generation
- [[effect-distance-and-padding]] — how much context a chunk receives
- [[internal-layer-levels]] — levels within a single layer also form dependencies in the DAG
- [[chunk-based-generation]] — the unit of data exchange

## References

- LayerProcGen documentation: Layer Dependencies
