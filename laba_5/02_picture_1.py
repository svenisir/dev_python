import pygame
import numpy as np
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 400))

dis_width = 600
dis_height = 400


def main():
    """
    Основная функция для отрисовки элементов картинки.
    :return: None
    """

    draw_background(screen, dis_width, dis_height, dis_height * 0.4, dis_height * 0.4 + dis_height * 0.3)

    draw_sun(screen, dis_width * 0.9, dis_height * 0.15, 50)

    draw_cloud(screen, dis_width * 0.2, dis_height * 0.1, dis_width * 0.15, dis_height * 0.1)

    draw_boat(screen, dis_width * 0.6, dis_height * 0.5, dis_width * 0.3, dis_height * 0.3)

    draw_umbrella(screen, dis_width * 0.2, dis_height * 0.9, dis_width * 0.2, dis_height * 0.4)


def draw_background(surface, width, height, sky_y, water_y):
    """
        Рисует задний фон.
    :param surface: поверхност отрисовки картинки
    :param width: ширина заднего фона
    :param height: высота заднего фона
    :param sky_y: нижняя координата дял неба
    :param water_y: нижняя координата для воды
    :return: None
    """
    rect(surface, (238, 246, 12), (0, water_y, width, height - water_y))
    rect(surface, (68, 35, 223), (0, sky_y, width, water_y - sky_y))
    rect(surface, (161, 245, 255), (0, 0, width, sky_y))


def draw_sun(surface, sun_x, sun_y, radius):
    """
    Рисует солнце с центром в координатах (x, y).
    :param surface: поверхность отрисовки
    :param sun_x: координта центра по x
    :param sun_y:  координата центра по y
    :param radius: радиус солнца
    :return: None
    """
    circle(surface, (255, 247, 29), (sun_x, sun_y), radius)


def draw_cloud(surface, cloud_x, cloud_y, cloud_width, cloud_height):
    """
    Рисует облако, у которго коордиаты нижнего левого угла (cloud_x, cloud_y).
    :param surface: поверхность отрисовки
    :param cloud_x: координата левого нижжнего угла по x
    :param cloud_y: координата ниженего левого угла по y
    :param cloud_width: ширина облака
    :param cloud_height: высота облака
    :return: None
    """
    ellipse(surface, (255, 255, 255), (cloud_x + 0.12 * cloud_width, cloud_y - 0.33 * cloud_height,
                                       0.36 * cloud_width, 0.66 * cloud_height))
    ellipse(surface, (170, 170, 170), (cloud_x + 0.12 * cloud_width, cloud_y - 0.33 * cloud_height,
                                       0.36 * cloud_width, 0.66 * cloud_height), 1)
    ellipse(surface, (255, 255, 255), (cloud_x + 0.36 * cloud_width, cloud_y - 0.33 * cloud_height,
                                       0.36 * cloud_width, 0.66 * cloud_height))
    ellipse(surface, (170, 170, 170), (cloud_x + 0.36 * cloud_width, cloud_y - 0.33 * cloud_height,
                                       0.36 * cloud_width, 0.66 * cloud_height), 1)
    ellipse(surface, (255, 255, 255), (cloud_x, cloud_y,
                                       0.36 * cloud_width, 0.66 * cloud_height))
    ellipse(surface, (170, 170, 170), (cloud_x, cloud_y,
                                       0.36 * cloud_width, 0.66 * cloud_height), 1)
    ellipse(surface, (255, 255, 255), (cloud_x + 0.24 * cloud_width, cloud_y,
                                       0.36 * cloud_width, 0.66 * cloud_height))
    ellipse(surface, (170, 170, 170), (cloud_x + 0.24 * cloud_width, cloud_y,
                                       0.36 * cloud_width, 0.66 * cloud_height), 1)
    ellipse(surface, (255, 255, 255), (cloud_x + 0.48 * cloud_width, cloud_y,
                                       0.36 * cloud_width, 0.66 * cloud_height))
    ellipse(surface, (170, 170, 170), (cloud_x + 0.48 * cloud_width, cloud_y,
                                       0.36 * cloud_width, 0.66 * cloud_height), 1)
    ellipse(surface, (255, 255, 255), (cloud_x + 0.6 * cloud_width, cloud_y - 0.33 * cloud_height,
                                       0.36 * cloud_width, 0.66 * cloud_height))
    ellipse(surface, (170, 170, 170), (cloud_x + 0.6 * cloud_width, cloud_y - 0.33 * cloud_height,
                                       0.36 * cloud_width, 0.66 * cloud_height), 1)
    ellipse(surface, (255, 255, 255), (cloud_x + 0.72 * cloud_width, cloud_y,
                                       0.36 * cloud_width, 0.66 * cloud_height))
    ellipse(surface, (170, 170, 170), (cloud_x + 0.72 * cloud_width, cloud_y,
                                       0.36 * cloud_width, 0.66 * cloud_height), 1)


