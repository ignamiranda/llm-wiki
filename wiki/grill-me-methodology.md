---
title: "Grill-Me Methodology"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [agent-skills, alignment, communication, requirements]
aliases: ["grill-me", "grill-with-docs"]
summary: "An alignment technique where the AI agent interviews the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree before starting work."
---

# Grill-Me Methodology

## Definition

The Grill-Me methodology is an agent skill pattern for achieving human-agent alignment before any code is written. The agent interviews the user about their plan, design, or requirements, asking detailed questions until every branch of the decision tree is resolved. This prevents the most common failure mode in AI-assisted development: the agent building something different from what the user wanted.

## Key Properties

- **Proactive questioning** — The agent drives the conversation by asking questions, not the user
- **Decision tree resolution** — Each branch of uncertainty is explored and resolved before proceeding
- **No premature action** — No code is written until alignment is confirmed
- **Two variants** — `grill-me` (for general/non-code plans) and `grill-with-docs` (which also updates CONTEXT.md and ADRs as decisions crystallise)

## Examples

A user says "I want to add a checkout flow." The agent responds with questions: "What payment providers? Guest checkout or account-only? What happens after payment? Error states? What modules are affected?" Each answer narrows uncertainty until the full scope is defined.

## Related Concepts

- [[agent-skills]] — the parent concept of composable skill files
- [[shared-language-context-md]] — often used alongside grill-me to document decisions
- [[2026-06-11-mattpocock-skills]] — the repository that popularized this methodology

## References

- [grill-me SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md)
- [grill-with-docs SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md)
