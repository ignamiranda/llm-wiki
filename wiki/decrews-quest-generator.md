---
title: "Decrews Procedural Quest Generator"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, csharp, unity, structural-analysis, scriptable-objects]
aliases: [decrews-quest-generator, decrews-pqg]
summary: "A C#/Unity implementation of Doran & Parberry's quest generation algorithm using Scriptable Objects for NPCs, locations, enemies, and items."
---

# Decrews Procedural Quest Generator

## Definition / 定义

A C# implementation of Doran & Parberry's procedural quest generation algorithm for the **Unity** game engine, by decrews. It creates **quest action trees** using Unity's **ScriptableObject** system to define NPCs, locations, enemies, and items as data assets, separating quest logic from game content.

## Key Properties / 关键特性

- **Engine**: Unity (C#)
- **Approach**: Doran & Parberry's quest structural analysis
- **Data Architecture**: ScriptableObjects for all game entities (NPCs, locations, enemies, items)
- **Output**: Quest action trees
- **Repository**: 11 stars
- **Design**: Clean separation between generation logic and game content via Unity's asset pipeline

## Related Concepts / 相关概念

- [[quest-structural-analysis]] — the underlying methodology
- [[npc-motivations]] — root taxonomy used for generation
- [[procedural-quest-generation]] — the broader field
- [[quest-generator-prolog]] — the original Prolog implementation
- [[questify-js]] — JavaScript implementation of the same algorithm
- [[ian-parberry]] — co-author
- [[jonathan-doran]] — co-author

## References / 参考资料

- Repository: https://github.com/decrews/Procedural-Quest-Generator
- Doran, J. & Parberry, I. (2011). A Prototype Quest Generator Based on a Structural Analysis of Quests from Four MMORPGs.
