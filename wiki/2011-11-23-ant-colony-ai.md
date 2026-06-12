---
title: "Ant Colony — Google AI Challenge"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [ai, game-development, competition, pathfinding]
summary: "Participation in the Google AI Challenge ant colony AI programming contest, using collaborative diffusion / flood-fill pathfinding for multi-goal AI. Ranked 39th worldwide, #1 in Denmark."
source_url: "https://blog.runevision.com/2011/11/ant-colony-google-ai-challenge.html"
---

# Ant Colony — Google AI Challenge

## Summary

Participation in the Google AI Challenge, a programming contest where competitors built AI for an ant colony simulation. A collaborative diffusion / flood-fill approach was used for multi-goal pathfinding, achieving 39th place worldwide and 1st in Denmark.

## Content

The Google AI Challenge pitted competitors' ant colony AI implementations against each other in a real-time strategy game where ants needed to collect food, explore the map, and engage enemy colonies. The key technical challenge was multi-goal pathfinding — coordinating dozens of ants simultaneously pursuing different objectives while avoiding obstacles and enemies.

The solution used collaborative diffusion (flood-fill) where each goal propagated influence values through the grid, and ants followed the gradient of combined influences. This approach naturally handled multiple competing goals and emergent ant distribution without explicit per-ant path assignment. The algorithm performed well, ranking 39th out of thousands of entries worldwide and first among Danish participants.

## Key Takeaways

- Collaborative diffusion / flood-fill for multi-goal pathfinding
- Ranked 39th worldwide, #1 in Denmark

## Related

- [[rune-skovbo-johansen]] — author
