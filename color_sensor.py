#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.media.ev3dev import ImageFile, Image

from leg_motor import stand_up, playful_legs
from head_motor import move_head, nod_head

def act(ev3):
    # 定義顏色感應器
    color_sensor = ColorSensor(Port.S4)
    current_color = color_sensor.color()

    if(current_color == Color.RED):
        stand_up(2, ev3)
        nod_head(ev3, 2)
        ev3.light.on(Color.RED)
        ev3.speaker.play_file("SFX/Dog-Bark.wav")
        ev3.screen.load_image(Image(ImageFile.ANGRY))
        wait(2000)

    elif(current_color == Color.GREEN):
        stand_up(1, ev3)
        nod_head(ev3, 1)
        ev3.light.on(Color.GREEN)
        ev3.speaker.play_file("SFX/Dog-Panting.wav")
        ev3.screen.load_image(Image(ImageFile.HAPPY))
        wait(2000)

    elif(current_color == Color.BLUE):
        stand_up(1, ev3)
        move_head(1, ev3)
        ev3.light.on(Color.BLUE)
        ev3.speaker.play_file("SFX/Dog-Howling.wav")
        ev3.screen.load_image(Image(ImageFile.TEAR))
        wait(2000)

    elif(current_color == Color.YELLOW):
        stand_up(2, ev3)
        move_head(2, ev3)
        playful_legs(ev3, 2)
        ev3.light.on(Color.YELLOW)
        ev3.screen.load_image(Image(ImageFile.NEUTRAL))
        wait(2000)

    else:
        playful_legs(ev3, 3)
        move_head(2, ev3)
        ev3.light.on(Color.ORANGE)
        ev3.screen.load_image(Image(ImageFile.TIRED_MIDDLE))
        wait(1800)