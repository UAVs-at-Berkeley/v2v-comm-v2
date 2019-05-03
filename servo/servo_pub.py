#!/usr/bin/env python
'''
A script for actuating a small hobby servo using the GPIO pins on a raspberry pi
which subscribes to a ROS topic for actuation commands.

TODO: this is untested! - Trey

'''
import rospy
from std_msgs.msg import Float32

import RPi.GPIO as GPIO
import time

DUTY_MAX = 12.5
DUTY_MIN = 2.5

DUTY_CENTER = (DUTY_MIN + DUTY_MAX)/2

servo_pin = 12 # physical pin number of RPi

# setup the GPIO pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_pin, GPIO.OUT)

p = GPIO.PWM(servo_pin, 50) # start PWM output on the servo pin at 50Hz
p.start(DUTY_CENTER) # center the servo on initialization

def callback(data):
    duty_cycle_cmd = data.data

    # debug output
    rospy.loginfo("commanding servo to " + duty_cycle_cmd + "\% duty cycle")

    p.ChangeDutyCycle(duty_cycle_cmd)
    
def listener():
    rospy.init_node('servo_listener', anonymous=True)

    # calls the call back every time a message is published to the "claw" topic
    rospy.Subscriber("claw", Float32, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
