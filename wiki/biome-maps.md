---
title: "Biome Maps"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, noise, biomes, terrain]
aliases: [elevation-moisture-biomes, biome-lookup]
summary: "A technique for assigning biomes using two independent noise maps — one for elevation and one for moisture — combined through a 2D lookup table."
---

# Biome Maps

## Definition

A biome assignment technique where two independent noise maps (elevation and moisture) are combined through a 2D lookup table to determine the biome at each map position. Low elevations become water and beaches, high elevations become rocky or snowy, and the combination of elevation and moisture produces diverse intermediate biomes like grassland, forest, desert, and tundra.

## Key Properties

- **Two-dimension lookup**: Biome is a function of both elevation (y-axis) and moisture (x-axis), avoiding banded terrain
- **Threshold-based**: Biome boundaries are defined by threshold values on elevation and moisture — these must be tuned per generator and per noise library
- **Threshold tuning**: Each game world needs different thresholds (Dagobah = more swamp, Hoth = more tundra, Tatooine = more desert)
- **Seeds must differ**: The two noise maps must use different seeds or offsets, otherwise they produce identical values and the map shows no variation
- **Alternative to discrete biomes**: Smooth gradient color ramps (per Tom Patterson's hypsometric tints) can replace discrete biome categories

## Examples

- Ocean → Beach → Grassland → Forest → Savanna → Desert → Snow (elevation-based only)
- Ocean → Beach → Scorched → Bare → Tundra → Snow | Temperate Desert → Shrubland → Taiga | Grassland → Seasonal Forest → Rain Forest (elevation × moisture)

## Related Concepts

- [[noise-based-terrain-generation]] — biome mapping is the final output stage
- [[fractional-brownian-motion]] — generates both elevation and moisture noise
- [[elevation-redistribution]] — redistributes elevation before biome lookup
- [[ridged-noise]] — can be used for mountainous biomes

## References

- Patel, Amit J., "Making maps with noise functions", Red Blob Games, 2015, https://www.redblobgames.com/maps/terrain-from-noise/
- Whittaker, Robert H., "Communities and Ecosystems", Macmillan, 1975
