# V2V-Comm Spring 2019

### Install Instructions

This project makes use of ROS which is primarily available in Linux, if you're not running Linux, you'll have to install a virtual machine:

1. **VirtualBox** is a free VM manager distributed by Oracle. Download it for your machine [here](https://www.virtualbox.org/wiki/Downloads). Also install the VirtualBox Extension Pack which allows for interfacing USB devices (like flight controllers) through the VM.

2. Download an .iso for **Ubuntu 16.04 LTS** [here](http://releases.ubuntu.com/16.04/). Pick the 64-bit or 32-bit desktop image depending on your machine architecture.

3. Next create a virtual machine using VirtualBox and the Ubuntu .iso file you downloaded.

4. Once your Linux VM is working, you can run through the **ROS** install instructions found [here](http://wiki.ros.org/kinetic/Installation/Ubuntu). We'll be installing ROS Kinetic.

5. Now we can install **rosflight**, its the ROS stack and flight firmware we'll use for the project. It's install documentation is [here](http://docs.rosflight.org/en/latest/user-guide/ros-setup/).

6. Now you can pip install **OpenCV** in the virtual machine, instructions [here](https://www.pyimagesearch.com/2018/09/19/pip-install-opencv/). We'll be using python3. If you're just installing OpenCV in the virtual machine then you can just install it to the root python version with:

   ​	`pip install opencv-python` 

   ​	`pip install opencv-contrib-python`

