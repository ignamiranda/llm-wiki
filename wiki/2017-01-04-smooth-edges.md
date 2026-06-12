---
title: "The Quest for Automatic Smooth Edges for 3D Models"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [graphics, 3d-modeling, vertex-normals, unity, shader]
summary: "A technique for automatically calculating face-weighted (area-weighted) vertex normals to produce smooth beveled edges on 3D models while keeping flat surfaces flat, without manual edge loops."
source_url: "https://blog.runevision.com/2017/01/the-quest-for-automatic-smooth-edges.html"
---

# The Quest for Automatic Smooth Edges for 3D Models

## Summary
A technique for automatically calculating face-weighted (area-weighted) vertex normals to produce smooth beveled edges on 3D models while keeping flat surfaces flat, without manual edge loops.

## Content
The challenge addressed is achieving smooth edges on beveled 3D models while preserving flat surfaces. Standard approaches like Blender's bevel modifier, subdivision surface modeling, and smooth shading each have drawbacks — they either require manual edge loops, increase polygon counts significantly, or produce unwanted smoothing across intended hard edges.

The solution is implemented as a Unity AssetPostprocessor that recalculates normals during model import using face-weighted (area-weighted) averaging. The algorithm works by computing each vertex's final normal as a weighted sum of the normals of all faces sharing that vertex, where each face contributes proportionally to its area. Large faces dominate the vertex normal direction, keeping flat surfaces flat, while small bevel faces have proportionally less influence, allowing smooth transitions along edges.

A threshold parameter controls which edges remain sharp. When the angle between face normals exceeds the threshold, their contributions are blended rather than averaged, preserving hard edges where geometry demands them. This produces results similar to 3ds Max's "smooth by angle" or Blender's "auto smooth" but with superior handling of non-uniform face sizes.

The implementation is publicly available as a GitHub Gist. Credit is given to Charis Marangos (Zoodinger) for deriving the original code this technique builds upon.

## Key Takeaways
- Face-weighted normals (area-weighted) produce smooth bevels without manual edge loops
- Implemented as Unity AssetPostprocessor for automatic import
- Threshold parameter controls which edges stay sharp

## Related
- [[rune-skovbo-johansen]] — author
- [[mesh-generation]] — related technique
