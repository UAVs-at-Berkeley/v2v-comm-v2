'''
all measurements are in meters, output size in pixels
'''

import cv2.aruco as aruco

# ROWS = 10
# COLS = 5
# markerLength = 0.40
# markerSeparation = 0.08
# output_size = (1200, 1000)
# aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

ROWS = 8
COLS = 5
markerLength = 0.025
markerSeparation = 0.015
output_size = (1200, 1000)
aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

# fill out after printing to confirm actual dimensions of the board
realMarkerLength = 0.02
realMarkerSeparation = 0.012
