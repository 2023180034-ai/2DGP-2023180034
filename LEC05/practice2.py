from pico2d import *
import math

open_canvas(800, 600)

character = load_image('character.png')
angle = 0
r = 200

while True:
    clear_canvas()


    x = r * math.cos(math.radians(angle)) + 400
    y = r * math.sin(math.radians(angle)) + 300

    angle -= 1
    character.draw(x, y)
    delay(0.01)
    update_canvas()

