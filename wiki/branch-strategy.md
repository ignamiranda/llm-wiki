---
title: "Branch Strategy"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [ai-coding, git, software-engineering, agent-orchestration]
aliases: []
summary: "A configuration in Sandcastle that controls how an AI coding agent's changes relate to git branches — supporting head, merge-to-head, and branch strategies."
source_url: "https://github.com/mattpocock/sandcastle"
source_hash: "4F6AC1946DC4EDEC69F10B54A3BB12916F3CC8DF5E491A6D78B85099FEA11837"
---

# Branch Strategy

## Definition

A Branch Strategy in [[sandcastle]] controls how an AI coding agent's changes relate to git branches. There are three strategies: **Head** — the agent writes directly to the host working directory without any branch indirection; **Merge-to-head** — a temporary branch is created in a git worktree, and changes are merged back to HEAD on completion (the temp branch is cleaned up); **Branch** — commits land on an explicitly named branch in a git worktree, and re-running with the same branch reuses and fast-forwards from origin when safe.

## Key Properties

- **Head** (`{ type: "head" }`) — no worktree, no branch indirection; default for bind-mount providers
- **Merge-to-head** (`{ type: "merge-to-head" }`) — temporary branch, auto-merged and cleaned up
- **Branch** (`{ type: "branch", branch: "foo" }`) — explicitly named branch, reusable across runs
- Default strategy depends on sandbox provider type (head for bind-mount, merge-to-head for isolated)

## Examples

```typescript
// Branch strategy configuration in Sandcastle run()
const result = await run({
  agent: claudeCode("claude-opus-4-7"),
  sandbox: docker(),
  branchStrategy: { type: "branch", branch: "agent/fix-42" },
  promptFile: ".sandcastle/prompt.md",
});
```

## Related Concepts

- [[sandcastle]] — uses branch strategies for change management
- [[2026-06-11-sandcastle]] — detailed article on Sandcastle
- [[sandbox-provider]] — default branch strategy depends on provider type
- [[agent-provider]] — the agent whose changes are managed by the strategy

## References

- [Sandcastle documentation on branch strategies](https://github.com/mattpocock/sandcastle#how-it-works)
