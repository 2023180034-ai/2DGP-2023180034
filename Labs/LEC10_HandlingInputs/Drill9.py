from pathlib import Path
from math import hypot

from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
BACKGROUND_PATH = Path(__file__).resolve().parent / "TUK_GROUND.png"
CHARACTER_PATH = Path(__file__).resolve().parent / "animation_sheet.png"
CHARACTER_FRAME_SIZE = 100
CHARACTER_DISPLAY_SIZE = 100
ANIMATION_FRAME_COUNT = 8
ANIMATION_FRAME_INTERVAL = 0.1
CHARACTER_SPEED = 300
ANIMATION_ROWS_FROM_TOP = {
	"idle_right": 0,
	"idle_left": 1,
	"run_right": 2,
	"run_left": 3,
}
RUN_FRAME_VISIBLE_BOUNDS = {
	"run_right": (18, 20, 79, 88),
	"run_left": (22, 20, 83, 88),
}


def create_animation_frames(sheet_height):
	return {
		name: tuple(
			(
				frame_index * CHARACTER_FRAME_SIZE,
				sheet_height - (row_index + 1) * CHARACTER_FRAME_SIZE,
				CHARACTER_FRAME_SIZE,
				CHARACTER_FRAME_SIZE,
			)
			for frame_index in range(ANIMATION_FRAME_COUNT)
		)
		for name, row_index in ANIMATION_ROWS_FROM_TOP.items()
	}


def handle_events(running, moving_right, moving_left, up_pressed, down_pressed):
	for event in get_events():
		if event.type == SDL_QUIT:
			running = False
		elif event.type == SDL_KEYDOWN:
			if event.key == SDLK_ESCAPE:
				running = False
			elif event.key == SDLK_RIGHT:
				moving_right = True
			elif event.key == SDLK_LEFT:
				moving_left = True
			elif event.key == SDLK_UP:
				up_pressed = True
			elif event.key == SDLK_DOWN:
				down_pressed = True
		elif event.type == SDL_KEYUP:
			if event.key == SDLK_RIGHT:
				moving_right = False
			elif event.key == SDLK_LEFT:
				moving_left = False
			elif event.key == SDLK_UP:
				up_pressed = False
			elif event.key == SDLK_DOWN:
				down_pressed = False
	return running, moving_right, moving_left, up_pressed, down_pressed


def main():
	open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
	background = load_image(str(BACKGROUND_PATH))
	character_sheet = load_image(str(CHARACTER_PATH))
	animation_frames = create_animation_frames(character_sheet.h)
	running = True
	moving_right = False
	moving_left = False
	up_pressed = False
	down_pressed = False
	character_x = CANVAS_WIDTH // 2
	character_y = CANVAS_HEIGHT // 2
	facing_direction = 1
	previous_animation_name = None
	frame_index = 0
	next_frame_time = get_time()
	previous_time = get_time()

	try:
		while running:
			running, moving_right, moving_left, up_pressed, down_pressed = handle_events(
				running,
				moving_right,
				moving_left,
				up_pressed,
				down_pressed,
			)
			if not running:
				break

			current_time = get_time()
			delta_time = current_time - previous_time
			previous_time = current_time
			move_x = int(moving_right) - int(moving_left)
			move_y = int(up_pressed) - int(down_pressed)
			if move_x != 0:
				facing_direction = move_x

			previous_x = character_x
			previous_y = character_y
			movement_length = hypot(move_x, move_y)
			if movement_length != 0:
				movement_step = CHARACTER_SPEED * delta_time / movement_length
				movement_direction = move_x if move_x != 0 else facing_direction
				movement_animation = "run_right" if movement_direction > 0 else "run_left"
				min_x, min_y, max_x, max_y = RUN_FRAME_VISIBLE_BOUNDS[movement_animation]
				scale = CHARACTER_DISPLAY_SIZE / CHARACTER_FRAME_SIZE
				left_extent = (CHARACTER_FRAME_SIZE / 2 - min_x) * scale
				right_extent = (max_x + 1 - CHARACTER_FRAME_SIZE / 2) * scale
				top_extent = (CHARACTER_FRAME_SIZE / 2 - min_y) * scale
				bottom_extent = (max_y + 1 - CHARACTER_FRAME_SIZE / 2) * scale
				character_x = max(
					left_extent,
					min(
						CANVAS_WIDTH - right_extent,
						character_x + move_x * movement_step,
					),
				)
				character_y = max(
					bottom_extent,
					min(
						CANVAS_HEIGHT - top_extent,
						character_y + move_y * movement_step,
					),
				)

			is_animating = character_x != previous_x or character_y != previous_y
			animation_direction = move_x if move_x != 0 else facing_direction
			if is_animating:
				animation_name = "run_right" if animation_direction > 0 else "run_left"
			else:
				animation_name = "idle_right" if facing_direction > 0 else "idle_left"

			if animation_name != previous_animation_name:
				frame_index = 0
				next_frame_time = current_time + ANIMATION_FRAME_INTERVAL
			elif current_time >= next_frame_time:
				frame_index = (frame_index + 1) % len(animation_frames[animation_name])
				next_frame_time = current_time + ANIMATION_FRAME_INTERVAL
			previous_animation_name = animation_name

			clear_canvas()
			background.draw(
				CANVAS_WIDTH // 2,
				CANVAS_HEIGHT // 2,
				CANVAS_WIDTH,
				CANVAS_HEIGHT,
			)
			frame_x, frame_y, frame_width, frame_height = animation_frames[animation_name][frame_index]
			character_sheet.clip_draw(
				frame_x,
				frame_y,
				frame_width,
				frame_height,
				character_x,
				character_y,
				CHARACTER_DISPLAY_SIZE,
				CHARACTER_DISPLAY_SIZE,
			)

			update_canvas()
			delay(0.01)
	finally:
		close_canvas()


if __name__ == "__main__":
	main()
