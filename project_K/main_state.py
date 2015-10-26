#__author__ = 'samsung'

import random
import os
import sys
from builtins import print
from tkinter.constants import RIGHT

from pico2d import *
import game_framework


import title_state


name = "MainState"

aircraft = None
background = None
enemy01 = None
boss01 = None
font = None

enemy_count=0
posX, posY = 0, 0
shot_count = 0

class background:
    def __init__(self):
        self.image = load_image('background02.png')

    def draw(self):
        self.image.draw(300, 400)

class aircraft:
    image = None

    STOP, GO = 0,1

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.stateU = self.STOP
        self.stateD = self.STOP
        self.stateL = self.STOP
        self.stateR = self.STOP
        #if aircraft.image == None:
        aircraft.image = load_image('aircraft00.png')
        self.dir = 1
    def handle_event(self, event):

        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            pass
        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            self.stateU = self.GO
        elif(event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            self.stateU = self.STOP

        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            self.stateD = self.GO
        elif(event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            self.stateD = self.STOP

        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            self.stateL = self.GO
        elif(event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            self.stateL = self.STOP
        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            self.stateR = self.GO
        elif(event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            self.stateR = self.STOP


    def update(self):
        global posX,posY
        self.frame = (self.frame + 1) % 8
        if self.stateR == self.GO:
            self.x = min(600, self.x + 3)

        if self.stateL == self.GO:
            self.x = max(0, self.x - 3)

        if self.stateU == self.GO:
            self.y = min(800, self.y + 3)

        if self.stateD == self.GO:
            self.y = max(0, self.y - 3)

        posX = self.x
        posY = self.y


    def draw(self):
        self.image.draw(self.x, self.y, 100, 100)

class enemy01:
    image = None

    def __init__(self):
        global enemy_count
        enemy_count += 1
        #self.x, self.y = random.randint(1, 5)*100, ((int)(enemy_count/4)+1) * 600
        self.x, self.y = random.randint(1, 5)*100, 800
        self.isCrash = False

        #if enemgy01.image == None
        enemy01.image = load_image('enemy01.png')

    def update(self):
        global posX, posYg

        self.y -= 2

        if self.y < 0:
            self.y = 800
            self.x = random.randint(1, 5)*100
            self.isCrash = False

        if (posX+30 > self.x-50) and (posY+30 > self.y-50) and (posX-30 < self.x+50) and (posY-30 < self.y+50):
            if self.isCrash == False:
                self.isCrash = True
                print('crash')

    def draw(self):
        self.image.draw(self.x, self.y, 100, 100)


class boss01:
    def __init__(self):
        self.image = load_image('boss_enemy01.png')

    def draw(self):
        self.image.draw(300, 780)


class bullet:
    def __init__(self):
        bullet.image = load_image('bullet.png')
        #self.y = 300
    def update(self):
        #self.y += 1
        pass
    def draw(self):
        self.image.draw(287, 687)

class shot:
    def __init__(self):
        global posX, posY
        global shooting
        shot.image = load_image('shot00.png')
        #self.x, self.y = posX, posY
        self.x, self.y = posX + 0, posY + 65

    def update(self):
         self.y += 5
         if self.y > 800:
             self.x, self.y = posX + 0, posY + 65

    def draw(self):
        self.image.draw(self.x, self.y)

def enter():
    global aircraft, background, enemy01, boss01, bullet, shot
    background = background()
    aircraft = aircraft()
    enemy01 = enemy01()
    boss01 = boss01()
    bullet = bullet()
    shot = shot()

def exit():
    global aircraft, background, enemy01, boss01, bullet, shot
    del(aircraft)
    del(background)
    del(enemy01)
    del(boss01)
    del(bullet)
    del(shot)

def pause():
    pass


def resume():
    pass


def handle_events():

    global moving
    global aircraft
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            moving = False
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(title_state)
            moving = False
        else:
            aircraft.handle_event(event)


open_canvas()


enemy01_team = [enemy01() for i in range(4)]
shots = [shot() for i in range(100)]

def update():
    aircraft.update()

    for enemy01 in enemy01_team:
        enemy01.update()
    for shot in shots:
        shot.update()
    bullet.update()
def draw():
    clear_canvas()
    background.draw()
    aircraft.draw()
    for enemy01 in enemy01_team:
        enemy01.draw()
    for shot in shots:
        shot.draw()
    boss01.draw()
    bullet.draw()


    update_canvas()


close_canvas()