#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

left_leg_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_leg_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
HALF_UP_ANGLE = 25
STAND_UP_ANGLE = 65
STRETCH_ANGLE = 125

# 站立動作函式
def stand_up():
    left_leg_motor.run_target(100, HALF_UP_ANGLE, wait=False)
    right_leg_motor.run_target(100, HALF_UP_ANGLE)
    while not (left_leg_motor.control.done() and right_leg_motor.control.done()):
        wait(100)

    left_leg_motor.run_target(50, STAND_UP_ANGLE, wait=False)
    right_leg_motor.run_target(50, STAND_UP_ANGLE)
    while not (left_leg_motor.control.done() and right_leg_motor.control.done()):
        wait(100)

    left_leg_motor.stop()
    right_leg_motor.stop()

# 坐下動作
def sit_down():
    left_leg_motor.run_target(50, 0, wait=False)
    right_leg_motor.run_target(50, 0)
    while not (left_leg_motor.control.done() and right_leg_motor.control.done()):
        wait(100)

    left_leg_motor.stop()
    right_leg_motor.stop()

# 伸展動作
def stretch():
    stand_up()

    left_leg_motor.run_target(100, STRETCH_ANGLE, wait=False)
    right_leg_motor.run_target(100, STRETCH_ANGLE)
    while not (left_leg_motor.control.done() and right_leg_motor.control.done()):
        wait(100)

    left_leg_motor.run_target(100, STAND_UP_ANGLE, wait=False)
    right_leg_motor.run_target(100, STAND_UP_ANGLE)
    while not (left_leg_motor.control.done() and right_leg_motor.control.done()):
        wait(100)

    left_leg_motor.stop()
    right_leg_motor.stop()

# 搖尾巴 / 活潑腳步動作
def playful_legs(times=2):
    sit_down()

    for _ in range(times):
        left_leg_motor.run_target(120, 18)
        left_leg_motor.run_target(120, 0, wait=False)
        right_leg_motor.run_target(120, 18)
        right_leg_motor.run_target(120, 0, wait=False)
    
    wait(100)

    left_leg_motor.stop()
    right_leg_motor.stop()