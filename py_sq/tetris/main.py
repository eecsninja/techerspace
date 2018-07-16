import ctypes
import sys

from sdl2 import *

# Local imports
import grid
import palette

# Screen defs.
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

# Game defs.
GRID_WIDTH = 10
GRID_HEIGHT = 20
# Dimensions of each block in pixels.
BLOCK_WIDTH = 32
BLOCK_HEIGHT = 32

def main():
  window = SDL_CreateWindow(b"Tetris",
                            SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
                            SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN)
  screen = SDL_GetWindowSurface(window)

  # Game data.
  game_grid = grid.Grid(GRID_WIDTH, GRID_HEIGHT)

  GRID_PALETTE = palette.GetPalette()
  grid_renderer = grid.GridRenderer(BLOCK_WIDTH, BLOCK_HEIGHT, GRID_PALETTE)

  # Draw the grid.
  for x in xrange(15):
    game_grid.SetValue(0, x, x)
  grid_renderer.DrawToSurface(game_grid, screen)

  running = True
  event = SDL_Event()
  while running:
    while SDL_PollEvent(ctypes.byref(event)) != 0:
      if event.type == SDL_QUIT:
        running = False
        break
    SDL_UpdateWindowSurface(window)

  SDL_DestroyWindow(window)
  SDL_Quit()
  return 0


if __name__ == "__main__":
    sys.exit(main())
