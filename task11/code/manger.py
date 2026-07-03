import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32

class TrafficManager(Node):
    def __init__(self):
        super().__init__('traffic_manager_node')
        
        # Details 
        self.name = "Robot_A"
        self.priority = 1
        self.my_pose = Pose2D()
        self.my_pose.x = 0.0
        self.my_pose.y = 0.0
        
        self.safe_distance = 2.0  # Zone Limit
        
        self.other_positions = {}
        self.other_priorities = {}

        
        self.pose_pub = self.create_publisher(Pose2D, f'/{self.name}/pose', 10)
        self.priority_pub = self.create_publisher(Int32, f'/{self.name}/priority', 10)

     
        self.external_fleet = ['Robot_B', 'Robot_C']
        self.listen_to_fleet()

        # Decision making 
        self.timer = self.create_timer(0.1, self.on_timer_tick)
        self.get_logger().info(f"Traffic Manager tracking system initiated for {self.name}.")

    def on_timer_tick(self):
        
        self.pose_pub.publish(self.my_pose)
        msg = Int32()
        msg.data = self.priority
        self.priority_pub.publish(msg)
        
       
        self.check_traffic_rules()

    def listen_to_fleet(self):
        for robot_name in self.external_fleet:
            self.other_positions[robot_name] = None
            
            self.create_subscription(
                Pose2D, 
                f'/{robot_name}/pose', 
                lambda msg, target=robot_name: self.update_position(msg, target), 
                10
            )
            self.create_subscription(
                Int32, 
                f'/{robot_name}/priority', 
                lambda msg, target=robot_name: self.update_priority(msg, target), 
                10
            )

    def update_position(self, msg, target_name):
        self.other_positions[target_name] = msg

    def update_priority(self, msg, target_name):
        self.other_priorities[target_name] = msg.data

    def check_traffic_rules(self):
        hazard_detected = False
        hazard_details = ""

        for name, pos in self.other_positions.items():
            if pos is None or name not in self.other_priorities:
                continue  

            dx = self.my_pose.x - pos.x
            dy = self.my_pose.y - pos.y
            distance = math.sqrt(dx*dx + dy*dy)

            
            if distance <= self.safe_distance:
                their_priority = self.other_priorities[name]
                if their_priority > self.priority:
                    hazard_detected = True
                    hazard_details = f"Robot {name} is at {distance:.2f}m with priority {their_priority}!"
                    break

        if hazard_detected:
            self.get_logger().warn(f"[DANGER] Yield path! -> {hazard_details}")
        else:
            self.get_logger().info("[CLEAR] Path is safe.")

def main(args=None):
    rclpy.init(args=args)
    node = TrafficManager()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("\nStopping Traffic Manager.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()