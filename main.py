#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port, Button
from pybricks.tools import wait

from color_sensor import act
from head_motor import reset_head

# 初始化EV3主機
ev3 = EV3Brick()
ev3.speaker.beep()
color_sensor = ColorSensor(Port.S4)

reset_head(ev3)

while True:
    act(ev3, color_sensor)
    buttons = ev3.buttons.pressed()
    if Button.CENTER in buttons:
        break
    wait(100)