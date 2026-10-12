# =============================================================================
# CHALLENGE 2: ARM RESET AND DELIVERY
# Reset the arm to a known start, then lift something and put it down.
# Cookbook section: 4 (attachment motors)
# =============================================================================

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Stop, Axis
from pybricks.tools import wait

# --- Setup: change the port to match your robot ---
hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.X)
arm = Motor(Port.A)


def deliver():
    # Run slowly until the arm hits its stop, then call that position 0.
    arm.run_until_stalled(-200, then=Stop.HOLD, duty_limit=40)
    arm.reset_angle(0)

    arm.run_target(300, 90)     # lift (find the angle that works for your arm)
    wait(500)
    arm.run_target(300, 0)      # lower


deliver()

# TRY IT: find the arm angle that works for your attachment.
#         run_target goes to a position measured from the reset.
#         run_angle goes a set amount from where the arm is now.
# BONUS:  call deliver() twice in a row. The arm should end up in the same
#         place both times, because of the reset.
