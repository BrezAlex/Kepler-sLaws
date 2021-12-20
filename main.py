import math
import pygame as pg

WIDTH = 800 # ширина
HEIGHT = 800 # высота
FPS = 120

# цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
Yellow = (255, 255, 0)

x = WIDTH / 5
y = HEIGHT / 5

r = 0
x = 100
y = 290
vx = 0.1
vy = 1.1
ax = 0
ay = 0
m = 10 #масса планеты

#Солнце
vx0 = 0
vy0 = 0
ax0 = 0
ay0 = 0
x0 = WIDTH / 2
y0 = HEIGHT / 2
M0 = 400

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Planets")
clock = pg.time.Clock()

running = True

while running:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((0, 0, 0))

    r = math.sqrt((x - x0) ** 2 + (y - y0) ** 2)
    ax = M0 * (x0 - x) / r ** 3
    ay = M0 * (y0 - y) / r ** 3

    ax0 = m * (x0 - x) / r ** 3
    ay0 = m * (y0 - y) / r ** 3


    vx += ax
    vy += ay

    vx0 += ax0
    vy0 += ay0

    x += vx
    y += vy

    x0 += vx0
    y0 += vy0

    # print(x, y)

    pg.draw.circle(screen, WHITE, (x, y), 6)
    pg.draw.circle(screen, Yellow, (x0, y0), 19)
    pg.display.update()

pg.quit()

