import rclpy
from rclpy.node import Node
import sys

from geometry_msgs.msg import Twist
from std_srvs.srv import Empty
from turtlesim.srv import TeleportAbsolute
from turtle_patrol_interface.srv import Patrol


class TurtlePatrolServer(Node):
    def __init__(self):
        super().__init__('turtle_patrol_server')
        self.name = sys.argv[1]

        # Publisher: actually drives turtle1

        self._cmd_pub = self.create_publisher(Twist, f'/{self.name}/cmd_vel', 10)
        self._srv = self.create_service(Patrol, f'/{self.name}/patrol', self.patrol_callback)

        # Current commanded speeds (what timer publishes)
        self._lin = 0.0
        self._ang = 0.0
        self._x = 0.0
        self._y = 0.0
        self._theta = 0.0

        # Timer: publish current speeds at 10 Hz
        self._pub_timer = self.create_timer(0.1, self._publish_current_cmd)

        self.get_logger().info('Turtle1PatrolServer ready (continuous publish mode).')

    # -------------------------------------------------------
    # Timer publishes current Twist
    # -------------------------------------------------------
    def _publish_current_cmd(self):
        msg = Twist()
        msg.linear.x = self._lin
        msg.angular.z = self._ang
        self._cmd_pub.publish(msg)


    # -------------------------------------------------------
    # Service callback: update speeds
    # -------------------------------------------------------
    def patrol_callback(self, request: Patrol.Request, response: Patrol.Response):
        self.get_logger().info(
            f"Patrol request: vel={request.vel:.2f}, omega={request.omega:.2f}, x={request.x:.2f}, y={request.y:.2f}, theta={request.theta:.2f}"
        )

        # Update the speeds that the timer publishes
        self._lin = float(request.vel)
        self._ang = float(request.omega)
        self._x = float(request.x)
        self._y = float(request.y)
        self._theta = float(request.theta)

        self._service_name = f'/{self.name}/teleport_absolute'
        self._client = self.create_client(TeleportAbsolute, self._service_name)
        pos = TeleportAbsolute.Request()
        pos.x = self._x
        pos.y = self._y
        pos.theta = self._theta
        self._future = self._client.call_async(pos)

        # Prepare response Twist reflecting current command
        cmd = Twist()
        cmd.linear.x = self._lin
        cmd.angular.z = self._ang
        response.cmd = cmd

        self.get_logger().info(
            f"Streaming cmd_vel: lin.x={self._lin:.2f}, ang.z={self._ang:.2f} (10 Hz)"
        )
        return response


def main(args=None):
    rclpy.init(args=args)
    node = TurtlePatrolServer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
