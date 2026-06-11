---
title: "Lloyd Relaxation"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, algorithm, voronoi]
aliases: [lloyds-algorithm]
summary: "An iterative algorithm that redistributes points to produce more evenly spaced Voronoi polygon centers, reducing the clumpiness of random point distributions."
source_url: "http://www-cs-students.stanford.edu/~amitp/game-programming/polygon-map-generation/"
source_hash: "B996558CD403FDD124ABCC155317B8BBDAF943366AEE3AF70521E0D7970D35D9"
---

# Lloyd Relaxation

## Definition

An iterative algorithm that improves the distribution of points used for Voronoi diagram generation. Each iteration replaces every seed point with the centroid of its Voronoi polygon. In practice, approximating the centroid by averaging the polygon corners produces similar results at lower cost.

## Key Properties

- Each iteration produces more evenly distributed polygon sizes
- Two iterations typically suffice for map generation; more iterations produce increasingly regular grids
- Running too many iterations approaches a regular hexagonal grid (loss of natural irregularity)
- Faster alternatives include Poisson disc sampling, which generates good distributions without iteration

## Examples

- In polygon map generation, running Lloyd relaxation twice produces natural-looking polygon distributions
- Comparing 1 iteration vs 2 iterations vs 50 iterations shows progressive regularization of polygon shapes
- The algorithm is used in Voronoi-based map generators, data clustering (k-means), and mesh optimization

## Related Concepts

- [[voronoi-diagram-mapgen]] — the context where Lloyd relaxation is applied
- [[2010-09-01-polygonal-map-generation]] — the article that popularized this technique for game maps

## References

- Wikipedia: Lloyd's algorithm
- Amit Patel, "Polygonal Map Generation for Games", Red Blob Games, 2010
