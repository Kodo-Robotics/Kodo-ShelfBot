# kodo_gazebo

Gazebo (Harmonic) simulation package for Kodo Shelfbot.

## Contents
- `worlds/`: Gazebo world(s)
- `models/`: models/meshes/materials used by the world
- `launch/`: launch files to bring up Gazebo and spawn the robot

## Third-party assets
This package includes modified assets from:
- aws-robotics/aws-robomaker-small-warehouse-world (ROS2 branch)

License text and notice:
- `third_party/aws_small_warehouse/ORIGINAL_LICENSE.txt`
- `third_party/aws_small_warehouse/NOTICE.md`

## Run
```bash
ros2 launch shelfbot_gazebo gazebo.launch.py
```

## Spawn Robot
```bash
ros2 launch shelfbot_gazebo spawn_robot.launch.py
```