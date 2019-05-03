'''
all measurements are in meters, output size in pixels
'''

import cv2.aruco as aruco

# test
# ROWS = 10
# COLS = 5
# markerLength = 0.40
# markerSeparation = 0.08
# output_size = (1200, 1000)
# aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

# board that is printed in the lab for small scale testing
# ROWS = 8
# COLS = 5
# markerLength = 0.025
# markerSeparation = 0.015
# output_size = (1200, 1000)
# aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

# full sized flight testing board
ROWS = 7
COLS = 7
markerLength = 0.1
markerSeparation = 0.086533
output_size = (5000, 5000)
aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

# fill out after printing to confirm actual dimensions of the board
realMarkerLength = 0.02
realMarkerSeparation = 0.012
