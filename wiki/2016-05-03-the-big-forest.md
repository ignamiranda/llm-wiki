---
title: "The Big Forest"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, game-development, terrain, forest]
summary: "First public reveal of the procedural infinite forest terrain project, using Perlin noise for tree placement with threshold-based clustering and footstep sounds."
source_url: "https://blog.runevision.com/2016/05/the-big-forest.html"
---

# The Big Forest

## Summary
First public reveal of the procedural infinite forest terrain project, using Perlin noise for tree placement with threshold-based clustering and footstep sounds.

## Content

The Big Forest began as an early prototype exploring procedural infinite forest terrain generation. The core technique uses Perlin noise to determine tree placement: a Perlin noise value is sampled at each candidate location, and a tree is placed only if the value exceeds a configurable threshold. Because Perlin noise produces smooth, continuous values, this creates natural-looking clusters of trees rather than uniform distribution — groves emerge where the noise is consistently above threshold, and clearings appear where it dips below.

The prototype was described as a walking simulator or virtual forest experience. Early features included footstep sounds that varied by surface type — a small detail that significantly enhanced immersion in the procedurally generated environment. The terrain itself was generated using noise-based height maps, creating gentle hills and valleys that the trees clustered around.

This early prototype later expanded into the full The Big Forest game project, which grew to encompass procedural creature generation, game progression dependency graphs, and advanced terrain generation techniques. The project became Rune's primary creative focus, and many of the later blog posts on procedural generation techniques directly serve its development.

## Key Takeaways
- Perlin noise threshold for natural tree clustering
- Infinite forest terrain generation
- Early prototype of the full The Big Forest project

## Related
- [[rune-skovbo-johansen]] — author
- [[infinite-terrain]] — related
- [[noise-based-terrain-generation]] — related
