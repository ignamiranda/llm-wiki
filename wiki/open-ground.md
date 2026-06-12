---
title: "Open Ground"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [ai, research, collaboration, distributed-systems, open-source]
aliases: ["distributed research", "untrusted compute pool"]
summary: "A model for collaborative AI research where an untrusted pool of workers on the internet contribute compute cycles to a shared research problem, with trusted workers performing verification."
---

# Open Ground

## Definition

A distributed research collaboration model proposed by Andrej Karpathy, inspired by SETI@home and Folding@home. An untrusted pool of workers on the internet contributes compute cycles to solve research problems where candidate generation is expensive but verification is cheap. Workers submit candidate solutions (commits), trusted workers verify them, and results are tracked on a leaderboard. The system is designed to tolerate malicious actors because verification catches bad inputs.

## Key Properties

- Untrusted workers contribute compute; trusted workers verify
- Blockchain-like structure: commits as blocks, proof-of-work is experimentation
- Verification is cheap relative to generation
- Enables a "swarm" that could potentially outcompete frontier labs
- Compute becomes the contribution currency
- Secure by design — arbitrary code execution requires sandboxing

## Examples

Auto research at home: instead of donating money to research institutions, people purchase compute and contribute to research swarms for causes they care about (cancer research, AI alignment, etc.).

## Related Concepts

- [[auto-research]] — the closed-loop system this enables
- [[andrej-karpathy]] — proponent

## References

- Karpathy, A. "No Priors Podcast" — YouTube
