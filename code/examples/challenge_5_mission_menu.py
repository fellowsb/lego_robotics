# =============================================================================
# CHALLENGE 5: MISSION MENU AND TIMER
# Combine your earlier challenges into missions and pick one from the hub.
# Cookbook sections: 10 (mission functions and menu), 8 (hub features)
#
# leave_base() and deliver() are copied from challenges 1 and 2 so this file
# runs on its own. Replace them with your own improved versions.
# =============================================================================

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Color, Direction, Port, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu

# --- Setup: change ports and measurements to match your robot ---
hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.X)
left_wheel = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.E)
arm = Motor(Port.A)
base = DriveBase(left_wheel, right_wheel, 57, 134.5)
base.use_gyro(True)


def leave_base():
    hub.light.on(Color.GREEN)
    base.straight(400)
    base.turn(90)
    base.straight(200)
    base.straight(-200)
    base.turn(-90)
    base.straight(-400)
    hub.speaker.beep(800, 200)


def deliver():
    arm.run_until_stalled(-200, then=Stop.HOLD, duty_limit=40)
    arm.reset_angle(0)
    arm.run_target(300, 90)
    wait(500)
    arm.run_target(300, 0)


# One function per mission keeps things tidy.
def mission_a():
    leave_base()


def mission_b():
    deliver()


# The program starts doing things from here down.
timer = StopWatch()

# Press LEFT/RIGHT on the hub to scroll, CENTER to choose.
program = hub_menu("A", "B", "C")

if program == "A":
    mission_a()
elif program == "B":
    mission_b()
elif program == "C":
    mission_a()     # a choice can run several missions in a row
    mission_b()

print("Run time:", timer.time() / 1000, "s")

# TRY IT: run all three menu choices.
# BONUS:  add a fourth choice "D" for the line challenge:
#           1. add "D" to hub_menu(...)
#           2. copy drive_to_line() and find_line() from challenge 4 above
#              the menu, plus a ColorSensor and its import
#           3. add  elif program == "D":  find_line()
