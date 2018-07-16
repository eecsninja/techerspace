import ctypes
import sys

from sdl2 import *
from sdl2.ext import sprite

# Local imports
import grid
import palette
import piece

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

  sprite_factory = sprite.SpriteFactory(sprite.SOFTWARE)

  # Game data.
  game_grid = grid.Grid(GRID_WIDTH, GRID_HEIGHT)

  GRID_PALETTE = palette.GetPalette()
  grid_renderer = grid.GridRenderer(BLOCK_WIDTH, BLOCK_HEIGHT, GRID_PALETTE)

  # For testing.
  piece_x = 0
  piece_y = 0

  current_piece = piece.GetRandomPiece()
  piece_sprite = SDL_CreateRGBSurface(0, BLOCK_WIDTH * 4, BLOCK_HEIGHT * 4, 32,
                                      0, 0, 0, 0)
  piece_dest = SDL_Rect()

  running = True
  event = SDL_Event()
  while running:
    # Handle user input.
    while SDL_PollEvent(ctypes.byref(event)) != 0:
      if event.type == SDL_QUIT:
        running = False
        break
      if event.type == SDL_KEYDOWN:
        if event.key.keysym.sym == SDLK_UP:
          piece_y -= 1
        elif event.key.keysym.sym == SDLK_DOWN:
          piece_y += 1
        elif event.key.keysym.sym == SDLK_LEFT:
          piece_x -= 1
        elif event.key.keysym.sym == SDLK_RIGHT:
          piece_x += 1

    # Draw the grid.
    for x in xrange(15):
      game_grid.SetValue(0, x, x)
    grid_renderer.DrawToSurface(game_grid, screen)

    # Draw pieces.
    grid_renderer.DrawToSurface(current_piece.grid, piece_sprite)

    piece_dest.x = piece_x * BLOCK_WIDTH
    piece_dest.y = piece_y * BLOCK_HEIGHT
    SDL_BlitSurface(piece_sprite, None, screen, piece_dest)

    SDL_UpdateWindowSurface(window)

  SDL_DestroyWindow(window)
  SDL_Quit()
  return 0


if __name__ == "__main__":
    sys.exit(main())
