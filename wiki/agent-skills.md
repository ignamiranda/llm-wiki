---
title: "Agent Skills"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [agent-skills, ai-agents, claude, anthropic, skill-development]
aliases: [skills, agent-skills-standard, claude-skills]
source_url: "https://github.com/anthropics/skills/"
source_hash: "299371c3dd28ad6d7066e8b9cf1bb799b408636eae8b710a30935b87b5f130c2"
summary: "A framework for equipping AI agents with reusable, specialized capabilities defined in structured SKILL.md files that agents load dynamically to improve performance on specific tasks."
---

# Agent Skills

## Definition

Agent Skills are folders of instructions, scripts, and resources that an AI agent (such as Claude) loads dynamically to improve performance on specialized tasks. They provide a repeatable way to teach agents how to complete specific tasks — whether creating documents with brand guidelines, analyzing data with organization-specific workflows, or automating personal tasks. The Agent Skills standard is maintained by Anthropic.

## Key Properties

- Self-contained: each skill is a folder with a `SKILL.md` file and supporting resources
- Dynamic loading: agents load skills on demand when a task matches the skill's description
- Minimal format: requires only `name` and `description` fields in YAML frontmatter
- Cross-platform: works with Claude Code, Claude.ai, and the Claude API
- Composable: multiple skills can be active simultaneously
- Reusable: skills can be shared, registered as plugins, and installed from marketplaces

## Examples

- A document-processing skill that teaches an agent how to create, edit, and format PDF files
- A brand-guidelines skill that enforces company visual identity across generated content
- A webapp-testing skill that runs browser-based tests and reports results
- An MCP-builder skill that creates MCP server configurations

## Related Concepts

- [[skill-file-format]] — The SKILL.md file format used to define skills
- [[claude-skills-plugin]] — Plugin marketplace registration for distributing skills
- [[2026-06-11-anthropic-skills-repo]] — Anthropic's reference repository of example skills
- [[2026-06-11-mattpocock-skills]] — Matt Pocock's skills repository (engineering-focused, composable skills)
- [[matt-pocock]] — Creator of the influential skills repository for AI coding agents
- [[shokunin]] — A large-scale skill ecosystem with 62 CI-validated engineering skills and persistent memory
- [[2026-06-11-shokunin]] — Article describing the Shokunin ecosystem as a concrete example

> 📝 **Updated from [[2026-06-11-shokunin]]**: Added Shokunin as a concrete example of a large-scale skill ecosystem with CI validation and multi-runtime support.

## References

- [anthropics/skills on GitHub](https://github.com/anthropics/skills/)
- [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Equipping agents for the real world with Agent Skills](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
