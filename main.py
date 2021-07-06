import RPi.GPIO as GPIO
import time


# import the stepper library
from RpiMotorLib import RpiMotorLib

# import Satellite libraries
from skyfield.api import load, wgs84
from datetime import datetime
from tracking import getTimescale

GpioPins = [18, 23, 24, 25]

# Declare an named instance of class pass a name and motor type
mymotortest = RpiMotorLib.BYJMotor("Azimuth", "28BYJ")

#loading the latest TLE data
stations_url = 'http://celestrak.com/NORAD/elements/stations.txt'
satellites = load.tle_file(stations_url)
print('Loaded', len(satellites), 'satellites')

# Defining which satellite to track
by_name = {sat.name: sat for sat in satellites}
satellite = by_name['ISS (ZARYA)']
print(satellite)

# getting the current time and calculating it in the timescale
ts = load.timescale()
while True:
	print(getTimescale(ts, datetime.utcnow()))
	time.sleep(1)

# call the function pass the parameters
#mymotortest.motor_run(GpioPins , 0.005, 512, False, False, "full", .05)
#mymotortest.motor_run(GpioPins , 0.005, 512, True, False, "half", .05)

# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()