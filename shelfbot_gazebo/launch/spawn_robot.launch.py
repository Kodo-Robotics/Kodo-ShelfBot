from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, PathJoinSubstitution, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import FindExecutable
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    use_sim_time = LaunchConfiguration("use_sim_time")

    declare_use_sim_time = DeclareLaunchArgument(
        "use_sim_time",
        default_value="true",
        description="Use simulation time"
    )

    # Path to xacro inside shelfbot_description package
    robot_xacro = PathJoinSubstitution([
        FindPackageShare("shelfbot_description"),
        "urdf",
        "robot.urdf.xacro"   # change if filename differs
    ])

    # Generate URDF from xacro
    robot_description = ParameterValue(
        Command([
            FindExecutable(name="xacro"),
            " ",
            robot_xacro,
            " ",
            "is_sim:=true"
        ]),
        value_type=str
    )

    # Robot State Publisher
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{
            "robot_description": robot_description,
            "use_sim_time": use_sim_time
        }],
        output="screen"
    )

    # Spawn into running Gazebo
    spawn_node = Node(
        package="ros_gz_sim",
        executable="create",
        arguments=[
            "-topic", "robot_description",
            "-name", "shelfbot",
            "-x", "0",
            "-y", "0",
            "-z", "0.2"
        ],
        output="screen"
    )

    return LaunchDescription([
        declare_use_sim_time,
        robot_state_publisher_node,
        spawn_node,
    ])