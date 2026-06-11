# Sword Generation — Source Analysis

## Overview

Analysis of four distinct procedural sword generation projects spanning Unity (C#), Godot (GLSL/GDScript), Blender (Python addon), and OpenSCAD. Together they cover 3D mesh generation, pixel art rendering, parametric CAD modelling, and physics-based damage calculation.

## Sources Analysed

| # | Project | Author | Platform | Approach | Stars |
|---|---------|--------|----------|----------|-------|
| 1 | PCG Swords (Honours Project) | Caius Walker | Unity/C# | CSV part data → vertex mesh generation + physics damage | — |
| 2 | Sword-Maker | BumbertFiddlesticks | Godot/GLSL+GDScript | Pixel art via shaders | 34★ |
| 3 | Procedural Sword Generator for Blender | Pamir Bal | Blender/Python | Geometry nodes addon (commercial) | — |
| 4 | Hello-Sword | mugenZebra | OpenSCAD | Parametric CAD blade modelling | 0★ |

## Key Dimensions

### Approach to Generation
- **Part-based assembly** (Caius Walker): Random selection from CSV part database, mesh generation per-part via vertex calculation
- **Shader-driven pixel art** (Sword-Maker): GLSL fragment shaders render 2D pixel art sword sprites in real-time
- **Geometry node parameters** (Pamir Bal): Blender addon exposing parametric controls for sword geometry
- **Procedural CAD** (Hello-Sword): OpenSCAD script generating blade geometry via CSG operations

### Output Format
- 3D mesh (Caius Walker, Pamir Bal, Hello-Sword)
- 2D pixel art sprite (Sword-Maker)
- STL/printable model (Hello-Sword via OpenSCAD)

### Technical Complexity
- Caius Walker: Highest — full physics engine integration (damage calculation via kinetic energy, point of balance, mass estimation from mesh volume)
- Sword-Maker: Medium — GPU shader-based rendering with UI controls
- Pamir Bal: Medium — Blender API integration with commercial packaging
- Hello-Sword: Low — single-file OpenSCAD script

## Relations Between Sources

- Caius Walker and Pamir Bal both target 3D mesh output for games/rendering
- Sword-Maker is the only 2D pixel art approach
- Hello-Sword is the only CAD-oriented (manufacturing-ready) approach
- None appear to directly reference each other

## Gaps

- No source implements AI/ML-based sword generation
- No source generates historical period-accurate swords with real metallurgical properties
- No source supports animation-ready rigged sword meshes
- No cross-project dependency or shared standards

## Extraction Status

| Source | URL | Extracted | Article | Person | Concept |
|--------|-----|-----------|---------|--------|---------|
| Caius Walker | https://www.caiuswalker.co.uk/pcg-swords | ✓ | `2026-06-11-caius-walker-pcg-swords` | `caius-walker` | — |
| Github repos | https://github.com/FirestarSW/... | ✓ | — | — | — |
| Sword-Maker | https://github.com/BumbertFiddlesticks/Sword-Maker | ✓ | — | — | `sword-maker-godot` |
| Blender addon | https://blender-addons.org/procedural-sword-generator-for-blender/ | ✓ | — | `pamir-bal` | `procedural-sword-gen-blender` |
| Hello-Sword | https://github.com/mugenZebra/Hello-Sword | ✓ | — | — | `hello-sword-openscad` |
