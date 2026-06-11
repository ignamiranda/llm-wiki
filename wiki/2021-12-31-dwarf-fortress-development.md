---
title: How Dwarf Fortress Is Built — 700,000 Lines of Code, 20 Years, and One Developer
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [dwarf-fortress, game-development, procedural-generation, solo-developer, pathfinding, c++, codebase-management]
source_url: https://stackoverflow.blog/2021/12/31/700000-lines-of-code-20-years-and-one-developer-how-dwarf-fortress-is-built/
source_hash: 1B28079B14D1D9F3DDB48962B432F8EC1C197987C0477DD310EB902859B08D7B
summary: "Interview with Tarn Adams covering Dwarf Fortress's ~711K-line C/C++ codebase, tech stack (MSVC, OpenGL, SDL, FMOD), pathfinding via A* with connected components, and the infamous drunken cat bug."
---

# How Dwarf Fortress Is Built

## Summary

Ryan Donovan interviews Tarn Adams about the engineering behind Dwarf Fortress's massive solo-developed codebase. Topics include the evolution of the C/C++ codebase (now ~711,000 lines), the tech stack (MSVC, OpenGL, SDL, FMOD), the biggest refactors (adding Z-axis, the mistaken polymorphic item system), A* pathfinding optimized via connected component indices, the seamless 32-to-64-bit transition, the drunken cat bug, and 90 side projects in various genres.

## Content

Dwarf Fortress is built on a custom engine using C/C++ that has accreted over 20 years. Adams uses Microsoft Visual Studio Community (since MSVC 6), OpenGL and SDL for graphics, and FMOD for sound. The codebase is a "mess that's accreted over time" — searching for semicolons as a proxy gives ~711,000 lines. Adams says he can no longer keep it all in his head, relying on consistent naming, generous comments, and heavy use of "Find In Files."

The biggest refactor was adding the Z coordinate to make the game mechanically 3D — weeks of adding Z parameters to every X/Y function call. Making the item system polymorphic was described as "ultimately a mistake," leading Adams toward an entity-component-style approach where items like stepladders, beehives, and mortars all share a flexible "tool" hierarchy instead of rigid class inheritance.

For pathfinding, DF uses A* with a connected component system. Walkable regions are tracked via flood-fill indices — if water cuts the fortress in half, one side gets re-indexed with a flood fill. Agents check component numbers first; if they match, A* will succeed, eliminating almost all failed pathfinding calls. The downside is that flying creatures lack specialized global pathfinding.

DF is single-threaded aside from the graphical display. The 32-to-64-bit transition was seamless because byte sizes were already controlled for save compatibility across OSes and endianness.

The drunken cat bug involved cats dying from alcohol poisoning — a single incorrect number in the ingest-while-cleaning code caused cats cleaning alcohol off their paws to experience full alcohol poisoning symptoms.

Adams has ~90 side projects accumulated over a decade, mostly games in other genres. He has not explored other programming languages, preferring to use side-project time for design relaxation rather than tech learning.

## Key Takeaways

- Dwarf Fortress is ~711K lines of C/C++ built entirely by one developer (Tarn Adams) over 20 years
- Pathfinding optimization: A* + connected component indices for walkable regions, cutting failed pathfinding calls
- Polymorphic class hierarchies for items was a mistake — ECS-like flexible composition preferred
- No multithreading in the game logic; 32-to-64-bit transition was accidentally seamless
- 90 side projects, all in C/C++ — Adams hasn't learned other languages

## Related

- [[tarn-adams]] — interview subject
- [[zach-adams]] — brother and co-designer
- [[connected-component-pathfinding]] — DF's pathfinding technique
- [[body-part-damage-model]] — DF's related damage system
- [[2019-06-03-dwarf-fortress-development-gamasutra]] — earlier companion interview
