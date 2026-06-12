---
title: "Compaction"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [llm, context, session, workflow]
aliases: ["context compaction", "session compaction"]
summary: "The technique of summarizing or pruning accumulated session history to keep the context window focused and combat attention degradation, typically performed by the harness or via handoff."
---

# Compaction

## Definition

The technique of summarizing or pruning the accumulated history in a [[Session|session]] to keep the [[context-window]] focused. As a session grows, [[attention-degradation]] sets in — the model has trouble finding relevant information among the accumulated tool results and conversation turns. Compaction reduces what the window carries, improving signal-to-noise ratio.

Compaction can be automatic (the [[harness]] summarizes old turns into a compact form) or manual (the agent or user writes a summary and [[clearing|clears]] the session). The related [[handoff]] pattern is a form of compaction that transfers to a new session.

## Key Properties

- Lightweight compaction = summarization within the same session
- Heavy compaction = [[handoff]] to a fresh session
- Automatic compaction is called [[autocompact]] in some harnesses
- Compaction is the primary tool against attention degradation

## Examples

After 30 turns of debugging, the agent summarizes what was learned and what remains, then continues in a fresh context rather than pushing through.

## Related Concepts

- [[attention-degradation]] — what compaction addresses
- [[handoff]] — full compaction with session transfer
- [[clearing]] — ending a session without compaction
- [[autocompact]] — automatic harness-level compaction
- [[compaction-vs-clearing]] — comparison of two context management strategies

## References

- Matt Pocock, *Dictionary of AI Coding*, Section 5
