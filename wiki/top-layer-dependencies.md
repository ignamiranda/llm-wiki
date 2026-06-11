---
title: "Top Layer Dependencies"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, dependencies, architecture, layerprocgen]
aliases: [top level dependencies, root dependencies]
summary: "Entry points for procedural generation — specifications that certain layer chunks are required within given world-space bounds."
---

# Top Layer Dependencies

## Definition

Top layer dependencies are the root entry points for generation in [[layer-based-procedural-generation]]. They specify that chunks from a particular layer are required within given world-space bounds, defined by a focus point and a size. All generation starts from one or more top layer dependencies. Typically, one is focused on the player's position to generate the world around them. Multiple top layer dependencies can coexist, and overlapping dependency regions share generated chunks without duplication.

## Key Properties

- Defined by a focus point (center) and size (extents)
- Can have different layers as targets, each with different generation radii
- Overlapping dependencies do not duplicate chunk generation
- Can be dynamically added/removed (e.g., for fast travel or map viewing)
- Different gameplay features may need different layers at different radii

## Examples

- Player dependency: generates the world around the player as they move
- Map dependency: generates a lightweight representation around the map scroll position
- Fast travel: a temporary dependency at the destination ensures the world is ready before teleporting
- Debug camera: generates what the debug camera is looking at
- Multiple dependencies: a PropsLayer might need a 200m radius while an NPCLayer only needs 50m

## Related Concepts

- [[layer-dependencies]] — the general mechanism; top layer dependencies are a special case
- [[layer-based-procedural-generation]] — the architecture these dependencies drive

## References

- LayerProcGen documentation: Layer Dependencies
