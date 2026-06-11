---
title: "Sandcastle"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [ai-coding, software-engineering, agent-orchestration, typescript]
aliases: ["@ai-hero/sandcastle"]
summary: "A TypeScript library for orchestrating AI coding agents in isolated sandboxes with configurable providers, branch strategies, and a flexible prompt system."
source_url: "https://github.com/mattpocock/sandcastle"
source_hash: "4F6AC1946DC4EDEC69F10B54A3BB12916F3CC8DF5E491A6D78B85099FEA11837"
---

# Sandcastle

## Definition

Sandcastle (`@ai-hero/sandcastle`) is a TypeScript library created by [[matt-pocock]] for orchestrating AI coding agents in isolated sandbox environments. It provides a provider-agnostic API where agents are invoked via `sandcastle.run()`, sandboxing is handled by configurable providers (Docker, Podman, Vercel), and changes are merged back through configurable branch strategies.

## Key Properties

- Provider-agnostic sandbox abstraction (Docker, Podman, Vercel, custom, or no-sandbox)
- Configurable branch strategies: head, merge-to-head, branch
- Multi-agent backend support: Claude Code, Pi, Codex, Cursor, OpenCode, Copilot
- Flexible prompt system with `{{KEY}}` substitution and `` !`command` `` expansion
- Structured output extraction via XML tags and schema validators
- Early termination via configurable completion signals
- Git worktree-based isolation for safe branch operations
- Automatic cleanup with `await using` pattern and `Symbol.asyncDispose`

## Examples

One-shot agent invocation:

```typescript
import { run, claudeCode } from "@ai-hero/sandcastle";
import { docker } from "@ai-hero/sandcastle/sandboxes/docker";

const result = await run({
  agent: claudeCode("claude-opus-4-7"),
  sandbox: docker(),
  promptFile: ".sandcastle/prompt.md",
});
```

Multi-run implement-then-review with reusable sandbox:

```typescript
await using sandbox = await createSandbox({
  branch: "agent/fix-42",
  sandbox: docker(),
});
const implResult = await sandbox.run({ agent: claudeCode("claude-opus-4-7"), promptFile: "implement.md" });
const reviewResult = await sandbox.run({ agent: claudeCode("claude-sonnet-4-6"), prompt: "Review the changes." });
```

## Related Concepts

- [[sandbox-provider]] — Sandcastle uses sandbox providers for isolation
- [[branch-strategy]] — Sandcastle uses branch strategies for change management
- [[agent-provider]] — Sandcastle uses agent providers for AI backend abstraction
- [[2026-06-11-sandcastle]] — detailed article about the project
- [[matt-pocock]] — creator of Sandcastle
- [[agent-skills]] — related pattern for composable agent capabilities

## References

- [GitHub Repository](https://github.com/mattpocock/sandcastle)
- [npm Package](https://www.npmjs.com/package/@ai-hero/sandcastle)
