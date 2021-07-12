import RPi.GPIO as GPIO
import time
import os
import numpy as np

# import the stepper library
from RpiMotorLib import RpiMotorLib

# import Satellite libraries
from skyfield.api import load, wgs84
from datetime import datetime
#import pandas as pd
from tracking import getTimescale, saveLocation, loadLocation, satLocation


GpioPins = [18, 23, 24, 25]

# Declare an named instance of class pass a name and motor type
az_mot = RpiMotorLib.BYJMotor("Azimuth", "28BYJ")

# loading the latest TLE data
stations_url = 'http://celestrak.com/NORAD/elements/stations.txt'
satellites = load.tle_file(stations_url)
print('Loaded', len(satellites), 'satellites')

# Defining which satellite to track
by_name = {sat.name: sat for sat in satellites}
satellite = by_name['ISS (ZARYA)']
print(satellite)

# getting the current time and calculating it in the timescale
ts = load.timescale()
t1 = getTimescale(ts, datetime.utcnow())

if os.path.exists('location.csv'):
	print("Loading data from location file")
	location = loadLocation()
else:
	print("No location file found \n Enter new data")
	name = input("Name of the location? ")
	lat = input("Latitude of your location? ")
	lon = input("Longitude of your location? ")
	elv = input("What is the elevation of your location? ")
	saveLocation(name, lat, lon, elv)
	location = loadLocation()
print("Current Location is:")
print(location)

# initializing motor angles
az_mot_ang = 0
alt_mot_ang = 0

# Definging function to drive to specific angle
def driveAz(motor, pins, des_ang, cur_ang):
	req_steps = (des_ang - cur_ang) * 1.4222
	motor.motor_run(pins, 0.005, req_steps, False, False, "half", 0.05)
	cur_ang = des_ang
	
	return cur_ang

while True:
	#we get the current time in the approriate timescale
	t1 = getTimescale(ts, datetime.utcnow())
	#we get the satellites location
	alt, az, height = satLocation(satellite, location, t1)

	# Printing the satellites location
	print('Altitude:', alt)
	print('Azimuth:', az)
	print('Height: {:.1f} km'.format(height.km))
	print("Azimuth motor angle:" ,az_mot_ang)

	# Driving the motors to the desired angle
	az_mot_ang = driveAz(az_mot, GpioPins, az, az_mot_ang)

	# Waiting 1 second before repeating and clearing the screen
	time.sleep(1)
	os.system('clear')



# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()