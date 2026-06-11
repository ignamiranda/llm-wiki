---
title: "Matt Pocock's Sandcastle — Orchestrating AI Coding Agents"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [ai-coding, software-engineering, sandbox, automation, typescript, agent-orchestration]
summary: "Sandcastle is a TypeScript library for orchestrating AI coding agents in isolated sandboxes with configurable providers, branch strategies, and a flexible prompt system."
source_url: "https://github.com/mattpocock/sandcastle"
source_hash: "4F6AC1946DC4EDEC69F10B54A3BB12916F3CC8DF5E491A6D78B85099FEA11837"
---

# Matt Pocock's Sandcastle — Orchestrating AI Coding Agents

## Summary

Sandcastle (`@ai-hero/sandcastle`) is a TypeScript library for orchestrating AI coding agents in isolated sandboxes. Agents are invoked with a single `sandcastle.run()`, Sandcastle handles sandboxing with a configurable branch strategy, and commits are merged back automatically. It is provider-agnostic — shipping with built-in providers for Docker, Podman, and Vercel — and supports multiple agent backends including Claude Code, Pi, Codex, Cursor, OpenCode, and Copilot.

## Content

### Architecture

Sandcastle's core is a `run()` function that accepts an agent provider and a sandbox provider. The agent provider abstracts the coding AI backend; the sandbox provider creates an isolated environment. A configurable branch strategy determines how agent changes relate to git branches:

- **Head** — agent writes directly to the host working directory (default for bind-mount providers)
- **Merge-to-head** — temporary branch in a git worktree, merged back to HEAD on completion
- **Branch** — explicitly named branch in a git worktree, reusable across runs

### Sandbox Providers

| Provider | Type | Isolation |
|----------|------|-----------|
| Docker | Bind-mount | Container with bind-mounted worktree |
| Podman | Bind-mount | Rootless container alternative |
| Vercel | Isolated | Firecracker microVMs via `@vercel/sandbox` |
| No-sandbox | None | Direct host execution |

Custom providers can be created via `createBindMountSandboxProvider` or `createIsolatedSandboxProvider`.

### API Surface

**`run()`** — one-shot agent invocation with automatic sandbox lifecycle:

```typescript
const result = await run({
  agent: claudeCode("claude-opus-4-7"),
  sandbox: docker(),
  promptFile: ".sandcastle/prompt.md",
});
```

**`createSandbox()`** — reusable sandbox for multi-run workflows (implement-then-review, etc.):

```typescript
await using sandbox = await createSandbox({
  branch: "agent/fix-42",
  sandbox: docker(),
});
```

**`createWorktree()`** — independent git worktree lifecycle, separate from any sandbox.

**`interactive()`** — interactive agent session in a sandbox or worktree.

### Prompt System

Prompts support `{{KEY}}` placeholder substitution and `` !`command` `` dynamic context expansion. Two built-in prompt arguments are always available: `{{SOURCE_BRANCH}}` (where the agent works) and `{{TARGET_BRANCH}}` (the host's active branch).

### Structured Output

`Output.object()` and `Output.string()` extract typed, schema-validated payloads from agent stdout using XML tags and Standard Schema validators (Zod, Valibot, ArkType).

### Early Termination

Agents emit `<promise>COMPLETE</promise>` (configurable) to stop the iteration loop early. A completion timeout handles hanging child processes gracefully.

### CLI Commands

- `sandcastle init` — scaffolds `.sandcastle/` config, Dockerfile, prompt, and .env
- `sandcastle docker build-image` / `sandcastle docker remove-image`
- `sandcastle podman build-image` / `sandcastle podman remove-image`

### Templates

Five init templates: `blank`, `simple-loop`, `sequential-reviewer`, `parallel-planner`, and `parallel-planner-with-review`.

## Key Takeaways

- Sandcastle provides a unified API (`run()`, `createSandbox()`, `createWorktree()`, `interactive()`) for running AI coding agents in isolation
- Provider-agnostic: Docker, Podman, Vercel, or custom sandbox backends
- Branch strategies give fine-grained control over how agent changes integrate into the repo
- The prompt system supports interpolation (`{{KEY}}`), dynamic context (`` !`command` ``), structured output, and early termination
- Built on git worktrees for safe branch isolation

## Related

- [[sandcastle]] — the core concept
- [[sandbox-provider]] — abstraction for isolated execution environments
- [[branch-strategy]] — controls how agent changes relate to branches
- [[agent-provider]] — abstraction for AI coding agent backends
- [[matt-pocock]] — author of Sandcastle
- [[2026-06-11-mattpocock-skills]] — Matt Pocock's agent skills repository (companion project)
- [[agent-skills]] — composable declarative skills for coding agents
