# Example import statements.  
# May not be complete depending on the exact feature that you are looking for.
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu

# initialize the Hub.  If using the Gyro, ensure that the top and front axis are
# properly defined.
hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.X)

# This is where we define menu options.  Extend with additional numbers to add
# new mission sets.  Letters like 'A' are also allowed.
program = hub_menu("1", "2")

# Define any motors.  Define both the wheel motors and any attachments.
# Define what will be considered the positive direction of travel.
# In complex configurations it is possible to define the attached gear ratios
left_wheel = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.E)

# Define any sensors that are to be used.
sensor = UltrasonicSensor(Port.C)

# For most wheeled robots, a DriveBase will be used.  DriveBase opens up a
# number of helper functions for navigation.
# The definition requires motor definitions for the wheels, the wheel diameter
# and the width between the driven wheels.
base = DriveBase(left_wheel, right_wheel, 57, 134.5)
base_settings = base.settings()
print("Current DriveBase Settings\n" +
"-----------------\n" +
f"Straight speed: {base_settings[0]} mm/s\n" +
f"Straight acceleration: {base_settings[1]} mm/s^2\n" +
f"Turn rate: {base_settings[2]} deg/sec\n" +
f"Turn acceleration: {base_settings[3]} deg/sec^2\n")

# How to initialize different programs
if program == "1":
    # Program 1 here
elif program == "2":
    # Program 2 here

# Battery voltage
print(str(hub.battery.voltage()/1000), " Volts")
    
# Navigation with the DriveBase
# It is possible to turn the use of the gyro on and off
base.use_gyro(True)

# Drive straight.  By default wait=True which means that the driving action will
# complete before going to the next command.  If wait=False, then the program will
# start driving and go immediately to the next command.
base.straight(100, wait=True)

# To monitor a sensor while driving.
base.straight(100, wait=False)

while base.done() == False: # this command states that as long as the last base
                            # action is not done, loop throught the following commands
    if sensor.distance() < 100:
        base.stop()  # stop driving
        break   # stop executing the loop and go to the next command

# to pivot turn the robot base
base.turn(180)  # positive degrees to the right, negative degrees to the left

# to arc turn (curve) the robot base. The first number is the radius of the turn
base.arc(10, angle=90, wait=True)


# continuously print a sensor value to the console/terminal
while(True):
    print(sensor.distance())
    wait(200) # pause the program for a number of milliseconds
    
# move a single motor.  Use these for attachments for instance.  There are 
# many other functions.
left_wheel.hold() # stop and hold
left_wheel.stop() # stop and spin freely
left_wheel.run_angle(speed=180, rotation_angle=720, wait=True) # speed is deg/s
d = left_wheel.done() # check if an ongoing command is done
left_wheel.close() # Closes the motor object so you can call Motor again to initialize a new object.
                    #This allows advanced users to change properties such as gearing in the middle of the program, which can be useful for removeable attachments.

c = left_wheel.control.limits() # set maximum speed , acceleration, and torque