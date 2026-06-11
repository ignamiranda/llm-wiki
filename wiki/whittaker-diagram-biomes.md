---
title: "Whittaker Diagram Biomes"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, biomes, geography, climate]
aliases: [whittaker-biomes]
summary: "A biome classification system that assigns biome types based on two axes: elevation (as a proxy for temperature) and moisture level, adapted for procedural map generation."
source_url: "http://www-cs-students.stanford.edu/~amitp/game-programming/polygon-map-generation/"
source_hash: "B996558CD403FDD124ABCC155317B8BBDAF943366AEE3AF70521E0D7970D35D9"
---

# Whittaker Diagram Biomes

## Definition

A biome classification scheme adapted from the Whittaker diagram for use in procedural map generation. Biome types are assigned to land polygons based on two parameters: elevation (serving as a proxy for temperature, with higher elevations being colder) and moisture level. The classification produces a grid of biome types ranging from snow at high elevations to tropical rain forest at low, wet areas.

## Key Properties

- **Water bodies:** OCEAN (connected to border), LAKE (not connected), ICE (high elevation lake), MARSH (low elevation lake)
- **Coast:** BEACH — land polygons adjacent to ocean
- **High elevation (4):** SNOW, TUNDRA, BARE, SCORCHED (from wet to dry)
- **Medium-high (3):** TAIGA, SHRUBLAND, TEMPERATE DESERT
- **Medium-low (2):** TEMPERATE RAIN FOREST, TEMPERATE DECIDUOUS FOREST, GRASSLAND, TEMPERATE DESERT *(note: TEMPERATE DESERT spans both tiers — dry conditions can occur at medium-high and medium-low elevations)*
- **Low elevation (1):** TROPICAL RAIN FOREST, TROPICAL SEASONAL FOREST, GRASSLAND, SUBTROPICAL DESERT
- Can be extended with latitude-based temperature (north/south colder than equator)
- Alternative approaches exist: noise-based moisture, wind/evaporation/rain shadows, groundwater models

## Examples

- In the mapgen2 demo, each polygon is colored by its Whittaker biome, producing visually distinct climate zones from snowy peaks to tropical coasts
- Realm of the Mad God used a custom biome formula derived from this Whittaker-based system
- The biome per-pixel approach interpolates elevation and moisture at each pixel for smoother transitions

## Related Concepts

- [[elevation-from-coast-distance]] — provides the elevation axis
- [[voronoi-diagram-mapgen]] — the polygons being classified
- [[2010-09-01-polygonal-map-generation]] — the article that adapted this for game maps

## References

- Amit Patel, "Polygonal Map Generation for Games", Red Blob Games, 2010
- Whittaker diagram (pcg.wikidot.com)
- Wikipedia: Biome
