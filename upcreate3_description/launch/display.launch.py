# The MIT License
# 
# Copyright (c) 2022 Giovanni di Dio Bruno https://gbr1.github.io
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
#
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