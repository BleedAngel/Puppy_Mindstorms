#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button
from pybricks.tools import wait

from color_sensor import act
from head_motor import reset_head

# 初始化EV3主機
ev3 = EV3Brick()
ev3.speaker.beep()

reset_head(ev3)

while True:
    act(ev3)
    buttons = ev3.buttons.pressed()
    if(Button.CENTER in buttons):
        break
    wait(100)