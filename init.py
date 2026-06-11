#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Image

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# 初始化EV3主機
ev3 = EV3Brick()
ev3.speaker.beep()

# 定義雙腿馬達和頭部馬達
def reset():
    buttons = ev3.buttons.pressed()
    left_leg_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
    right_leg_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    head_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, gears = [[1, 24], [12, 36]])
    return buttons, left_leg_motor, right_leg_motor, head_motor

def reset_motor_angles():
    HALF_UP_ANGLE = 25
    STAND_UP_ANGLE = 65
    HEAD_UP_ANGLE = 0
    HEAD_DOWN_ANGLE = -40