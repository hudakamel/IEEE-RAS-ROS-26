import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32
import json

class ExternalRobotEmulator(Node):
    def __init__(self, name, x, y, priority):
        super().__init__(name)
        self.name = name
        self.priority = priority
        self.my_pose = Pose2D(x=float(x), y=float(y))

        self.pose_pub = self.create_publisher(Pose2D, f'/{name}/pose', 10)
        self.priority_pub = self.create_publisher(Int32, f'/{name}/priority', 10)
        self.timer = self.create_timer(0.1, self.on_timer_tick)

    def on_timer_tick(self):
        self.pose_pub.publish(self.my_pose)
        msg = Int32(data=self.priority)
        self.priority_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    
    #  node
    param_loader = Node('emulator_param_loader')
    param_loader.declare_parameter(
        'robot_positions', 
        '[{"name":"Robot_B","x":1.5,"y":1.0,"priority":5},{"name":"Robot_C","x":10.0,"y":10.0,"priority":10}]'
    )
    
    config_string = param_loader.get_parameter('robot_positions').get_parameter_value().string_value
    fleet_data = json.loads(config_string)

    executor = MultiThreadedExecutor()
    active_nodes = []

    for robot in fleet_data:
        node = ExternalRobotEmulator(robot['name'], robot['x'], robot['y'], robot['priority'])
        active_nodes.append(node)
        executor.add_node(node)

    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        for node in active_nodes:
            node.destroy_node()
        param_loader.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()