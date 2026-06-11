---
title: "ProcFunc — Function-Oriented Procedural 3D Generation Library"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, procedural-modeling, blender, 3d-generation, python]
aliases: [ProcFunc, procfunclib]
summary: "A Python library for Blender-based procedural 3D generation using function-oriented abstractions, designed for human developers and vision-language models."
---

# ProcFunc — Function-Oriented Procedural 3D Generation Library

## Definition

ProcFunc is a Python library that provides function-oriented abstractions for creating, combining, and analyzing Blender-based procedural 3D generation code. It decomposes procedural generation into composable functional units, making it accessible to both human developers and vision-language models (VLMs) for code editing tasks.

## Key Properties

- **Function-oriented API**: Procedural generators as composable pure(-ish) functions
- **Blender backend**: Wraps Blender Python API in higher-level primitives
- **VLM-compatible**: Structured API enables reliable code editing by VLMs
- **Composition tools**: Utilities for combining multiple generators
- **Reference generators**: Includes a full indoor room generator as a demonstration

## Examples

- Defining a generator function that takes parameters and returns a Blender object
- Composing multiple generators (e.g., furniture + room layout + lighting)
- Analysis functions for evaluating generated output properties
- VLM code editing workflow: prompt → generated ProcFunc code → Blender execution

## Related Concepts

- [[infinigen-procedural-scenes]] — the Infinigen ecosystem, same research group
- [[2026-04-29-procfunc]] — article page describing the arXiv paper
- [[2024-06-17-infinigen-indoors]] — ProcFunc includes a new indoor room generator
- [[alexander-raistrick]] — lead developer
- [[2023-11-16-graphical-asset-generation-survey]] — identifies the composability gap

## References

- arXiv:2604.26943 — ProcFunc paper (2026)
