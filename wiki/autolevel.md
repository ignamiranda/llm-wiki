---
title: "AutoLevel"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [wfc, wave-function-collapse, unity, procedural-generation, level-design, unity-editor]
aliases: []
summary: "A free Unity editor-integrated WFC-based procedural level generator with weight, volume, and boundary constraints."
source_url: "https://github.com/Al-Asl/AutoLevel"
source_hash: "103AE5ED509E03036F6DA2D52FDAE501153EE55716633D3AC49D1A12E722182F"
---

# AutoLevel

## Definition / 定义

AutoLevel is a Unity-based procedural level generator using the Wave Function Collapse algorithm, created by Al-Asl. It provides editor tools for configuring art constraints, weight/volume/boundary conditions, and supports big blocks, layers, FBX export, and multithreaded solving.

## Key Properties / 关键特性

- Weight, volume, and boundary constraints
- Unity editor tools (Level Builder, Block Repo, Block Asset)
- Big Block system for composite blocks
- FBX export
- Multi-threaded solver (constraint-based)
- Layer support for multi-level generation
- Selection rebuild (partial regeneration)
- Complete C# source provided
- MIT licensed, 148 GitHub stars

## Examples / 示例

Room-and-corridor dungeon generation, multi-layered level design with empty/solid group definitions. Includes a runtime API for building levels procedurally during gameplay.

## Related Concepts / 相关概念

- [[debroglie]] — another C# WFC implementation
- [[2026-06-11-wfc-implementations-survey]] — surveyed in the WFC survey article
- [[noise-based-terrain-generation]] — alternative terrain generation approach

## References / 参考资料

- https://github.com/Al-Asl/AutoLevel