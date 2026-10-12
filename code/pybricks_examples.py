# =============================================================================
# Pybricks cookbook for SPIKE Prime / Robot Inventor (PrimeHub)
#
# This file is a COOKBOOK to read, not a program to run from top to bottom.
# The sections build on each other and introduce one idea at a time, from
# simple driving up to advanced topics. Each recipe is a function: copy the
# parts you need into your own program.
#
# Contents
#   Python basics ... a quick reminder of the syntax used in this file
#   Setup ........... hub, motors, sensors, DriveBase
#   Recipes
#     1. Driving and turning          6. Drive to a line, run mission
#     2. Stop for an obstacle         7. Follow a line
#     3. Read sensors                 8. Hub features (lights, sound, buttons)
#     4. Attachment motors            9. Turn to an absolute heading
#     5. Read reflection and HSV      10. Mission functions and menu
#                                     11. ADVANCED: doing two things at once
#
# Units: distances in mm, speeds in mm/s, angles in degrees, time in ms.
# (1000 ms = 1 second)
# =============================================================================


# =============================================================================
# PYTHON BASICS - a reminder of the syntax used below
#
# Comments:   anything after a # is ignored by Python. It is a note for humans.
#
# Variables:  a name that stores a value.
#                 speed = 100
#             = means "store this value", it is NOT a math "equals".
#
# Indentation: Python uses SPACES AT THE START OF A LINE to show which lines
#             belong together. Use 4 spaces. Every line inside a function,
#             if, while or for must be indented the same amount.
#
# Functions:  a named group of commands. "def" creates it, and you run it
#             by writing its name with parentheses. The line with def ends
#             in a colon (:).
#                 def say_hello():
#                     print("Hello")
#                 say_hello()          <- this line runs it
#
# if / elif / else:  only run some lines when something is true.
#                 if distance < 100:
#                     print("close")
#                 elif distance < 300:
#                     print("medium")
#                 else:
#                     print("far")
#
# Comparing:  ==  equal to      !=  not equal to
#             <   less than     >   greater than
#             <=  less or equal >=  greater or equal
#             (use two equals signs == to compare, one = to store)
#
# Combining:  and, or, not    e.g.  if a > 5 and not b:
#
# while loop: repeat the indented lines as long as the condition is true.
#                 while True:            <- True means "forever"
#                 while not arm.done():  <- repeat until the arm is finished
#             "break" jumps out of the loop early.
#
# for loop:   repeat a set number of times.
#                 for _ in range(4):     <- runs the indented lines 4 times
#
# print():    writes text and values to the terminal in Pybricks Code.
#                 print("distance:", 42)
# f-string:   put a value inside text with {}. The text starts with f.
#                 print(f"Battery: {volts} V")
# =============================================================================


# Bring in the Pybricks code we need. Each "import" line makes tools
# available. If you use a new tool (e.g. a new type of sensor), add its name
# to the matching line.
from pybricks.hubs import PrimeHub                # the hub (brain) itself
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase           # drives both wheels together
from pybricks.tools import wait, StopWatch, hub_menu, multitask, run_task   # multitask and run_task: see section 11


# =============================================================================
# SETUP
# Everything here runs once when the program starts. Setup must come BEFORE
# the code that uses it.
# =============================================================================

# The hub. top_side / front_side tell the gyro (turning sensor) how the hub is
# mounted on the robot: which way is up and which way is forward.
hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.X)

# Motors. Port.F means the motor is plugged into port F on the hub.
# positive_direction decides which way of spinning counts as "forward".
# Wheels on opposite sides face opposite ways, so one needs to be reversed.
# If your robot drives backward, swap COUNTERCLOCKWISE for CLOCKWISE on the
# left wheel and add positive_direction=Direction.COUNTERCLOCKWISE to the
# right wheel.
# Attachment motors (arms, etc.) are defined the same way.
left_wheel = Motor(Port.F, positive_direction=Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.E)
arm = Motor(Port.A)

# Sensors. Every device needs its OWN port. Delete the lines for any sensor
# you are not using, otherwise the program stops with an error when that
# sensor is not plugged in.
dist_sensor = UltrasonicSensor(Port.C)    # measures distance to objects
color_sensor = ColorSensor(Port.D)        # measures color and brightness
force_sensor = ForceSensor(Port.B)        # a button that measures push strength

# DriveBase: lets us say "drive 200 mm" instead of spinning each motor.
# The four values are, in order:
#   left motor, right motor, wheel diameter (mm), axle track (mm)
# Axle track = distance between the centers of the two wheels' contact points.
# If the robot drives or turns too far/short, check these two measurements.
base = DriveBase(left_wheel, right_wheel, 57, 134.5)

