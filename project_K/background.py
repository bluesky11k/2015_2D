
import random
from pico2d import *


class Background:
    MOVE_PER_SEC = 100

    def __init__(self):
        self.image = load_image('resource/background.png')

        self.bgm = load_music('resource/backgruoundmusic.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

        self.y = 0


    def update(self, frame_time):
        speed = frame_time * self.MOVE_PER_SEC
        self.y += speed
        if self.y >= 800:
            self.y = 0

    def draw(self): # 2800 3840
        self.image.clip_draw
        self.image.clip_draw(0, int(self.y), 1400, int(1920-self.y)+1, 700, int((1920 - self.y)/2))



