# llm-wiki — AGENTS.md

LLM Wiki (Karpathy pattern) — persistent interlinked knowledge base on procedural generation, WFC, terrain, fonts, etc. **Not a software project.** No build, test, lint, typecheck, or CI.

## Layout

| Path | Purpose |
|------|---------|
| `wiki/` | All pages (flat, no subdirs) |
| `wiki/.llm-wiki/schema.md` | Canonical page types, frontmatter fields, and conventions |
| `wiki/.llm-wiki/index.md` | Auto-generated index (do not edit by hand) |
| `wiki/.llm-wiki/inbox/` | Source analysis files from ingestion |
| `wiki/.raw/` | Raw source material (txt files) |
| `wiki/.llm-wiki/graph.json` | Machine-readable link graph |
| `wiki/.llm-wiki/review.json` | Review queue (empty by default) |

## Page types

See `wiki/.llm-wiki/schema.md` for full spec. Four types:

- **concept** (`{slug}.md`) — term, idea, methodology
- **article** (`{YYYY-MM-DD}-{slug}.md`) — research notes, blog drafts, imported docs
- **person** (`{slug}.md`) — notable individual
- **synthesis** (`synth-{YYYY-MM-DD}-{slug}.md`) — saved query answer

## Key conventions

- **Wikilinks**: `[[slug]]` or `[[slug|display text]]` — slugs are filenames minus `.md`, no paths
- **Frontmatter**: Every page needs `title`, `type`, `language`, `created`, `modified`, `tags`, `summary`
- **Language detection**: CJK >70% → `zh`, Latin >70% → `en`, 30-70% mix → `bilingual`
- **Aliases**: Used for cross-language wikilink resolution; check frontmatter `aliases` when resolving `[[target]]`

## Commands

This repo is managed by the opencode `llm-wiki` skill (`~/.config/opencode/skills/llm-wiki/`). Load with `<skill name="wiki">` for:

- `/wiki-ingest` — ingest source URLs into wiki pages
- `/wiki-query` — answer a question from the wiki
- `/wiki-lint` — validate frontmatter, broken links, orphans, stale index
- `/wiki-save` — commit and push
- `/wiki-graph` — examine/visualize the link graph
- `/wiki-review` — manage review queue

## For agents answering questions

Always check `wiki/.llm-wiki/index.md` first before answering factual questions. Do not answer from training data without consulting the wiki.
