---
title: "AC-4 Constraint Propagation (WFC)"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, wfc, constraint-satisfaction, algorithm]
summary: "The constraint propagation algorithm used in WFC's propagation phase, based on the AC-4 arc consistency algorithm by Mohr and Henderson (1986)."
---

# AC-4 Constraint Propagation (WFC)

## Definition

AC-4 is the constraint propagation algorithm employed by WFC during the propagation phase. After each observation step collapses a region into a definite state, AC-4 propagates this new information through the output by enforcing arc consistency — removing patterns from neighboring regions that are incompatible with the collapsed state, then propagating those removals further. This is a general arc consistency algorithm originally developed for constraint satisfaction problems by Roger Mohr and Thomas C. Henderson in 1986.

## Key Properties

- Enforces arc consistency after each observation
- Maintains a queue of nodes whose constraints need updating
- Significantly faster than loopy belief propagation on CPU (which WFC originally used)
- WFC uses the AC-4 variant specifically (not AC-3)
- The propagation is deterministic and runs until no more reductions are possible or a contradiction occurs

## Related Concepts

- [[wave-function-collapse]] — the parent algorithm
- [[observation-propagation-cycle]] — the cycle this algorithm powers
- [[model-synthesis]] — prior work using AC-3

## References

- Roger Mohr & Thomas C. Henderson, "Arc and Path Consistency Revisited" (1986)
- Alan K. Mackworth, "Consistency in Networks of Relations" (1977)
