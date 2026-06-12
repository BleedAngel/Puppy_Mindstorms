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

# 校準頭部位置
def reset_head():
    
    ev3.screen.print("Calibrating...")
    ev3.light.on(Color.ORANGE)

    # 定義頭部馬達和按鈕
    head_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, gears = [[1, 24], [12, 36]])
    buttons = ev3.buttons.pressed()
    HEAD_UP_ANGLE = 20
    HEAD_DOWN_ANGLE = -20

    while True:
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

# 根據反應做出頭部動作
def move_head(x):

    # 定義頭部馬達和按鈕
    head_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, gears = [[1, 24], [12, 36]])
    buttons = ev3.buttons.pressed()
    HEAD_UP_ANGLE = 20
    HEAD_DOWN_ANGLE = -20

    if(x==1):
        head_motor.run_target(50, HEAD_DOWN_ANGLE)
    else:
        head_motor.run_target(50, HEAD_UP_ANGLE)