---
title: "SKILL.md File Format"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [agent-skills, skill-development, file-format, yaml, markdown]
aliases: [skill-format, skillyml, skill-frontmatter]
source_url: "https://github.com/anthropics/skills/"
source_hash: "299371c3dd28ad6d7066e8b9cf1bb799b408636eae8b710a30935b87b5f130c2"
summary: "The SKILL.md file format defines agent skills using YAML frontmatter (name, description) followed by markdown instructions, examples, and guidelines."
---

# SKILL.md File Format

## Definition

The SKILL.md file format is the standard format for defining Agent Skills. Each skill lives in its own folder with a `SKILL.md` file containing YAML frontmatter for metadata and markdown content for instructions. The format is designed to be minimal — only `name` and `description` fields are required — while allowing rich, structured instructions in the body.

## Key Properties

- **Frontmatter**: YAML between `---` delimiters, requiring only `name` (unique kebab-case identifier) and `description` (what the skill does and when to use it)
- **Body**: Freeform markdown following the frontmatter, containing instructions, examples, and guidelines that the agent follows when the skill is active
- **Self-contained**: All resources (scripts, templates, assets) live in the same folder as `SKILL.md`
- **Single-file entry point**: The agent reads only `SKILL.md`; supporting files are referenced from within

## Examples

```markdown
---
name: my-skill-name
description: A clear description of what this skill does and when to use it
---

# My Skill Name

[Instructions that the agent follows when this skill is active]

## Examples
- Example usage 1
- Example usage 2

## Guidelines
- Guideline 1
- Guideline 2
```

## Related Concepts

- [[agent-skills]] — The Agent Skills framework that uses this format
- [[claude-skills-plugin]] — Plugin marketplace registration for distributing skills
- [[2026-06-11-anthropic-skills-repo]] — Reference repository with example skills using this format

## References

- [How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [anthropics/skills template](https://github.com/anthropics/skills/tree/main/template)
