from pathlib import Path

from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
BACKGROUND_PATH = Path(__file__).resolve().parent / "TUK_GROUND.png"
CHARACTER_PATH = Path(__file__).resolve().parent / "animation_sheet.png"
CHARACTER_FRAME_SIZE = 100
CHARACTER_DISPLAY_SIZE = 200
ANIMATION_FRAME_COUNT = 8
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


def handle_events():
	for event in get_events():
		if event.type == SDL_QUIT:
			return False
		if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
			return False
	return True


def main():
	open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
	background = load_image(str(BACKGROUND_PATH))
	character_sheet = load_image(str(CHARACTER_PATH))
	animation_frames = create_animation_frames(character_sheet.h)
	running = True

	try:
		while running:
			clear_canvas()
			background.draw(
				CANVAS_WIDTH // 2,
				CANVAS_HEIGHT // 2,
				CANVAS_WIDTH,
				CANVAS_HEIGHT,
			)
			frame_x, frame_y, frame_width, frame_height = animation_frames["run_right"][0]
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
			running = handle_events()
			delay(0.01)
	finally:
		close_canvas()


if __name__ == "__main__":
	main()
