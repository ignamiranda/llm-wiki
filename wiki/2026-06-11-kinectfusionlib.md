---
title: "KinectFusionLib — C++14/CUDA KinectFusion Implementation"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [computer-vision, kinect-fusion, cuda, 3d-reconstruction, marching-cubes, tsdf]
summary: "A modern C++14 and CUDA implementation of the KinectFusion real-time dense surface mapping and tracking pipeline."
---

# KinectFusionLib — C++14/CUDA KinectFusion Implementation

## Summary

KinectFusionLib by Christian Diller implements the KinectFusion algorithm in modern C++14 with CUDA GPU acceleration, providing real-time fusion of depth camera data into a volumetric TSDF representation with Marching Cubes mesh extraction.

## Content

Based on Newcombe et al.'s 2011 paper, this library provides a clean C++14 API for real-time depth frame fusion, camera pose tracking (ICP), and surface mesh extraction via Marching Cubes. It supports export to PLY format for both point clouds and meshes. Dependencies include CUDA 8.0, OpenCV 3.0+, and Eigen3.

## Key Takeaways

- GPU-accelerated (CUDA) real-time depth fusion
- Exports point clouds and dense surface meshes (PLY)
- Modern C++14 API with RAII and clean interfaces
- 488 stars on GitHub

## Related

- [[kinect-fusion]] — algorithm implemented
- [[marching-cubes]] — used for mesh extraction
- [[christian-diller]] — author
- [[2026-06-11-kinectfusionapp]] — sample application

## Links

- Repository: https://github.com/chrdiller/KinectFusionLib
