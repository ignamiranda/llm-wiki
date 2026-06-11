---
title: "Planning Approach to Procedural Generation"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, planning, top-down, design]
aliases: [top-down procedural generation, planning approach]
summary: "A procedural generation approach where content is generated top-down with intent — planning connections, purpose, and meaning behind placed items."
---

# Planning Approach to Procedural Generation

## Definition

The planning approach generates content from the top down, with intentional design behind the placement of items and how things are connected. It knows what things exist and why, enabling features like road signs pointing to distant locations, region unlocking based on player progress, and NPCs referencing far-away places. This contrasts with the [[functional-approach-procgen]] where each location is generated as a local function without context of its surroundings.

## Key Properties

- Top-down: higher-level layers plan, lower-level layers fill in details
- Items have purpose and context beyond their immediate surroundings
- Enables non-sandbox gameplay in open worlds
- Rare in infinite procedurally generated games — most use the functional approach
- [[layer-based-procedural-generation]] makes this practical in infinite worlds

## Examples

- In The Cluster (powered by [[layerprocgen]]), a RegionLayer plans paths between villages, gates, and shrines across 50-area regions, while MazeChunks generate actual platformer areas following those plans
- Road signs at junctions point to named distant locations because the maze layer queries data from the region layer
- Artefacts hidden in specific locations, with shrine spirits revealing approximate locations to the player

## Related Concepts

- [[functional-approach-procgen]] — the contrasting approach
- [[layer-based-procedural-generation]] — the architecture enabling planning at scale
- [[layerprocgen]] — framework that supports this approach

## References

- LayerProcGen documentation: Planning at Scale
