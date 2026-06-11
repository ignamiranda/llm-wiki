# llm-wiki — AGENTS.md

LLM Wiki (Karpathy pattern) — persistent interlinked knowledge base on procedural generation, WFC, terrain, fonts, etc. **Not a software project.** No tests, lint, or typecheck for wiki content.

## Quick start

```bash
pip install -r requirements.txt   # mkdocs, mkdocs-material, pyyaml
mkdocs serve                       # local preview at http://127.0.0.1:8000
mkdocs build --strict              # production build to site/ (also runs in CI)
```

## CI

Push to `master` → GitHub Actions (`deploy.yml`) runs `mkdocs build --strict` + deploys to GitHub Pages. `site/` is in `.gitignore`.

## Structure

| Path | Purpose |
|------|---------|
| `wiki/` | All pages (flat, no subdirs, 191+ files) |
| `wiki/.llm-wiki/schema.md` | Page types, frontmatter fields, conventions |
| `wiki/.llm-wiki/index.md` | Auto-generated index (do not edit by hand) |
| `wiki/.llm-wiki/inbox/` | Source analysis files from `/wiki-ingest` |
| `wiki/.raw/` | Raw source material (txt files) |
| `wiki/.llm-wiki/graph.json` | Machine-readable link graph |
| `wiki/.llm-wiki/review.json` | Review queue (contradictions, quality issues, gaps) |
| `wiki/.llm-wiki/source-manifest.json` | Tracks ingested URLs → pages created/updated |
| `hooks/wikilinks.py` | MkDocs plugin: converts `[[slug]]` to relative links at build time |
| `mkdocs.yml` | MkDocs config (Material theme, wikilinks hook, dark/light mode) |
| `requirements.txt` | `mkdocs~=1.6`, `mkdocs-material~=9.5`, `pyyaml~=6.0` |

## Page types

See `wiki/.llm-wiki/schema.md` for full spec.

- **concept** (`{slug}.md`) — term, idea, methodology
- **article** (`{YYYY-MM-DD}-{slug}.md`) — research notes, blog imports
- **person** (`{slug}.md`) — researcher, notable individual
- **synthesis** (`synth-{YYYY-MM-DD}-{slug}.md`) — saved query answer

## Key conventions

- **Wikilinks**: `[[slug]]` or `[[slug|display text]]` — resolved to `{slug}/` at build time by `hooks/wikilinks.py`. Slugs are filenames minus `.md`, no paths.
- **Frontmatter**: Every page needs `title`, `type`, `language`, `created`, `modified`, `tags`, `summary`. Person pages also need `aliases`.
- **Language detection**: CJK >70% → `zh`, Latin >70% → `en`, 30-70% → `bilingual`
- **Aliases**: Used for cross-language wikilink resolution in frontmatter

## Wiki management commands

This repo is managed by the opencode `llm-wiki` skill (`~/.config/opencode/skills/llm-wiki/`). Load with `<skill name="wiki">`:

- `/wiki-ingest` — ingest source URLs into wiki pages
- `/wiki-query` — answer a question from the wiki
- `/wiki-lint` — validate frontmatter, broken links, orphans, stale index
- `/wiki-save` — commit and push
- `/wiki-graph` — examine/visualize the link graph
- `/wiki-review` — manage review queue

## For agents answering questions

Always check `wiki/.llm-wiki/index.md` first. Do not answer from training data without consulting the wiki.
