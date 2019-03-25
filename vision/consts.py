import cv2.aruco as aruco

ROWS = 7
COLS = 5
markerLength = 40
markerSeparation = 8
output_size = (600, 500)
aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
