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

### Copying a Raspberry Pi Image - [reference](https://raspberrypi.stackexchange.com/questions/311/how-do-i-backup-my-raspberry-pi)
After a vanilla Raspberry Pi distribution (the Ubiquity distribution with ROS Kinetic, in our case) has been installed and modified with the appropriate packages, the image can be resaved for installation on other Raspberry Pis. In Ubuntu:
1. Install GParted - a GUI partition manager for Ubuntu

   `sudo apt install gparted`

2. Shutdown the Pi and plug in its SD card into the Ubuntu machine

3. Launch GParted, find the 2 partitions of the Pi image (PI_BOOT and PI_ROOT). Whichever is listed second in the partition list will have the greatest number of "sectors". Right click on the partition and hit `information`, and copy the "last sector" number which determines the total number of bytes to copy into the resultant .img file.

4. Run `dd` to copy the files (for the SD card mounted at `/dev/sdc` and a last sector of `31116287`):

   `sudo dd if=/dev/sdc of=pi.img bs=512 count=31116287`

**Note:** Using `dd` as described copies all the contents of the SD card (including free space), so the image file created will be as many gigabytes as the SD card has storage for. This should be avoidable (TODO). 
