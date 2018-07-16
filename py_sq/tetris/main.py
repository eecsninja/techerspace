import ctypes
import sys

from sdl2 import *

# Local imports
import grid
from common.color import *

# Screen defs.
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Game defs.
GRID_WIDTH = 10
GRID_HEIGHT = 20

# Game data.
game_grid = grid.Grid(GRID_WIDTH, GRID_HEIGHT)

def main():
  window = SDL_CreateWindow(b"Tetris",
                            SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
                            SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN)
  screen = SDL_GetWindowSurface(window)

  dark_green = RGBToColorValue(screen, 0, 0x7f, 0)
  SDL_FillRect(screen, None, dark_green)

  SDL_UpdateWindowSurface(window)

  running = True
  event = SDL_Event()
  while running:
      while SDL_PollEvent(ctypes.byref(event)) != 0:
          if event.type == SDL_QUIT:
              running = False
              break

  SDL_DestroyWindow(window)
  SDL_Quit()
  return 0


if __name__ == "__main__":
    sys.exit(main())
