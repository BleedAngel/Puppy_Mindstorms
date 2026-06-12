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
def stand_up(x):

    left_leg_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
    right_leg_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    HALF_UP_ANGLE = 25
    STAND_UP_ANGLE = 90

    left_leg_motor.run_target(50, HALF_UP_ANGLE, wait = False)
    right_leg_motor.run_target(50, HALF_UP_ANGLE)

    # --- 坐下 ---
    if(x==1):
        target_angle = 0
    
    # --- 完全站立(兩段) ---
    if(x==2):
        target_angle = STAND_UP_ANGLE

    left_leg_motor.run_target(50, target_angle, wait = False)
    right_leg_motor.run_target(50, target_angle)

    while not (left_leg_motor.control.done() and right_leg_motor.control.done()):
        wait(500)