from pico2d import *
import math

open_canvas(800, 600)

character = load_image('character.png')

# 원의 중심과 반지름
center_x, center_y = 400, 300
radius = 200

# 각도 (라디안으로 계산)
angle = 0

while True:
    clear_canvas()

    # 원형 경로 좌표 계산
    x = center_x + radius * math.cos(math.radians(angle))
    y = center_y + radius * math.sin(math.radians(angle))

    # 각도를 조금씩 증가시켜 계속 회전
    angle += 1
    if angle >= 360:
        angle = 0

    character.draw(x, y)
    update_canvas()
    delay(0.01)
