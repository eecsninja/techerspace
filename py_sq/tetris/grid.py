from sdl2 import *

from common.color import *

class Grid:
  def __init__(self, width, height):
    self.width = width
    self.height = height

    self.array = [0] * width * height

  def SetValue(self, x, y, value):
    # TODO: Check bounds.
    self.array[x + self.width * y] = value

  def GetValue(self, x, y, border=None):
    # Add imaginary border (or lack thereof) if caller specifies boundary
    # checking.
    if x < 0 or x >= self.width or y < 0 or y >= self.height:
      if border != None:
        return 1 if border == True else 0

    return self.array[x + self.width * y]


class GridRenderer:
  def __init__(self, block_width, block_height, palette):
    self.block_width = block_width  # integer
    self.block_height = block_height  # integer
    self.palette = palette  # SDL_Color array


  def DrawToSurface(self, grid, surface):
    # Draws to (0, 0) of surface. Does not check whether surface is big enough.
    # grid: Grid object
    # surface: SDL surface
    rect = SDL_Rect()
    rect.w = self.block_width
    rect.h = self.block_height
    for y in xrange(grid.height):
      rect.y = y * self.block_height
      for x in xrange(grid.width):
        rect.x = x * self.block_width
        value = grid.GetValue(x, y)
        if value == 0:
          continue
        color = self.palette[value]
        SDL_FillRect(surface, rect, SDLColorToColorValue(surface, color))