# Use the hub's gyro to keep the robot straight and make turns accurate.
base.use_gyro(True)


def print_settings():
    # Print the drive settings and battery level (handy when tuning).
    # settings() gives back 4 numbers at once. We give each one a name so
    # they are easy to use. This is called "unpacking".
    straight_speed, straight_accel, turn_rate, turn_accel = base.settings()
    print("DriveBase settings")
    print("------------------")
    print(f"Straight speed:        {straight_speed} mm/s")
    print(f"Straight acceleration: {straight_accel} mm/s^2")
    print(f"Turn rate:             {turn_rate} deg/s")
    print(f"Turn acceleration:     {turn_accel} deg/s^2")
    # The battery reads in millivolts, so divide by 1000 to get volts.
    print(f"Battery:               {hub.battery.voltage() / 1000} V")


# =============================================================================
# 1. DRIVING AND TURNING
# =============================================================================
def drive_and_turn():
    # Optional: change how fast the robot moves. You only need to list the
    # ones you want to change:
    #   straight_speed (mm/s), straight_acceleration (mm/s^2),
    #   turn_rate (deg/s), turn_acceleration (deg/s^2)
    # Higher speed = faster but less accurate.
    base.settings(straight_speed=300, turn_rate=150)

    base.straight(200)       # drive forward 200 mm. A negative number drives backward.
    base.turn(90)            # turn on the spot. Positive = right (clockwise),
                             # negative = left.
    base.arc(200, angle=90)  # drive in a curve: radius of the circle (mm), then
                             # how many degrees around the circle to go.
                             # (older Pybricks firmware calls this base.curve)

    # By default each command finishes before the next one starts.
    # Adding wait=False starts the move and goes straight to the next line:
    #     base.straight(200, wait=False)

    # Driving a square. "for _ in range(4)" repeats the indented lines 4 times.
    # (The _ is just a name for a counter we don't need.)
    for _ in range(4):
        base.straight(200)
        base.turn(90)


# =============================================================================
# 2. STOP FOR AN OBSTACLE
# wait=False starts the move so the program can check a sensor while driving.
# =============================================================================
def stop_for_obstacle():
    base.straight(1000, wait=False)     # start driving but don't wait for it to finish

    # base.done() is True once the move has finished. "not" flips it, so this
    # loop repeats WHILE the robot is still driving.
    while not base.done():
        if dist_sensor.distance() < 100:    # distance is in mm
            base.stop()                     # stop the wheels
            break                           # leave the while loop
        wait(10)    # pause 10 ms so we don't check the sensor non-stop

    print("Stopped. Distance to object:", dist_sensor.distance(), "mm")


# =============================================================================
# 3. READ SENSORS
# Open the terminal in Pybricks Code to see the output.
# Handy for finding the numbers you need (distances, brightness, etc.).
# =============================================================================
def read_sensors():
    while True:     # repeat forever (press the hub button to stop the program)
        # The parentheses let one print() be split over several lines.
        # Text goes in quotes. The sensor commands get the current reading.
        print(
            "distance:", dist_sensor.distance(), "mm |",
            "color:", color_sensor.color(), "|",
            "reflection:", color_sensor.reflection(), "% |",
            "force:", force_sensor.force(), "N |",
            "pressed:", force_sensor.pressed(),
        )
        wait(200)   # wait 200 ms (a fifth of a second) between readings


# =============================================================================
# 4. ATTACHMENT MOTORS (arms, lifts, etc.)
# =============================================================================
def attachment_motor():
    # Find a known start position: run the arm slowly until it hits its
    # mechanical stop, then call that position 0. A negative speed spins the
    # other way. duty_limit keeps the motor gentle (a % of full power).
    # Do this at the start of every run so the arm always begins in the same place.
    arm.run_until_stalled(-200, then=Stop.HOLD, duty_limit=40)
    arm.reset_angle(0)

    # Relative move: turn by an amount from where it is now.
    # The two numbers are speed (deg/s) then angle (deg).
    arm.run_angle(300, 90)

    # Absolute move: go to a position, measured from the reset_angle(0) above.
    # The two numbers are speed (deg/s) then the target angle (deg).
    arm.run_target(300, 0)

    # Start a move without waiting, do other things, then wait for it to end.
    arm.run_angle(300, 120, wait=False)
    while not arm.done():       # repeat until the arm has finished moving
        wait(10)

    # Three ways to stop a motor:
    arm.stop()    # let it spin freely
    arm.brake()   # slow it down gently
    arm.hold()    # actively hold the current position (resists being pushed)

    # Limit speed, acceleration and torque (useful for gentle or heavy
    # attachments). With no values it just reports the current limits.
    print(arm.control.limits())
    arm.control.limits(speed=500, acceleration=1000)

    # Release the motor so it can be set up again with different settings,
    # e.g. a different gear ratio for a swapped attachment. Remove the # to use.
    # arm.close()


