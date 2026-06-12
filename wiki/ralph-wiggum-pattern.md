---
title: "Ralph Wiggum Pattern"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [ai, software-engineering, development-pattern, iteration]
aliases: ["Ralph Wiggum development"]
summary: "An iterative AI-assisted development pattern where you specify the end goal (PRD) and instruct the AI to make small changes that get progressively closer, looping until completion."
---

# Ralph Wiggum Pattern

## Definition

An iterative software development pattern for AI coding agents. Instead of writing multi-phase plans with fixed steps (phase 1, phase 2, phase 3...), you specify the end goal via a PRD (Product Requirements Document) and give a single instruction: "Make a small change that gets us closer." The AI loops on this instruction until the goal is met. Named after the Simpsons character Ralph Wiggum.

## Key Properties

- Single instruction: "Make a small change that gets us closer to the goal"
- Eliminates over-planning and brittle multi-phase specs
- Each loop iteration stays within the [[smart-zone-dumb-zone|smart zone]]
- Requires clear goal definition (PRD)
- Less structure than multi-phase plans but more autonomous
- Prone to getting stuck without the right framing

## Related Concepts

- [[smart-zone-dumb-zone]] — why small iterations matter
- [[specs-to-code-criticism]] — contrasting approach
- [[grill-me-skill]] — how to define the goal before iterating

## References

- Pocock, M. "AI Software Engineering Workshop" — YouTube
