from pathlib import Path

from dataclasses import dataclass

from pico2d import *


BASE_DIR = Path(__file__).resolve().parent
SPRITE_PATH = BASE_DIR / "sonic-sprite.png"

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
SCALE_FACTOR = 4
FRAME_INTERVAL = 0.1
MOTION_REPEAT_COUNT = 5
MOTION_PAUSE_SECONDS = 1.0


@dataclass(frozen=True)
class Frame:
    x: int
    y: int
    width: int
    height: int


@dataclass(frozen=True)
class Motion:
    name: str
    frames: tuple[Frame, ...]


MOTIONS = (
    Motion(
        "공중 회전",
        (
            Frame(0, 165, 33, 38),
            Frame(34, 165, 33, 38),
            Frame(68, 165, 33, 38),
            Frame(101, 165, 33, 38),
            Frame(134, 165, 33, 38),
            Frame(168, 165, 58, 38),
            Frame(227, 165, 38, 38),
            Frame(265, 165, 38, 38),
        ),
    ),
    Motion(
        "점프",
        (
            Frame(0, 118, 35, 48),
            Frame(37, 118, 38, 48),
            Frame(87, 118, 38, 48),
            Frame(128, 118, 38, 48),
            Frame(179, 118, 38, 48),
            Frame(226, 118, 36, 48),
        ),
    ),
    Motion(
        "구르기",
        (
            Frame(0, 204, 32, 30),
            Frame(35, 204, 31, 30),
            Frame(69, 204, 31, 30),
            Frame(104, 204, 31, 30),
            Frame(138, 204, 31, 30),
            Frame(173, 204, 31, 30),
        ),
    ),
    Motion(
        "회전",
        (
            Frame(0, 234, 32, 40),
            Frame(34, 234, 34, 40),
            Frame(72, 234, 34, 40),
            Frame(109, 234, 34, 40),
            Frame(147, 234, 34, 40),
            Frame(184, 234, 34, 40),
        ),
    ),
    Motion(
        "스핀 대시",
        (
            Frame(0, 281, 32, 39),
            Frame(34, 281, 33, 39),
            Frame(69, 281, 43, 39),
            Frame(120, 281, 45, 39),
            Frame(168, 281, 45, 39),
            Frame(214, 281, 45, 39),
        ),
    ),
)


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