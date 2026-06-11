---
title: "Ink Weave Structure"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [interactive-fiction, ink, narrative-design, weave-structure]
aliases: [weave-structure]
summary: "Ink's core narrative flow construct — an always-dropping-downwards system of knots, stitches, and diverts that prevents the player from retreating to earlier story states."
---

# Ink Weave Structure

## Definition

The Weave Structure is Ink's core narrative flow construct, designed for the Ink scripting language. It organizes story content into knots (scenes) and stitches (sub-scenes) connected by diverts. The structure always drops downwards — once the narrative passes a point, it cannot go back to it, preventing the player from retreating to earlier story states. This enables narrative momentum by construction.

## Key Properties

- Always-dropping-downwards flow: once past a point, cannot return
- Knots: top-level scene containers
- Stitches: sub-containers within knots
- Diverts: explicit transitions between knots/stitches
- Glue: prevents line breaks for continuous flow
- Gather: convergence point for branching storylines

## Related Concepts

- [[ink-scripting-language]] — the language this structure belongs to
- [[narrative-momentum]] — design principle enforced by the weave structure
- [[only-forwards-design]] — broader design philosophy of always-pushing-forward narrative
