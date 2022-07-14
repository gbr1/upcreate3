from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, PathJoinSubstitution
from launch.substitutions.launch_configuration import LaunchConfiguration

from launch_ros.actions import Node


ARGUMENTS = [
    DeclareLaunchArgument('use_sim_time', default_value='false',
                          choices=['true', 'false'],
                          description='use_sim_time'),
]


def generate_launch_description():
    upcreate3_description_path = get_package_share_directory('upcreate3_description')
    xacro_file = PathJoinSubstitution([upcreate3_description_path,
                                       'urdf',
                                       'upcreate3.urdf.xacro'])

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[
            {'use_sim_time': LaunchConfiguration('use_sim_time')},
            {'robot_description': Command(['xacro', ' ', xacro_file, ' ', 'gazebo:=ignition'])},
        ],
    )

    ld = LaunchDescription(ARGUMENTS)
    ld.add_action(robot_state_publisher)
    return ld