---
title: "Claude Skills Plugin"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [agent-skills, claude, plugin-marketplace, claude-code, skill-distribution]
aliases: [skills-plugin, claude-code-plugin, skills-marketplace]
source_url: "https://github.com/anthropics/skills/"
source_hash: "299371c3dd28ad6d7066e8b9cf1bb799b408636eae8b710a30935b87b5f130c2"
summary: "A plugin marketplace system in Claude Code for registering, discovering, and installing Agent Skills from GitHub repositories via /plugin commands."
---

# Claude Skills Plugin

## Definition

The Claude Skills Plugin system enables distribution and installation of Agent Skills through a marketplace mechanism in Claude Code. Skills are registered as plugins from GitHub repositories and can be installed via `/plugin` commands. The anthropics/skills repository, for example, provides two plugins: `document-skills` (docx, pdf, pptx, xlsx) and `example-skills` (creative, technical, enterprise skills).

## Key Properties

- **Marketplace registration**: Repositories are registered with `/plugin marketplace add <owner>/<repo>`
- **Plugin groups**: Skills within a repo are organized into named plugin bundles (e.g., `document-skills`, `example-skills`)
- **Command interface**: Installation via `/plugin install <plugin-name>@<marketplace-name>`
- **GitHub-based**: Skills are distributed through public GitHub repositories
- **Instant activation**: Installed skills are available immediately without restart

## Examples

```bash
# Register the marketplace
/plugin marketplace add anthropics/skills

# Install specific plugin bundles
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

Once installed, skills are activated by mentioning the task — for example: "Use the PDF skill to extract form fields from path/to/file.pdf"

## Related Concepts

- [[agent-skills]] — The skills that plugins distribute
- [[skill-file-format]] — The format used to define skills within plugins
- [[2026-06-11-anthropic-skills-repo]] — The reference repository that serves as the primary skills marketplace
- [[shokunin]] — A broader ecosystem supporting 6 runtimes (OpenCode, Claude Code, Cursor, Windsurf, Cline, Continue.dev) with skills, memory, and MCP servers

> 📝 **Updated from [[2026-06-11-shokunin]]**: Added Shokunin as an example of multi-runtime skill distribution beyond Claude Code's plugin system.

## References

- [anthropics/skills on GitHub](https://github.com/anthropics/skills/)
