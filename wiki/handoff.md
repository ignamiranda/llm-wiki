---
title: "Handoff"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [llm, workflow, session, context]
aliases: ["task handoff"]
summary: "The practice of transferring context from one session to another, typically by writing a structured summary document that a fresh agent session reads to continue a task."
---

# Handoff

## Definition

The practice of transferring context from one [[Agent|agent]] [[Session|session]] to another. Because the [[Model|model]] is [[stateless]], a new session starts with zero knowledge of what happened before. A handoff bridges this gap by writing a structured summary — a handoff artifact — to the [[filesystem]], which the next session loads into its [[context-window]].

Handoffs are necessary when a task exceeds a single session's capacity (due to [[attention-degradation]]) or spans multiple work sessions. They are also used to delegate work to different agents or models.

## Key Properties

- A handoff artifact is a file that captures: current state, decisions made, remaining work, conventions learned
- The handoff pattern enables [[AFK]] operation — the agent works, hands off, and the next session picks up
- Handoffs are the bridge between the model's permanent statelessness and the need for multi-session work
- Related to [[compaction]], which is a lighter form of context transfer within a session

## Examples

An agent working on a large refactor that exceeds 50 turns writes a `handoff.md` summarizing what was done, what remains, and key decisions — then the developer starts a fresh session that reads the handoff.

## Related Concepts

- [[compaction]] — lighter form of context transfer
- [[clearing]] — ending a session without handoff
- [[attention-degradation]] — what makes handoffs necessary
- [[stateless]] — why handoffs are needed
- [[compaction-vs-clearing]] — comparison of context management approaches

## References

- Matt Pocock, *Dictionary of AI Coding*, Section 5
