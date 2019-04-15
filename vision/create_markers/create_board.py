'''
Generate an aruco board in the 4x4_50 dictionary
and save to a directory, which will throw and error if the
directory already exists
'''

import numpy as np
import cv2
import cv2.aruco as aruco
import os
from consts import *

# create a directory to fill with the markers
dirname = "boards"
os.mkdir(dirname)

# all measurements are in centimeters
board = aruco.GridBoard_create(ROWS, COLS, markerLength, markerSeparation, aruco_dict)

# draw the board
img = board.draw(output_size)
cv2.imwrite(os.path.join(dirname, "4x4_board.png"), img)
