from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    name = LaunchConfiguration("name")
    x = LaunchConfiguration("x")
    y = LaunchConfiguration("y")
    z = LaunchConfiguration("z")

    return LaunchDescription([
        DeclareLaunchArgument("name", default_value="shelfbot"),
        DeclareLaunchArgument("x", default_value="0.0"),
        DeclareLaunchArgument("y", default_value="0.0"),
        DeclareLaunchArgument("z", default_value="0.1"),

        Node(
            package="ros_gz_sim",
            executable="create",
            output="screen",
            arguments=[
                "-entity", name,
                "-topic", "robot_description",
                "-x", x,
                "-y", y,
                "-z", z,
            ],
        ),
    ])