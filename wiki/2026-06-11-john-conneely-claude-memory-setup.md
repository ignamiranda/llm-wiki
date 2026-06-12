---
title: "John Conneely's Structured Claude Code Memory Setup"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [claude-code, memory-systems, hooks, pretooluse, knowledge-management]
source_url: "https://www.youngleaders.tech/p/how-i-finally-sorted-my-claude-code-memory"
source_hash: "20A0D91C3EEC05370D70552A2BA00C49900A21E333E84EC8D143D31952A88C34"
summary: "John Conneely's detailed guide (Young Leaders in Tech #98, Mar 18, 2026) to setting up a structured, persistent memory system for Claude Code with directory organization, PreToolUse hooks, and domain knowledge lifecycle management."
---

# John Conneely's Structured Claude Code Memory Setup

## Summary

A comprehensive walkthrough of building a structured memory system for Claude Code, inspired by [[pavel-huryn]]'s foundational concept. Conneely's system adds directory organization (global vs project memory), a PreToolUse hook for automatic context injection, and a domain knowledge lifecycle that promotes accumulated knowledge into reusable skills.

## Content

### Key Insight: Architecture Over Volume

"More memory is not the answer. Better architecture is." Conneely realized that a flat memory.md becomes the same bloated pattern as CLAUDE.md — appended to every session, with knowledge loading at the wrong time or buried. The structured version with subdirectories solves this.

### Memory Structure

```
~/.claude/memory/
  memory.md           <- index (read at session start)
  general.md          <- cross-project conventions
  tools/
    {tool}.md         <- tool configs, CLI patterns, workarounds
  domain/
    {topic}/          <- domain-specific knowledge
```

### Global vs Project Memory

- **Global** (`~/.claude/memory/`) — tools, conventions, credential patterns
- **Project** (`~/.claude/projects/{project}/memory/MEMORY.md`) — repo-specific: active tickets, doc structure, codebase patterns

### Key Technical Details

- **200-line limit**: Project MEMORY.md only loads first 200 lines at session start. Routing rules belong in CLAUDE.md, not in auto-memory files.
- **PreToolUse hook**: `~/.claude/hooks/pre-tool-memory.sh` injects memory before first tool call each session. Uses PPID as session identifier (not `CLAUDE_SESSION_ID`, which doesn't exist in hooks) with a `/tmp/` flag file to prevent re-injection per process context.
- **Auto memory**: Shipped in Claude Code v2.1.59 on Feb 26, 2026. Scoped per project with memory/ folder in `~/.claude/projects/{mapped-path}/`.

### Domain Knowledge Lifecycle

1. **Staging** — knowledge accumulates in `domain/{name}/`
2. **Promotion** — enough knowledge exists to package as a skill
3. **Pointer** — after promotion, the memory file becomes a pointer to the skill

### CLAUDE.md Sections

Conneely's CLAUDE.md went from 189 lines to 63 lines after reorganization. Sections added:
- Memory Management (reading/writing rules)
- Global Memory (topic file list)
- Global Memory Reference Rule (project pointer, not duplication)
- Repo Memory Auto-Init (auto-create MEMORY.md in new projects)
- Domain Knowledge Lifecycle

### Team Sharing

Domain files can be synced with teammates via git. Subject matter experts contribute their context directly as living files. Recommendations: create a private git repo for `~/.claude/`, with .gitignore for sensitive content.

### Part 2: PreToolUse Hook

Optional hook injects project memory and global index before the first tool call of every session, including for new subagents. Two-file design: bash wrapper (~5ms) gates a Python script. Survives context compression in long sessions.

## Key Takeaways

- Structured memory with subdirectories is more effective than flat files
- Routing rules belong in CLAUDE.md (full load), not in project MEMORY.md (200-line budget)
- PreToolUse hook with PPID-based dedup provides reliable auto-injection
- Domain knowledge lifecycle prevents stale accumulation
- Git enables team sharing of memory files

## Related

- [[pavel-huryn]] — originated the basic concept
- [[john-connolly]] — the author's person page
- [[2026-06-11-claude-code-memory-systems]] — Level 2 in the taxonomy (enhanced hooks)
- [[memory-system-ai]] — general AI memory category
