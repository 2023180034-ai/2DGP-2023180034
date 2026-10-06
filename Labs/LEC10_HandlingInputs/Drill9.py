from pathlib import Path

from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
BACKGROUND_PATH = Path(__file__).resolve().parent / "TUK_GROUND.png"


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

			update_canvas()
			running = handle_events()
			delay(0.01)
	finally:
		close_canvas()


if __name__ == "__main__":
	main()
