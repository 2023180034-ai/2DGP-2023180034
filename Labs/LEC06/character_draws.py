# 실습 과제 진행
from pico2d import *
import math



# 맨처음 해야할 일은.
open_canvas(800, 600)
character = load_image('character.png')

def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()

def move_circle():
    print("CIRCLE")
    degree = 0
    # 캐릭터 이미지 표시
    for degree in range(360):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)

        draw_character(x, y)
        delay(0.01)
    pass

def draw_top():
    print("TOP")
    for x in range(200, 600, 1):
        draw_character(x, 500)

def draw_right():
    print("RIGHT")
    for y in range(500, 100, -1):
        draw_character(600, y)

def draw_bottom():
    print("BOTTOM")
    for x in range(600, 200, -1):
        draw_character(x, 100)
   
def draw_left():
    print("LEFT")
    for y in range(100, 500, 1):
        draw_character(200, y)

def move_rectangle():
    print("RECTANGLE")
    draw_top()
    draw_right()
    draw_bottom()
    draw_left()
    pass

def move_triangle():
    print("TRIANGLE")
    pass

while True:
    # move_circle()
    move_rectangle()
    move_triangle()
    pass

close_canvas()