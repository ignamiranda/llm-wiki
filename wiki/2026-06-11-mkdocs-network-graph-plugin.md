---
title: "MkDocs Network Graph Plugin"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [mkdocs, mkdocs-plugin, material-for-mkdocs, d3js, graph-visualization, documentation, knowledge-graph]
summary: "A plugin for Material for MkDocs that generates interactive D3.js network graph visualizations of documentation structure and page relationships."
source_url: "https://github.com/develmusa/mkdocs-network-graph-plugin"
source_hash: "9011413440502c097c1df89a3a12383e543c85145add23c65a81fda473bb2254"
---

# MkDocs Network Graph Plugin

## Summary / 摘要

The MkDocs Network Graph Plugin by [[develmusa]] adds an interactive network graph visualization to [[material-for-mkdocs]] documentation sites. It uses D3.js to render page relationships as an interactive force-directed graph, with dual view modes for full-site overview and local page connections.

## Content / 内容

### Features

- **Interactive Graph Visualization** — Force-directed network graph of documentation structure and page relationships
- **Dual View Modes** — Switch between a full-site overview and a localized view showing connections for the current page
- **Theme Integration** — Automatically adapts to Material for MkDocs theme colors
- **Performance Optimized** — Minimal impact on build times with responsive client-side rendering

### Installation

```bash
pip install mkdocs-network-graph-plugin
```

### Configuration

Enable in `mkdocs.yml`:

```yaml
plugins:
  - graph
```

The plugin requires `site_url` to be set in `mkdocs.yml` for proper URL generation.

#### Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `name` | string | `"title"` | Node naming strategy: `"title"` or `"file_name"` |
| `debug` | boolean | `false` | Enable debug logging |

### Customization

Appearance can be customized via CSS variables in `extra.css`:

```css
:root {
  --md-graph-node-color: #1976d2;
  --md-graph-node-color--hover: #1565c0;
  --md-graph-node-color--current: #ff5722;
  --md-graph-link-color: #757575;
  --md-graph-text-color: #212121;
}
```

### Dependencies

- Python 3.10+
- Material for MkDocs (v9.0.0+)
- D3.js (bundled client-side)

### Related Projects

The plugin was inspired by [[mkdocs-obsidian-interactive-graph-plugin|mkdocs-obsidian-interactive-graph-plugin]] and related knowledge graph visualization tools like Digital Garden and Foam.

## Key Takeaways / 关键收获

- Provides an interactive knowledge graph visualization layer for MkDocs documentation
- Requires no client-side configuration — D3.js graph is auto-generated from the site's page structure
- Fully theme-aware with CSS variable customization
- Dual-mode view distinguishes global structure from local page context

## Related / 关联

- [[mkdocs-network-graph-plugin]] — concept page for the tool
- [[material-for-mkdocs]] — required theme dependency
- [[develmusa]] — creator
- [[mkdocs-obsidian-interactive-graph-plugin]] — inspiration and related project
