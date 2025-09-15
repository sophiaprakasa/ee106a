import rclpy
from rclpy.node import Node
import sys

# This line imports the built-in string message type that our node will use to structure its data to pass on our topic
from geometry_msgs.msg import Twist

# We're creating a class called Talker, which is a subclass of Node
class TurtleController(Node):
    # Here, we define the constructor
    def __init__(self):
        super().__init__('turtle_controller')
        turtle = f"{sys.argv[1]}/cmd_vel"
        print(turtle)
        self.publisher_ = self.create_publisher(Twist, turtle, 10)
        self.timer = self.create_timer(0.5, self.publish_msg)

    def publish_msg(self):
        while rclpy.ok(): 
            line = input("Please choose an action:")
            msg = Twist()
            if line == 'w':
                msg.linear.x = 2.0
            if line == 'a':
                msg.angular.z = 2.0
            if line == 's':
                msg.linear.x = -2.0
            if line == 'd':
                msg.angular.z = -2.0

            self.publisher_.publish(msg)
            self.get_logger().info('Publishing: "%s"' % msg)
            


def main(args=None):
    rclpy.init(args=args)
    node = TurtleController()
    # Spin the node so its callbacks are called
    rclpy.spin(node)
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
