"""
IRI - TP1 - Ex 1
By: Gonçalo Leão
"""

from controller import Robot
from controllers.utils import cmd_vel



# Create the Robot instance.
robot: Robot = Robot()

while True:
    cmd_vel(robot, linear_vel=0.1, angular_vel=0)
    robot.step()
# TODO: Use cmd_vel and robot.step()
