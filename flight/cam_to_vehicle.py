#!usr/bin/env python

'''
subscribe to the pose of the camera attached to the vehicle and transform
it to the vehicle frame and publish the vehicle pose estimate
'''

import numpy as np
import rospy
import tf.transformations as tfs # for rotation matrix <> quaternions
import std_msgs.msg # for Header in the stamped point
from geometry_msgs.msg import Point, Quaternion, Pose, PoseStamped, PointStamped # stamped msgs include a header

# setup ros node and publisher
rospy.init_node('transform', anonymous=True)
pose_pub = rospy.Publisher('vehicle_pose', PoseStamped, queue_size = 10)


def transform(camPose):
	# transform the camera pose to the vehicle pose and publish

	# TODO: perform the transform here
	campose = camPose.pose # strip off the header

	cam_pos = campose.position
	cam_quats = campose.orientation

	# convert cam_quats into rotation matrix

	# for now just doing the rotation so that the axis are correct
	# and ignore the translation between camera center and vehicle CoM
	# transformation is 180 deg about the camera x-axis, look up this rotation matrix
	# R = [[1, 0, 0], [0, -1, 0], [0, 0, 1]]

	# the homogeneous transformation matrix is
	T = [[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

	# decompose the PoseStamped into rotation matrix for transforming

	# TODO: publish the new vehicle pose
	pose_pub.publish(header, pose)

def listener():
    rospy.init_node('transform')
	rospy.Subscriber('cam_pose', PoseStamped, transform)

    # continue execution until node is explicitly stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

