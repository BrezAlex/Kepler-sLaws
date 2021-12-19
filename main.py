import math

import pygame as pg

WIDTH = 700 # ширина
HEIGHT = 700 # высота
FPS = 30
# цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
Yellow = (255, 255, 0)

x0 = WIDTH / 4
y0 = HEIGHT / 4
M = 1.99 * 10 ** 30 # Масса Солнца кг
G = 6.67 * 10 ** -11 # Гравитационная постоянная кг
m = 3.33 * 10 ** 23 # Масса Меркурия кг
R = 2439 * 10 ** 3 # Радиус Меркурия км
alpha = 45
t = 0
v0 = 10
dt = 0.1



print(M, G, v0)

speed = 5

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

    r = math.sqrt(x0 ** 2 + y0 ** 2)
    t += dt
    vx = v0 * math.cos(alpha) * dt
    vy = v0 * math.sin(alpha) * dt
    screen.fill((0, 0, 0))
    x0 += vx
    y0 += vy
    pg.draw.circle(screen, WHITE, (x0, y0), 6)
    pg.draw.circle(screen, Yellow, (WIDTH / 2, HEIGHT / 2), 19)
    pg.display.update()

pg.quit()

