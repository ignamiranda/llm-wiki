---
title: "Claude.md"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [claude-code, memory-systems, configuration, agent-skills]
aliases: [claude-dot-md, project-instructions]
summary: "A plain markdown file in a project folder that stores rules, brand information, coding style, and instructions — always loaded into every Claude Code session as a system prompt."
source_url: "https://youtu.be/UHVFcUzAGlM"
source_hash: "f3624d705c6e04e2e7538ae9bf26cb817ebab58bc58a64cb6d04be83c6486c2e"
---

# Claude.md

## Definition

A plain markdown file (`claude.md`) placed in a project folder that stores rules, brand information, client preferences, coding style, and project-level instructions. It is always loaded into every Claude Code session, effectively functioning as a per-project system prompt.

## Key Properties

- Can exist at multiple levels: global Claude project folder (all instances), root folder (multiple projects), or individual project folder (specific instructions)
- Lower-level claude.md files inherit from parent claude.md but override conflicting rules locally
- Should be kept **under 200 lines** to avoid [[context-rot]]
- Larger documents (brand guides, tone-of-voice docs, client lists) should be kept in separate files referenced from claude.md, loaded only when needed

## Best Practices

- Treat claude.md as an index/table of contents, not a dump of all context
- Reference external files for detailed documentation
- Use alongside memory.md (auto memory) for complementary purposes
- Keep focused on rules, conventions, and frequently-needed facts

## Related Concepts

- [[memory-system-ai]] — broader context of AI agent memory
- [[context-rot]] — why keeping claude.md under 200 lines matters
- [[2026-06-11-claude-code-memory-systems]] — level 1 native memory coverage

## References

- "Every Claude Code Memory System Compared" — YouTube video
