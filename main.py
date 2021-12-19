import math
import pygame as pg

WIDTH = 800 # ширина
HEIGHT = 800 # высота
FPS = 60

# цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
Yellow = (255, 255, 0)

x = WIDTH / 4
y = HEIGHT / 4
x0 = WIDTH // 2
y0 = HEIGHT // 2
M0 = 800 #Масса Солнца

r = 0
x = 100
y = 290
vx = 0.1
vy = 1.5
ax = 0
ay = 0

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

    vx += ax
    vy += ay

    x += vx
    y += vy

    print(x, y)

    pg.draw.circle(screen, WHITE, (x, y), 6)
    pg.draw.circle(screen, Yellow, (x0, y0), 19)
    pg.display.update()

pg.quit()

