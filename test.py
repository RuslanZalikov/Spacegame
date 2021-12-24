import pygame as pg
from circle import Circle

circ = Circle(30)
kx = 0; ky = 0
kxx = 1; kyy = 1
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

pg.init()
pg.display.set_caption("Spacegame")
gameScreen = pg.display.set_mode((640, 360))
gameScreen.fill((black))
runGame = True
pg.display.update()
k = False
pg.draw.rect(gameScreen, white, (160, 90, 320, 180))
pg.display.update()
while runGame:
    centralx = circ.radius
    centraly = circ.radius
    if (centralx + circ.radius + kx >= 640):
        kxx = -1
    if (centralx - circ.radius + kx <= 0):
        kxx = 1
    if (centraly + circ.radius + ky >= 360):
        kyy = -1
    if (centraly - circ.radius + ky <= 0):
        kyy = 1
    kx += kxx
    ky += kyy
    for i in pg.event.get():
        if i.type == pg.QUIT:
            runGame = False
        if i.type == pg.MOUSEBUTTONUP:
            k = True
            kx, ky = pg.mouse.get_pos()
            kx -= circ.radius
            ky -= circ.radius
    if k:
        pg.draw.circle(gameScreen, black, (centralx + kx - kxx, centraly + ky - kyy), circ.radius)
        pg.draw.circle(gameScreen, green, (centralx + kx, centraly + ky), circ.radius)
        pg.display.update()