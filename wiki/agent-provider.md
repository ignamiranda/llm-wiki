---
title: "Agent Provider"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [ai-coding, software-engineering, agent-orchestration]
aliases: []
summary: "An abstraction in Sandcastle that wraps different AI coding agent backends (Claude Code, Pi, Codex, Cursor, OpenCode, Copilot) behind a unified interface."
source_url: "https://github.com/mattpocock/sandcastle"
source_hash: "4F6AC1946DC4EDEC69F10B54A3BB12916F3CC8DF5E491A6D78B85099FEA11837"
---

# Agent Provider

## Definition

An Agent Provider is an abstraction in [[sandcastle]] that wraps different AI coding agent backends behind a unified interface. It allows Sandcastle's `run()` and related APIs to invoke any supported coding agent without changing the orchestration code. Currently supported agent providers include `claudeCode()`, `pi()`, `codex()`, `cursor()`, `opencode()`, and `copilot()`, each accepting a model string and optional provider-specific options (e.g., effort level).

## Key Properties

- Unified interface for diverse AI coding agent backends
- Provider-specific options (e.g., `{ effort: "high" }` for Claude Code)
- Agents are invoked inside the sandbox environment with the configured prompt
- Compile-time type safety via the `AgentProvider` type
- Agent model selection is separate from sandbox provider selection

## Examples

```typescript
import { run, claudeCode } from "@ai-hero/sandcastle";

// Claude Code with high effort
await run({
  agent: claudeCode("claude-opus-4-7", { effort: "high" }),
  sandbox: docker(),
  prompt: "Fix issue #42.",
});

// Using Pi, Codex, or other supported agents
// agent: pi("claude-sonnet-4-6")
// agent: codex("gpt-5.4")
// agent: cursor("composer-2")
// agent: opencode("opencode/big-pickle")
// agent: copilot("claude-sonnet-4.5")
```

## Related Concepts

- [[sandcastle]] — uses agent providers for backend abstraction
- [[2026-06-11-sandcastle]] — detailed article on Sandcastle
- [[sandbox-provider]] — paired with agent provider in Sandcastle's API
- [[branch-strategy]] — independent of which agent provider is used

## References

- [Sandcastle API documentation](https://github.com/mattpocock/sandcastle#api)
