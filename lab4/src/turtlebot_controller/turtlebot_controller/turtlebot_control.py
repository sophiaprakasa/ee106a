#!/usr/bin/env python3
import sys
import numpy as np

import rclpy
from rclpy.node import Node
from rclpy.time import Time

from geometry_msgs.msg import Twist

from tf2_ros import Buffer, TransformListener
from tf2_ros import TransformException, LookupException, ConnectivityException, ExtrapolationException

class TurtleBotController(Node):
    def __init__(self, frame1, frame2):
        super().__init__('turtlebot_controller')

        self.turtle_frame = frame1
        self.ar_frame = frame2

        self.x = self.turtle_frame[0]
        self.y = self.turtle_frame[1]
        self.xd = self.ar_frame[0]
        self.yd = self.ar_frame[1]

        # Note: these constants might not work for your turtlebot, be willing to tune them if it isn't reaching the goal!
        self.K1 = 0.3
        self.K2 = 1.0

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.loop)

        self.get_logger().info(
            f"TurtleBotController: frame1 (robot)='{self.turtle_frame}', frame2 (target)='{self.ar_frame}', "
            f"K1={self.K1}, K2={self.K2}"
        )

    def loop(self):
        try:
            tf = self.tf_buffer.lookup_transform(self.turtle_frame, self.ar_frame, Time())
            """
Transformed stamped --> 
Header header
string child_frame_id # the frame id of the child frame
Transform transform


Transform --> 
Vector3 translation
Quaternion rotation

Twist --> 
Vector3 linear
Vector3 angular


            """
            print(tf.transform.translation)
            leftMatrix = np.array([[self.K1, 0],
                                   [0, self.K2]])
            rightMatrix = np.array([[tf.transform.translation.x],
                                    [tf.transform.translation.y]])
            control_cmd = np.matmul(leftMatrix, rightMatrix)
            print(control_cmd)
            cmd = Twist()
            cmd.linear.x = control_cmd[0][0]
            cmd.angular.z = control_cmd[1][0]
            print(cmd)
            self.pub.publish(cmd)

        except (TransformException, LookupException, ConnectivityException, ExtrapolationException):
            self.pub.publish(Twist())
    
    def destroy_node(self):
        try:
            self.pub.publish(Twist())
        finally:
            super().destroy_node()


def main(args=None):
    rclpy.init(args=args)

    if len(sys.argv) != 3:
        print("Usage: python3 turtlebot_control.py frame1 frame2")
        rclpy.shutdown()
        return

    frame1 = sys.argv[1] #turtle bot 
    frame2 = sys.argv[2] #target tag. origin
    # trans = tfBuffer.lookup_transform(target_frame, source_frame, rclpy.time.Time())

    node = TurtleBotController(frame1, frame2)
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
