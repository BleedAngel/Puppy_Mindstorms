#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Image

from leg_motor import stand_up
from head_motor import adjust_head

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# 初始化EV3主機
ev3 = EV3Brick()
ev3.speaker.beep()

'''
Port S1: 觸碰感應器
Port S4: 顏色感應器
Port D: 左後腿馬達
Port A: 右後腿馬達
Port B: 頭部馬達
'''

NEUTRAL_EYES = Image(ImageFile.NEUTRAL)
TIRED_EYES = Image(ImageFile.TIRED_MIDDLE)
TIRED_LEFT_EYES = Image(ImageFile.TIRED_LEFT)
TIRED_RIGHT_EYES = Image(ImageFile.TIRED_RIGHT)
SLEEPING_EYES = Image(ImageFile.SLEEPING)
HURT_EYES = Image(ImageFile.HURT)
ANGRY_EYES = Image(ImageFile.ANGRY)
HEART_EYES = Image(ImageFile.LOVE)
SQUINTY_EYES = Image(ImageFile.TEAR)

# 定義雙腿馬達和頭部馬達
left_leg_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_leg_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
head_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, gears = [[1, 24], [12, 36]])
HALF_UP_ANGLE = 25
STAND_UP_ANGLE = 65
HEAD_UP_ANGLE = 0
HEAD_DOWN_ANGLE = -40



stand_up(left_leg_motor, right_leg_motor, HALF_UP_ANGLE, STAND_UP_ANGLE)
adjust_head(head_motor, HEAD_UP_ANGLE, HEAD_DOWN_ANGLE)

while True:
    wait(1000)
