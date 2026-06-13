#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Color
from pybricks.tools import wait
from pybricks.media.ev3dev import Image, ImageFile, SoundFile

from head_motor import move_head, nod_head
from leg_motor import stand_up, sit_down, playful_legs, stretch

def act(ev3, color_sensor):
    current_color = color_sensor.color()

    if current_color == Color.RED:
        ev3.light.on(Color.RED)
        ev3.screen.load_image(Image(ImageFile.ANGRY))
        stand_up()
        for i in range(2):
            nod_head()
            ev3.speaker.play_file(SoundFile.DOG_GROWL)
        wait(2000)

    elif current_color == Color.GREEN:
        ev3.light.on(Color.GREEN)
        ev3.screen.load_image(Image(ImageFile.HAPPY))
        stand_up()
        for i in range(2):
            nod_head()
            ev3.speaker.play_file(SoundFile.DOG_BARK_1)
        wait(2000)

    elif current_color == Color.BLUE:
        ev3.light.on(Color.BLUE)
        ev3.screen.load_image(Image(ImageFile.TEAR))
        sit_down()
        move_head(1)
        ev3.speaker.play_file(SoundFile.DOG_WHINE)
        wait(2000)

    elif current_color == Color.YELLOW:
        ev3.light.on(Color.YELLOW)
        ev3.screen.load_image(Image(ImageFile.NEUTRAL))
        stand_up()
        move_head(2)
        playful_legs()
        ev3.speaker.play_file(SoundFile.DOG_BARK_2)
        wait(2000)

    else:
        ev3.light.on(Color.ORANGE)
        ev3.screen.load_image(Image(ImageFile.TIRED_MIDDLE))
        move_head(2)
        playful_legs()
        wait(1800)