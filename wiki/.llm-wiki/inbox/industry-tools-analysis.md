# Industry Tools Analysis — Procedural Geometry & Asset Tools

**Date:** 2026-06-11
**Purpose:** Analysis of 3 industry tool/resource sources for procedural geometry, game asset pipelines, and mesh/texture generation.

## Source Summary

| # | Source | Type | Focus | Key Topics |
|---|--------|------|-------|------------|
| 1 | Blender Geometry Nodes Manual | Official documentation | Node-based procedural modeling | Fields, attributes, instances, baking, node tools |
| 2 | "Creating procedural game assets with Houdini" Part 1 (Gatis Kurzemnieks) | Tutorial series | Houdini procedural asset pipeline | PDG, Substance Automation Toolkit, RizomUV, rock generation |
| 3 | Resources-for-Procedural-Mesh-and-Texture-Generation (VoxelBoy) | Curated list (GitHub, 3★) | Unity procedural mesh/texture | Catlike Coding, Jayelinda, ScrawkBlog, ProceduralToolkit, LibNoise |

## Key Observations

1. **Two major node-based paradigms** — Blender Geometry Nodes (free, integrated in Blender 3.0+) and Houdini (industry-standard, node-based DCC with PDG for pipeline automation). Both use visual node graphs but target different workflows and price points.

2. **Houdini PDG bridges DCC and automation** — Kurzemnieks' pipeline demonstrates PDG orchestrating Houdini generation → Substance Designer texturing (via Automation Toolkit) → RizomUV unwrapping, all in one automated graph. This represents a mature industry pipeline pattern.

3. **Unity ecosystem has strong community resources** — The VoxelBoy list curates tutorials (Catlike Coding, Jayelinda, ScrawkBlog) and libraries (ProceduralToolkit, LibNoise) that lower the barrier for procedural mesh/texture work in Unity, though none are as comprehensive as Houdini or Geometry Nodes.

4. **Substance Designer is the industry standard for procedural texturing** — Both Kurzemnieks' Houdini pipeline and general game art practices point to Substance as the texturing component. Its Automation Toolkit enables headless/scripted texture generation.

5. **All three sources address the same gap** — procedural generation of 3D game assets, but at different levels: Blender's Geometry Nodes (node-based modeling inside a free DCC), Houdini PDG (full pipeline automation in a high-end DCC), and Unity resources (code-driven generation within a game engine).

## Pages Created

- [[2019-12-12-houdini-procedural-assets]] — Article on Houdini tutorial series part 1
- [[blender-geometry-nodes]] — Concept page for Blender Geometry Nodes
- [[houdini-procedural-asset-pipeline]] — Concept page for Houdini PDG pipeline
- [[unity-procedural-mesh-resources]] — Concept page for VoxelBoy resource list
- [[gatis-kurzemnieks]] — Person page for the tutorial author

## Cross-References

- [[wave-function-collapse]] — related procedural technique used in game asset generation
- [[boris-the-brave]] — creator of DeBroglie (Unity WFC), relevant to Unity procgen ecosystem
- [[autolevel]] — Unity WFC tool, part of the Unity procedural generation ecosystem
- [[layerprocgen]] — Unity C# framework for procedural generation
- [[oskar-stalberg]] — known for procedural generation in games (Townscaper)
