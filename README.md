# V2V-Comm Spring 2019

### Local Install Instructions

This project makes use of ROS which is primarily available in Linux, if you're not running Linux, you'll have to install a virtual machine:

1. **VirtualBox** is a free VM manager distributed by Oracle. Download it for your machine [here](https://www.virtualbox.org/wiki/Downloads). Also install the VirtualBox Extension Pack which allows for interfacing USB devices (like flight controllers) through the VM.

2. Download an .iso for **Ubuntu 16.04 LTS** [here](http://releases.ubuntu.com/16.04/). Pick the 64-bit or 32-bit desktop image depending on your machine architecture.

3. Next create a virtual machine using VirtualBox and the Ubuntu .iso file you downloaded.

4. Once your Linux VM is working, you can run through the **ROS** install instructions found [here](http://wiki.ros.org/kinetic/Installation/Ubuntu). We'll be installing ROS Kinetic.

5. Now we can install **rosflight**, its the ROS stack and flight firmware we'll use for the project. It's install documentation is [here](http://docs.rosflight.org/en/latest/user-guide/ros-setup/).

6. Now you can pip install **OpenCV** in the virtual machine, instructions [here](https://www.pyimagesearch.com/2018/09/19/pip-install-opencv/). We'll be using python3. If you're just installing OpenCV in the virtual machine then you can just install it to the root python version with:

   ​	`pip install opencv-python` 

   ​	`pip install opencv-contrib-python`

### Install the Custom v2v Raspberry Pi Image

1. This Raspberry pi image is based off the Ubiquity Robotics distribution of Ubuntu 16.04 for Raspberry Pi 3s. Download the zipped image file from our Google Drive (TODO: link here), it is not necessary to unzip it.
2. Download Etcher, a GUI image flashing tool (TODO: link here)
3. Plug the SD card into your computer and flash the device using Etcher, be sure to select the correct storage device and zipped image file.

**After flashing the custom image to the pi's SD card and booting for the first time:**

1. The pi should boot up in access point mode with a network called `black_piXXXX` with `XXXX` part of the MAC address of the device. Connect to the access point's wireless network:

```
SSID: black_piXXXX
Pass: robotseverywhere
```

2. ssh into the pi with `ssh ubuntu@10.42.0.1`, the password is `ubuntu`.
3. Now we'll change the hostname of this pi to reflect the vehicle this device belongs to. We'll use Ubiquity's `pifi` networking utility to set the hostname. `sudo pifi set-hostname "white_pi"` for the white v2v vehicle for example.
4. Then disable the access point and connect the pi to a network for usage with ROS. Run `sudo pifi add "SSID" "PASSWORD"`. In the UAV lab the v2v project uses its own network/router:

```
sudo pifi add "8 Via Robotics" "rosrouter"
```

4. Then reboot with `sudo reboot now` in order for changes to take place. Disconnect from the pi's wifi access point and reconnect to the proper network (8 Via Robotics in the case of the v2v project).
5. Find the pi's new IP address on this network (by accessing the router's administration page for example) and ssh back into it to test ros is working.
6. To test that ros is working properly try running `roscore`. If it comes up with network related errors try reseting the following environment variables:

**ROS Network Setup**

```
export ROS_HOSTNAME=localhost
export ROS_MASTER_URI=http://localhost:11311
```

Now try again: `roscore`

If `roscore` runs without issue you're ready to start testing some v2v code!

```
More Pi Image Notes:

custom pi image: [here](https://drive.google.com/file/d/1tmHx_Uq52bamYr-GzQjtTrJsXn3OgjC3/view?usp=sharing).

in case ssh-ing into the pi gives you trouble the first time:

`ssh-keygen -R 10.42.0.1`

before connecting to a network you have to change the hostname on the pi:

`sudo set-hostname "red_pi"`

then ssh with:

`ssh red_pi@10.42.0.1`

to enable the camera module

`sudo raspi-config > interfacing options > Camera`

now reboot `sudo reboot now`

to test that the camera is supported and detected

`vcgencmd get_camera`

should report: `supported=1 detected=1`

for a test picture which will save to the home directory after a short preview:

`raspistill -o output.jpg`

to set the hostname to be unique after installing the custom image: `sudo pifi set-hostname <hostname>`
example: `red_pi, back_pi, white_pi` for the three v2v quadcopters
```

### X4R Firmware Flashing
ROSflight currently only supports PPM input from the receiver, and FrSky X4R receivers do not support PPM output from the factory. FrSky has made a firmware available that adds this capability (available in ```firmwares/non-EU-X4R-PPM```). [Oscar Liang](https://oscarliang.com/flash-frsky-rx-firmware/) has a good article on how to the flash the receiver through the Smart Port from a Taranis. [This](https://quadmeup.com/ppm-output-on-frsky-x4r-and-x4r-sb-receivers/) article is specific to getting PPM out of an X4R and walks through tricks in the binding process.

### Raspberry 3 Image
An Ubuntu 16.04 image with ROS Kinetic pre-installed is maintained by Ubiquity Robotics. It is available for download [here](https://downloads.ubiquityrobotics.com/pi.html).

The micro SD card (I used a 32GB SanDisk) can be formatted with ```gnome-disk-utility``` as recommended by Ubiquity, or Etcher.

The image will default to the Pi as an access point so it can be easily connected to. Information on setting the Pi's wifi configuration can be found [here](https://learn.ubiquityrobotics.com/connect_network) (it's different on Ubiquity's image than vanilla images).

#### Adjustments to Ubiquity Robotics Image

* First use Ubiquity's `pifi` wifi configuration tool to connect the pi to a network *with* Internet access: `sudo pifi add "MyNetwork" "password"`.
* install rosflight with `sudo apt install ros-kinetic-rosflight-pkgs` and run `sudo apt update` and `sudo apt upgrade`.
* Then use pifi to connect to the network you plan on using the robot with.

* Run `sudo systemctl disable magni-base.service` to disable Ubiquity's services for their robot since we'll be using our own hardware.
* Run `sudo systemctl disable roscore.service` to avoid `roscore` starting at startup on its own.

### Install the Custom v2v Raspberry Pi Image
1. This Raspberry pi image is based off the Ubiquity Robotics distribution of Ubuntu 16.04 for Raspberry Pi 3s. Download the zipped image file from our Google Drive (TODO: link here), it is not necessary to unzip it.

2. Download Etcher, a GUI image flashing tool (TODO: link here)

3. Plug the SD card into your computer and flash the device using Etcher, be sure to select the correct storage device and zipped image file.
