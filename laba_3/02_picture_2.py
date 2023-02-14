import pygame
from pygame.draw import *

def build_parabola(A, B, V, x):
    x1, y1 = A
    x2, y2 = B
    xv, yv = V

    a = (y1-y2) / (x1**2 - x2**2 - 2*xv*(x1-x2))
    b = -2*xv*a
    c = y1 - a*(x1**2 - 2*xv*x1)

    return a*x**2 + b*x + c

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 600))

#background
rect(screen, (179,134,148), (0, 400, 800, 200))
rect(screen, (254,213,148), (0, 270, 800, 130))
rect(screen, (254,213,196), (0, 140, 800, 130))
rect(screen, (254,213,162), (0, 0, 800, 140))

#sun
circle(screen, (252,238,33), (400, 140), 50)

#back mountains
points = [(0,280),(10,250)]

for x in range(10, 180):
    points.append((x, build_parabola((10,250), (180,130), (10,250), x)))

points.extend([(180,130),(200,140),(210,160),(320,250),
               (390,240),(410,257),(450,230),(470,240),
               (490,210)])

for x in range(490, 570):
    points.append((x, build_parabola((490,210), (570,130), (490,210), x)))

for x in range(570, 600):
    points.append((x, build_parabola((570,130), (600,120), (589,110), x)))

points.extend([(600,120),(620,160), (650,150)])

for x in range(650, 720):
    points.append((x, build_parabola((650,150), (720,220), (640,150), x)))

points.extend([(720,220),(740,200),(800,240)])

polygon(screen, (252,152,49), points)
aalines(screen, (252,152,49), True, points)

#forward mountains
points_for = [(0,410),(0,305),(10,305)]

for x in range(20, 160):
    points_for.append((x, build_parabola((20,315), (160,390), (76,250), x)))

points_for.extend([(190,320),(250,350),(280,280),(350,300),(410,350)])

for x in range(490, 591):
    points_for.append((x, build_parabola((490,330), (590,270), (570,260), x)))

for x in range(590, 671):
    points_for.append((x, build_parabola((590,270), (670,320), (670,330), x)))

points_for.extend([(700,280),(720,300),(740,270),(770,280),(800,230),(800,400)])

polygon(screen, (172,67,52), points_for)
aalines(screen, (172,67,52), True, points_for)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event == pygame.QUIT:
            finished = True
pygame.quit()
                                 
