---
title: "DESIGN.md"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [design-systems, design-tokens, ai-agents, ui-generation, google-stitch]
aliases: [design-dot-md, design system markdown]
summary: "A plain-text design system document format introduced by Google Stitch that AI coding agents read to generate consistent, brand-matching UI — no parsing or configuration required."
---

# DESIGN.md

## Definition

DESIGN.md is a plain-text design system document format introduced by Google Stitch. It is a standard markdown file that defines how a project's UI should look and feel — including visual theme, color palette, typography, components, layout, depth, and responsive behavior. AI coding agents read the file directly to generate consistent, brand-matching UI without any special parsing, configuration, or tooling.

The format follows the same principle as `AGENTS.md` (which tells coding agents how to build the project): `DESIGN.md` tells design agents how the project should look.

## Key Properties

- **Plain markdown** — Readable by any LLM without parsing or configuration; markdown is the format LLMs read best
- **No special tooling** — No Figma exports, JSON schemas, or proprietary formats required
- **Drop-in usage** — Copy to project root and the AI agent immediately understands the design language
- **Comprehensive sections** — Covers visual theme, color palette, typography hierarchy, component styling (with states), layout principles, depth/elevation, do's and don'ts, responsive behavior, and agent prompt guide
- **Brand-consistent output** — Enables AI agents to generate UI that visually matches a brand's design system

## Examples

- [[2026-06-11-awesome-design-md]] — A curated collection of 73 DESIGN.md files from real brand websites (Claude, Stripe, Apple, Tesla, Spotify, and more)
- Google Stitch's reference implementation at stitch.withgoogle.com

## Related Concepts

- [[google-stitch]] — Google's platform that introduced the DESIGN.md format
- [[agent-skills]] — The parallel concept of `AGENTS.md` files that tell coding agents how to build a project

## References

- [Google Stitch DESIGN.md Specification](https://stitch.withgoogle.com/docs/design-md/specification/)
- [Google Stitch DESIGN.md Overview](https://stitch.withgoogle.com/docs/design-md/overview/)
- [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)
