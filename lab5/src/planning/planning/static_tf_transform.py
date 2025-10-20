#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros import StaticTransformBroadcaster

import numpy as np
from scipy.spatial.transform import Rotation as rot


class ConstantTransformPublisher(Node):
    def __init__(self):
        super().__init__('constant_tf_publisher')
        self.br = StaticTransformBroadcaster(self)

        # Homogeneous transform G_ar->base
        G = np.array([
            [-1, 0, 0, 0.0],
            [ 0, 0, 1, 0.16],
            [ 0, 1, 0, -0.13],
            [ 0, 0, 0, 1.0]
        ])

        # Create TransformStamped
        self.transform = TransformStamped()
        # ---------------------------
        # TODO: Fill out TransformStamped message
        # --------------------------

        rotation = G[:3, :3]
        translation = G[:3, 3]
        quaternion = rot.from_matrix(rotation).as_quat()
        self.transform = TransformStamped()

        self.transform.header.frame_id = 'ar_marker_10'       
        self.transform.child_frame_id = 'base_link'          

        self.transform.transform.translation.x = translation[0]
        self.transform.transform.translation.y = translation[1]
        self.transform.transform.translation.z = translation[2]

        self.transform.transform.rotation.x = quaternion[0]
        self.transform.transform.rotation.y = quaternion[1]
        self.transform.transform.rotation.z = quaternion[2]
        self.transform.transform.rotation.w = quaternion[3]

        self.timer = self.create_timer(0.05, self.broadcast_tf)

    def broadcast_tf(self):
        self.transform.header.stamp = self.get_clock().now().to_msg()
        self.br.sendTransform(self.transform)

def main():
    rclpy.init()
    node = ConstantTransformPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()