# =============================================================================
# 5. FIND THE LINE THRESHOLD
# The color sensor's reflection() is a number from 0 (dark) to 100 (bright).
# The "threshold" is the value halfway between the mat and the line.
# A reading BELOW the threshold means "on the line".
# Mats and lighting differ, so measuring beats guessing:
#   1. run read_reflection() and hold the sensor over the mat, then the line
#   2. write down both numbers
#   3. add them together and divide by 2 (for example mat 85, line 5: (85 + 5) / 2 = 45)
# =============================================================================
def read_reflection():
    # Print the reflection (0 to 100) over and over. Press the hub button to stop.
    while True:
        print("reflection:", color_sensor.reflection())
        wait(100)       # wait 100 ms between readings


def read_hsv():
    # Print the color as HSV values over and over. Press the hub button to stop.
    #   h (hue)        0 to 359: the color itself (red 0, green 120, blue 240)
    #   s (saturation) 0 to 100: how strong the color is (0 = gray/white)
    #   v (value)      0 to 100: how bright it is (0 = black)
    while True:
        hsv = color_sensor.hsv()    # one reading holding all three numbers
        print("h:", hsv.h, " s:", hsv.s, " v:", hsv.v)
        wait(100)


# =============================================================================
# 6. DRIVE TO A LINE, THEN RUN THE NEXT MISSION
# Crossing a line gives the robot a repeatable starting spot: no matter where
# it started, it stops in the same place relative to the line. Do this before
# a mission that needs to be lined up accurately.
# The line only counts if the sensor sees dark for several readings in a row,
# so a single bad reading or a small mark on the mat is ignored.
# =============================================================================
# This function drives forward until it finds a line, then stops.
# It gives back (returns) True if it found the line, or False if the robot
# drove max_distance mm without finding one.
# "max_distance=1000" is a default: if you call drive_to_line(threshold) without
# the second number, it uses 1000. Call drive_to_line(threshold, 400) to change it.
def drive_to_line(threshold, max_distance=1000):
    # How many dark readings IN A ROW count as a real line. One dark reading
    # could be a bad reading or a small mark on the mat, so we wait until the
    # sensor has seen dark several times in a row.
    # Each trip around the loop below takes about 10 ms (the wait(10) at the
    # bottom), so a sample is roughly 10 ms. At 100 mm/s the robot moves about
    # 1 mm per sample, so 5 samples means a mark must be about 5 mm wide.
    #   Missing real lines? Make it smaller.
    #   Triggering on small marks or dirt? Make it bigger.
    MIN_SAMPLES = 5

    dark_samples = 0                        # how many dark readings in a row so far

    base.straight(max_distance, wait=False)     # start driving without waiting

    while not base.done():                  # repeat until the robot has driven max_distance
        if color_sensor.reflection() < threshold:
            # Darker than the threshold: one more dark reading in a row.
            dark_samples = dark_samples + 1
        else:
            # A bright reading breaks the streak. Start counting again.
            dark_samples = 0

        if dark_samples >= MIN_SAMPLES:     # enough dark readings: it is a real line
            base.stop()
            return True                     # leave the function and answer "yes, found it"

        wait(10)

    base.stop()
    return False                            # drove the whole distance and found no line


def line_detect():
    threshold = 15   # 15 is an example number: type your own threshold

    # A slower speed makes the stopping spot more repeatable, because the
    # robot coasts less after it sees the line.
    base.settings(straight_speed=100)

    # drive_to_line gives back True or False. We store the answer in "found".
    found = drive_to_line(threshold)

    if found:
        # The color sensor is usually mounted in front of the wheels, so the
        # robot is now stopped with the sensor on the line. Optionally move
        # forward to position the wheels (or an attachment) where you want:
        # base.straight(60)
        hub.speaker.beep(800, 100)      # frequency (Hz), duration (ms)
        mission_1()                     # now run the next mission from this spot
    else:
        # No line was found, so do NOT run the mission from the wrong spot.
        print("Line not found!")
        hub.speaker.beep(200, 500)      # a low, long beep means a problem


