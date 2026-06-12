#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Image

from leg_motor import stand_up
from head_motor import move_head

# 初始化EV3主機
ev3 = EV3Brick()
ev3.speaker.beep()

def act():
    # 定義顏色感應器
    color_sensor = ColorSensor(Port.S4)

    if(color_sensor.color() == Color.RED):
        stand_up(2)
    elif(color_sensor.color() == Color.GREEN):
        stand_up(1)
    elif(color_sensor.color() == Color.BLUE):
        stand_up(1)
    elif(color_sensor.color() == Color.YELLOW):
        stand_up(2)