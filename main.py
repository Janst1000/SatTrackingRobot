import RPi.GPIO as GPIO

# import the library
from RpiMotorLib import RpiMotorLib

GpioPins = [18, 23, 24, 25]

# Declare an named instance of class pass a name and motor type
mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")

# call the function pass the parameters
mymotortest.motor_run(GpioPins , 0.005, 512, False, False, "full", .05)
mymotortest.motor_run(GpioPins , 0.005, 512, True, False, "half", .05)

# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()