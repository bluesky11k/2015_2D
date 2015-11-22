#__author__ = 'KimSeunghyeon'
import random

from pico2d import *

#
# class Background:
#     # PIXEL_PER_METER = (10.0 / 0.3)           # (10.0 / 0.3) = 10 pixel 30 cm
#     # SCROLL_SPEED_KMPH = 100.0                    # Km / Hour
#     # SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
#     # SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
#     # SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)
#
#     def __init__(self, w, h):
#         self.image = load_image('resource/background02.png')
#         self.up = 0
#         self.bottom = 0
#         self.screen_width = w
#         self.screen_height = h
#
#     def get_bb(self):
#         pass
#
#     def draw(self):
#         y = int (self.up)
#         h = min (self.image.h - y, self.screen_height)
#         self.image.clip_draw_to_origin (0, y, self.screen_width, h, 0, 0)
#         self.image.clip_draw_to_origin (0, 0, self.screen_width, self.screen_height - h, 0, h)
#
#     def update(self, frame_time):
#         self.up = (self.up + frame_time * self.speed) % self.image.h
#
#     def draw_bb(self):
#         pass
#
#     def stop(self):
#         return
#
