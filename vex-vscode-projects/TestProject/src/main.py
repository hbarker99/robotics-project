# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       jack                                                         #
# 	Created:      4/1/2025, 8:29:35 PM                                         #
# 	Description:  EXP project                                                  #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *
import sys

# Brain should be defined by default
brain=Brain()
inertial = Inertial()
brain.screen.print("Hello EXP")

TIMEOUT = 3

inertial.calibrate()
sleep(2000)

while True:
    res = sys.stdin.readline()

    if (len(res) == 0):
        continue
    
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print(res)

    if(res[0:4] == "roll"):
        print(inertial.orientation(OrientationType.ROLL))
    
