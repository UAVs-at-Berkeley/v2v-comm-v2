#!usr/bin/env python

import numpy as np
import cv2
import cv2.aruco as aruco
import glob
import extract_calibration
import rospy
from std_msgs.msg import String

DEBUG = 1

def talker():
    # initialize ros publisher node
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker 1')
    rate = rospy.Rate(10)

    # initialize video capture
    cap = cv2.VideoCapture(0)

    # get existing calibration data for pose estimation
    mtx = extract_calibration.camera_matrix
    dist = extrac_calibration.dist_matrix
    
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
        parameters = aruco.DetectorParameters_create()

        # lists of corners and ids belonging to each tag
        corners, ids, _ = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

        if np.all(ids != None):
            # estimate pose of each marker 
            rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners[0], 0.05, mtx, dist)
            # drone should report the id(s) it sees and its pose
            info = [ids, corners, rvec, tvec]
            if DEBUG:
                rospy.loginfo(str(ids))
            pub.publish(str(info)) # listener should use eval(info) to convert back to a list
        rate.sleep()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
        
