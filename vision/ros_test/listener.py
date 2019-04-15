#!usr/bin/env/python

'''
a test script which prints out the information published to the chatter topic
'''

import rospy
from std_msgs.msg import String

DEBUG = 1

def callback(data):
    if DEBUG:
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    #TODO: This should retrieve the data and determine how close this drone is to 
    # the other drone that sent the message. 
    # It may make more sense to move this file to the directory we put the flight
    # controller code

def listener():
    rospy.init_node('listener_1')
    rospy.Subscriber('chatter', String, callback)

    # continue execution until node is explicitly stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

