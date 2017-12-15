# JeVois--Python-Tracking
Python Scripting to read Jevois XY and transmit over Mavling Precision_Landing Messages

This is a set of scripts to control an ArduPilot based quadcopter to track Aruco Codes using JeVois smart camera

JeVois.py: Reads Jevois serial x-y signal from  serial.Serial(port='/dev/ttyAMA0',baudrate=9600, timeout = 0.2) and outputs as Found, X , Y and Tag Code (The balloon reference to the opentracker code, where it has been copied)

Precision_Landing_Jevois.py: Take the x-y coordinates, calibrate and adjust gain and transmit to vehicle = connect('/dev/ttyUSB0', baud = 57600), using a USB-Serial FDTI converter.

On the Flight controler, you need to read mavlink message @ 57600 bauds and have precision_landing enabled http://ardupilot.org/copter/docs/precision-landing-with-irlock.html

On the Jevois , you need to configure https://github.com/patrickpoirier51/JeVois--Python-Tracking/blob/master/initscript.cfg#L21
Add the associated video mapping https://github.com/patrickpoirier51/JeVois--Python-Tracking/blob/master/videomappings.cfg#L281

You need to power the camera with 5V Min 3Amps on a Mini-Usb Connector
Read the signal using the JST connector (Ground - Tx Data)


