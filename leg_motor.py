#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# 初始化EV3主機
ev3 = EV3Brick()
ev3.speaker.beep()

# 站立動作函式
def stand_up(act,left_leg_motor, right_leg_motor, HALF_UP_ANGLE, STAND_UP_ANGLE):
    ev3.screen.print("Action: Standing Up")

    # --- 第一階段：先撐起一半 ---
    left_leg_motor.run_target(100, HALF_UP_ANGLE, wait = False)
    right_leg_motor.run_target(100, HALF_UP_ANGLE)

    while not (left_leg_motor.control.done() and right_leg_motor.control.done()):
        wait(10)

    if(act==False):
        break

    # --- 第二階段：完全站立 ---
    left_leg_motor.run_target(50, STAND_UP_ANGLE, wait = False)
    right_leg_motor.run_target(50, STAND_UP_ANGLE)

    while not (left_leg_motor.control.done() and right_leg_motor.control.done()):
        wait(10)

    ev3.screen.print("Status: Standed")
    ev3.speaker.beep()