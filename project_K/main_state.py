#__author__ = 'KimSeunghyeon'

import random
import os
import sys
import math

# import Boy class from boy.py
from pico2d import *
from tanmak import *
from builtins import print
from tkinter.constants import RIGHT
from tile import TileMap

import game_framework
import title_state

name = "MainState"

aircraft = None
background = None
enemy_small = None
enemy_boss = None
font = None

EnemySmall_count = 0
posX, posY = 0, 0
aircraftshot_count = 0
aircraft_shot = []
updateI = 0

C_Barrage = 20
C_Barrage_Speed = 1
C_Barrage_Odd = 1
N_Barrage = 20 # same as C_Barrage
N_Theta = 5
N_X = 0
N_Y = 1
#circle missile
(cvx, cvy) = init_circle_bullets(C_Barrage, C_Barrage_Speed, C_Barrage_Odd)
#nway missile
(nvx, nvy) = init_nway_bullets(N_X, N_Y, N_Theta, N_Barrage)
#guided missile
(gvx, gvy) = init_nway_bullets(N_X, N_Y, N_Theta, N_Barrage)


#def create_world():
    # global boy, grass, balls, big_balls
    # boy = Boy()
    # big_balls = [BigBall() for i in range(10)]
    # balls = [Ball() for i in range(10)]
    # balls = big_balls + balls
    # grass = Grass()


#def destroy_world():
    # global boy, grass, balls, big_balls
    # del(boy)
    # del(balls)
    # del(grass)
    # del(big_balls)


def init_g():
    global gvx, gvy
    (gvx, gvy) = init_nway_bullets(N_X, N_Y, N_Theta, N_Barrage)


class Background:
    def __init__(self):
        self.image = load_image('resource/background02.png')

    def draw(self):
        self.image.draw(300, 400)

    # PIXEL_PER_METER = (10.0 / 0.3)           # (10.0 / 0.3) = 10 pixel 30 cm
    # SCROLL_SPEED_KMPH = 100.0                # Km / Hour
    # SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    # SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    # SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)
    #
    # def __init__(self, w, h):
    #     self.image = load_image('resource/background02.png')
    #     self.speed = 0
    #     self.up = 0
    #     self.bottom = 0
    #     self.screen_width = w
    #     self.screen_height = h
    #
    # def draw(self):
    #     y = int(self.up)
    #     h = min(self.image.h - y, self.screen_height)
    #     self.image.clip_draw_to_origin (0, y, self.screen_width, h, 0, 0)
    #     self.image.clip_draw_to_origin (0, 0, self.screen_width, self.screen_height - h, 0, h)
    #
    # def get_bb(self):
    #     pass
    #
    # def update(self, frame_time):
    #     self.up = (self.up + frame_time * self.speed) % self.image.h
    #
    # def draw_bb(self):
    #     pass
    #
    # def handle_event(self, event):
    #     if event.type == SDL_KEYDOWN:
    #         if event.key == SDLK_UP: self.speed -= Background.SCROLL_SPEED_PPS


class Aircraft:
    # PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    # MOVE_SPEED_KMPH = 20.0                    # Km / Hour
    # MOVE_SPEED_MPM = (MOVE_SPEED_KMPH * 1000.0 / 60.0)
    # MOVE_SPEED_MPS = (MOVE_SPEED_MPM / 60.0)
    # MOVE_SPEED_PPS = (MOVE_SPEED_MPS * PIXEL_PER_METER)
    #
    # TIME_PER_ACTION = 0.5
    # ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    # FRAMES_PER_ACTION = 8

    image = None

    STOP, GO = 0, 1

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.stateU = self.STOP
        self.stateD = self.STOP
        self.stateL = self.STOP
        self.stateR = self.STOP
        if Aircraft.image == None:
            Aircraft.image = load_image('resource/aircraft00.png')
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
        self.image.draw(self.x, self.y, 59, 55)

    def aircraft_shooting(self):
        aircraft_shot_now = aircraft_shot(self.x, self.y)
        aircraft_shot.append(aircraft_shot_now)


