# Ingest Analysis — Fast and Gorgeous Erosion Filter
**Source hash:** 98524c25a93c23bc1c62a8cfdadc4ab61059f0ccfde490c8ed8f2f292ab76e6d (blog) / 9b0d5a42065582a75f247a631b840b846aff989abb8e66d9c6d41b493177682d (video)
**Language detected:** en
**Analyzed:** 2026-06-11T13:30:00Z

## Source Summary
Rune Skovbo Johansen presents a non-simulated erosion filter technique (originally by Clay John, refined by Felix Westin/Fewes, then significantly evolved by Johansen) that produces branching gullies and ridges on terrain using a special kind of noise. Every point can be evaluated in isolation — fast, GPU-friendly, and trivial to generate in chunks. The blog post (2026-03-30) details implementation of the final iteration, while the companion YouTube video covers the process of discovery, refinement, and evolution.

## Concepts to Extract
| Concept | Action | Reason |
|---------|--------|--------|
| erosion-filter-technique | create | Core technique — non-simulated erosion via stripe-based directional noise |
| phacelle-noise | create | Directional noise function extracted by Johansen from the erosion filter |
| directional-noise | maybe-update | New information about directional noise (Phacelle Noise) |
| shadertoy | maybe-update | Shadertoy as platform for prototyping PCG techniques |

## Persons to Create/Update
| Person | Action | Details |
|--------|--------|---------|
| clay-john | create | Original creator of the eroded terrain noise Shadertoy (2018) |
| felix-westin | create | Refined the technique visually (2023), aka Fewes |
| rune-skovbo-johansen | update | New work: erosion filter technique, Phacelle Noise |

## Pages to Create
| Filename | Type | Title | Key Content |
|----------|------|-------|-------------|
| 2026-03-30-fast-and-gorgeous-erosion-filter | article | Fast and Gorgeous Erosion Filter — Rune Skovbo Johansen (2026) | Blog post summary: stripe-noise erosion filter, gradient-based gully generation, cell-based pivot points, frequency vs fade approach, stacked fading, normalized gullies, straight gullies, ridge maps |
| erosion-filter-technique | concept | Erosion Filter Technique | Non-simulated terrain erosion using gradient-aligned stripes as a filter applied to any height function |
| phacelle-noise | concept | Phacelle Noise | Directional noise function extracted from the erosion filter, with consistent magnitude via partial normalization |
| clay-john | person | Clay John | Original creator of the eroded terrain noise Shadertoy (2018) |
| felix-westin | person | Felix Westin (Fewes) | Refined the erosion noise Shadertoy visually (2023) |

## Existing Pages to Update
| Page | What to Add |
|------|-------------|
| [[rune-skovbo-johansen]] | New work: erosion filter technique (2025-2026), Phacelle Noise, companion video |
| [[ridged-noise]] | Possibly link to erosion filter technique as a related concept |

## Contradictions Detected
None — this is a novel technique not previously covered in the wiki.

## Proposed Cross-Links
- [[2026-03-30-fast-and-gorgeous-erosion-filter]] ↔ [[erosion-filter-technique]] — article describes the technique
- [[2026-03-30-fast-and-gorgeous-erosion-filter]] ↔ [[phacelle-noise]] — Phacelle Noise extracted from erosion filter
- [[2026-03-30-fast-and-gorgeous-erosion-filter]] ↔ [[clay-john]] — original creator
- [[2026-03-30-fast-and-gorgeous-erosion-filter]] ↔ [[felix-westin]] — visual refinement
- [[2026-03-30-fast-and-gorgeous-erosion-filter]] ↔ [[rune-skovbo-johansen]] — author
- [[erosion-filter-technique]] ↔ [[phacelle-noise]] — directional noise derived from technique
- [[erosion-filter-technique]] ↔ [[layerprocgen]] — both by Rune Skovbo Johansen
- [[phacelle-noise]] ↔ [[directional-noise]] — type of directional noise

## Items for User Review
- [ ] Proceed to Phase 2 generation? (config has no require_review setting)
