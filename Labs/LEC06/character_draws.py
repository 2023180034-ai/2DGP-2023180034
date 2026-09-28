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
    delay(0.01)

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
    for x in range(200, 600, 5):
        draw_character(x, 500)

def draw_right():
    print("RIGHT")
    for y in range(500, 100, -5):
        draw_character(600, y)

def draw_bottom():
    print("BOTTOM")
    for x in range(600, 200, -5):
        draw_character(x, 100)
   
def draw_left():
    print("LEFT")
    for y in range(100, 500, 5):
        draw_character(200, y)

def move_rectangle():
    print("RECTANGLE")
    draw_top()
    draw_right()
    draw_bottom()
    draw_left()
    pass



def draw_tri_bottom(points):
    x1, y1 = points[0]
    x2, y2 = points[1]
    for i in range(101):
        t = i / 100
        cx = x1 + (x2 - x1) * t
        cy = y1 + (y2 - y1) * t
        draw_character(cx, cy)

    pass

def draw_tri_right(points):
    x2, y2 = points[1]
    x3, y3 = points[2]
    for i  in range(101):
        t = i / 100
        cx = x2 + (x3 - x2) * t
        cy = y2 + (y3 - y2) * t
        draw_character(cx, cy)
    pass

def draw_tri_left(points):
    x3, y3 = points[2]
    x1, y1 = points[0]
    for i in range(101):
        t = i / 100
    pass

def move_triangle():
    print("TRIANGLE")
    points = [(100, 100), (700, 100), (400, 500)]
    
    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]

    draw_tri_bottom(points)
    draw_tri_right(points)
    draw_tri_left(points)
    pass

while True:
    # move_circle()
    # move_rectangle()
    move_triangle()
    pass

close_canvas()