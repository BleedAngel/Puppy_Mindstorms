#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Image

from color_sensor import act

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# 初始化EV3主機
ev3 = EV3Brick()
ev3.speaker.beep()

NEUTRAL_EYES = Image(ImageFile.NEUTRAL)
TIRED_EYES = Image(ImageFile.TIRED_MIDDLE)
TIRED_LEFT_EYES = Image(ImageFile.TIRED_LEFT)
TIRED_RIGHT_EYES = Image(ImageFile.TIRED_RIGHT)
SLEEPING_EYES = Image(ImageFile.SLEEPING)
HURT_EYES = Image(ImageFile.HURT)
ANGRY_EYES = Image(ImageFile.ANGRY)
HEART_EYES = Image(ImageFile.LOVE)
SQUINTY_EYES = Image(ImageFile.TEAR)

while True:
    act()
    if(Button.CENTER in buttons):
        break