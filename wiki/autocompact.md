---
title: "Autocompact"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [llm, context, session, workflow, compaction]
aliases: [automatic-compaction]
summary: "Automatic harness-level session compaction — the harness summarizes or prunes accumulated history without requiring manual agent intervention."
---

# Autocompact

## Definition

Autocompact is the automatic compaction mechanism built into certain AI coding harnesses. When enabled, the harness monitors session length and context usage, and automatically summarizes older turns into a compact form to keep the context window focused. Unlike manual [[compaction]] (where the agent writes a summary), autocompact runs transparently at the harness level.

## Key Properties

- Harness-triggered, not agent-initiated
- Reduces context window pressure during long sessions
- Some harnesses allow configuring compaction thresholds
- Complementary to manual [[handoff]] compaction

## Related Concepts

- [[compaction]] — the general technique of session summarization
- [[handoff]] — full compaction with session transfer
- [[attention-degradation]] — what compaction addresses
