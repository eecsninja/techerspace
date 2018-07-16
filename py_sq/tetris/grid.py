from sdl2 import *

from common.color import *

class Grid:
  def __init__(self, width, height):
    self.width = width
    self.height = height

    self.array = [[0] * width for row in [[]] * height]

  def SetValue(self, x, y, value):
    # TODO: Check bounds.
    self.array[y][x] = value

  def GetValue(self, x, y, border=None):
    # Add imaginary border (or lack thereof) if caller specifies boundary
    # checking.
    if x < 0 or x >= self.width or y < 0 or y >= self.height:
      if border != None:
        return 1 if border == True else 0

    return self.array[y][x]

  # Adds the blocks from another grid to this grid at a particular location.
  def AddBlocks(self, other_grid, other_x, other_y):
    for offset_y in xrange(other_grid.height):
      for offset_x in xrange(other_grid.width):
        other_value = other_grid.GetValue(offset_x, offset_y)
        if other_value != 0:
          self.SetValue(other_x + offset_x, other_y + offset_y, other_value)

  # Removes all full rows. Returns the number of full rows removed.
  def RemoveFullRows(self):
    num_rows_removed = 0

    new_array = [[0] * self.width] * self.height
    new_array_y = self.height - 1
    for y in xrange(self.height - 1, -1, -1):
      num_blocks_in_row = self.GetNumBlocksInRow(y)
      if num_blocks_in_row == self.width:
        num_rows_removed += 1
        continue

      # Copy over non-full rows.
      new_array[new_array_y] = self.array[y]
      new_array_y -= 1

    self.array = new_array

  def GetNumBlocksInRow(self, y):
    return sum([1 if block else 0 for block in self.array[y]])


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
