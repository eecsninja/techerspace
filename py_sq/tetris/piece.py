import random

# Local imports
import grid
import palette

class Piece:
  def __init__(self, width, height, color, values):
    self.grid = grid.Grid(width, height)
    self.color = color
    self.values = values
    self.rotation = 0
    # Values is an array of arrays of width x height containing 0/1. Each inner
    # array is one rotation of the piece.
    self.FillGrid(values[0])

  def FillGrid(self, values):
    for y in xrange(self.grid.height):
      for x in xrange(self.grid.width):
        self.grid.SetValue(x, y,
                           self.color if values[x + y * self.grid.width] else 0)

  def Rotate(self):
    self.rotation = (self.rotation + 1) % len(self.values)
    self.FillGrid(self.values[self.rotation])

  def Copy(self):
    return Piece(self.grid.width, self.grid.height, self.color, self.values)


# These are basically templates for each piece type. Use Copy() to create an
# individual instance of a piece that can be mutated.
SQUARE = Piece(2, 2, palette.RED, [[1, 1, 1, 1]])
BAR = Piece(4, 4, palette.GREEN,
            [
              [0, 0, 0, 0,
               1, 1, 1, 1,
               0, 0, 0, 0,
               0, 0, 0, 0],
              [0, 1, 0, 0,
               0, 1, 0, 0,
               0, 1, 0, 0,
               0, 1, 0, 0],
            ])

PIECE_TEMPLATES = [SQUARE, BAR]

# Returns a Piece of random type. Does not modify existing Piece objects.
def GetRandomPiece():
  random_value = random.randint(0, len(PIECE_TEMPLATES) - 1)
  return PIECE_TEMPLATES[random_value].Copy()
