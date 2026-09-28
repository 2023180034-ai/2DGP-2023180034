from pico2d import *
import math

open_canvas(800, 600)
character = load_image('character.png')


def draw_character(x, y):
    pass


def move_circle():
    pass


def move_rectangle():
    pass


def move_triangle():
    pass


def move_sequence():
    move_circle()
    move_rectangle()
    move_triangle()


while True:
    move_sequence()

close_canvas()
