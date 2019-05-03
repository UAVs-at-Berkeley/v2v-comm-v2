#!/usr/bin/env python
'''
A ROS node for publishing duty cycle commands to the "claw" topic for actuating
the servo driven claw on the v2v quadcopters. User is prompted for a new command which is
immediately published to the "claw"t opic

TODO: this is untested! - Trey
'''
import rospy
from std_msgs.msg import Float32

def talker():
    pub = rospy.Publisher('claw', Float32, queue_size=10)
    rospy.init_node('servo_pub', anonymous=True)

    while not rospy.is_shutdown():
        # get user input for the new duty cycle command
        new_cmd = float(input("new servo duty cycle? "))
        pub.publish(new_cmd)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass