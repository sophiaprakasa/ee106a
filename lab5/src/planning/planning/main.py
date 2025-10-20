# ROS Libraries
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PointStamped 
from tf2_ros import Buffer, TransformListener
import numpy as np
import tf2_geometry_msgs

class UR7e_CubeGrasp(Node):
    def __init__(self):
        super().__init__('cube_grasp')

        self.cube_sub = self.create_subscription(PointStamped, '/cube_pose', self.cube_callback, 1)

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        self.pub = self.create_publisher(PointStamped, '/cube_pose_base_link', 10)
        rclpy.spin_once(self, timeout_sec=2)

        self.cube_pose = None

    def cube_callback(self, cube_pose):
        self.cube_pose = self.transform_cube_pose(cube_pose)
        self.get_logger().info('Received cube pose')
        self.pub.publish(self.cube_pose)


    def transform_cube_pose(self, msg: PointStamped):
        """ 
        Transform point into base_link frame
        Args: 
            - msg: PointStamped - The message from /cube_pose, of the position of the cube in camera_depth_optical_frame
        Returns:
            PointStamped: point in base_link_frame in form [x, y, z]
        """

        # ------------------------
        #TODO: Add your code here!
        # ------------------------
        transform = self.tf_buffer.lookup_transform(
            'base_link', msg.header.frame_id, rclpy.time.Time(),
            rclpy.duration.Duration(seconds=1.0)
        )
        point = tf2_geometry_msgs.do_transform_point(msg, transform)
        point.header.frame_id = 'base_link'

        return point

def main(args=None):
    rclpy.init(args=args)
    node = UR7e_CubeGrasp()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
