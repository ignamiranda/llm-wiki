---
title: "Noisy Edges"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, rendering, voronoi]
aliases: []
summary: "A rendering technique that replaces straight polygon borders with noisy, organic-looking lines constrained to quadrilateral regions defined by the dual graph, hiding the underlying polygon structure."
source_url: "http://www-cs-students.stanford.edu/~amitp/game-programming/polygon-map-generation/"
source_hash: "B996558CD403FDD124ABCC155317B8BBDAF943366AEE3AF70521E0D7970D35D9"
---

# Noisy Edges

## Definition

A technique for making polygonal map borders look organic by replacing straight polygon edges with irregular, noisy lines. Each straight edge between two polygon centers and their shared corner pair defines a quadrilateral region. The noisy line is constrained to stay within allocated sub-quadrilaterals, preventing different edges from crossing each other.

## Key Properties

- Every Delaunay-Voronoi edge pair defines a quadrilateral (A-p1-B-p2) that constrains noise
- Each quadrilateral is subdivided: two sub-quadrilaterals for the Delaunay edge, two for the Voronoi edge
- Lines stay within their allocated space and meet at the center, guaranteeing no crossings
- The entire map can be partitioned into these quadrilaterals with no gaps
- Recursive subdivision within quadrilaterals produces more detailed noise at higher zoom levels
- Has a large visual impact, especially on rivers and coastlines

## Examples

- A Voronoi coastline rendered with noisy edges appears as an organic shoreline rather than a jagged polygon outline
- River paths with noisy edges blend in with the terrain instead of appearing as straight segments
- Later implementations (mapgen4) use a different algorithm with curved splines for smoother results

## Related Concepts

- [[dual-graph-representation]] — the dual graph defines the quadrilateral constraints
- [[voronoi-diagram-mapgen]] — the underlying geometric structure
- [[2010-09-01-polygonal-map-generation]] — the article that introduced this technique

## References

- Amit Patel, "Polygonal Map Generation for Games", Red Blob Games, 2010
- Amit Patel, "Noisy Edges", Red Blob Games (interactive guide)
