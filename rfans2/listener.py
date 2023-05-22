#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException
from sensor_msgs.msg import PointCloud2

class rfans2_listener(Node):

    def __init__(self):
        super().__init__('listener')
        self.sub = self.create_subscription(PointCloud2, '/rfans_driver/rfans_points', self.callback, 10)

    def callback(self, msg):
        # self.get_logger().info('scan data: [%f]' % msg.data)
        print(msg.data)

def main(args=None):
    rclpy.init(args=args)

    node = rfans2_listener()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()

if __name__ == '__main__':
    main()
