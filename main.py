#!/usr/bin/env pybricks-micropython

import urandom

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Button, Color, Direction
from pybricks.media.ev3dev import Image, ImageFile, SoundFile
from pybricks.tools import wait, StopWatch


class Puppy:
    HALF_UP_ANGLE = 25
    STAND_UP_ANGLE = 65
    STRETCH_ANGLE = 125

    HEAD_UP_ANGLE = 0
    HEAD_DOWN_ANGLE = -40

    NEUTRAL_EYES = Image(ImageFile.NEUTRAL)
    TIRED_EYES = Image(ImageFile.TIRED_MIDDLE)
    TIRED_LEFT_EYES = Image(ImageFile.TIRED_LEFT)
    TIRED_RIGHT_EYES = Image(ImageFile.TIRED_RIGHT)
    SLEEPING_EYES = Image(ImageFile.SLEEPING)
    HURT_EYES = Image(ImageFile.HURT)
    ANGRY_EYES = Image(ImageFile.ANGRY)
    HEART_EYES = Image(ImageFile.LOVE)
    SQUINTY_EYES = Image(ImageFile.TEAR)

    def __init__(self):
        self.ev3 = EV3Brick()

        self.left_leg_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
        self.right_leg_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
        self.head_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE,
                                gears=[[1, 24], [12, 36]])

        self.color_sensor = ColorSensor(Port.S4)
        self.touch_sensor = TouchSensor(Port.S1)

        self.pet_count_timer = StopWatch()
        self.feed_count_timer = StopWatch()
        self.count_changed_timer = StopWatch()

        self.pet_target = None
        self.feed_target = None
        self.pet_count = None
        self.feed_count = None

        self._behavior = None
        self._behavior_changed = None
        self._eyes = None

        self.eyes_timer_1 = StopWatch()
        self.eyes_timer_1_end = 0
        self.eyes_timer_2 = StopWatch()
        self.eyes_timer_2_end = 0

        self.playful_timer = StopWatch()
        self.playful_bark_interval = None

        self.prev_petted = None
        self.prev_color = None

    def adjust_head(self):
        self.ev3.screen.load_image(ImageFile.EV3_ICON)
        self.ev3.light.on(Color.ORANGE)
        while True:
            buttons = self.ev3.buttons.pressed()
            if Button.CENTER in buttons:
                break
            elif Button.UP in buttons:
                self.head_motor.run(20)
            elif Button.DOWN in buttons:
                self.head_motor.run(-20)
            else:
                self.head_motor.stop()
            wait(100)
        self.head_motor.stop()
        self.head_motor.reset_angle(0)
        self.ev3.light.on(Color.GREEN)

    def move_head(self, target):
        self.head_motor.run_target(20, target)

    def reset(self):
        self.left_leg_motor.reset_angle(0)
        self.right_leg_motor.reset_angle(0)
        self.pet_target = urandom.randint(3, 6)
        self.feed_target = urandom.randint(2, 4)
        self.pet_count, self.feed_count = 1, 1
        self.pet_count_timer.reset()
        self.feed_count_timer.reset()
        self.count_changed_timer.reset()
        self.behavior = self.idle

    # ---------- 8 behaviors ----------

    def idle(self):
        if self.did_behavior_change:
            self.stand_up()
        self.update_eyes()
        self.update_behavior()
        self.update_pet_count()
        self.update_feed_count()

    def go_to_sleep(self):
        if self.did_behavior_change:
            self.eyes = self.TIRED_EYES
            self.sit_down()
            self.move_head(self.HEAD_DOWN_ANGLE)
            self.eyes = self.SLEEPING_EYES
            self.ev3.speaker.play_file(SoundFile.SNORING)
        if self.touch_sensor.pressed() and Button.CENTER in self.ev3.buttons.pressed():
            self.count_changed_timer.reset()
            self.behavior = self.wake_up

    def wake_up(self):
        if self.did_behavior_change:
            self.eyes = self.TIRED_EYES
            self.ev3.speaker.play_file(SoundFile.DOG_WHINE)
            self.move_head(self.HEAD_UP_ANGLE)
            self.sit_down()
            self.stretch()
            wait(1000)
            self.stand_up()
            self.behavior = self.idle

    def act_playful(self):
        if self.did_behavior_change:
            self.eyes = self.NEUTRAL_EYES
            self.stand_up()
            self.playful_bark_interval = 0
        if self.update_pet_count():
            self.behavior = self.idle
        if self.playful_timer.time() > self.playful_bark_interval:
            self.ev3.speaker.play_file(SoundFile.DOG_BARK_2)
            self.playful_timer.reset()
            self.playful_bark_interval = urandom.randint(4, 8) * 1000

    def act_angry(self):
        if self.did_behavior_change:
            self.eyes = self.ANGRY_EYES
            self.ev3.speaker.play_file(SoundFile.DOG_GROWL)
            self.stand_up()
            wait(1500)
            self.ev3.speaker.play_file(SoundFile.DOG_BARK_1)
            self.pet_count -= 1
            self.behavior = self.idle

    def act_hungry(self):
        if self.did_behavior_change:
            self.eyes = self.HURT_EYES
            self.sit_down()
            self.ev3.speaker.play_file(SoundFile.DOG_WHINE)
        if self.update_feed_count():
            self.behavior = self.idle
        if self.update_pet_count():
            self.behavior = self.act_angry

    def go_to_bathroom(self):
        if self.did_behavior_change:
            self.eyes = self.SQUINTY_EYES
            self.stand_up()
            wait(100)
            self.right_leg_motor.run_target(100, self.STRETCH_ANGLE)
            wait(800)
            self.ev3.speaker.play_file(SoundFile.HORN_1)
            wait(1000)
            for _ in range(3):
                self.right_leg_motor.run_angle(100, 20)
                self.right_leg_motor.run_angle(100, -20)
            self.right_leg_motor.run_target(100, self.STAND_UP_ANGLE)
            self.feed_count = 1
            self.behavior = self.idle

    def act_happy(self):
        if self.did_behavior_change:
            self.eyes = self.HEART_EYES
            self.sit_down()
            for _ in range(3):
                self.ev3.speaker.play_file(SoundFile.DOG_BARK_1)
                self.hop()
            wait(500)
            self.sit_down()
            self.reset()

    # ---------- actions ----------

    def sit_down(self):
        self.left_leg_motor.run(-50)
        self.right_leg_motor.run(-50)
        wait(1000)
        self.left_leg_motor.stop()
        self.right_leg_motor.stop()
        wait(100)

    def stand_up(self):
        self.left_leg_motor.run_target(100, self.HALF_UP_ANGLE, wait=False)
        self.right_leg_motor.run_target(100, self.HALF_UP_ANGLE)
        while not self.left_leg_motor.control.done():
            wait(100)
        self.left_leg_motor.run_target(50, self.STAND_UP_ANGLE, wait=False)
        self.right_leg_motor.run_target(50, self.STAND_UP_ANGLE)
        while not self.left_leg_motor.control.done():
            wait(100)
        wait(500)

    def stretch(self):
        self.stand_up()
        self.left_leg_motor.run_target(100, self.STRETCH_ANGLE, wait=False)
        self.right_leg_motor.run_target(100, self.STRETCH_ANGLE)
        while not self.left_leg_motor.control.done():
            wait(100)
        self.ev3.speaker.play_file(SoundFile.DOG_WHINE)
        self.left_leg_motor.run_target(100, self.STAND_UP_ANGLE, wait=False)
        self.right_leg_motor.run_target(100, self.STAND_UP_ANGLE)
        while not self.left_leg_motor.control.done():
            wait(100)

    def hop(self):
        self.left_leg_motor.run(500)
        self.right_leg_motor.run(500)
        wait(275)
        self.left_leg_motor.hold()
        self.right_leg_motor.hold()
        wait(275)
        self.left_leg_motor.run(-50)
        self.right_leg_motor.run(-50)
        wait(275)
        self.left_leg_motor.stop()
        self.right_leg_motor.stop()

    # ---------- properties ----------

    @property
    def behavior(self):
        return self._behavior

    @behavior.setter
    def behavior(self, value):
        if self._behavior != value:
            self._behavior = value
            self._behavior_changed = True

    @property
    def did_behavior_change(self):
        if self._behavior_changed:
            self._behavior_changed = False
            return True
        return False

    @property
    def eyes(self):
        return self._eyes

    @eyes.setter
    def eyes(self, value):
        if value != self._eyes:
            self._eyes = value
            self.ev3.screen.load_image(value)

    # ---------- update helpers ----------

    def update_behavior(self):
        if self.pet_count == self.pet_target and self.feed_count == self.feed_target:
            self.behavior = self.act_happy
        elif self.pet_count > self.pet_target and self.feed_count < self.feed_target:
            self.behavior = self.act_angry
        elif self.pet_count < self.pet_target and self.feed_count > self.feed_target:
            self.behavior = self.go_to_bathroom
        elif self.pet_count == 0 and self.feed_count > 0:
            self.behavior = self.act_playful
        elif self.feed_count == 0:
            self.behavior = self.act_hungry

    def update_eyes(self):
        if self.eyes_timer_1.time() > self.eyes_timer_1_end:
            self.eyes_timer_1.reset()
            if self.eyes == self.SLEEPING_EYES:
                self.eyes_timer_1_end = urandom.randint(1, 5) * 1000
                self.eyes = self.TIRED_RIGHT_EYES
            else:
                self.eyes_timer_1_end = 250
                self.eyes = self.SLEEPING_EYES
        if self.eyes_timer_2.time() > self.eyes_timer_2_end:
            self.eyes_timer_2.reset()
            if self.eyes != self.SLEEPING_EYES:
                self.eyes_timer_2_end = urandom.randint(1, 10) * 1000
                if self.eyes != self.TIRED_LEFT_EYES:
                    self.eyes = self.TIRED_LEFT_EYES
                else:
                    self.eyes = self.TIRED_RIGHT_EYES

    def update_pet_count(self):
        changed = False
        petted = self.touch_sensor.pressed()
        if petted and petted != self.prev_petted:
            self.pet_count += 1
            self.count_changed_timer.reset()
            if self.behavior != self.act_hungry:
                self.eyes = self.SQUINTY_EYES
                self.ev3.speaker.play_file(SoundFile.DOG_SNIFF)
            changed = True
        self.prev_petted = petted
        return changed

    def update_feed_count(self):
        color = self.color_sensor.color()
        changed = False
        if color is not None and color != Color.BLACK and color != self.prev_color:
            self.feed_count += 1
            changed = True
            self.count_changed_timer.reset()
            self.prev_color = color
            self.eyes = self.SQUINTY_EYES
            self.ev3.speaker.play_file(SoundFile.CRUNCHING)
        return changed

    def monitor_counts(self):
        if self.pet_count_timer.time() > 15000:
            self.pet_count_timer.reset()
            self.pet_count = max(0, self.pet_count - 1)
        if self.feed_count_timer.time() > 15000:
            self.feed_count_timer.reset()
            self.feed_count = max(0, self.feed_count - 1)
        # 30 秒無互動 → 睡覺
        if self.count_changed_timer.time() > 30000:
            self.count_changed_timer.reset()
            self.behavior = self.go_to_sleep

    def run(self):
        self.sit_down()
        self.adjust_head()
        self.eyes = self.SLEEPING_EYES
        self.reset()
        while True:
            self.monitor_counts()
            self.behavior()
            wait(100)


# 蓋掉 TEAR 圖的淚滴，做成瞇眼表情
Puppy.SQUINTY_EYES.draw_box(120, 60, 140, 85, fill=True, color=Color.WHITE)

puppy = Puppy()
puppy.run()