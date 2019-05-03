#!usr/bin/env python

'''
A node which listens to the pose of the vehicle published by the Aruco board tracking system,
implements a position controller for the vehicle, and publishes control setpoints to the rosflight /command
topic.

Inputs to the PID position controller:
	- (x, y, z) position setpoint, user defined.
	- (x, y, z) current position estimate from vision
Outputs of the PID position controller:
	- (pitch, roll, yaw) commands published to /command

Note the attitude commands outputted from the position controller are inputs to the rosflight attitude controller,
which is assumed to track its command perfectly and instantaneously.
'''

import rospy
import numpy as np
import std_msgs.msg # for Header in the stamped point
from geometry_msgs.msg import Point, Quaternion, Pose, PoseStamped, PointStamped # stamped msgs include a header

def controller(quadPose):
    # decompose the quadPose PoseStamped message
    pose = quadPose.pose

    pos = pose.position # the position of the vehicle
    quats = pose.orientation # the quaternion orientation of the vehicle

    # TODO: PIDs would go here maybe?
    pos_setpoint = [0, 0, 0]

    kp = 1;
    ki = 1;
    kd = 1;

    # just implemented p-control on each axis for now
    angle_x = kp*(pos[0] - pos_setpoint[0])
    angle_y = kp*(pos[1] - pos_setpoint[1])
    angle_z = kp*(pos[2] - pos_setpoint[2])

    rospy.loginfo("X: " + angle_x)
    
def listener():
    rospy.init_node('position_controller', anonymous=True)

    # subscribe to the cam pose topic and call the controller function as a callback
    rospy.Subscriber('cam_pose', PoseStamped, controller)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
