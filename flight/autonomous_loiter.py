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

This node is both a listener and a publisher, it subscribes to position information from vision and publishes 
the control output to the rosflight command topic for autonomous loitering

TODO: current requires the body and inertial frames to be roughly aligned for this controller to work!!!
'''

import rospy
import numpy as np
import std_msgs.msg # for Header in the stamped point
from geometry_msgs.msg import Point, Quaternion, Pose, PoseStamped, PointStamped # stamped msgs include a header
from rosflight_msgs.msg import Command

'''
msg = Command()
msg.header.stamp = rospy.Time.now()
msg.mode = Command.MODE_ROLL_PITCH_YAWRATE_THROTTLE
msg.ignore = Command.IGNORE_NONE
msg.x = 0.0
msg.y = 0.0
msg.z = 0.0
msg.F = 0.6
'''

DEBUG = False

# position control gains
X_P = 0.01
X_I = 0
X_D = 0

Y_P = 0.01
Y_I = 0
Y_D = 0

Z_P = 0.1
Z_I = 0
Z_D = 0

# position setpoint
POS_SETPOINT = [1.11, 1.11, 1]

# hover thrust TODO, WHAT IS THIS???
HOVER_THRUST = 0.25 
MAX_THRUST = 0.75

def deg_from_rad(rad):
    deg = (180 / np.pi)*rad

    return deg

def cmd_publish(roll_cmd, pitch_cmd, yaw_rate_cmd, thrust_cmd):
    pub = rospy.Publisher('command', Command, queue_size=10)

    # construct the rosflight command message to publish
    msg = Command()
    msg.header.stamp = rospy.Time.now()
    msg.mode = Command.MODE_ROLL_PITCH_YAWRATE_THROTTLE
    msg.ignore = Command.IGNORE_NONE
    msg.x = roll_cmd
    msg.y = pitch_cmd
    msg.z = yaw_rate_cmd
    msg.F = thrust_cmd

    pub.publish(msg)
       

def controller(quadPose):
    # decompose the quadPose PoseStamped message
    pose = quadPose.pose

    pos = pose.position # the position of the vehicle
    quats = pose.orientation # the quaternion orientation of the vehicle

    # TODO: implement I and D terms here...
    # compute translation PID output
    roll_cmd = Y_P*(pos.y - POS_SETPOINT[1])
    pitch_cmd = X_P*(pos.x - POS_SETPOINT[0])
    yaw_rate_cmd = 0

    # compute altitude PID output
    thrust_cmd = HOVER_THRUST - Z_P*(pos.z - POS_SETPOINT[2])
    
    if thrust_cmd > MAX_THRUST:
        # bound the maximum thrust
        thrust_cmd = MAX_THRUST

    if DEBUG:
        rospy.loginfo("Position Ctrl Outputs (deg)")
        rospy.loginfo("roll_cmd: " + str(deg_from_rad(roll_cmd)))
        rospy.loginfo("pitch_cmd: " + str(deg_from_rad(pitch_cmd)))
        rospy.loginfo("yaw_rate_cmd: " + str(deg_from_rad(yaw_rate_cmd)))
        rospy.loginfo("thrust_cmd: " + str(thrust_cmd))

    # TODO: is a try/except block here?
    cmd_publish(roll_cmd, pitch_cmd, yaw_rate_cmd, thrust_cmd)

    
def listener():
    rospy.init_node('position_controller', anonymous=True)

    # subscribe to the cam pose topic and call the controller function as a callback
    rospy.Subscriber('cam_pose', PoseStamped, controller)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()

