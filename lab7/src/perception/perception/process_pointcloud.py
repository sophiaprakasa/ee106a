import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
from geometry_msgs.msg import PointStamped
import numpy as np
import sensor_msgs_py.point_cloud2 as pc2
from std_msgs.msg import Header

class RealSensePCSubscriber(Node):
    def __init__(self):
        super().__init__('realsense_pc_subscriber')

        self.declare_parameter('plane.a', 0.0)
        self.declare_parameter('plane.b', 0.0)
        self.declare_parameter('plane.c', 0.0)
        self.declare_parameter('plane.d', 0.0)
        self.declare_parameter('max_distance', 0.6)

        self.a = self.get_parameter('plane.a').value
        self.b = self.get_parameter('plane.b').value
        self.c = self.get_parameter('plane.c').value
        self.d = self.get_parameter('plane.d').value
        self.max_distance = self.get_parameter('max_distance').value

        self.pc_sub = self.create_subscription(
            PointCloud2,
            '/camera/camera/depth/color/points',
            self.pointcloud_callback,
            10
        )

        self.cube_pose_pub = self.create_publisher(PointStamped, '/cube_pose', 1)
        self.filtered_points_pub = self.create_publisher(PointCloud2, '/filtered_points', 1)

        self.get_logger().info("Subscribed to PointCloud2 topic and marker publisher ready")

    def pointcloud_callback(self, msg: PointCloud2):
        points = []
        for p in pc2.read_points(msg, field_names=('x','y','z'), skip_nans=True):
            points.append([p[0], p[1], p[2]])

        points = np.array(points)

        if points.shape[0] == 0:
            self.get_logger().info("Received empty point cloud.")
            self.publish_filtered_points(np.array([]), msg.header)
            return

        # ------------------------
        # TODO: Add your code here! 
        # ------------------------
        z_coords = points[:, 2]
        distance_mask = z_coords <= self.max_distance
        plane_values = points[:, 0] * self.a + \
                       points[:, 1] * self.b + \
                       points[:, 2] * self.c + self.d
        plane_mask = plane_values > 0
        combined_mask = np.logical_and(distance_mask, plane_mask)
        filtered_points = points[combined_mask]
        cube_x = 0.0
        cube_y = 0.0
        cube_z = 0.0

        if filtered_points.shape[0] == 0:
            self.get_logger().warn("No points left after filtering.")
        else:
            centroid = np.mean(filtered_points, axis=0)
            cube_x = float(centroid[0])
            cube_y = float(centroid[1])
            cube_z = float(centroid[2])

        self.get_logger().info(f"Filtered points: {filtered_points.shape[0]}")

        cube_pose = PointStamped()
        
        # Fill in message
        cube_pose.header = msg.header
        cube_pose.point.x = cube_x
        cube_pose.point.y = cube_y
        cube_pose.point.z = cube_z

        self.cube_pose_pub.publish(cube_pose)

        self.publish_filtered_points(filtered_points, msg.header)

    def publish_filtered_points(self, filtered_points: np.ndarray, header: Header):
        # Create PointCloud2 message from filtered Nx3 array
        # Ensure points are in a list format for create_cloud_xyz32
        filtered_msg = pc2.create_cloud_xyz32(header, filtered_points.tolist())
        self.filtered_points_pub.publish(filtered_msg)


def main(args=None):
    rclpy.init(args=args)
    node = RealSensePCSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()