"""Simple demo of the Python Curses library.

The coordinate system (like many screen spaces) is in the upper left.
"""

import curses
import math
import time


def DrawCoords(window):
  window.border()
  for i in range(10):
    window.addstr(i, 2*i, '(%d, %d)' % (2*i, i))

  h, w = window.getmaxyx()
  coord_str = '(%d, %d)' % (w - 1, h - 1)
  window.addstr(h - 1, w - (len(coord_str) + 1), coord_str)

  window.refresh()


def DrawSine(window):
  h, w = window.getmaxyx()
  y = h / 2
  w_mid = w / 2
  for t in range(1000):
    time.sleep(0.01)
    x = w_mid + int(0.8 * math.sin(t / 100.0) * w_mid)
    window.move(y, x)
    window.addch(ord('X'))
    #window.vline(y, x, ord('X'), 4)
    window.refresh()


def Main(window):
  DrawCoords(window)
  window.getch()  # Block until any key press.
  curses.beep()
  DrawSine(window)


if __name__ == '__main__':
  curses.wrapper(Main)
