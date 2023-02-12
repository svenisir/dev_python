import pygame
from pygame.draw import *

#Инициализируем библиотеку
pygame.init()

#Создаём окно
FPS = 30
screen = pygame.display.set_mode((400, 400))

#backdraund
rect(screen, (217, 217, 217), (0, 0, 400, 400))

#face
circle(screen, (255, 255, 0), (200,200), 100)
circle(screen, (0, 0, 0), (200,200), 100, 1)

#left eye
circle(screen, (255, 0, 0), (150,180), 20)
circle(screen, (0, 0, 0), (150,180), 20, 1)
circle(screen, (0, 0, 0), (150,180), 8)

#right eye
circle(screen, (255, 0, 0), (250,180), 15)
circle(screen, (0, 0, 0), (250,180), 15, 1)
circle(screen, (0, 0, 0), (250,180), 8)

#eyebrows
polygon(screen, (0, 0, 0), [(103, 116), (98, 124),
                            (177, 174), (182, 166)])
polygon(screen, (0, 0, 0), [(298, 136), (301, 144),
                            (222, 174), (219, 166)])

#mouth
rect(screen, (0, 0, 0), (150, 250, 100, 20))


#Для отрисовки фигур
pygame.display.update()


#Цикл в котором отслеживаются происходящие события.
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()            


