#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from image_transport import ImageTransport

class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_transport_node')
        self.it = ImageTransport(self)
        self.subscriber = self.it.subscribe('camera/image_raw', self.image_callback, 'raw')

    def image_callback(self, msg):
        self.get_logger().info('Received an image!')

def main(args=None):
    rclpy.init(args=args)
    node = ImageSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
