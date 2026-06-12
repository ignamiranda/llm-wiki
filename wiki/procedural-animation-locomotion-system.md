---
title: "Key Takeaways: Procedural Animation / Locomotion System"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [animation, procedural-generation, game-development, locomotion]
aliases: [locomotion-system, semi-procedural-animation]
summary: "A kinematic approach to procedural character locomotion using forward kinematics, inverse kinematics, and data-driven gait parameters — developed as a Master's thesis by Rune Skovbo Johansen (2009)."
---

# Key Takeaways: Procedural Animation / Locomotion System

## Definition

A semi-procedural animation system that controls character locomotion through FK and IK without physics simulation or training. Feet placed via raycasts, footstep positions calculated from gait parameters, inverse kinematics solves leg poses. Gait parameters derived from analysis of reference animations (foot lift vs stride distance plots). Two-pass IK with foot rotation, later extended to IK-controlled foot rotation. Presented at GDC 2009 as "Dynamic Walking with Semi-Procedural Animation" in the Programming track.

## Key Properties

- Purely kinematic (no physics simulation)
- FK and IK with raycast-based foot placement
- Gait parameters fitted to reference animation data
- Two-pass IK → iterative IK with foot rotation control

## Related Concepts

- [[rune-skovbo-johansen]] — author

## References

- Source: runevision blog
