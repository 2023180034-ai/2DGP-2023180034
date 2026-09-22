from pico2d import *

open_canvas(800, 600)

character = load_image('character.png')

move_state = 0  # 시계 방향으로 움직임
                # 0부터 위쪽
x = 300
y = 500
while True:
    clear_canvas()
    if move_state == 0:
        x += 2
        if x >= 600:
            move_state = 1
    elif move_state == 1:
        y -= 2
        if y <= 100:
            move_state = 2
    elif move_state == 2:
        x -= 2
        if x <= 200:
            move_state = 3
    elif move_state == 3:
        y += 2
        if y >= 500:
            move_state = 0

    character.draw(x, y)
    delay(0.01)
    update_canvas()

close_canvas()