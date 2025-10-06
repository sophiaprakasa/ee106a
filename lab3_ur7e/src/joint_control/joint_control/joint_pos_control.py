#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import sys
import tty
import termios
import threading
import select

# Key mappings
INCREMENT_KEYS = ['1','2','3','4','5','6']
DECREMENT_KEYS = ['q','w','e','r','t','y']
JOINT_STEP = 0.065 # radians per key press

class KeyboardController(Node):
    def __init__(self):
        super().__init__('ur7e_keyboard_controller')
        
        self.joint_names = [
            f'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint',
            'wrist_2_joint', 'wrist_3_joint'
        ]
        self.shoulder_pan_joint = float(sys.argv[1])
        self.shoulder_lift_joint = float(sys.argv[2])
        self.elbow_joint = float(sys.argv[3])
        self.wrist_1_joint = float(sys.argv[4])
        self.wrist_2_joint = float(sys.argv[5])
        self.wrist_3_joint = float(sys.argv[6])

        self.joint_positions = [0.0]*6

        self.joint_positions[0] = self.shoulder_pan_joint
        self.joint_positions[1] = self.shoulder_lift_joint
        self.joint_positions[2] = self.elbow_joint
        self.joint_positions[3] = self.wrist_1_joint
        self.joint_positions[4] = self.wrist_2_joint
        self.joint_positions[5] = self.wrist_3_joint

        self.got_joint_states = False  # Failsafe: don't publish until joint states received

        self.timer = self.create_timer(1, self.handle_angles)
        self.pub = self.create_publisher(JointTrajectory, '/scaled_joint_trajectory_controller/joint_trajectory', 10)
        
        self.running = True
        self.handle_angles()
    
    def handle_angles(self):
        traj = JointTrajectory()
        traj.joint_names = self.joint_names
        point = JointTrajectoryPoint()
        print(self.joint_positions)
        new_positions = self.joint_positions.copy()
        point.positions = new_positions #takes in a join posotopns 
        point.velocities = [0.0]*6
        point.time_from_start.sec = 5
        traj.points.append(point)
        self.pub.publish(traj)
        


def main(args=None):
    rclpy.init(args=args)
    node = KeyboardController()

    try:
        rclpy.spin_once(node)
    except KeyboardInterrupt:
        node.running = False
        print("\nExiting keyboard controller...")
    finally:
        node.destroy_node()
        rclpy.shutdown()          
        

if __name__ == "__main__":
    main()
