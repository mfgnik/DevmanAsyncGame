import asyncio
from utils import draw_frame, get_frame_size


SPACE_KEY_CODE = 32
LEFT_KEY_CODE = 260
RIGHT_KEY_CODE = 261
UP_KEY_CODE = 259
DOWN_KEY_CODE = 258


def read_controls(canvas):
    """Read keys pressed and returns tuple witl controls state."""

    rows_direction = columns_direction = 0
    space_pressed = False
    key_code_to_direction = {
        UP_KEY_CODE: (-1, 0),
        DOWN_KEY_CODE: (1, 0),
        RIGHT_KEY_CODE: (0, 1),
        LEFT_KEY_CODE: (0, -1),
    }

    while True:
        pressed_key_code = canvas.getch()

        if pressed_key_code == -1:
            break

        if pressed_key_code in key_code_to_direction:
            rows_direction, columns_direction = key_code_to_direction[pressed_key_code]

        if pressed_key_code == SPACE_KEY_CODE:
            space_pressed = True

    return rows_direction, columns_direction, space_pressed


async def animate_spaceship(canvas, row, column, frames):
    last_frame = ''
    canvas.nodelay(True)
    last_row, last_column = (row, column)
    rows_number, columns_number = canvas.getmaxyx()

    while True:
        for frame in frames:
            draw_frame(canvas, last_row, last_column, last_frame, negative=True)
            draw_frame(canvas, row, column, frame)

            last_frame = frame
            last_row, last_column = (row, column)
            frame_rows, frame_columns = get_frame_size(last_frame)

            rows_direction, columns_direction, space_pressed = read_controls(canvas)

            row += rows_direction
            column += columns_direction

            if  row < 0 or \
                row + frame_rows > rows_number or \
                column < 0 or \
                column + frame_columns > columns_number:
                row, column = (last_row, last_column)
            await asyncio.sleep(0)