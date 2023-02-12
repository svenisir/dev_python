import pygame
import numpy as np
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 402))

#sand
rect(screen, (238,246,12), (0, 280, 600, 122))

#whater
rect(screen, (68,35,223), (0, 180, 600, 100))

#sky
rect(screen, (161,245,255), (0, 0, 600, 180))

#sun
circle(screen, (255,247,29), (535, 60), 40)

#cloud
circle(screen, (255,255,255), (130, 45), 20)
circle(screen, (170,170,170), (130, 45), 20, 1)
circle(screen, (255,255,255), (150, 45), 20)
circle(screen, (170,170,170), (150, 45), 20, 1)
circle(screen, (255,255,255), (170, 45), 20)
circle(screen, (170,170,170), (170, 45), 20, 1)
circle(screen, (255,255,255), (115, 63), 20)
circle(screen, (170,170,170), (115, 63), 20, 1)
circle(screen, (255,255,255), (140, 65), 20)
circle(screen, (170,170,170), (140, 65), 20, 1)
circle(screen, (255,255,255), (160, 65), 20)
circle(screen, (170,170,170), (160, 65), 20, 1)
circle(screen, (255,255,255), (180, 65), 20)
circle(screen, (170,170,170), (180, 65), 20, 1)

#boat
rect(screen, (186,80,5), (350, 200, 150, 35))
rect(screen, (157,70,59), (350, 200, 150, 35), 1)
rect(screen, (0,0,0), (400, 100, 10, 100))
polygon(screen, (222,213,153), [(410, 100), (430, 150), (460, 150)])
polygon(screen, (133,130,96), [(410, 100), (430, 150), (460, 150)], 1)
polygon(screen, (222,213,153), [(410, 198), (430, 150), (460, 150)])
polygon(screen, (133,130,96), [(410, 199), (430, 150), (460, 150)], 1)
circle(screen, (186,80,5), (350, 200), 35, 0, draw_bottom_left=True)
circle(screen, (157,70,59), (350, 200), 35, 1, draw_bottom_left=True)
polygon(screen, (186,80,5), [(500, 200), (500, 234), (570, 200)])
polygon(screen, (157,70,59), [(499, 200), (499, 234), (570, 200)], 1)
circle(screen, (0,0,0), (515, 212), 10)
circle(screen, (255,255,255), (515, 212), 7)

#umbrella
rect(screen, (227,130,25), (90, 260, 5, 120)) 
rect(screen, (244,81,81), (90, 230, 5, 30))
polygon(screen, (244,81,81), [(90, 230), (90, 260), (40, 260)])
polygon(screen, (157,52,52), [(90, 230), (90, 260), (40, 260)], 1)
polygon(screen, (244,81,81), [(95, 230), (95, 260), (145, 260)])
polygon(screen, (157,52,52), [(95, 230), (95, 260), (145, 260)], 1)
line(screen, (180,60,60), (90, 230), (55, 260), 1)
line(screen, (180,60,60), (90, 230), (70, 260), 1)
line(screen, (180,60,60), (90, 230), (85, 260), 1)
line(screen, (180,60,60), (95, 230), (130, 260), 1)
line(screen, (180,60,60), (95, 230), (115, 260), 1)
line(screen, (180,60,60), (95, 230), (100, 260), 1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event == pygame.QUIT:
            finished = True

pygame.quit()
