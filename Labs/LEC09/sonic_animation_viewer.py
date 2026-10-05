from pathlib import Path

from dataclasses import dataclass

from pico2d import *


BASE_DIR = Path(__file__).resolve().parent
SPRITE_PATH = BASE_DIR / "sonic-sprite.png"

SCALE_FACTOR = 4
CANVAS_PADDING = 32
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
        "달리기",
        (
            Frame(0, 37, 32, 42),
            Frame(32, 37, 27, 42),
            Frame(59, 37, 28, 42),
            Frame(87, 37, 29, 42),
            Frame(116, 37, 32, 42),
            Frame(148, 37, 32, 42),
            Frame(180, 37, 34, 42),
            Frame(214, 37, 29, 42),
            Frame(243, 37, 28, 42),
            Frame(271, 37, 29, 42),
            Frame(300, 37, 35, 42),
        ),
    ),
    Motion(
        "질주",
        (
            Frame(0, 77, 33, 43),
            Frame(33, 77, 33, 43),
            Frame(66, 77, 33, 43),
            Frame(99, 77, 33, 43),
            Frame(132, 77, 33, 43),
            Frame(165, 77, 33, 43),
            Frame(198, 77, 33, 43),
            Frame(231, 77, 33, 43),
            Frame(264, 77, 33, 43),
            Frame(297, 77, 33, 43),
            Frame(330, 77, 33, 43),
            Frame(363, 77, 36, 43),
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
    Motion(
        "공격 전환",
        (
            Frame(0, 324, 28, 48),
            Frame(29, 324, 32, 48),
            Frame(63, 324, 24, 48),
            Frame(88, 324, 29, 48),
            Frame(117, 324, 29, 48),
            Frame(146, 324, 25, 48),
            Frame(180, 324, 46, 48),
            Frame(228, 324, 46, 48),
        ),
    ),
    Motion(
        "표정 변화",
        (
            Frame(0, 375, 35, 44),
            Frame(37, 375, 36, 44),
            Frame(74, 375, 22, 44),
            Frame(97, 375, 37, 44),
            Frame(134, 375, 36, 44),
            Frame(174, 375, 36, 44),
            Frame(215, 375, 36, 44),
            Frame(252, 375, 38, 44),
        ),
    ),
    Motion(
        "반응",
        (
            Frame(3, 422, 40, 50),
            Frame(46, 422, 40, 50),
            Frame(93, 422, 30, 50),
            Frame(122, 422, 30, 50),
        ),
    ),
)


def get_canvas_size():
    max_width = max(frame.width for motion in MOTIONS for frame in motion.frames)
    max_height = max(frame.height for motion in MOTIONS for frame in motion.frames)
    return (
        max_width * SCALE_FACTOR + CANVAS_PADDING * 2,
        max_height * SCALE_FACTOR + CANVAS_PADDING * 2,
    )


def validate_motions(sprite_sheet):
    if not MOTIONS:
        raise ValueError("재생할 모션이 정의되지 않았습니다.")

    for motion in MOTIONS:
        if not motion.frames:
            raise ValueError(f"모션에 프레임이 없습니다: {motion.name}")
        for frame in motion.frames:
            if frame.width <= 0 or frame.height <= 0:
                raise ValueError(f"프레임 크기가 올바르지 않습니다: {motion.name}")
            if frame.x < 0 or frame.y < 0:
                raise ValueError(f"프레임 좌표가 올바르지 않습니다: {motion.name}")
            if frame.x + frame.width > sprite_sheet.w or frame.y + frame.height > sprite_sheet.h:
                raise ValueError(f"프레임이 스프라이트 시트 경계를 벗어납니다: {motion.name}")


def draw_frame(sprite_sheet, frame):
    frame_bottom = sprite_sheet.h - frame.y - frame.height
    draw_x = get_canvas_width() // 2
    draw_y = get_canvas_height() // 2
    sprite_sheet.clip_draw(
        frame.x,
        frame_bottom,
        frame.width,
        frame.height,
        draw_x,
        draw_y,
        frame.width * SCALE_FACTOR,
        frame.height * SCALE_FACTOR,
    )


def load_sprite_sheet():
    if not SPRITE_PATH.is_file():
        raise FileNotFoundError(f"스프라이트 파일을 찾을 수 없습니다: {SPRITE_PATH}")
    try:
        return load_image(str(SPRITE_PATH))
    except Exception as error:
        raise RuntimeError(f"스프라이트 파일을 불러오지 못했습니다: {SPRITE_PATH}") from error


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