def draw_boat(surface, boat_x, boat_y, boat_width, boat_height):
    """
    Рисует корабль шириы boat_width, высоты boat_height и
    Левый нижний угол коробля находится в координатах boat_x, boat_y.
    :param surface: поверхность отрисовки
    :param boat_x: координаты левого нижнего угла корабля по x
    :param boat_y: координаты левого нижнего угла корабля по y
    :param boat_width: ширина корабля
    :param boat_height: высота корабля
    :return: None
    """
    draw_boat_mast(surface, boat_x + 0.4 * boat_width, boat_y - boat_height, 0.03 * boat_width, 0.8 * boat_height)
    draw_boat_sail(surface, boat_x + 0.43 * boat_width, boat_y - boat_height, 0.3 * boat_width, 0.8 * boat_height)
    draw_boat_forward(surface, boat_x + 0.899 * boat_width, boat_y - 0.2 * boat_height, 0.3 * boat_width,
                      0.2 * boat_height)
    draw_boat_body(surface, boat_x + 0.2 * boat_width, boat_y - 0.2 * boat_height, 0.7 * boat_width, 0.2 * boat_height)
    draw_boat_back(surface, boat_x + 0.2 * boat_width, boat_y - 0.2 * boat_height, 0.2 * boat_height)


def draw_boat_mast(surface, x, y, width, height):
    """
    Рисует мачту корабля.
    Точка (x, y) левый верхний угол мачты.
    :param surface: поверхность отрисовки
    :param x: координаты мачты по x
    :param y: координаты мачты по y
    :param width: шиирна мачты
    :param height: высота мачты
    :return: None
    """
    rect(surface, (0, 0, 0), (x, y, width, height))


