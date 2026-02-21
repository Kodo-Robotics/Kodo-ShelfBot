import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, SetEnvironmentVariable, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, EnvironmentVariable


def generate_launch_description():

    pkg_share = get_package_share_directory("shelfbot_gazebo")
    ros_gz_sim_share = get_package_share_directory("ros_gz_sim")

    world_default = os.path.join(
        pkg_share,
        "worlds",
        "shelfbot_world.world"
    )

    world = LaunchConfiguration("world")

    # Warehouse models
    shelfbot_models = os.path.join(pkg_share, "models")

    # shelfbot_description share path
    shelfbot_desc_share = get_package_share_directory("shelfbot_description")

    # IMPORTANT: we need the parent of share directory
    # so that Gazebo sees:
    #   <parent>/shelfbot_description/meshes/...
    shelfbot_parent_dir = os.path.dirname(shelfbot_desc_share)

    # Build complete resource path
    resource_paths = [
        shelfbot_models,
        shelfbot_parent_dir,
    ]

    # Append safely to existing variable
    full_resource_path = [
        EnvironmentVariable("GZ_SIM_RESOURCE_PATH", default_value=""),
        os.pathsep,
        os.pathsep.join(resource_paths),
    ]

    return LaunchDescription([

        DeclareLaunchArgument(
            "world",
            default_value=world_default,
            description="Full path to world file"
        ),

        SetEnvironmentVariable(
            name="GZ_SIM_RESOURCE_PATH",
            value=full_resource_path
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(
                    ros_gz_sim_share,
                    "launch",
                    "gz_sim.launch.py"
                )
            ),
            launch_arguments={
                "gz_args": world
            }.items(),
        ),
    ])