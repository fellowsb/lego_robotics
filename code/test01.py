from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, ColorLightMatrix,UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

#define left and right motor variable
left_motor = Motor(Port.B,Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F,Direction.CLOCKWISE)

#define the robot with wheel and axle track
robot = DriveBase(left_motor,right_motor,wheel_diameter=56,axle_track=100)


robot.straight(200)
wait(200)
robot.straight(-200)



"""
hub = PrimeHub()
sensor = UltrasonicSensor(Port.E)


hub.light.on(Color.GREEN)
wait(2000)

while True:
    detect_distance = sensor.distance()
    print (detect_distance)
    wait(500)"""

