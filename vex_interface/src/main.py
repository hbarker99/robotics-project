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

TIMEOUT = 3

inertial.calibrate()
sleep(2000)
brain.screen.print("Hello EXP")

motor_left_front = Motor(Ports.PORT1)
motor_left_back = Motor(Ports.PORT2)
motor_right_front = Motor(Ports.PORT3)
motor_right_back = Motor(Ports.PORT4)


def MotorCommand(command):
    global motor_left_front, motor_left_back, motor_right_back, motor_right_front
    
    drive_controls = command.split(" ")
    left_drive = drive_controls[1]
    right_drive = drive_controls[2]

    motor_left_front.set_velocity(int(left_drive), VelocityUnits.RPM)
    motor_left_back.set_velocity(int(left_drive), VelocityUnits.RPM)
    motor_right_front.set_velocity(int(right_drive), VelocityUnits.RPM)
    motor_right_back.set_velocity(int(right_drive), VelocityUnits.RPM)

    motor_left_front.spin(FORWARD)
    motor_left_back.spin(FORWARD)
    motor_right_front.spin(REVERSE)
    motor_right_back.spin(REVERSE)

def GetMotorPositions():
    global motor_left_front, motor_left_back, motor_right_back, motor_right_front
    left_average = int((motor_left_front.position(RotationUnits.RAW) + motor_left_back.position(RotationUnits.RAW)) / 2)
    right_average = -int((motor_right_front.position(RotationUnits.RAW) + motor_right_back.position(RotationUnits.RAW)) / 2)

    return str(left_average) + " " + str(right_average)
    
def DebugLog(type, msg):
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    brain.screen.print(type)
    brain.screen.set_cursor(2, 1)
    brain.screen.print(msg)


while True:
    res = sys.stdin.readline().strip()

    if (len(res) == 0):
        continue
    
    if (res[0] == "m"):
        MotorCommand(res)

    elif (res[0] == "e"):
      pass

    else:
        DebugLog("Unknown Command.", res)

      
    print(GetMotorPositions())
    sleep(1)
    
