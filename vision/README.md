# v2v-comm Vision

This repository contains python scripts for camera calibration as well as the creation, detection, and pose estimation of aruco tags and aruco grid boards.

Some scripts integrate with ROS to publish pose information.

### Camera Calibration

It is necessary to determine the camera intrinsic and extrinsic parameters using a calibration in order to properly transform camera plane information into world coordinates. This must be done for each camera individually.

1. Print the 9x6 vertex checkerboard called `checkboard.png` in the calibration directory.

2. Take 10 or more images of the checkerboard in different positions and orientations with the camera that you are calibrating and put them in the `calibration/calib_images` directory.

3. Switch to the calibration directory `cd calibration` then run the calibration script 

   `python calibration/camera_calib.py` 

   which detects the vertices of the checkerboard and determines the camera calibration parameters and writes them to a YAML file called `calibration.yaml` for later access.

### Creating Markers

The `create_markers` directory contains code for generating individual aruco tags as well as aruco grid boards.

#### Creating Aruco Tags

Aruco tags are organized into dictionaries based on their size (the number of bits needed to store their codification), as well as how many unique markers exist in that dictionary. We do not require a high number of markers so we use the `aruco.DICT_4X4_50`, a dictionary of 50 unique markers with 4x4 squares inside the border which identify the marker. There are other dictionaries (example `DICT_6X6_250` a collection of 250 markers with 6x6 squares inside the border).

1. To generate images of the markers for printing out, run `python create_marker.py`. This will create a directory called `markers` which contains every member of the 50 marker dictionary.

   **Note:** The script will error out if there is already a `markers` directory on the same level as the script, so delete the existing `markers` directory to regenerate if you need to.

#### Creating Aruco Grid Boards

From  [OpenCV](<https://docs.opencv.org/3.4.2/db/da9/tutorial_aruco_board_detection.html>):

"The difference between a Board and a set of independent markers is that the relative position between the markers in the Board is known a priori. This allows that the corners of all the markers can be used for estimating the pose of the camera respect to the whole Board. The benefits of boards are:

- The pose estimation is much more versatile. Only some markers are necessary to perform pose estimation. Thus, the pose can be calculated even in the presence of occlusions or partial views.
- The obtained pose is usually more accurate since a higher amount of point correspondences (marker corners) are employed."

1. To generate a board, first specify the parameters of the board's geometry in the helper script called `consts.py`.

2. Then run `python create_board.py` which will create an image of an aruco board in a directory called `boards`. 

   **Note:** Again, this script will fail if a directory called `boards` already exists.

   **Note:** Be sure the number of tags in the board you are creating does not exceed the number of aruco markers in the directory you've chosen.

