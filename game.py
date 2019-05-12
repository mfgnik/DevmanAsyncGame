import time
import curses
from random import randint, choice
from fire import fire
from stars import blink
from utils import get_frames_from_files
from ship import animate_spaceship


TIC_TIMEOUT = 0.1


def draw(canvas, stars_count):
    max_y, max_x = canvas.getmaxyx()
    canvas.nodelay(True)
    rocket_frames = get_frames_from_files(('frame_1.txt', 'frame_2.txt'))
    coroutine_fire = fire(canvas, max_y / 2, max_x / 2, columns_speed=0)
    coroutine_ship = animate_spaceship(canvas, 20, 20, rocket_frames)
    coroutines = [blink(canvas, randint(1, max_y - 1), randint(1, max_x - 1), choice('+*.:'), randint(1, 5))
                  for _ in range(stars_count)]
    coroutines.append(coroutine_fire)
    coroutines.append(coroutine_ship)
    canvas.border()
    curses.curs_set(False)
    while coroutines:
        for coroutine in coroutines:
            try:
                coroutine.send(None)
                canvas.refresh()
            except StopIteration:
                coroutines.remove(coroutine)
        time.sleep(TIC_TIMEOUT)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw, 100)
