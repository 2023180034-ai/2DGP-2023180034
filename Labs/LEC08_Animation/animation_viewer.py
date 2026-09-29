from pico2d import *

def character_idle():
	global idle_frame
	for idle_frame in range(4):
		clear_canvas()
		idle_image.clip_draw(idle_start_points[idle_frame], 0, idle_widths[idle_frame], idle_height, 400, 300)
		update_canvas()
		delay(0.1)

def character_walk():
	global walk_frame
	for walk_frame in range(8):
		clear_canvas()
		walk_image.clip_draw(walk_start_points[walk_frame], 0, walk_widths[walk_frame], walk_height, 400, 300)
		update_canvas()
		delay(0.1)

def character_jump():
	pass

def character_attack():
	pass

def character_roll():
	pass

open_canvas()

idle_image = load_image('idle.png')
walk_image = load_image('walk.png')
jump_image = load_image('jump.png')
attack_image = load_image('attack.png')
roll_image = load_image('roll.png')

idle_height = 124
idle_widths = [88, 84, 84, 84]
idle_start_points = [0, 88, 172, 256]
idle_frame = 0
walk_height = 128
walk_widths = [96, 88, 84, 84, 88, 84, 88, 92]
walk_start_points = [0, 96, 184, 268, 352, 440, 524, 612]
walk_frame = 0

while True:
	character_idle()
	character_walk()
	character_jump()
	character_attack()
	character_roll()

close_canvas()
