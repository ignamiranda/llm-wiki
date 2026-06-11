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
| `wiki/` | All pages (flat, 191 pages, ~199 files incl. graph.html) |
| `wiki/index.md` | Main landing page (hand-written) |
| `wiki/graph.html` | Interactive D3 knowledge graph (embedded data) |
| `wiki/.llm-wiki/schema.md` | Page types, frontmatter fields, conventions |
| `wiki/.llm-wiki/index.md` | Auto-generated index (**do not edit by hand**) |
| `wiki/.llm-wiki/config.md` | Wiki config (language: en) |
| `wiki/.llm-wiki/graph.json` | Machine-readable link graph |
| `wiki/.llm-wiki/review.json` | Review queue (contradictions, quality issues, gaps; has pending items) |
| `wiki/.llm-wiki/source-manifest.json` | Tracks ingested URLs → pages created/updated |
| `wiki/.llm-wiki/inbox/` | Source analysis files from `/wiki-ingest` |
| `wiki/.llm-wiki/cache/` | Cached analysis data |
| `wiki/.raw/` | Raw source material (txt files) |
| `hooks/wikilinks.py` | MkDocs plugin: converts `[[slug]]` → relative links at build time |
| `mkdocs.yml` | MkDocs config (Material theme, wikilinks hook) |
| `requirements.txt` | `mkdocs~=1.6`, `mkdocs-material~=9.5`, `pyyaml~=6.0` |

## Page types

See `wiki/.llm-wiki/schema.md` for full spec.

| Type | File pattern | Extra required frontmatter |
|------|-------------|---------------------------|
| concept | `{slug}.md` | — |
| article | `{YYYY-MM-DD}-{slug}.md` | — |
| person | `{slug}.md` | `aliases` |
| synthesis | `synth-{YYYY-MM-DD}-{slug}.md` | `query`, `based_on`, `confidence` |

## Key conventions

- **Wikilinks**: `[[slug]]` or `[[slug|display text]]` — resolved to `{slug}/` at build time by `hooks/wikilinks.py`. Slugs are filenames minus `.md`, no paths.
- **Frontmatter**: Every page needs `title`, `type`, `language`, `created`, `modified`, `tags`, `summary`. Person pages also need `aliases`.
- **Aliases**: Used for wikilink resolution in frontmatter

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
