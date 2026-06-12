---
title: "Specs-to-Code Criticism"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [ai, software-engineering, vibe-coding, methodology]
aliases: ["specs to code", "vibe coding critique"]
summary: "Critique of the 'specs-to-code' / vibe coding approach where developers write specifications and let AI generate code without understanding the output — arguing that the code must remain the developer's battleground."
---

# Specs-to-Code Criticism

## Definition

Matt Pocock's critique of the "specs-to-code" movement (closely related to [[vibe-coding]]), where developers write specifications and treat AI-generated code as an opaque output. The argument: this approach fails because it delegates understanding of the codebase itself. The code is the developer's battleground — you must maintain a handle on what's in it and shape it directly. Specs-to-code treats code as a derivative artifact rather than a primary artifact to be managed.

## Key Properties

- Specs-to-code treats code as output, not territory
- Developers lose the ability to shape code quality directly
- Silent assumption gaps compound across iterations
- Misalignments only surface late (when code is wrong)
- The grill-me skill is the antidote: surface assumptions before coding
- Code must be read, understood, and curated — not generated and forgotten

## Related Concepts

- [[grill-me-skill]] — requirements alignment before coding
- [[ralph-wiggum-pattern]] — iterative code shaping alternative
- [[vibe-coding]] — related practice
- [[matt-pocock]] — critic

## References

- Pocock, M. "AI Software Engineering Workshop" — YouTube
