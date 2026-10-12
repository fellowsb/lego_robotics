# Pybricks Challenges

Five short challenges for a custom LEGO robot on the Bioglow FIRST LEGO League mat. Each one practices a key part of the cookbook, [pybricks_examples.py](../pybricks_examples.py). Each file runs on its own, with its imports and robot setup included.

Before you start, check the **Setup** block at the top of each file. Make sure the ports (`Port.A`, `Port.E`, ...) and the wheel measurements match your robot.

Do them in order. Each one builds on the one before.

| # | File | Cookbook sections | What you practice |
|---|------|-------------------|-------------------|
| 1 | [challenge_1_leave_base.py](challenge_1_leave_base.py) | 1, 8 | Driving, turning, `for` loops |
| 2 | [challenge_2_arm_delivery.py](challenge_2_arm_delivery.py) | 4 | Attachment motor, reset, `run_target` |
| 3 | [challenge_3_stop_before_crash.py](challenge_3_stop_before_crash.py) | 2, 3 | Distance sensor, `while` and `if` |
| 4 | [challenge_4_find_the_line.py](challenge_4_find_the_line.py) | 5, 6 | Color sensor, threshold, functions that return a value |
| 5 | [challenge_5_mission_menu.py](challenge_5_mission_menu.py) | 10, 8 | Mission functions, hub menu, timer |

## Challenge 1: Leave Base
**Goal:** Drive from base to a mission model, turn to face it, and come back home.
- **Try it:** Change the numbers until the robot ends up back in the same spot every time.
- **Bonus:** Use a `for` loop to do the whole trip 3 times.

## Challenge 2: Arm Reset and Delivery
**Goal:** Reset the arm to a known start, then lift something and put it down.
- **Try it:** Find the arm angle that works for your attachment. `run_target` goes to a position measured from the reset. `run_angle` goes a set amount from where the arm is now.
- **Bonus:** Run `deliver()` twice in a row. The arm should end up in the same place both times.

## Challenge 3: Stop Before You Crash
**Goal:** Drive toward a model and stop about 50 mm away from it.
1. Run `read_sensors()` and point the robot at a model. Write down the distances.
2. Run `stop_for_obstacle()`. Change the numbers to fit the mat.
- **Try it:** Start from three different spots. It should stop in about the same place each time.
- **Bonus:** Show `STOP` on the hub display (already included). Try other stopping distances.

## Challenge 4: Find the Line
**Goal:** Drive until the robot finds a dark line on the mat, beep, then do a short move.
1. Run `read_reflection()`. Hold the sensor over the mat, then over the line, and write down both numbers.
2. Add them and divide by 2. This is your **threshold**.
3. Type your threshold into `find_line()` and run it.
- **Try it:** Start the robot a bit crooked. It should still stop at the line in the same place.
- **Bonus:** Run it off the mat. You should hear the low beep that means "line not found."

## Challenge 5: Mission Menu and Timer
**Goal:** Combine your earlier challenges into missions and pick one from the hub.
- **Try it:** Run all three menu choices (`A`, `B`, `C`) and read the run time in the terminal.
- **Bonus:** Add a fourth choice `D` that runs the line challenge.
