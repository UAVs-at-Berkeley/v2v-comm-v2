#!usr/bin/env python

'''
A listener that retrieves the image stream from board_publish.py.

TODO: This script is currently erroring out without displaying any images
'''

import rospy
import numpy as np
import std_msgs.msg
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

DEBUG = False

bridge = CvBridge()

# callback function for converting ROS imgmsg to CV2 matrix
def retrieveImage(imgmsg):
    try:
        mat = bridge.imgmsg_to_cv2(imgmsg, "bgr8")
        
        if DEBUG:
            print("Matrix: ")
            rospy.loginfo(mat)
        
        cv2.imshow("Image stream", mat)

    except CvBridgeError as e:
        print(e)
        rospy.loginfo(e)

def listener():
    # subscribe to the image stream topic and call retrieveImage function as a callback
    rospy.init_node('cam_stream_listener', anonymous=True)

    rospy.Subscriber("cam_stream", Image, retrieveImage)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

