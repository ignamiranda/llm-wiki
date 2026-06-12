---
title: "L-System Tree Generation"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, graphics, l-systems, vegetation]
aliases: []
summary: "The use of L-systems (Lindenmayer systems) for procedurally generating tree and plant geometry through iterative string rewriting."
---

# L-System Tree Generation

## Definition

L-systems generate tree geometry via a formal grammar with production rules applied iteratively: start with an axiom (e.g., "F"), repeatedly apply rules (e.g., "F → F[+F]F[-F]F"), and interpret the resulting string as turtle graphics commands (F = forward, + = turn right, - = turn left, [ = push state, ] = pop state). Parameters control branching angle, segment length, and recursion depth. Used by Rune Skovbo Johansen for procedural tree generation in "A Study in Composition".

## Key Properties

- Formal grammar with iterative rewriting
- Turtle graphics interpretation
- Parameters: branching angle, length, recursion depth
- Stochastic variation for natural results

## Related Concepts

- [[rune-skovbo-johansen]] — author

## References

- Source: runevision blog
