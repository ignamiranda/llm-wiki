---
title: "Token Awareness"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [ai, software-engineering, context, token-management]
aliases: ["token monitoring", "context tracking"]
summary: "The practice of continuously monitoring the exact token count during an AI coding session to know how close the session is to the dumb zone."
---

# Token Awareness

## Definition

The practice of watching the exact token count during an AI-assisted coding session. By knowing precisely how many tokens are in the context window, the developer can predict when the session will enter the [[smart-zone-dumb-zone|dumb zone]] and take corrective action ([[compaction-vs-clearing|clear or compact]]) before quality degrades. Matt Pocock considers this "essential information on every coding session."

## Key Properties

- Monitor exact token count, not estimates
- ~100K tokens is a practical warning threshold
- Token awareness enables proactive context management
- Most coding harnesses display token count in the status line
- Without token awareness, degradation is only noticed after it has already affected output

## Related Concepts

- [[smart-zone-dumb-zone]] — why token awareness matters
- [[compaction-vs-clearing]] — what to do when approaching the limit
- [[attention-degradation]] — the phenomenon being managed
- [[session-stages]] — lifecycle context

## References

- Pocock, M. "AI Software Engineering Workshop" — YouTube
