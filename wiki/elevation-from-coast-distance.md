---
title: "Elevation from Coast Distance"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, elevation, terrain, voronoi]
aliases: [coast-distance-elevation]
summary: "A terrain elevation model where elevation is defined as the distance from the coastline, producing monotonic elevation that increases inland with no local minima."
source_url: "http://www-cs-students.stanford.edu/~amitp/game-programming/polygon-map-generation/"
source_hash: "B996558CD403FDD124ABCC155317B8BBDAF943366AEE3AF70521E0D7970D35D9"
---

# Elevation from Coast Distance

## Definition / 定义

An elevation model for island maps where elevation at any point is set to its distance from the nearest coastline. Lake polygons are skipped in the distance calculation so they remain flat and contribute to valley formation. The result produces monotonic elevation — moving inland always increases elevation, and following downhill slopes from any point always leads to the ocean.

## Key Properties / 关键特性

- Elevation is set after coastlines are defined ("elevation after oceans")
- Guarantees no local minima — the downhill direction always leads to the ocean
- Elevation is set on Voronoi corners, then polygon elevation is the average of its corners
- Corner-to-corner edges serve as natural ridges and valleys
- Elevation values are redistributed to match a desired distribution (`y(x) = 1 - (1-x)^2`) so more area is low-elevation than mountainous
- Perfect for volcanic island geometry where difficulty monotonically increases from beach to mountain peak
- Not suitable for all projects — more realistic approaches use noise-based elevation before defining coastlines, or plate tectonics

## Examples / 示例

- In Realm of the Mad God, players start on beaches (low elevation) and progress uphill to mountaintop boss fights (high elevation)
- Redistribution: sorting corners by raw distance and applying the inverse cumulative distribution produces realistic proportions of coastline vs mountain area

## Related Concepts / 相关概念

- [[voronoi-island-generation]] — coastlines are defined before this elevation model
- [[downhill-river-generation]] — depends on monotonic elevation to reach the ocean
- [[whittaker-diagram-biomes]] — uses elevation as a temperature proxy
- [[2010-09-01-polygonal-map-generation]] — the article describing this technique

## References / 参考资料

- Amit Patel, "Polygonal Map Generation for Games", Red Blob Games, 2010
