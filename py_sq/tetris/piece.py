import grid
import palette

class Piece:
  def __init__(self, width, height, color, values):
    self.grid = grid.Grid(width, height)
    self.color = color

    # Values is an array of width x height containing True/False.
    for y in xrange(height):
      for x in xrange(width):
        self.grid.SetValue(x, y, color if values[x + y * width] else 0)


SQUARE = Piece(2, 2, palette.RED, [1, 1, 1, 1])
BAR = Piece(1, 4, palette.GREEN, [1, 1, 1, 1])