# =============================================================================
# 7. FIND A LINE AND FOLLOW IT
# Start the robot moving BEFORE calling follow_line(), for example:
#     base.drive(100, 0)          # drive straight at 100 mm/s, no turning
#     follow_line()
# follow_line() keeps the robot moving until it finds the line (same "dark
# several times in a row" check as section 6), then follows the line's edge.
#
# Steering rule: the further the sensor is from the edge of the line, the
# harder the robot steers back. This is called "P control" (P = proportional).
# The "D" part reacts to how fast the error is changing, which calms wiggling.
# =============================================================================
# Gives back True after following the line, or False if no line was found.
def follow_line():
    # Settings to tune. Capital letters are a habit for values that stay fixed.
    # Halfway between the mat and the line. Use read_reflection() or the
    # read_sensors recipe to measure it. 15 is only an example number.
    THRESHOLD = 15
    MIN_SAMPLES = 5         # dark readings in a row that count as the line (see section 6)
    SEARCH_DISTANCE = 1000  # mm to travel looking for the line before giving up
    FOLLOW_DISTANCE = 1000  # mm to follow the line before stopping
    DRIVE_SPEED = 100       # mm/s while following. Start slow, speed up once it works.
    KP = 1.2                # how hard to steer per point of error.
                            #   Robot wiggles or oscillates? Make it smaller.
                            #   Robot turns too slowly and loses the line? Make it bigger.
    KD = 4.0                # extra damping. Set to 0 to turn this part off.
    SIDE = 1                # if the robot steers AWAY from the line, change to -1

    # --- Part 1: find the line (the robot is already moving) ---
    # base.distance() is how far the robot has driven in total. We remember
    # where we started and compare, so we never have to stop the robot.
    start = base.distance()
    dark_samples = 0
    while dark_samples < MIN_SAMPLES:
        if base.distance() - start > SEARCH_DISTANCE:
            base.stop()
            return False                    # never found a line: give up

        if color_sensor.reflection() < THRESHOLD:
            dark_samples = dark_samples + 1
        else:
            dark_samples = 0                # a bright reading breaks the streak
        wait(10)

    # --- Part 2: follow the line ---
    follow_start = base.distance()
    last_error = 0

    while base.distance() - follow_start < FOLLOW_DISTANCE:
        # error: how far the reading is from the threshold.
        # Negative = darker (more on the line), positive = brighter (off the line).
        error = color_sensor.reflection() - THRESHOLD
        derivative = error - last_error     # how much the error changed
        last_error = error                  # remember it for next time

        # drive(speed in mm/s, turn rate in deg/s) drives and steers at once.
        base.drive(DRIVE_SPEED, SIDE * (KP * error + KD * derivative))
        wait(10)

    base.stop()
    return True


# =============================================================================
# 8. HUB FEATURES
# =============================================================================
def hub_features():
    print("Battery:", hub.battery.voltage() / 1000, "V")

    hub.light.on(Color.GREEN)               # the light by the center button

    hub.display.number(42)                  # the 5x5 grid of lights
    wait(1000)
    hub.display.text("GO")
    wait(1000)
    hub.display.off()

    hub.speaker.beep(500, 200)              # frequency (Hz), duration (ms)

    # Wait for a button press. The center button stops programs, so use
    # another one: Button.LEFT or Button.RIGHT.
    hub.display.text("?")
    while Button.RIGHT not in hub.buttons.pressed():
        wait(10)

    # Stopwatch: useful for timing a run (an FLL round is 2 min 30 s).
    timer = StopWatch()
    wait(1500)
    print("Elapsed:", timer.time() / 1000, "s")     # time() is in ms

    # Gyro heading in degrees. Reset it while the robot is sitting still.
    hub.imu.reset_heading(0)
    print("Heading:", hub.imu.heading())


# =============================================================================
# 9. TURN TO AN ABSOLUTE HEADING
# base.turn(90) means "turn 90 degrees from wherever you point now", so small
# errors add up over a long run. Turning to a heading measured from the START
# does not drift.
# =============================================================================
def turn_to(heading):
    # Turn (the short way) so the robot faces 'heading' degrees from the start.
    # base.angle() is how far the robot has turned since base.reset().
    # The "% 360" part keeps the answer between -180 and +180 so the robot
    # always takes the shorter way around.
    error = (heading - base.angle() + 180) % 360 - 180
    base.turn(error)


def turn_to_heading():
    base.reset()            # the direction the robot faces now becomes heading 0
    base.straight(300)
    turn_to(90)             # face 90 degrees to the right of the start
    base.straight(300)
    turn_to(0)              # face the starting direction again
    base.straight(-300)     # back up


