#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# 初始化EV3主機
ev3 = EV3Brick()
ev3.speaker.beep()

# 
'''
Port S1: 觸碰感應器
Port S4: 顏色感應器
Port D: 左後腿馬達
Port A: 右後腿馬達
Port B: 頭部馬達
'''

# 初始化後腿馬達+站立角度
left_leg_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_leg_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
HALF_UP_ANGLE = 25
STAND_UP_ANGLE = 65

def stand_up():
    #
    ev3.screen.print("Action: Standing Up")

    #
    left_leg_motor.run_target(100, HALF_UP_ANGLE, wait = False)
    right_leg_motor.run_target(100, HALF_UP_ANGLE)

    while not (left_leg_motor.control.donr() and right_leg_motor.control.done()):
        wait(i0)

    #
    left_leg_motor.run_target(50, STAND_UP_ANGLE, wait = False)
    right_leg_motor.run_target(50, STAND_UP_ANGLE)

    while not (left_leg_motor.control.done() and right_leg_motor.control.donr()):
        wait(10)

    #
    ev3.screen.print("Status: Standed")
    ev3.speaker.beep()
