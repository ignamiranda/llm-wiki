---
title: "Anthropic Skills Repository"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [agent-skills, claude, anthropic, ai-agents, skill-development, plugin-marketplace]
source_url: "https://github.com/anthropics/skills/"
source_hash: "299371c3dd28ad6d7066e8b9cf1bb799b408636eae8b710a30935b87b5f130c2"
summary: "Anthropic's public repository of Agent Skills — self-contained skill folders with SKILL.md files demonstrating how to equip Claude with reusable capabilities for specialized tasks."
---

# Anthropic Skills Repository

## Summary

The [anthropics/skills](https://github.com/anthropics/skills) repository is Anthropic's public collection of Agent Skills — folders containing instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. It includes ~17 example skills spanning creative, technical, enterprise, and document-processing domains, the Agent Skills specification, and a skill template.

## Content

### Repository Structure

The repo has three main areas:

- **`./skills/`** — Skill examples organized by category: Creative & Design, Development & Technical, Enterprise & Communication, and Document Skills
- **`./spec/`** — The Agent Skills specification
- **`./template/`** — A skill template for creating new skills

### Skills Included

| Skill | Description |
|-------|-------------|
| algorithmic-art | Creative coding / generative art |
| brand-guidelines | Enforce brand consistency |
| canvas-design | Canvas-based design workflows |
| claude-api | Claude API integration patterns |
| doc-coauthoring | Collaborative document editing |
| docx | Document creation & editing (source-available) |
| frontend-design | UI/frontend design assistance |
| internal-comms | Internal communication templates |
| mcp-builder | MCP server generation |
| pdf | PDF creation & editing (source-available) |
| pptx | Presentation creation & editing (source-available) |
| skill-creator | Skill development assistance |
| slack-gif-creator | Slack GIF creation |
| theme-factory | Theme/vibe generation |
| web-artifacts-builder | Web artifact building |
| webapp-testing | Web application testing |
| xlsx | Spreadsheet creation & editing (source-available) |

The document skills (docx, pdf, pptx, xlsx) are source-available (not open source) and power Claude's built-in document capabilities.

### Skill File Format

Each skill is defined by a `SKILL.md` file with YAML frontmatter and markdown body:

```yaml
---
name: my-skill-name
description: A clear description of what this skill does and when to use it
---
```

### Usage

Skills can be used in three environments:

1. **Claude Code** — Register via `/plugin marketplace add anthropics/skills`, then install `document-skills` or `example-skills` plugins
2. **Claude.ai** — All example skills are available to paid plans
3. **Claude API** — Upload custom skills via the Skills API

## Key Takeaways

- Skills are a repeatable way to teach Claude specialized tasks using structured instructions
- The format is minimal: name + description frontmatter + freeform markdown
- The repository serves as both a reference implementation and a marketplace of skill examples
- Document skills (docx, pdf, pptx, xlsx) are production-quality, source-available components

## Related

- [[agent-skills]] — The Agent Skills concept and standard
- [[skill-file-format]] — The SKILL.md format specification
- [[claude-skills-plugin]] — Plugin marketplace registration for skills
- [[2026-06-11-mattpocock-skills]] — Matt Pocock's skills repository (comparable engineering-focused skills collection)
- [[matt-pocock]] — Creator of the influential skills repository for AI coding agents
