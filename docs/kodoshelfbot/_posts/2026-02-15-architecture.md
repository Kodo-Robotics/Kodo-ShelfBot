---
layout: post
title: "System Architecture Overview"
date: 2026-02-15
---

This post describes the system-level architecture of Kodo ShelfBot.

The robot consists of:

- Differential drive mobile base
- 2D LiDAR for localization
- RGB-D camera for perception
- 6DOF arm with top grasp strategy
- Parallel gripper

Navigation is handled via Nav2, while manipulation uses MoveIt 2.
