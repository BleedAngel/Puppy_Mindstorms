#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Direction, Button, Color
from pybricks.tools import wait

# 校準頭部位置
def reset_head(ev3):
    
    ev3.screen.print("Calibrating...")
    ev3.light.on(Color.ORANGE)

    # 定義頭部馬達
    head_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, gears = [[1, 24], [12, 36]])
    HEAD_UP_ANGLE = 45
    HEAD_DOWN_ANGLE = -45

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

# 點頭動作
def nod_head(ev3, times=2):

    head_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, gears = [[1, 24], [12, 36]])
    HEAD_DOWN_ANGLE = -20

    for _ in range(times):
        head_motor.run_target(80, HEAD_DOWN_ANGLE)
        wait(120)
        head_motor.run_target(80, 0)
        wait(120)

# 根據反應做出頭部動作
def move_head(x, ev3):

    # 定義頭部馬達
    head_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, gears = [[1, 24], [12, 36]])
    HEAD_UP_ANGLE = 45
    HEAD_DOWN_ANGLE = -45

    if(x==1):
        head_motor.run_target(50, HEAD_DOWN_ANGLE)
    elif(x==2):
        head_motor.run_target(50, 0)
    else:
        head_motor.run_target(50, HEAD_UP_ANGLE)