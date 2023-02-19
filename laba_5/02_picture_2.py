import pygame
from pygame.draw import *


def build_parabola(A, B, V, x):
    x1, y1 = A
    x2, y2 = B
    xv, yv = V

    a = (y1 - y2) / (x1 ** 2 - x2 ** 2 - 2 * xv * (x1 - x2))
    b = -2 * xv * a
    c = y1 - a * (x1 ** 2 - 2 * xv * x1)

    return a * x ** 2 + b * x + c


pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 600))

width = 800
height = 600


def main():
    """
    Главная функция вызывающая остальные для рисования картинки.
    :return: None
    """
    draw_background(screen, width, height, 140, 270, 400)
    draw_sun(screen, 400, 140, 50)
    draw_up_mountains(screen, (252, 152, 49), 400, 257, width, 170)
    draw_down_mountains(screen, (172, 67, 52), 400, 405, 800, 180)


def draw_background(surface, dis_width, dis_height, up_sky_y, down_sky_y, up_sand_y):
    """
        Рисует задний фон картинки, не изменяемый по ширине.
        :param surface: поверхность отрисовки
        :param dis_width: ширина экрана
        :param dis_height: высота экрана
        :param up_sky_y: нижняя координата неба сверху по y
        :param down_sky_y: нижняя координата неба снизу по y
        :param up_sand_y: нижняя координата песка сверху по y
        :return: None
        """
    rect(surface, (179, 134, 148), (0, up_sand_y,
                                    dis_width, dis_height - up_sand_y))
    rect(surface, (254, 213, 148), (0, down_sky_y,
                                    dis_width, up_sand_y - down_sky_y))
    rect(surface, (254, 213, 196), (0, up_sky_y,
                                    dis_width, down_sky_y - up_sky_y))
    rect(surface, (254, 213, 162), (0, 0,
                                    dis_width, up_sky_y))


def draw_sun(surface, sun_x, sun_y, sun_radius):
    """
    Рисует солнце с центром в координатах (sun_x, sun_y).
    :param surface: поверхность отрисовки
    :param sun_x: координаты центра солнца по x
    :param sun_y: координаты центра солнца по y
    :param sun_radius: радиус солнца
    :return: None
    """
    circle(surface, (252, 238, 33), (sun_x, sun_y), sun_radius)


def draw_up_mountains(surface, color, up_mountains_x, up_mountains_y, up_mountains_width, up_mountains_height):
    """
    Рисует горы на заднем фоне, центр гор находится в координатох (up_mountains_x, up_mountains_y).
    :param surface: поверхность отрисовки
    :param color: цвет гор
    :param up_mountains_x: координата центра гор по x
    :param up_mountains_y: координата центра гор по y
    :param up_mountains_width: ширина гор
    :param up_mountains_height: высота гор
    :return: None
    """
    x = up_mountains_x
    y = up_mountains_y
    w = up_mountains_width
    h = up_mountains_height
    points = [(x - 0.5 * w, y + 0.135 * h), (x - 0.488 * w, y - 0.041 * h)]

    for i in range(round(x - 0.488 * w), round(x - 0.275 * w)):
        points.append((i, build_parabola((x - 0.488 * w, y - 0.041 * h),
                                         (x - 0.275 * w, y - 0.747 * h),
                                         (x - 0.488 * w, y - 0.041 * h), i)))

    points.extend([(x - 0.275 * w, y - 0.747 * h), (x - 0.250 * w, y - 0.688 * h),
                   (x - 0.238 * w, y - 0.571 * h), (x - 0.100 * w, y - 0.041 * h),
                   (x - 0.012 * w, y - 0.100 * h), (x - 0.000 * w, y - 0.000 * h),
                   (x + 0.062 * w, y - 0.159 * h), (x + 0.087 * w, y - 0.100 * h),
                   (x + 0.112 * w, y - 0.276 * h)])

    for i in range(round(x + 0.112 * w), round(x + 0.213 * w)):
        points.append((i, build_parabola((x + 0.112 * w, y - 0.276 * h),
                                         (x + 0.213 * w, y - 0.747 * h),
                                         (x + 0.112 * w, y - 0.276 * h), i)))

    for i in range(round(x + 0.213 * w), round(x + 0.250 * w)):
        points.append((i, build_parabola((x + 0.213 * w, y - 0.747 * h),
                                         (x + 0.250 * w, y - 0.806 * h),
                                         (x + 0.236 * w, y - 0.865 * h), i)))

    points.extend([(x + 0.250 * w, y - 0.806 * h), (x + 0.275 * w, y - 0.571 * h), (x + 0.312 * w, y - 0.629 * h)])

    for i in range(round(x + 0.312 * w), round(x + 0.400 * w)):
        points.append((i, build_parabola((x + 0.312 * w, y - 0.629 * h),
                                         (x + 0.400 * w, y - 0.218 * h),
                                         (x + 0.300 * w, y - 0.629 * h), i)))

    points.extend([(x + 0.400 * w, y - 0.218 * h), (x + 0.425 * w, y - 0.335 * h), (x + 0.500 * w, y - 0.100 * h)])

    polygon(surface, color, points)
    aalines(surface, color, True, points)


def draw_down_mountains(surface, color, down_mountains_x, down_mountains_y,
                        down_mountains_width, down_mountains_height):
    """
    Рисует горыв на переднем плане.
    Серидина гор находится в точке (down_mountains_x, down_mountains_y)
    :param surface: поверхность отрисовки
    :param color: цвет гор
    :param down_mountains_x: координато центра гор по x
    :param down_mountains_y: координато центра гор по y
    :param down_mountains_width: ширина гор
    :param down_mountains_height: высота гор, от самой низкой точки (левый нижний угол) до самой верхней
    :return: None
    """
    x = down_mountains_x
    y = down_mountains_y
    w = down_mountains_width
    h = down_mountains_height

    points_for = [(x - 0.500*w, y + 0.028*h), (x - 0.500*w, y - 0.556*h), (x - 0.488*w, y - 0.556*h)]

    for i in range(round(x - 0.480*w), round(x - 0.300*w)):
        points_for.append((i, build_parabola((x - 0.460*w, y - 0.600*h),
                                             (x - 0.300*w, y - 0.083*h),
                                             (x - 0.405*w, y - 0.861*h), i)))

    points_for.extend([(x - 0.263*w, y - 0.472*h), (x - 0.188*w, y - 0.305*h),
                       (x - 0.150*w, y - 0.694*h), (x - 0.063*w, y - 0.583*h),
                       (x - 0.000*w, y - 0.305*h)])

    for i in range(round(x + 0.112*w), round(x + 0.239*w)):
        points_for.append((i, build_parabola((x + 0.112*w, y - 0.416*h),
                                             (x + 0.239*w, y - 0.750*h),
                                             (x + 0.213*w, y - 0.806*h), i)))

    for i in range(round(x + 0.238*w), round(x + 0.339*w)):
        points_for.append((i, build_parabola((x + 0.238*w, y - 0.750*h),
                                             (x + 0.338*w, y - 0.472*h),
                                             (x + 0.338*w, y - 0.417*h), i)))

    points_for.extend([(x + 0.375*w, y - 0.694*h), (x + 0.400*w, y - 0.583*h),
                       (x + 0.425*w, y - 0.750*h), (x + 0.463*w, y - 0.694*h),
                       (x + 0.500*w, y - 0.972*h), (x + 0.500*w, y - 0.028*h)])

    polygon(surface, color, points_for)
    aalines(surface, color, True, points_for)


main()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event == pygame.QUIT:
            finished = True
            pygame.quit()
