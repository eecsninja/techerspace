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
# Location of next piece display.
NEXT_PIECE_X = BLOCK_WIDTH * (GRID_WIDTH + 2)
NEXT_PIECE_Y = BLOCK_HEIGHT * 4

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
  next_piece = piece.GetRandomPiece()
  # For rendering a piece onto a surface.
  piece_sprite = SDL_CreateRGBSurface(0, BLOCK_WIDTH * 4, BLOCK_HEIGHT * 4, 32,
                                      0, 0, 0, 0)
  SDL_SetColorKey(piece_sprite, 1, 0)  # Black == transparent.
  piece_dest = SDL_Rect()
  next_piece_dest = SDL_Rect()
  next_piece_dest.x = NEXT_PIECE_X
  next_piece_dest.y = NEXT_PIECE_Y
  print next_piece_dest

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
          current_piece.Rotate()
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

    # Test for collisions.
    if current_piece.CollidesWithGridBlocks(game_grid, piece_x, piece_y):
      print "Grid collision"
    if current_piece.CollidesWithGridBorder(game_grid, piece_x, piece_y):
      print "Border collision"

    # Draw current piece.
    grid_renderer.DrawToSurface(current_piece.grid, piece_sprite)
    piece_dest.x = piece_x * BLOCK_WIDTH
    piece_dest.y = piece_y * BLOCK_HEIGHT
    SDL_BlitSurface(piece_sprite, None, screen, piece_dest)

    # Draw next piece.
    SDL_FillRect(screen, next_piece_dest, 0)
    grid_renderer.DrawToSurface(next_piece.grid, piece_sprite)
    SDL_BlitSurface(piece_sprite, None, screen, next_piece_dest)

    SDL_UpdateWindowSurface(window)

  SDL_DestroyWindow(window)
  SDL_Quit()
  return 0


if __name__ == "__main__":
    sys.exit(main())
