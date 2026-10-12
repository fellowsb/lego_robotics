# =============================================================================
# CHALLENGE 3: STOP BEFORE YOU CRASH
# Drive toward a model and stop about 50 mm away from it.
# Cookbook sections: 2 (stop for an obstacle), 3 (read sensors)
#
# Step 1: run read_sensors() once (remove the # below) and point the robot at a
#         model. Write down the distance readings.
# Step 2: put the # back, then run stop_for_obstacle().
# =============================================================================

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.parameters import Direction, Port, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# --- Setup: change ports and measurements to match your robot ---
hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.X)
left_wheel = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.E)
dist_sensor = UltrasonicSensor(Port.C)
base = DriveBase(left_wheel, right_wheel, 57, 134.5)
base.use_gyro(True)


def read_sensors():
    while True:     # press the hub button to stop the program
        print("distance:", dist_sensor.distance(), "mm")
        wait(200)


def stop_for_obstacle():
    base.straight(1000, wait=False)     # change 1000 to fit the mat

    while not base.done():
        if dist_sensor.distance() < 50:     # stop when closer than 50 mm
            base.stop()
            break
        wait(10)

    print("Stopped. Distance to object:", dist_sensor.distance(), "mm")
    hub.display.text("STOP")


# read_sensors()
stop_for_obstacle()

# TRY IT: run it from three different starting spots. It should stop in about
#         the same place each time.
# BONUS:  change 50 to a different number. How close can you get safely?
