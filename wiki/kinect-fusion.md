---
title: "KinectFusion"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [computer-vision, 3d-reconstruction, kinect, depth-sensor, tsdf, marching-cubes]
aliases: [kinectfusion, kinect-fusion]
summary: "A real-time 3D reconstruction pipeline that fuses depth camera data into a volumetric TSDF representation and extracts surface meshes using Marching Cubes."
---

# KinectFusion

## Definition

KinectFusion is a real-time dense surface mapping and tracking system that uses a moving depth camera (such as Microsoft Kinect) to reconstruct 3D scenes. It fuses incoming depth frames into a volumetric Truncated Signed Distance Function (TSDF) representation on the GPU, enabling real-time camera tracking and surface reconstruction. The final surface mesh is extracted from the TSDF volume using Marching Cubes.

## Key Properties

- Real-time GPU-accelerated pipeline (CUDA)
- Volumetric TSDF representation for surface fusion
- Iterative Closest Point (ICP) for camera pose tracking
- Marching Cubes for final mesh extraction
- Outputs point clouds and dense surface meshes (PLY format)
- Original paper: Newcombe et al., ISMAR 2011

## Related Concepts

- [[marching-cubes]] — used for final mesh extraction from TSDF volume
- [[voxel-carving]] — related 3D reconstruction technique from silhouettes

## References

- KinectFusionLib: https://github.com/chrdiller/KinectFusionLib
- KinectFusionApp: https://github.com/chrdiller/KinectFusionApp
