# =============================================================================
# CHALLENGE 4: FIND THE LINE
# Drive until the robot finds a dark line on the mat, beep, then do a short move.
# Cookbook sections: 5 (find the line threshold), 6 (drive to a line)
#
# Step 1: run read_reflection() once (remove the # below). Hold the sensor over
#         the mat, then over the line, and write down both numbers.
# Step 2: add the two numbers and divide by 2. That is your threshold.
# Step 3: put the # back, type your threshold into find_line(), and run it.
# =============================================================================

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# --- Setup: change ports and measurements to match your robot ---
hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.X)
left_wheel = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.E)
color_sensor = ColorSensor(Port.D)
base = DriveBase(left_wheel, right_wheel, 57, 134.5)
base.use_gyro(True)


def read_reflection():
    while True:     # press the hub button to stop the program
        print("reflection:", color_sensor.reflection())
        wait(100)


# Drives forward until the sensor sees dark several times in a row.
# Gives back True if it found the line, False if it did not.
def drive_to_line(threshold, max_distance=1000):
    MIN_SAMPLES = 5
    dark_samples = 0

    base.straight(max_distance, wait=False)

    while not base.done():
        if color_sensor.reflection() < threshold:
            dark_samples = dark_samples + 1
        else:
            dark_samples = 0

        if dark_samples >= MIN_SAMPLES:
            base.stop()
            return True

        wait(10)

    base.stop()
    return False


def find_line():
    threshold = 40          # use YOUR number from step 2
    base.settings(straight_speed=100)

    found = drive_to_line(threshold, 600)
    if found:
        hub.speaker.beep(800, 100)
        base.straight(100)
    else:
        print("Line not found!")
        hub.speaker.beep(200, 500)      # low, long beep means a problem


# read_reflection()
find_line()

# TRY IT: start the robot a bit crooked. It should still stop at the line in
#         the same place.
# BONUS:  run it off the mat or hold a hand over the sensor. It should give
#         the low beep.
