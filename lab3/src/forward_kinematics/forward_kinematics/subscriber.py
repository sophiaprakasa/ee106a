import rclpy
from rclpy.node import Node
from .forward_kinematics import ur7e_forward_kinematics_from_joint_state
from sensor_msgs.msg import JointState



class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            JointState,
            'joint_states',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
    

    def listener_callback(self, msg):
        joints = msg.position
        print(ur7e_forward_kinematics_from_joint_state(msg))


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

'''
header:
  stamp:
    sec: 1758072776
    nanosec: 872442249
  frame_id: base_link
name:
- shoulder_lift_joint
- elbow_joint
- wrist_1_joint
- wrist_2_joint
- wrist_3_joint
- shoulder_pan_joint
position:
- -2.278550764123434
- -1.615183711051941
- -1.4831759941628953
- 0.8377456665039062
- -2.711463276539938
- 4.153355121612549
velocity:
- 0.0
- -0.0
- 0.0
- 0.0
- 0.0
- 0.0
effort:
- 4.285924911499023
- 1.5968265533447266
- 0.13570083677768707
- -0.13598214089870453
- -0.002794601023197174
- 0.008587000891566277
'''
