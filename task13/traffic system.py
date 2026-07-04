from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    
    safety_zone_arg = DeclareLaunchArgument('safety_zone', default_value='2.0')
    robot_priority_arg = DeclareLaunchArgument('robot_priority', default_value='1')
    
    robot_position_arg = DeclareLaunchArgument(
        'robot_position', 
        default_value='[{"name":"Robot_B","x":1.5,"y":1.0,"priority":5},{"name":"Robot_C","x":10.0,"y":10.0,"priority":10}]'
    )

   
    traffic_manager_node = Node(
        package='fleet_management',
        executable='traffic_manager',
        name='traffic_manager_node',
        output='screen',
        parameters=[{
            'safety_zone': LaunchConfiguration('safety_zone'),
            'robot_priority': LaunchConfiguration('robot_priority'),
        }]
    )

    fleet_emulator_node = Node(
        package='fleet_management',
        executable='fleet_emulator',
        name='fleet_emulator_node',
        output='screen',
        parameters=[{
            'robot_positions': LaunchConfiguration('robot_position'),
        }]
    )

    return LaunchDescription([
        safety_zone_arg,
        robot_priority_arg,
        robot_position_arg,
        traffic_manager_node,
        fleet_emulator_node
    ])