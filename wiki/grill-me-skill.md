---
title: "Grill Me Skill"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [ai, software-engineering, agent-skills, requirements, workflow]
aliases: ["grill me"]
summary: "An agent skill pattern for requirements alignment where the AI grills the developer on a brief or specification before any implementation begins, surfacing assumptions and clarifying scope."
---

# Grill Me Skill

## Definition

An [[agent-skills|agent skill]] pattern popularized by Matt Pocock where the AI grills the developer on a client brief or specification before writing any code. The developer invokes the skill with the brief, and the AI asks targeted questions to surface assumptions, clarify scope, and identify blind spots. This prevents the silent misalignment that occurs when developers jump directly from specs to code.

## Key Properties

- Invoked before any implementation work
- The AI asks clarifying questions about the brief
- Surfaces assumptions that would otherwise remain hidden
- Works with minimal context — just the skill and the brief
- Prevents the "specs to code" fallacy
- Suitable as the first step in any AI-assisted project
- The skill file is wonderfully small and focused

## Examples

A developer receives a Slack message from a client requesting gamification features. Instead of writing code, they clear their context, invoke the grill-me skill with the Slack message, and let the AI ask questions about retention goals, success metrics, and scope boundaries before any code is written.

## Related Concepts

- [[specs-to-code-criticism]] — the problem grill-me solves
- [[agent-skills]] — the skill framework
- [[matt-pocock]] — creator
- [[ralph-wiggum-pattern]] — what comes after alignment

## References

- Pocock, M. "AI Software Engineering Workshop" — YouTube
- Pocock, M. "mattpocock/skills" — GitHub
