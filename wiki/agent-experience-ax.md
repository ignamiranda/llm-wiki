---
title: "Agent Experience (AX)"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [ai-coding, agent, codebase, best-practices]
aliases: ["AX", "agent experience"]
summary: "A measure of how well a codebase is set up to support AI coding agents — including documentation, discoverability, separation of concerns, and tooling."
---

# Agent Experience (AX)

## Definition

A measure of how well a codebase is set up to support [[Agent|AI coding agents]]. Modeled on Developer Experience (DX), AX covers: how easily an agent discovers relevant files, how well the codebase structure avoids misleading the agent, how clearly conventions are documented, and whether the agent has the [[Tool|tools]] it needs.

A codebase with good AX has clear AGENTS.md files, well-separated concerns, explicit type definitions, and minimal ambiguity in naming and structure. A codebase with poor AX has deeply nested structures, ambiguous naming, implicit conventions, and missing type definitions — all of which cause agents to make incorrect assumptions.

## Key Properties

- AX is shaped by the [[environment]] — what the agent can perceive and act on
- AGENTS.md, clear naming, and explicit types improve AX
- Poor AX leads to agent guessing, hallucination, and wasted tool calls
- Improving AX benefits both human developers and AI agents

## Examples

An agent confidently describing a file that no longer exists, or inventing fields not in a type, is often an AX problem — the codebase's structure and documentation failed to guide the agent correctly.

## Related Concepts

- [[AGENTS.md]] — key AX artifact
- [[environment]] — what the agent works in
- [[Tool]] — what the agent uses to interact with the environment
- [[progressive-disclosure]] — AX documentation strategy

## References

- Matt Pocock, *Dictionary of AI Coding*, Section 7