# =============================================================================
# 10. MISSION FUNCTIONS AND MENU
# One function per mission keeps things tidy. Then a menu lets you pick which
# one to run, without changing the code between runs.
# =============================================================================

# Step 1: write each mission as its own function.
def mission_1():
    base.straight(300)
    base.turn(90)
    base.straight(300)


def mission_2():
    base.arc(200, angle=90)
    arm.run_angle(180, 90)


# Step 2: the program starts doing things from here down.
print_settings()

# Step 3: hub_menu shows the names you give it on the hub's light matrix.
# Press LEFT/RIGHT to scroll through them and the CENTER button to choose.
# Whatever you chose is stored in the variable "program" as text, so the
# names must be in quotes. They can be numbers or letters ("1", "A", ...).
program = hub_menu("1", "2", "3")

# Step 4: run the code that matches the choice.
#   if / elif checks one choice at a time. Only the first one that matches runs.
#   == compares "program" to the text. (One = would store a value, not compare.)
#   Remember the colon (:) and the 4 spaces of indentation under each line.
if program == "1":
    mission_1()
elif program == "2":
    mission_2()
elif program == "3":
    # A choice can run several missions in a row, in the order written.
    mission_2()
    mission_1()

# To add a new choice:
#   1. add its name to hub_menu(...) above, e.g. hub_menu("1", "2", "3", "4")
#   2. add a matching "elif program == "4":" with the code to run under it
# To try a recipe from this file, call it here the same way as a mission,
# e.g.  elif program == "4":
#           base.drive(100, 0)    # follow_line needs the robot already moving
#           follow_line()


# =============================================================================
# 11. ADVANCED: DOING TWO THINGS AT ONCE (concurrency)
# Normally Python runs one line at a time: while base.straight(500) is driving,
# the arm cannot move. The easy way around that is wait=False (see section 2),
# but then YOU must write a loop to check on the motors.
# Pybricks has a second way: "tasks" that take turns running, so it looks like
# they run at the same time. You need three new ideas:
#
#   async def name():   makes a TASK (a function that can take turns).
#                       Use "async def" instead of "def".
#   await something     inside a task: "start this and let other tasks run
#                       until it finishes". Motor moves and wait() can be
#                       awaited. Use it in front of every one of them.
#   multitask(a(), b()) start several tasks together. Put "await" in front of
#                       it to continue when ALL of them are finished.
#                       Add race=True to continue as soon as ANY ONE of them
#                       finishes, which cancels the others.
#   run_task(main())    start the first task from normal code. It returns
#                       when that task is finished.
#
# Rules to remember:
#   - Inside a task use "await wait(10)", NOT plain "wait(10)". Plain wait()
#     freezes every task, so nothing else gets a turn.
#   - A task that loops must "await" something each time around the loop,
#     or it will hog all the time.
#   - "await" only works inside "async def". Normal "def" functions can't use it.
#   - Inside multitask(...) write each task with parentheses but WITHOUT its own
#     await: multitask(a(), b()). Only the multitask itself gets an await.
# =============================================================================

# --- Example A: move the arm while driving -----------------------------------
async def drive_and_move_arm_task():
    # Both start at the same moment. We continue after BOTH have finished.
    await multitask(
        base.straight(500),
        arm.run_angle(300, 90),
    )


def drive_and_move_arm():
    run_task(drive_and_move_arm_task())     # start the task from normal code


# --- Example B: drive until something is in the way --------------------------
# Same job as section 2, but without writing the driving loop ourselves.
async def wait_for_obstacle_task():
    while dist_sensor.distance() > 100:     # keep going while nothing is close
        await wait(10)                      # let the driving task take its turn
    # Reaching the end of the function means "obstacle found".


async def drive_until_obstacle_task():
    # race=True: as soon as ONE task finishes (the obstacle watcher, or the
    # drive reaching 1000 mm), the other one is cancelled.
    await multitask(
        base.straight(1000),
        wait_for_obstacle_task(),
        race=True,
    )
    base.stop()     # make sure the wheels stop


def drive_until_obstacle():
    run_task(drive_until_obstacle_task())


# --- Example C: a background task that never ends ----------------------------
# A "while True" task is fine as long as it awaits inside the loop and you use
# race=True. When the driving finishes, the endless task is cancelled.
async def beep_every_second_task():
    while True:
        hub.speaker.beep(800, 100)
        await wait(1000)


async def drive_with_beeps_task():
    await multitask(
        base.straight(800),
        beep_every_second_task(),
        race=True,
    )


def drive_with_beeps():
    run_task(drive_with_beeps_task())
