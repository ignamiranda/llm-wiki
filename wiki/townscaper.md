---
title: "Townscaper"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, wfc, game-development, town-building, mixed-initiative]
aliases: []
summary: "An indie town-building toy by Oskar Stålberg that uses Wave Function Collapse on irregular grids with marching cubes for organic 3D geometry."
---

# Townscaper

## Definition

Townscaper is an indie town-building toy created by [[oskar-stalberg]] that demonstrates Wave Function Collapse on irregular (non-rectangular) grids combined with marching cubes for organic 3D geometry. Rather than a traditional game with goals, Townscaper is a mixed-initiative design tool where the player places colored houses on a grid and the algorithm fills in details procedurally.

## Key Properties

- **Irregular grid WFC**: adapts WFC from rectangular tiles to arbitrary polygonal grids
- **Marching cubes**: generates smooth 3D surfaces from the tile-based output
- **Mixed-initiative**: player places seeds, algorithm completes the pattern
- **Custom entropy heuristic**: avoids local minima by weighing pattern frequency differently
- **No explicit goals**: functions as a creative toy rather than a game

## Examples

- Players click to place colored houses on an archipelago grid; WFC fills in the surrounding architecture, stairs, gardens, and archways
- Removing blocks causes WFC to re-collapse the area, creating organic ruins or eroded structures

## Related Concepts

- [[wave-function-collapse]] — the core algorithm
- [[oskar-stalberg]] — creator
- Bad North — another Stålberg game using WFC for level generation
- [[chiseling-method]] — related technique for WFC connectivity

## References

- [Townscaper on Steam](https://store.steampowered.com/app/1291340/Townscaper/)
- [[2010-09-01-polygonal-map-generation]] — Amit Patel's foundational work on procedural generation
