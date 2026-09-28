from pico2d import *
import math


open_canvas(800, 600)
character = load_image('character.png')


def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)


def move_circle():
    for degree in range(360):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)
        draw_character(x, y)


def move_rectangle():
    for x in range(200, 600, 5):
        draw_character(x, 500)

    for y in range(500, 100, -5):
        draw_character(600, y)

    for x in range(600, 200, -5):
        draw_character(x, 100)

    for y in range(100, 500, 5):
        draw_character(200, y)


def move_triangle():
    points = [(100, 100), (700, 100), (400, 500)]

    for i in range(3):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % 3]

        for t in range(101):
            x = x1 + (x2 - x1) * t / 100
            y = y1 + (y2 - y1) * t / 100
            draw_character(x, y)


def move_sequence():
    move_circle()
    move_rectangle()
    move_triangle()


while True:
    move_sequence()

close_canvas()
