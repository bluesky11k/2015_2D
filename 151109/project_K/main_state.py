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
EnemySmall = None
EnemyBoss = None
font = None

EnemySmall_count=0
posX, posY = 0, 0
aircraftShot_count = 0
aircraftShot = list()


class background:
    def __init__(self):
        self.image = load_image('resource/background02.png')

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
        aircraft.image = load_image('resource/aircraft.png')
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
        global posX, posY
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

    def aircraftShooting(self):
        aircraftshotnow = aircraftShot(self.x, self.y)
        aircraftShot.append(aircraftshotnow)

class EnemySmall:
    image = None

    def __init__(self):
        global EnemySmall_count
        EnemySmall_count += 1
        #self.x, self.y = random.randint(1, 5)*100, ((int)(enemy_count/4)+1) * 600
        self.x, self.y = random.randint(1, 5)*100, 800
        self.isCrash = False

        #if enemgy01.image == None
        EnemySmall.image = load_image('resource/enemy01.png')

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


class EnemyBoss:
    def __init__(self):
        self.image = load_image('resource/EnemyBoss.png')

    def draw(self):
        self.image.draw(300, 780)


class enemybarrage:
    def __init__(self):
        #self.x, self.y = x, y
        enemybarrage.image = load_image('resource/barrageitem.png')

    def update(self):
        pass
        # self.y += 5
        # if(self.y > 800):
        #     self.y = 0

    def draw(self):
        self.image.draw(287, 687)
        #self.image.draw(self.x, self.y + 30)


class aircraftShot:
    global aircraft

    def __init__(self):
        global posX, posY
        global shooting
        aircraftShot.image = load_image('resource/shot00.png')
        self.x, self.y = posX + 0, posY + 65

    def update(self):
         self.y += 5
         if self.y > 800:
             self.x, self.y = posX + 0, posY + 65

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x-50, self.y-50, self.x+50, self.y+50


def enter():
    global aircraft, background, EnemySmall, EnemyBoss, enemybarrage, aircraftShot
    background = background()
    aircraft = aircraft()

    EnemySmall = EnemySmall()
    EnemyBoss = EnemyBoss()
    enemybarrage = enemybarrage()
    aircraftShot = aircraftShot()


def exit():
    global aircraft, background, EnemySmall, EnemyBoss, enemybarrage, aircraftShot
    del(aircraft)
    del(background)
    del(EnemySmall)
    del(EnemyBoss)
    del(enemybarrage)
    del(aircraftShot)


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


EnemySmall_team = [EnemySmall() for i in range(4)]
aircraftShotList = [aircraftShot() for i in range(100)]


def update():
    aircraft.update()

    for EnemySmall in EnemySmall_team:
        EnemySmall.update()
    for aircraftShot in aircraftShotList:
        aircraftShot.update()
    enemybarrage.update()


def draw():
    clear_canvas()
    background.draw()
    aircraft.draw()
    for EnemySmall in EnemySmall_team:
        EnemySmall.draw()
    for aircraftShot in aircraftShotList:
        aircraftShot.draw()
    EnemyBoss.draw()
    enemybarrage.draw()

    update_canvas()


close_canvas()