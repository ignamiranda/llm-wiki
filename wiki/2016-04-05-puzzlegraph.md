---
title: "Working with Puzzle Design Through State Space Visualization"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [game-design, puzzle, procedural-generation, tool, unity]
summary: "PuzzleGraph — a free open-source tool for analyzing and visualizing puzzle state spaces using graph theory to help designers understand solution paths, dead ends, and fail states."
source_url: "https://blog.runevision.com/2016/04/working-with-puzzle-design-through.html"
---

# Working with Puzzle Design Through State Space Visualization

## Summary
PuzzleGraph — a free open-source tool for analyzing and visualizing puzzle state spaces using graph theory to help designers understand solution paths, dead ends, and fail states.

## Content
PuzzleGraph is a tool for puzzle design that visualizes the complete state space of a puzzle as an interactive graph. The tool models puzzle elements including gates, toggles, pressure plates, boulders, one-way edges, and hazards — each with defined behaviors that affect puzzle state. By exploring the full state space, designers can identify unintended shortcuts, dead ends, unsolvable states, and whether the intended solution path is sufficiently constrained.

The state space search algorithm cleanly separates puzzle design (the static configuration of elements) from puzzle state (the dynamic configuration of values at a given moment). Starting from the initial state, the algorithm performs BFS or DFS to explore all reachable states, building a graph where each node is a distinct state and each edge is a player action. Spring-force simulation lays out the graph, positioning states that differ by few actions close together and states requiring many actions further apart.

The tool is open source under MPL 2.0 and was inspired by analysis of puzzles from games like Lara Croft and the Guardian of Light. The article discusses state space suitability — not all puzzles benefit from state space analysis — and state collapse techniques for simplifying rich state spaces to manageable graph sizes, using Sokoban as an example of a puzzle whose state space benefits from careful abstraction.

## Key Takeaways
- Separate puzzle design (static) from puzzle state (dynamic) for state space analysis
- Spring-force graph layout with ideal distances based on state change count
- State collapse can simplify rich state spaces to manageable sizes
- Open source at hg.sr.ht/~runevision/puzzlegraph

## Related
- [[rune-skovbo-johansen]] — author
- [[game-progression-dependency-graph]] — related graph-based design technique
