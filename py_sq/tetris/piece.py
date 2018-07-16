import random

# Local imports
import grid
import palette

class Piece:
  def __init__(self, width, height, color, values):
    self.grid = grid.Grid(width, height)
    self.color = color
    self.values = values

    # Values is an array of width x height containing True/False.
    for y in xrange(height):
      for x in xrange(width):
        self.grid.SetValue(x, y, color if values[x + y * width] else 0)

  def Copy(self):
    return Piece(self.grid.width, self.grid.height, self.color, self.values)


# These are basically templates for each piece type. Use Copy() to create an
# individual instance of a piece that can be mutated.
SQUARE = Piece(2, 2, palette.RED, [1, 1, 1, 1])
BAR = Piece(1, 4, palette.GREEN, [1, 1, 1, 1])

PIECE_TEMPLATES = [SQUARE, BAR]

# Returns a Piece of random type. Does not modify existing Piece objects.
def GetRandomPiece():
  random_value = random.randint(0, len(PIECE_TEMPLATES) - 1)
  return PIECE_TEMPLATES[random_value].Copy()
