#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

# 站立動作函式
def stand_up(x, ev3):

    left_leg_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
    right_leg_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    HALF_UP_ANGLE = 25
    STAND_UP_ANGLE = 90

    left_leg_motor.run_target(50, HALF_UP_ANGLE, wait = False)
    right_leg_motor.run_target(50, HALF_UP_ANGLE)

    # --- 坐下 ---
    if(x==1):
        target_angle = 0
    
    # --- 完全站立(兩段) ---
    if(x==2):
        target_angle = STAND_UP_ANGLE

    left_leg_motor.run_target(50, target_angle, wait = False)
    right_leg_motor.run_target(50, target_angle)

    while not (left_leg_motor.control.done() and right_leg_motor.control.done()):
        wait(500)

    # 釋放馬達
    left_leg_motor.stop()
    right_leg_motor.stop()

# 搖尾巴 / 活潑腳步動作
def playful_legs(ev3, times=2):

    left_leg_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
    right_leg_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)

    for _ in range(times):
        left_leg_motor.run_target(120, 18, wait=False)
        right_leg_motor.run_target(120, 12)
        wait(120)
        left_leg_motor.run_target(120, 0, wait=False)
        right_leg_motor.run_target(120, 0)
        wait(120)

    left_leg_motor.stop()
    right_leg_motor.stop()