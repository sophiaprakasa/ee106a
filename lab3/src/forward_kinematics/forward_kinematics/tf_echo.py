import tf2_ros
import sys

import rclpy
from rclpy.node import Node
import time 

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.target_frame = sys.argv[1]
        self.source_frame =  sys.argv[2]

        self.tfBuffer = tf2_ros.Buffer()
        self.tfListener = tf2_ros.TransformListener(self.tfBuffer, self)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.lookup)
        self.i = 0

    def lookup(self):
        # time.sleep(3)
        try: 
            trans = self.tfBuffer.lookup_transform(self.target_frame, self.source_frame, rclpy.time.Time())
            print(trans)
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as e:
            print(f"Exception caught: {e}")


def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.lookup()
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()