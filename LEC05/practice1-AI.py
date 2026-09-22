from pico2d import *

open_canvas(800, 600)

character = load_image('character.png')

# 시작 위치와 이동 방향 상태
x, y = 100, 100
state = 'RIGHT'
speed = 5
side_length = 300
move_count = 0

while True:
    clear_canvas()

    if state == 'RIGHT':
        x += speed
        move_count += speed
        if move_count >= side_length:
            x = 100 + side_length
            move_count = 0
            state = 'UP'

    elif state == 'UP':
        y += speed
        move_count += speed
        if move_count >= side_length:
            y = 100 + side_length
            move_count = 0
            state = 'LEFT'

    elif state == 'LEFT':
        x -= speed
        move_count += speed
        if move_count >= side_length:
            x = 100
            move_count = 0
            state = 'DOWN'

    elif state == 'DOWN':
        y -= speed
        move_count += speed
        if move_count >= side_length:
            y = 100
            move_count = 0
            state = 'RIGHT'

    character.draw(x, y)
    update_canvas()
    delay(0.01)
