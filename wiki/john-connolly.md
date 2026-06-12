---
title: "John Conneely"
type: person
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [claude-code, memory-systems, agent-skills, ai-engineering, hooks]
aliases: [john-connolly]
summary: "Developer and author of Young Leaders in Tech who created an advanced structured Claude Code memory system with PreToolUse hooks, PPID-based dedup, and domain knowledge lifecycle, building on Paweł Huryn's foundational concept."
source_url: "https://www.youngleaders.tech/p/how-i-finally-sorted-my-claude-code-memory"
source_hash: "20A0D91C3EEC05370D70552A2BA00C49900A21E333E84EC8D143D31952A88C34"
---

# John Conneely

## Bio

Developer and author of the Young Leaders in Tech Substack publication. Conneely published a detailed article in March 2026 (issue #98) describing his structured Claude Code memory system, building on [[pavel-huryn]]'s earlier concept. His system adds directory-based organization (global vs project memory), a PreToolUse hook for automatic context injection, PPID-based dedup to prevent re-injection per subagent, a domain knowledge lifecycle, and an auto-init workflow for new projects.

## Key Contributions

- Developed a production-grade structured memory system for Claude Code with `~/.claude/memory/` directories
- Introduced PreToolUse hook with PPID-based flag file dedup for auto-injection
- Defined the domain knowledge lifecycle: staging → promotion → pointer (to skill)
- Identified the 200-line budget constraint of project MEMORY.md (routing rules → CLAUDE.md, not MEMORY.md)
- Created auto-init workflow for new projects (Claude scaffolding on first open)
- Documented team sharing of memory domain files via git
- Reduced CLAUDE.md from 189 lines to 63 lines through reorganization
- Published complete setup prompts for both Part 1 (memory structure) and Part 2 (PreToolUse hook)

## Related Work

- [[2026-06-11-claude-code-memory-systems]] — Level 2 of the memory taxonomy
- [[pavel-huryn]] — originated the concept his system builds on
- [[memory-system-ai]] — general AI memory concept

## Links

- Young Leaders in Tech: https://www.youngleaders.tech/
- Memory setup article (#98): https://www.youngleaders.tech/p/how-i-finally-sorted-my-claude-code-memory
