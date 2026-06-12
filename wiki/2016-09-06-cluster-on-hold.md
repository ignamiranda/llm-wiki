---
title: "Development of The Cluster Put on Hold"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [game-development, procedural-generation, the-cluster, postmortem]
summary: "Analysis of why The Cluster was put on hold after 10+ years: burdensome design constraints around no-getting-stuck guarantees, gravity without flight, AI-follow, and 3rd person art requirements."
source_url: "https://blog.runevision.com/2016/09/development-of-cluster-put-on-hold.html"
---

# Development of The Cluster Put on Hold

## Summary

After more than a decade of development, The Cluster was put on hold because its design constraints became too burdensome. The analysis identified five specific constraints that made continued work prohibitively expensive, leading to a shift toward first-person projects with fewer restrictions.

## Content

The Cluster's development paused after 10+ years due to an accumulation of design constraints that each compounded the difficulty of the others. First, the infinite procedural world had to guarantee the player could never get stuck anywhere — a hard problem when geometry is generated on the fly. Second, gravity without flight constrained level design significantly, requiring carefully placed platforms and paths.

Third, the AI companion had to be able to follow the player through any part of the world, which meant every area had to be navigable by both player and AI. Fourth, the large grid size made detail work expensive in both generation time and memory. Fifth, the 3rd person perspective required more detailed art assets than a first-person game would need.

The decision led to a strategic pivot: future projects would be first-person, feature no jumping mechanics, avoid humanoid characters, and have no story-driven narrative. This played to existing strengths in environment creation while shedding the constraints that had made The Cluster unmanageable.

## Key Takeaways

- Design constraints became too restrictive for development pace
- Shift to first-person, no-jumping, no-story direction

## Related

- [[rune-skovbo-johansen]] — author
- [[the-cluster]] — game reference
