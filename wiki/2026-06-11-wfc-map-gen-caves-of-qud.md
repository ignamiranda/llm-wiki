---
title: "Tile-Based Map Generation using Wave Function Collapse in Caves of Qud"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, wave-function-collapse, caves-of-qud, map-generation, gdc, brian-butler, texture-synthesis]
summary: "Brian Butler's GDC talk on how Caves of Qud uses Wave Function Collapse in texture mode for tile-based map generation, starting from hand-authored samples."
source_url: "https://www.youtube.com/watch?v=AdCgi9E90jw"
source_hash: "96EAA8470F9F0329347F571DB8959FEE95D515B75B5EB3AAAF2393CAC100949F"
---

# Tile-Based Map Generation using Wave Function Collapse in Caves of Qud

## Summary

[[brian-butler]] presents how Caves of Qud uses Wave Function Collapse (WFC) for tile-based map generation. Unlike the common tile-mode approach that uses edge-colored adjacency constraints, Caves of Qud uses WFC's *texture mode* — providing hand-authored map samples as input and generating new maps that preserve the sample's character.

## Content

The talk demonstrates the power and flexibility of WFC texture mode for game maps:

- **Texture vs tile mode**: Tile mode uses explicit edge-colored adjacency rules; texture mode infers adjacency from example maps, producing more organic results
- **Sample-based generation**: Hand-author small map samples (palaces, caves, towers, villages) and let WFC generate variations that preserve their visual character
- **Results shown**: Rectilinear palaces, narrow underground corridors with flooded rooms, circular towers embedded in rock salt, dispersed village layouts — all from the same algorithm with different samples
- **Supplementing WFC's weaknesses**: WFC alone produces maps that may lack global structure; Caves of Qud combines WFC with other techniques (room placement, corridor carving, post-processing) to compensate

Caves of Qud was the first commercial game to use WFC, and the talk provides practical lessons for integrating WFC into a production game pipeline.

## Key Takeaways

- WFC texture mode is more flexible than tile mode for game maps — samples naturally encode desired aesthetics
- Different map styles require different samples, not different algorithms
- WFC works best when combined with other techniques that provide global structure
- Hand-authoring samples gives designers direct creative control over generated output

## Related

- [[wave-function-collapse]] — the algorithm discussed
- [[brian-butler]] — presenter
- [[caves-of-qud]] — game discussed
- [[2026-06-11-end-to-end-procgen-caves-of-qud]] — related talk on broader procgen architecture
- [[procedural-generation]] — broader topic