def draw_boat_sail(surface, x, y, width, height):
    """
    Рисует парус корабля.
    Точка (x, y) левый верхний угол паруса.
    :param surface: поверхность отрисовки
    :param x: координаты паруса по x
    :param y: координаты паруса по y
    :param width: шиирна паруса
    :param height: высота паруса
    :return: None
    """
    polygon(screen, (222, 213, 153), [(x, y), (x + 0.2 * width, y + height / 2), (x + width, y + height // 2)])
    polygon(screen, (222, 213, 153), [(x, y + height), (x + 0.2 * width, y + height / 2), (x + width, y + height // 2)])
    aalines(surface, (133, 130, 96), True,
            [(x - 2, y), (x + 0.2 * width, y + height / 2), (x + width, y + height // 2)])
    aalines(surface, (133, 130, 96), True,
            [(x, y + height), (x + 0.2 * width, y + height / 2), (x + width, y + height // 2)])


def draw_boat_forward(surface, x, y, width, height):
    """
    Рисует переднюю часть корабля.
    Точка (x, y) левый верхний угол.
    :param surface: поверхность отрисовки
    :param x: координаты левого верхнего угла по x
    :param y: координаты левого верхнего угла по y
    :param width: шиирна передней части
    :param height: высота передней части
    :return: None
    """
    radius = (width + height - np.sqrt(width ** 2 + height ** 2)) // 2
    polygon(surface, (186, 80, 5), [(x, y), (x + width, y), (x, y + height)])
    aalines(surface, (157, 70, 59), True, [(x, y), (x + width, y), (x, y + height)])
    circle(surface, (0, 0, 0), (x + radius, y + radius), radius * 0.7)
    circle(surface, (255, 255, 255), (x + radius, y + radius), radius * 0.5)


def draw_boat_body(surface, x, y, width, height):
    """
    Рисует среднюю часть коробля.
    Верхний левый угол с координатами (x, y).
    :param surface: поверхность отрисовки
    :param x: координаты левого верхнего угла по x
    :param y: координаты левого верхнего угла по y
    :param width: шиирна средней части
    :param height: высота средней части
    :return: None
    """
    rect(surface, (186, 80, 5), (x, y, width, height))
    aalines(surface, (157, 70, 59), True, [(x, y), (x + width, y), (x + width, y + height), (x, y + height)])


def draw_boat_back(surface, x, y, radius):
    """
    Рисует заднюю часть коробля.
    Центр с координатами (x, y).
    :param surface: поверхность отрисовки
    :param x: координаты центра по x
    :param y: координаты центра по y
    :param radius: радиус задней части
    :return: None
    """
    circle(surface, (186, 80, 5), (x, y), radius, 0, draw_bottom_left=True)
    circle(surface, (157, 70, 59), (x, y), radius, 1, draw_bottom_left=True)


def draw_umbrella(surface, x, y, umbrella_width, umbrella_height):
    """
    Функция рисует зонтик, (x, y) координаты центра основания зонтика.
    :param surface: поверхность отрисовки
    :param x: координата центра основания зонтика по x
    :param y: координата центра основания зонтика по y
    :param umbrella_width: ширина зонтика
    :param umbrella_height: высота зонтика
    :return: None
    """
    draw_umbrella_hat(surface, x, y - 0.8 * umbrella_height, umbrella_width, 0.2 * umbrella_height)
    draw_umbrella_handle(surface, x, y, 0.05 * umbrella_width, 0.8 * umbrella_height)


def draw_umbrella_handle(surface, x, y, um_h_width, um_h_height):
    """
    Рисует ручку зонта.
    Точка (x, y) координаты центра ручки зонта.
    :param surface: поверхность отрисовки
    :param x: координата центра ручки зонта по x
    :param y: координата центра ручки зонта по y
    :param um_h_width: ширина ручки зонта
    :param um_h_height: высота ручки зонта
    :return: None
    """
    rect(surface, (227, 130, 25), (x - 0.5 * um_h_width, y - um_h_height, um_h_width, um_h_height))
    rect(surface, (244, 81, 81), (x - 0.5 * um_h_width, y - 1.25 * um_h_height, um_h_width, 0.25 * um_h_height))


def draw_umbrella_hat(surface, x, y, um_hat_width, um_hat_height):
    """
    Рисует шляпку зонта.
    Точка (x, y) координата центра шляпки
    :param surface: поверхность отрисовки
    :param x: координата центра шляпки по x
    :param y: координата центра шляпки по y
    :param um_hat_width: ширина шляпки
    :param um_hat_height: высота шляпки
    :return: None
    """
    polygon(surface, (244, 81, 81), [(x + 0.5 * um_hat_width, y), (x, y), (x + 0.01 * um_hat_width, y - um_hat_height)])
    polygon(surface, (157, 52, 52), [(x + 0.5 * um_hat_width, y), (x, y), (x + 0.01 * um_hat_width, y - um_hat_height)],
            1)
    polygon(surface, (244, 81, 81), [(x - 0.5 * um_hat_width, y), (x, y), (x - 0.01 * um_hat_width, y - um_hat_height)])
    polygon(surface, (157, 52, 52), [(x - 0.5 * um_hat_width, y), (x, y), (x - 0.01 * um_hat_width, y - um_hat_height)],
            1)
    aaline(surface, (180, 60, 60), (x + 0.01 * um_hat_width, y - um_hat_height), (x + 0.38 * um_hat_width, y))
    aaline(surface, (180, 60, 60), (x + 0.01 * um_hat_width, y - um_hat_height), (x + 0.26 * um_hat_width, y))
    aaline(surface, (180, 60, 60), (x + 0.01 * um_hat_width, y - um_hat_height), (x + 0.14 * um_hat_width, y))
    aaline(surface, (180, 60, 60), (x - 0.01 * um_hat_width, y - um_hat_height), (x - 0.14 * um_hat_width, y))
    aaline(surface, (180, 60, 60), (x - 0.01 * um_hat_width, y - um_hat_height), (x - 0.26 * um_hat_width, y))
    aaline(surface, (180, 60, 60), (x - 0.01 * um_hat_width, y - um_hat_height), (x - 0.38 * um_hat_width, y))


main()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event == pygame.QUIT:
            finished = True

pygame.quit()
