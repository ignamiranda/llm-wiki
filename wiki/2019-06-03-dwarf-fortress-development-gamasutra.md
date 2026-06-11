---
title: Q&A: Dissecting the Development of Dwarf Fortress with Creator Tarn Adams
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [dwarf-fortress, game-development, procedural-generation, world-generation, game-loop, simulation]
source_url: https://www.gamedeveloper.com/design/q-a-dissecting-the-development-of-i-dwarf-fortress-i-with-creator-tarn-adams
source_hash: 031F8FF649E333F4B1DF4DED59F517CCB814D4746EDA19EB5DF5464FC597F0B6
summary: "In-depth 2019 interview with Tarn Adams covering Dwarf Fortress world generation, the staggered tick-based game loop, the body-part damage model (no hit points), tile rendering, and planned features including Steam release, magic systems, and economy."
---

# Q&A: Dissecting the Development of Dwarf Fortress

## Summary

John Harris interviews Tarn Adams about the development of Dwarf Fortress. Topics include the world generation process (fractal seeding of elevation, rainfall, temperature, drainage, volcanism, wildness), the staggered tick-based game loop, the complex body-part damage model that replaces hit points, planned features (villains, Steam release with pixel graphics, the "Big Wait" magic/myth system, economy, boats), and the division between player control and dwarf autonomy.

## Content

### World Generation

The world is built in stages: memory allocation, choosing pole type, fractal seeding of map fields (elevation, rainfall, temperature, drainage, volcanism, wildness), setting vegetation based on combined fields, smoothing mid-level elevations, placing volcanoes, then the erosion and river stage where simulated rivers carve channels. Lakes grow along rivers. Rain shadows and orographic precipitation adjust rainfall. Geological layers, biomes, and underground layers are assigned. Finally, wildlife and weather variables are set, and a zero-player strategy game generates history by recording the simulation log of thousands of agents.

### Game Loop

The main loop uses staggered tick intervals:
- **Every tick**: fluids, map tile updates, vermin, fires, projectiles, creature movement, temperature, camera
- **Every 10 ticks**: seasons advance (weather, map changes), plot element checks (diplomats, sieges)
- **Every 50 ticks**: taverns/temples/libraries, stockpiles, storage, building updates
- **Every 100 ticks**: job assignments, strange moods, world map army movement, job auction, item rotting
- **Every 1000 ticks**: garbage collection (delete marked objects)

### Body Part Damage Model

DF has no explicit hit point system. Damage is resolved through a complex body part hierarchy — creatures have detailed anatomical structures with individual body parts, each with material properties. This provides more specific, relatable story moments and lasting consequences. Adams describes being "as anti-numeric as possible" since "numbers usually make for poor stories."

### Tile Rendering

Each tile is a character byte plus color bytes. Rendering goes bottom-to-top (ground → items → creatures), overwriting previous decisions. A small array allows flipping animations so all units in a tile are visible over time when paused.

### Planned Features

At the time (2019, version 0.44), DF was ~44% to 1.0. Planned releases: villains release, Steam/itch version with graphics and QoL improvements, siege improvements, then "the Big Wait" — the largest restructuring ever — enabling creation myths, procedural magic systems, and multiple view windows. After that: property/law/customs, economy, boats, and other major missing components.

### Micro vs. Macro Control

The player is the "official will of the fortress" while dwarves exercise autonomy outside their official duties. The quartermaster system was removed for being too slow and confusing. Emergency levers use job priority to override autonomy.

## Key Takeaways

- World generation is a multi-stage fractal pipeline producing elevation, rainfall, temperature, drainage, volcanism, and wildness maps before civilization history is simulated
- Game loop uses staggered tick intervals (1, 10, 50, 100, 1000 ticks) for different subsystems
- Body part damage model replaces HP — anti-numeric design philosophy for better emergent stories
- Version 0.44 indicated ~44% completion; major features remaining include magic systems, economy, and boats
- Player is the "official will" — dwarves have autonomous lives but can be overridden via job priority

## Related

- [[tarn-adams]] — interview subject
- [[zach-adams]] — brother and co-designer (the "Threetoe" stories that inspire mechanics)
- [[2021-12-31-dwarf-fortress-development]] — later companion interview on engineering
- [[body-part-damage-model]] — DF's damage system detailed here
- [[connected-component-pathfinding]] — DF's pathfinding (covered more in 2021 interview)
