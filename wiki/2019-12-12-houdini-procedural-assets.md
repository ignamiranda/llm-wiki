---
title: "Creating Procedural Game Assets with Houdini — Part 1"
type: article
language: en
created: 2019-12-12
modified: 2026-06-11
tags: [procedural-generation, houdini, game-assets, tutorial]
source_url: "https://www.rendereverything.com/game_assets_with_houdini_1/"
summary: "Gatis Kurzemnieks introduces a 4-part series on building automated Houdini pipelines for procedural game asset generation, covering motivation, tool selection, and the Houdini PDG + Substance + RizomUV toolchain."
---

# Creating Procedural Game Assets with Houdini — Part 1

## Summary

Gatis Kurzemnieks presents the first installment of a 4-part tutorial series on using Houdini to create automated pipelines for procedural game assets. This part establishes the motivation (efficiency, consistency, iterability) and the toolchain: Houdini with PDG for orchestration, Substance Designer via Automation Toolkit for texturing, and RizomUV for UV unwrapping.

## Content

### Motivation

Natural formations (cliffs, stones, sand dunes) are tedious to create by hand. Manual workflows suffer from:

- **Inconsistency** across large asset counts
- **Costly rework** when art direction changes
- **Repetitive low-level work** that could be automated

Kurzemnieks argues that natural phenomena are ideal for procedural generation because they follow physical rules that can be approximated algorithmically, allowing infinite consistent variations.

### Toolchain

The pipeline uses:

- **[[houdini-procedural-asset-pipeline|Houdini]]** — primary DCC for procedural geometry generation, fully node-based with full low-level data access
- **PDG (Procedural Dependency Graph)** — introduced in Houdini 17, enables parallelized pipeline execution across multiple machines or threads
- **[[blender-geometry-nodes|Substance Designer]]** — industry-standard procedural texturing, integrated via Substance Automation Toolkit
- **RizomUV** — UV unwrapping integrated through PDG automation

COPs (Compositing Operators) in Houdini were initially explored for texturing but found too slow; they are retained only for baking texture maps for Substance input.

## Key Takeaways

- PDG enables orchestrating geometry generation, texturing (via Substance Automation Toolkit), and UV unwrapping (RizomUV) in a single automated graph
- The subscription model (Houdini Indie ~269$/year, Substance Toolkit ~220$/year, RizomUV ~150$ one-time) makes the toolchain accessible to individuals and small studios
- A well-built procedural pipeline shifts creative effort: invest upfront in the pipeline, then iterate freely throughout development

## Related

- [[gatis-kurzemnieks]] — Author of the series
- [[houdini-procedural-asset-pipeline]] — The PDG-based pipeline concept
- [[unity-procedural-mesh-resources]] — Unity-focused procedural mesh resources (complementary ecosystem)
