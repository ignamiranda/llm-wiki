---
title: "Effect Distance and Padding"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, padding, context, chunk-boundaries]
aliases: [padding, effect distance]
summary: "The mechanism by which chunks receive context from neighboring areas through padded data requests to lower layers."
---

# Effect Distance and Padding

## Definition

Effect distance and padding refer to how much surrounding context a chunk receives from lower layers to enable [[contextual-generation]]. When a chunk requests data from another layer, it specifies bounds that extend beyond its own size by a certain padding amount. This padding gives the chunk visibility into neighboring areas, enabling operations like blurring, pathfinding, or point relaxation across what would otherwise be hard chunk boundaries.

## Key Properties

- Padding is specified per-layer-dependency in the layer constructor
- Must be at least as large as any data request the layer's chunks will make
- Insufficient padding causes runtime errors with a message specifying the required padding
- Larger padding increases generation cost (more provider chunks need to exist)
- Padding enables seamless cross-boundary results

## Examples

- A CultivationLayer specifies Point(16, 16) padding on its GeoGridLayer dependency, allowing pathfinding to consider terrain 16 units beyond the chunk's own bounds
- A LandscapeLayer collects all locations and paths that overlap its bounds from LocationLayer and CultivationLayer to ensure seamless path deformation in adjacent terrain chunks

## Related Concepts

- [[contextual-generation]] — the feature enabled by padding
- [[layer-dependencies]] — where padding is configured
- [[chunk-based-generation]] — the context for padding

## References

- LayerProcGen documentation: Layer Dependencies, Contextual Generation