class AircraftShot:
    global aircraft

    def __init__(self):
        global posX, posY
        global shooting
        AircraftShot.image = load_image('resource/shot00.png')
        self.x, self.y = posX + 0, posY + 35

    def update(self):
        self.y += 5
        if self.y > 800:
            self.x, self.y = posX + 0, posY + 35


    def draw(self):
        self.image.draw(self.x, self.y, 8, 15)

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50


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
        global posX, posY

        self.y -= 2

        if self.y < 0:
            self.y = 800
            self.x = random.randint(1, 5)*100
            self.isCrash = False

        if (posX+30 > self.x-50) and (posY+30 > self.y-50) and (posX-30 < self.x+50) and (posY-30 < self.y+50):
            if self.isCrash == False:
                self.isCrash = True
                print('crash-Enemy')

    def draw(self):
        self.image.draw(self.x, self.y, 75, 75)


class EnemyBoss:
    def __init__(self):
        self.image = load_image('resource/EnemyBoss.png')

    def draw(self):
        self.image.draw(300, 780)


class EnemyBarrage:

    def __init__(self):
        self.x, self.y = 300, 780 # boss
        EnemyBarrage.image = load_image('resource/barrageitem.png')
        self.which = 'c'
        self.isCrash = False

    def update(self, i, airx, airy): #airx and y = aircraft x and y
        global posX, posY
        if(self.which == 'c'):
            self.x -= cvx[i]
            self.y -= cvy[i]
            if (posX+30 > self.x-50) and (posY+30 > self.y-50) and (posX-30 < self.x+50) and (posY-30 < self.y+50):
                if self.isCrash == False:
                    self.isCrash = True
                    print('crash-Circle Bullet')

        if(self.which == 'n'):
            self.x -= nvx[i]
            self.y -= nvy[i]

            if (posX+30 > self.x-50) and (posY+30 > self.y-50) and (posX-30 < self.x+50) and (posY-30 < self.y+50):
                if self.isCrash == False:
                    self.isCrash = True
                    print('crash-Nway Bullet')

        if(self.which == 'g'):
            vx_new, vy_new = update_guided_bullets(self.x, self.y, gvx[i], gvy[i], airx, airy)

            if(airy + 50 < self.y):
                gvx[i] = vx_new
                gvy[i] = vy_new

            self.x -= gvx[i]
            self.y -= (gvy[i])

            if (posX+30 > self.x-50) and (posY+30 > self.y-50) and (posX-30 < self.x+50) and (posY-30 < self.y+50):
                if self.isCrash == False:
                    self.isCrash = True
                    print('crash-Guided Bullet')


        x_dist = self.x - 300
        y_dist = self.y - 780

        if x_dist * x_dist + y_dist * y_dist > 780 * 780:
            self.y = 780
            self.x = 300

            if(self.which == 'n'):
                self.which = 'c'
            elif(self.which == 'c'):
                #init_g()
                self.which = 'g'
            elif(self.which == 'g'):
                self.which = 'n'



    def draw(self):
        self.image.draw(self.x, self.y, 13, 13)
        self.isCrash = False


def enter():
    global aircraft, background, enemy_small, enemy_boss, enemy_barrage, aircraft_shot
    #create_world()

    background = Background()
    enemy_boss = EnemyBoss()
    aircraft = Aircraft()
    enemy_small = EnemySmall()
    enemy_barrage = EnemyBarrage()
    aircraft_shot = AircraftShot()


def exit():
    global aircraft, background, enemy_small, enemy_boss, enemy_barrage, aircraft_shot
    #destroy_world()
    del(aircraft)
    del(background)
    del(enemy_boss)
    del(enemy_small)
    del(enemy_barrage)
    del(aircraft_shot)


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

enemybarrage_List = [EnemyBarrage() for i in range(N_Barrage)]
enemysmall_List = [EnemySmall() for i in range(4)]
aircraftshot_List = [AircraftShot() for i in range(100)]


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def update():
    global updateI

    aircraft.update()

    for enemy_small in enemysmall_List:
        enemy_small.update()

    aircraftshot_List[(int)(updateI/15)].y = 0

    for aircraft_shot in aircraftshot_List:
        aircraft_shot.update()

    i = 0
    for enemy_barrage in enemybarrage_List: # aircraft x,y attribute to implement guided missile
        enemy_barrage.update(i, aircraft.x, aircraft.y)
        i += 1

    if updateI < 999:
        updateI += 1


def draw():
    clear_canvas()
    background.draw()
    aircraft.draw()
    enemy_boss.draw()


    for enemy_small in enemysmall_List:
        enemy_small.draw()

    for aircraft_shot in aircraftshot_List:
        aircraft_shot.draw()

    for enemy_barrage in enemybarrage_List:
        enemy_barrage.draw()

    update_canvas()

close_canvas()