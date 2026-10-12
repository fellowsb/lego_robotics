# =============================================================================
# CHALLENGE 1: LEAVE BASE
# Drive from base to a mission model, turn to face it, and come back home.
# Cookbook sections: 1 (driving and turning), 8 (hub features)
# =============================================================================

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Color, Direction, Port, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# --- Setup: change ports and measurements to match your robot ---
hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.X)
left_wheel = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.E)
base = DriveBase(left_wheel, right_wheel, 57, 134.5)
base.use_gyro(True)


def leave_base():
    hub.light.on(Color.GREEN)
    base.straight(400)      # measure the real distance on the mat
    base.turn(90)           # positive = right, negative = left
    base.straight(200)
    base.straight(-200)     # backing up is a negative number
    base.turn(-90)
    base.straight(-400)
    hub.speaker.beep(800, 200)


leave_base()

# TRY IT: change the numbers until the robot ends up back in the same spot
#         every time.
# BONUS:  use a for loop to do the whole trip 3 times:
#             for _ in range(3):
#                 leave_base()
