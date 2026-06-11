---
title: "System Prompt"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [llm, agent, configuration, prompt]
aliases: ["system message", "system instruction"]
summary: "The instructions a harness prepends to every model provider request — the agent's standing brief defining who it is, how to behave, which tools it can call, and what conventions to follow."
---

# System Prompt

## Definition

The instructions the [[harness]] prepends to every model provider request — the [[Agent|agent]]'s standing brief: who it is, how to behave, which [[Tool|tools]] it can call, what conventions to follow. Usually stable across a [[Session|session]].

The system prompt is written by the harness vendor, not by the user, and in coding harnesses it is large — often tens of thousands of [[Token|tokens]] of behavioral rules, tool descriptions, and edge-case handling. User standing instructions (AGENTS.md files) are loaded next to the system prompt.

## Key Properties

- Models are trained to prioritize the system prompt over user messages
- Because it is identical on every request, it forms the start of the [[prefix-cache]] prefix
- Some harnesses give full access to customize the system prompt
- When an agent insists on a convention you never asked for, it is usually the system prompt

## Examples

"Two harnesses, same model, totally different behavior on the same prompt." — "Different system prompts. One is tuned for terse code edits, the other for explaining."

## Related Concepts

- [[harness]] — delivers the system prompt
- [[Agent]] — the entity the system prompt configures
- [[prefix-cache]] — the system prompt is the start of the cached prefix
- [[AGENTS.md|AGENTS.md file]] — user instructions loaded alongside the system prompt

## References

- Matt Pocock, *Dictionary of AI Coding*, Section 2
