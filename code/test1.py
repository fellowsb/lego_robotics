from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu

hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.X)

program = hub_menu("1", "2")

left_wheel = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.E)

sensor = UltrasonicSensor(Port.C)

base = DriveBase(left_wheel, right_wheel, 57, 134.5)

if program == "1":
    print(str(hub.battery.voltage()/1000), " Volts")
    
    base.use_gyro(True)

    base.straight(6767, wait=False)

    while base.done() == False:
        if sensor.distance() < 100:
            base.stop()

    wait(1000)

    base.turn(-180)
    base.straight(100)

elif program == "2":
    while(True):
        print(sensor.distance())
        wait(200)
    
