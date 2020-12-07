import pygame as pg
from settings import *
from numpy import array as vec


screen = pg.display.set_mode(res)
clock = pg.time.Clock()


def line(a, b, c, d, color):
    pg.draw.line(screen, color, (a, b), (c, d))


def rect(x, y, w, h, color, l_w=0):
    x, y, w, h = int(x), int(y), int(w), int(h)

    pg.draw.rect(screen, color, pg.Rect(x, y, w, h), l_w)


def polygon(points, color, w=0):
    pg.draw.polygon(screen, color, points, w)


class Camera:
    def __init__(self, x, y, w, h, c_w, c_h, speed = 0):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.c_w, self.c_h = c_w, c_h
        self.dir = vec([0, 0])
        self.speed = speed

        self.childs = []

    def draw(self):
        rect(self.x + width / 2 - self.w / 2 - self.x,
             self.y + height / 2 - self.w / 2 - self.y,
             self.w, self.h,
             (255, 255, 255), 1)

    def move(self):
        self.x += self.dir[0] * self.speed
        self.y += self.dir[1] * self.speed


class Rect:
    def __init__(self, x, y, w, h, color):
        self.x, self.y, self.w, self.h, self.c = x, y, w, h, color

    def draw(self, cam):
        if cam.x - cam.c_w / 2 - self.w <= self.x <= cam.x + cam.c_w / 2 + self.w and\
                cam.y - cam.c_h / 2 - self.h <= self.y <= cam.y + cam.c_h / 2 + self.h:

            rect(self.x + width / 2 - self.w / 2 - cam.x,
                 self.y + height / 2 - self.w / 2 - cam.y,
                 self.w, self.h,
                 self.c)

            offset = vec([self.x, self.y]) - vec([cam.x, cam.y])
            offset[0] = int(offset[0])
            offset[1] = int(offset[1])

            
            
            rect(self.x + width / 2 - self.w / 2 - cam.x + offset[0],
                 self.y + height / 2 - self.h / 2 - cam.y + offset[1],
                 self.w, self.h,
                 self.c)


player = Camera(0, 0, 10, 10, width, height, 1)

objs = [
    Rect(-40, -20, 20, 20, (255, 255, 255))
]


while True:
    clock.tick(60)

    screen.fill((0, 0, 0))

    for e in pg.event.get():
        if e.type == pg.QUIT:
            exit()

        if e.type == pg.KEYDOWN:
            if e.key == pg.K_UP:
                player.dir[1] = -1

            if e.key == pg.K_RIGHT:
                player.dir[0] = 1

            if e.key == pg.K_DOWN:
                player.dir[1] = 1

            if e.key == pg.K_LEFT:
                player.dir[0] = -1

        if e.type == pg.KEYUP:
            if e.key == pg.K_UP:
                player.dir[1] = 0

            if e.key == pg.K_RIGHT:
                player.dir[0] = 0

            if e.key == pg.K_DOWN:
                player.dir[1] = 0

            if e.key == pg.K_LEFT:
                player.dir[0] = 0

    player.move()
    player.draw()

    for o in objs:
        o.draw(player)

    pg.display.flip()
