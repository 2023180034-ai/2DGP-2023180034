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
    pass


def move_sequence():
    move_circle()
    move_rectangle()
    move_triangle()


while True:
    move_sequence()

close_canvas()
