from pathlib import Path

from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
BACKGROUND_PATH = Path(__file__).resolve().parent / "TUK_GROUND.png"
CHARACTER_PATH = Path(__file__).resolve().parent / "animation_sheet.png"
CHARACTER_FRAME_SIZE = 100
CHARACTER_DISPLAY_SIZE = 200
ANIMATION_FRAME_COUNT = 8
ANIMATION_FRAME_INTERVAL = 0.1
ANIMATION_ROWS_FROM_TOP = {
	"idle_right": 0,
	"idle_left": 1,
	"run_right": 2,
	"run_left": 3,
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
	previous_animation_direction = None
	frame_index = 0
	next_frame_time = get_time()

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
			direction = int(moving_right) - int(moving_left)
			if direction != 0:
				facing_direction = direction

			is_animating = direction != 0 or up_pressed or down_pressed
			animation_direction = direction if direction != 0 else facing_direction
			if is_animating:
				if animation_direction != previous_animation_direction:
					frame_index = 0
					next_frame_time = current_time + ANIMATION_FRAME_INTERVAL
				elif current_time >= next_frame_time:
					frame_index = (frame_index + 1) % ANIMATION_FRAME_COUNT
					next_frame_time = current_time + ANIMATION_FRAME_INTERVAL
			else:
				frame_index = 0
			previous_animation_direction = animation_direction if is_animating else None

			clear_canvas()
			background.draw(
				CANVAS_WIDTH // 2,
				CANVAS_HEIGHT // 2,
				CANVAS_WIDTH,
				CANVAS_HEIGHT,
			)
			if animation_direction > 0 and is_animating:
				animation_name = "run_right"
			elif animation_direction < 0 and is_animating:
				animation_name = "run_left"
			else:
				animation_name = "idle_right" if facing_direction > 0 else "idle_left"
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
