---
title: "Sandbox Provider"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [ai-coding, sandbox, software-engineering, agent-orchestration]
aliases: []
summary: "An abstraction in Sandcastle for creating isolated execution environments for AI coding agents, with built-in providers for Docker, Podman, and Vercel."
source_url: "https://github.com/mattpocock/sandcastle"
source_hash: "4F6AC1946DC4EDEC69F10B54A3BB12916F3CC8DF5E491A6D78B85099FEA11837"
---

# Sandbox Provider

## Definition

A Sandbox Provider is an abstraction in [[sandcastle]] that creates isolated execution environments for AI coding agents. It encapsulates the logic for provisioning, mounting, and tearing down sandbox environments. Built-in providers include Docker (bind-mount containers), Podman (rootless containers), and Vercel (Firecracker microVMs), and custom providers can be created via `createBindMountSandboxProvider` or `createIsolatedSandboxProvider`.

## Key Properties

- **Bind-mount type** — mounts a git worktree directory into the container; agent writes directly to the host filesystem (Docker, Podman)
- **Isolated type** — fully isolated environment with no host filesystem access; changes merged back via git operations (Vercel)
- **No-sandbox type** — runs the agent directly on the host without isolation
- Provider-specific configuration (image name, mounts, networks, devices, CPU limits, SELinux labels)
- The `noSandbox()` provider is also accepted by `interactive()` for direct host sessions
- Default branch strategy depends on provider type: `head` for bind-mount, `merge-to-head` for isolated

## Examples

```typescript
import { docker } from "@ai-hero/sandcastle/sandboxes/docker";
import { podman } from "@ai-hero/sandcastle/sandboxes/podman";
import { vercel } from "@ai-hero/sandcastle/sandboxes/vercel";
import { noSandbox } from "@ai-hero/sandcastle/sandboxes/no-sandbox";

// Docker with custom config
docker({ imageName: "sandcastle:local", mounts: [{ hostPath: "~/.npm", sandboxPath: "/home/agent/.npm", readonly: true }] });
```

## Related Concepts

- [[sandcastle]] — uses sandbox providers for agent isolation
- [[2026-06-11-sandcastle]] — detailed article on Sandcastle
- [[branch-strategy]] — interacts with sandbox provider type to determine defaults
- [[agent-provider]] — paired with sandbox provider in Sandcastle's `run()` API

## References

- [Sandcastle Sandbox Providers documentation](https://github.com/mattpocock/sandcastle#sandbox-providers)
