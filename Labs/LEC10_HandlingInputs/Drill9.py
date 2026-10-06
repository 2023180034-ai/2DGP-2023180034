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
CHARACTER_SPEED = 300
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


def handle_events(running, moving_right):
	for event in get_events():
		if event.type == SDL_QUIT:
			running = False
		elif event.type == SDL_KEYDOWN:
			if event.key == SDLK_ESCAPE:
				running = False
			elif event.key == SDLK_RIGHT:
				moving_right = True
		elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
			moving_right = False
	return running, moving_right


def main():
	open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
	background = load_image(str(BACKGROUND_PATH))
	character_sheet = load_image(str(CHARACTER_PATH))
	animation_frames = create_animation_frames(character_sheet.h)
	running = True
	moving_right = False
	character_x = CANVAS_WIDTH // 2
	character_y = CANVAS_HEIGHT // 2
	frame_index = 0
	next_frame_time = get_time()
	previous_time = get_time()

	try:
		while running:
			running, moving_right = handle_events(running, moving_right)
			if not running:
				break

			current_time = get_time()
			delta_time = current_time - previous_time
			previous_time = current_time

			if moving_right:
				character_x = min(
					CANVAS_WIDTH - CHARACTER_DISPLAY_SIZE // 2,
					character_x + CHARACTER_SPEED * delta_time,
				)
				if current_time >= next_frame_time:
					frame_index = (frame_index + 1) % ANIMATION_FRAME_COUNT
					next_frame_time = current_time + ANIMATION_FRAME_INTERVAL
			else:
				frame_index = 0

			clear_canvas()
			background.draw(
				CANVAS_WIDTH // 2,
				CANVAS_HEIGHT // 2,
				CANVAS_WIDTH,
				CANVAS_HEIGHT,
			)
			animation_name = "run_right" if moving_right else "idle_right"
			frame_x, frame_y, frame_width, frame_height = animation_frames[animation_name][frame_index]
			character_sheet.clip_draw(
				frame_x,
				frame_y,
				frame_width,
				frame_height,
				CANVAS_WIDTH // 2,
				CANVAS_HEIGHT // 2,
				CHARACTER_DISPLAY_SIZE,
				CHARACTER_DISPLAY_SIZE,
			)

			update_canvas()
			delay(0.01)
	finally:
		close_canvas()


if __name__ == "__main__":
	main()
