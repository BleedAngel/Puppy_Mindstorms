#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Image

# 初始化EV3主機
ev3 = EV3Brick()
ev3.speaker.beep()

#初始化顏色感應器
color_sensor = ColorSensor(Port.S4)

if(color_sensor.color() == Color.RED):
    ev3.screen.print("Red Detected")
elif(color_sensor.color() == Color.GREEN):
    ev3.screen.print("Green Detected")
elif(color_sensor.color() == Color.BLUE):
    ev3.screen.print("Blue Detected")
elif(color_sensor.color() == Color.YELLOW):
    ev3.screen.print("Yellow Detected")