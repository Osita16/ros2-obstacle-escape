import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import random

class ObstacleAvoidance(Node):

    def __init__(self):
        super().__init__('obstacle_avoidance')

        self.sub = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10)

        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)

        self.status_pub = self.create_publisher(String, '/explorer_status', 10)

    def scan_callback(self, msg):

        front = min(min(msg.ranges[0:30]), min(msg.ranges[330:360]))

        cmd = Twist()
        status = String()

        if front < 0.8:
            cmd.angular.z = random.choice([-0.5, 0.5])
            status.data = f"Obstacle detected at {front:.2f} m"
        else:
            cmd.linear.x = 0.2
            status.data = f"Moving forward. Distance {front:.2f} m"

        self.pub.publish(cmd)
        self.status_pub.publish(status)


def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoidance()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()