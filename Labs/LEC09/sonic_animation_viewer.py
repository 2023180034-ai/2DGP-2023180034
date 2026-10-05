from pathlib import Path

from pico2d import *


BASE_DIR = Path(__file__).resolve().parent
SPRITE_PATH = BASE_DIR / "sonic-sprite.png"

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


def load_sprite_sheet():
    if not SPRITE_PATH.is_file():
        raise FileNotFoundError(f"스프라이트 파일을 찾을 수 없습니다: {SPRITE_PATH}")
    return load_image(str(SPRITE_PATH))


def main():
    open_canvas(WINDOW_WIDTH, WINDOW_HEIGHT)
    hide_lattice()

    try:
        load_sprite_sheet()
        while True:
            events = get_events()
            if any(event.type == SDL_QUIT for event in events):
                break
            clear_canvas()
            update_canvas()
    finally:
        close_canvas()


if __name__ == "__main__":
    main()