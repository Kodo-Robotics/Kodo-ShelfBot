import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, SetEnvironmentVariable, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    pkg_share = get_package_share_directory("shelfbot_gazebo")
    ros_gz_sim_share = get_package_share_directory("ros_gz_sim")

    world_default = os.path.join(
        pkg_share,
        "worlds",
        "shelfbot_world.world"
    )

    world = LaunchConfiguration("world")
    assets_path = os.path.join(pkg_share, "models")

    return LaunchDescription([

        DeclareLaunchArgument(
            "world",
            default_value=world_default,
            description="Full path to world file"
        ),

        SetEnvironmentVariable(
            name="GZ_SIM_RESOURCE_PATH",
            value=assets_path
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