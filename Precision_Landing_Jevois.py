#!/usr/bin/env python2
import math
import numpy as np
from dronekit import connect, VehicleMode, LocationGlobal, LocationGlobalRelative
from pymavlink import mavutil
from JeVois import JeVois

#camera
horizontal_fov = 70.2 * math.pi/180
vertical_fov = 43.3 * math.pi/180
horizontal_resolution = 320
vertical_resolution = 240

#Real Time Moving Average of the TAG ID
readings = np.array([])
z = 17
max_samples = 4
Ratio = 13  # This is the ratio of the Aruco Tags ID to switch Tracking 
x=0
y=0

vehicle = connect('/dev/ttyUSB0', baud = 57600)
#vehicle = connect('tcp:192.168.2.18:5763',wait_ready=True)
#vehicle = connect('udp:0.0.0.0:14550' ,wait_ready=True)


# Define function to send landing_target mavlink message for mavlink based precision landing
# http://mavlink.org/messages/common#LANDING_TARGET
def send_land_message(x,y,z):
    msg = vehicle.message_factory.landing_target_encode(
        0,          # time since system boot, not used
        0,          # target num, not used
        mavutil.mavlink.MAV_FRAME_BODY_NED, # frame, not used
        (x-horizontal_resolution/2)*horizontal_fov/horizontal_resolution,
        (y-vertical_resolution/2)*vertical_fov/vertical_resolution,
        z,          # distance, in meters
        0,          # Target x-axis size, in radians
        0           # Target y-axis size, in radians
    )


    vehicle.send_mavlink(msg)
    vehicle.flush()

while(1):
    found, h, v, z = JeVois.balloon_xysize()
    if not found == 0:

        readings = np.append(readings, z)
        avg = np.mean(readings)
        #print 'current average =', avg
        #print 'readings used for average:', readings
        
        if len(readings) == max_samples:
            readings = np.delete(readings, 0)

        if (avg > Ratio) and (z == 17):
            x = int(h+1650)/10
            y = int(v+750)/6
            #print z,x,y
            send_land_message(x,y,z)

        if (avg <= Ratio) and (z == 8):
            x = int(h+1650)/10
            y = int(v+750)/6
            #print z, x,y
            send_land_message(x,y,z)

        
    else:
        pass
    
    

