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

#校準頭部馬達
def adjust_head(head_motor, HEAD_UP_ANGLE, HEAD_DOWN_ANGLE):
    ev3.screen.print("Calibrating...")
    ev3.light.on(Color.ORANGE)

    while True:
        buttons = ev3.buttons.pressed()

        if Button.CENTER in buttons:
            ev3.light.on(Color.GREEN)
            ev3.screen.print("Calibration Done")
            wait(500)
            break
        elif Button.UP in buttons:
            if head_motor.angle() < HEAD_UP_ANGLE:
                head_motor.run(20)
            else:
                head_motor.stop()
        elif Button.DOWN in buttons:
            if head_motor.angle() > HEAD_DOWN_ANGLE:
                head_motor.run(-20)
            else:
                head_motor.stop()
        else:
            head_motor.stop()

        wait(100)
    head_motor.reset_angle(0)
    wait(500)