from pico2d import *

def character_idle():
	idle_height = 124
	idle_widths = [88, 84, 84, 84]
	idle_start_points = [0, 88, 172, 256]
	for repetition in range(2):
		for idle_frame in range(4):
			clear_canvas()
			idle_image.clip_draw(idle_start_points[idle_frame], 0, idle_widths[idle_frame], idle_height, 400, 300)
			update_canvas()
			delay(0.1)

def character_walk():
	walk_height = 128
	walk_widths = [96, 88, 84, 84, 88, 84, 88, 92]
	walk_start_points = [0, 96, 184, 268, 352, 440, 524, 612]
	for repetition in range(2):
		for walk_frame in range(8):
			clear_canvas()
			walk_image.clip_draw(walk_start_points[walk_frame], 0, walk_widths[walk_frame], walk_height, 400, 300)
			update_canvas()
			delay(0.1)

def character_jump():
	jump_height = 192
	jump_widths = [84, 84, 88, 88, 88, 96]
	jump_start_points = [0, 84, 168, 256, 344, 432]
	for repetition in range(2):
		for jump_frame in range(6):
			clear_canvas()
			jump_image.clip_draw(jump_start_points[jump_frame], 0, jump_widths[jump_frame], jump_height, 400, 300)
			update_canvas()
			delay(0.1)

def character_attack():
	attack_height = 140
	attack_widths = [92, 112, 112, 140, 120, 112]
	attack_start_points = [0, 92, 204, 316, 456, 576]
	for repetition in range(2):
		for attack_frame in range(6):
			clear_canvas()
			attack_image.clip_draw(attack_start_points[attack_frame], 0, attack_widths[attack_frame], attack_height, 400, 300)
			update_canvas()
			delay(0.1)

def character_roll():
	roll_height = 120
	roll_widths = [88, 112, 124, 128, 108, 112, 88]
	roll_start_points = [0, 88, 200, 324, 452, 560, 672]
	for repetition in range(2):
		for roll_frame in range(7):
			clear_canvas()
			roll_image.clip_draw(roll_start_points[roll_frame], 0, roll_widths[roll_frame], roll_height, 400, 300)
			update_canvas()
			delay(0.1)

open_canvas()

idle_image = load_image('idle.png')
walk_image = load_image('walk.png')
jump_image = load_image('jump.png')
attack_image = load_image('attack.png')
roll_image = load_image('roll.png')

while True:
	character_idle()
	character_walk()
	character_jump()
	character_attack()
	character_roll()

close_canvas()
