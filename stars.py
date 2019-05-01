import asyncio
import curses


async def blink(canvas, row, column, symbol='*'):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        for _ in range(3):
            await asyncio.sleep(0)
        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)
        canvas.addstr(row, column, symbol, curses.A_BOLD)
        for _ in range(2):
            await asyncio.sleep(0)
        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)