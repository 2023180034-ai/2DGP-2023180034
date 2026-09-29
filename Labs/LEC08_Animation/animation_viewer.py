from pico2d import *

def character_idle():
	pass

def character_walk():
	pass

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

while True:
	character_idle()
	character_walk()
	character_jump()
	character_attack()
	character_roll()

close_canvas()
