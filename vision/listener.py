#!usr/bin/env/python

import rospy
from std_msgs.msg import String

DEBUG = 1

def callback(data):
    if DEBUG:
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", eval(data.data)[0])
    #TODO: This should retrieve the data and determine how close this drone is to 
    # the other drone that sent the message. 
    # It may make more sense to move this file to the directory we put the flight
    # controller code

def listener():
    rospy.init_node('listener 1')
    rospy.Subscriber('chatter', string, callback)

    # continue execution until node is explicitly stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

