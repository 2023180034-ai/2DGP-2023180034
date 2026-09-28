# 실습 과제 진행
from pico2d import *
import math

def draw_top():
    pass

def draw_right():
    pass
    
def draw_bottom():
    pass
   
def draw_left():
    pass
    

# 맨처음 해야할 일은.
open_canvas(800, 600)
character = load_image('character.png')

def move_circle():
    print("CIRCLE")
    degree = 0
    # 캐릭터 이미지 표시
    for degree in range(360):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)

        clear_canvas()
        character.draw(x, y)

        update_canvas()
        delay(0.01)
    pass

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
    move_circle()
    move_rectangle()
    move_triangle()
    pass

close_canvas()