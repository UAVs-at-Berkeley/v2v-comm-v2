'''
all measurements are in centimeters
'''

import cv2.aruco as aruco

# ROWS = 10
# COLS = 5
# markerLength = 40
# markerSeparation = 8
# output_size = (1200, 1000)
# aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

ROWS = 8
COLS = 5
markerLength = 2.5
markerSeparation = 1.5
output_size = (1200, 1000)
aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
