'''
Generate an aruco board in the 4x4_50 dictionary
and save to a directory, which will throw and error if the
directory already exists
'''

import numpy as np
import cv2
import cv2.aruco as aruco
import os

# Create a board of ROWS x COLS dimensions
ROWS = 7
COLS = 5

# create a directory to fill with the markers
dirname = "boards"
os.mkdir(dirname)

aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

# all measurements are in centimeters
markerLength = 40 # edge lengths
markerSeparation = 8 # how far two neighboring tags are
board = aruco.GridBoard_create(ROWS, COLS, markerLength, markerSeparation, aruco_dict)

# draw the board
output_size = (600, 500) # in pixels
img = board.draw(output_size)
cv2.imwrite(os.path.join(dirname, "4x4_board.png"), img)
