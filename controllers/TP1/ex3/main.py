"""
IRI - TP1 - Ex 3
By: Gonçalo Leão
"""

import math
import time
from controller import Robot
from controllers.utils import cmd_vel

def simple_timer(seconds):
    time.sleep(seconds)

robot: Robot = Robot()
timer = 0
while True:
    cmd_vel(robot, linear_vel=6, angular_vel=0)
    robot.step()


# TODO
