import math
import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32

class RobotID(Node):
    def __init__(self, name, x, y, priority):
        super().__init__(name)
        self.name = name
        self.priority = priority
        
        self.my_pose = Pose2D()
        self.my_pose.x = float(x)
        self.my_pose.y = float(y)
        
        self.safe_distance = 2.0  
        
        self.other_positions = {}
        self.other_priorities = {}

        self.pose_pub = self.create_publisher(Pose2D, f'/{name}/pose', 10)
        self.priority_pub = self.create_publisher(Int32, f'/{name}/priority', 10)
        
        self.timer = self.create_timer(0.1, self.on_timer_tick)

        self.get_logger().info(f"Robot {self.name} started (Priority: {self.priority})")

    def on_timer_tick(self):
        self.pose_pub.publish(self.my_pose)
        
        msg = Int32()
        msg.data = self.priority
        self.priority_pub.publish(msg)
        
        self.check_traffic_rules()

    def listen_to_fleet(self, fleet_list):
        for robot_name, info in fleet_list.items():
            if robot_name == self.name:
                continue  
            
            self.other_priorities[robot_name] = info['priority']
            self.other_positions[robot_name] = None
            
            self.create_subscription(
                Pose2D, 
                f'/{robot_name}/pose', 
                lambda msg, target=robot_name: self.update_position(msg, target), 
                10
            )

    def update_position(self, msg, target_name):
        self.other_positions[target_name] = msg

    def check_traffic_rules(self):
        hazard_detected = False
        hazard_details = ""

        for name, pos in self.other_positions.items():
            if pos is None:
                continue  

            dx = self.my_pose.x - pos.x
            dy = self.my_pose.y - pos.y
            distance = math.sqrt(dx*dx + dy*dy)

            if distance <= self.safe_distance:
                their_priority = self.other_priorities[name]
                if their_priority > self.priority:
                    hazard_detected = True
                    hazard_details = f"Robot {name} is too close ({distance:.2f}m) and has higher priority!"
                    break

        if hazard_detected:
            self.get_logger().warn(f"[DANGER] Yield path! -> {hazard_details}")
        else:
            self.get_logger().info("[CLEAR] Path is safe.")


def main(args=None):
    rclpy.init(args=args)

    fleet = {
        'Robot_A': {'x': 0.0, 'y': 0.0, 'priority': 1},
        'Robot_B': {'x': 1.5, 'y': 1.0, 'priority': 5},   
        'Robot_C': {'x': 10.0, 'y': 10.0, 'priority': 10}  
    }

    executor = MultiThreadedExecutor()
    active_nodes = []

    for name, info in fleet.items():
        node = RobotID(name, info['x'], info['y'], info['priority'])
        active_nodes.append(node)
        executor.add_node(node)

    for node in active_nodes:
        node.listen_to_fleet(fleet)

    try:
        print("Running decentralized multi-robot system... (Ctrl+C to stop)")
        executor.spin()
    except KeyboardInterrupt:
        print("\nStopping system.")
    finally:
        for node in active_nodes:
            node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()