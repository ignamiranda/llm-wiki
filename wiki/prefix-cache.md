---
title: "Prefix Cache"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [llm, cost, caching, inference]
aliases: ["context caching", "prompt caching"]
summary: "A provider-side store that lets consecutive model provider requests skip re-processing a shared prefix of tokens, billing the cached portion as cheap cache tokens."
---

# Prefix Cache

## Definition

The [[model-provider]]-side store that lets consecutive model provider requests skip re-processing a shared prefix. When the start of a request matches the start of a recent one — same [[system-prompt]], same history up to some point — the provider reuses its prior work and bills those [[Token|tokens]] as cache tokens at a much lower rate.

Without the prefix cache, a 50-turn session would pay to re-process turn one fifty times. The cache makes long sessions economically viable.

## Key Properties

- Matches exact prefixes — if anything changes early in the conversation, the cache misses from that point
- Cache entries expire after minutes (varies by provider), not hours
- A session resumed after a long pause re-pays its history once
- When cost jumps without cause, compare cache tokens to input tokens in the usage report

## Examples

If the harness starts injecting the current time into the system prompt every turn, the prefix cache breaks at the first changed token — every subsequent request bills at full input rate.

## Related Concepts

- [[cache-tokens|cache tokens]] — tokens billed at the cached rate
- [[input-tokens|input tokens]] — what gets cached
- [[model-provider-request|model provider request]] — the request that benefits from caching

## References

- Matt Pocock, *Dictionary of AI Coding*, Section 1
