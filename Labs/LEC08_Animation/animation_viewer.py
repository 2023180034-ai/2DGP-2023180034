from pico2d import *

open_canvas()

while True:
	character_idle()
	character_walk()
	character_jump()
	character_attack()
	character_roll()

close_canvas()
