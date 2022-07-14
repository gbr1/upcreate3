from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, PathJoinSubstitution
from launch.substitutions.launch_configuration import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():

    upcreate3_description_path = get_package_share_directory('upcreate3_description')
    rviz_file_path = os.path.join(upcreate3_description_path, 'rviz', 'display.rviz')
    rvizconfig = LaunchConfiguration('rvizconfig')
    
    robot_description_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([upcreate3_description_path, '/launch/description.launch.py'])
    )

    declare_rvizconfig_cmd = DeclareLaunchArgument(
        name='rvizconfig',
        default_value=rviz_file_path,
        description='RViz visualization file')


    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rvizconfig],
    )
    
    ld = LaunchDescription()
    ld.add_action(robot_description_launch)
    ld.add_action(declare_rvizconfig_cmd)
    ld.add_action(rviz_node)
    return ld