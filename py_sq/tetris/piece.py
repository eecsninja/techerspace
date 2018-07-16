import random

# Local imports
import grid
import palette

class Piece:
  def __init__(self, width, height, color, values, rotation=0):
    self.grid = grid.Grid(width, height)
    self.color = color
    self.values = values
    self.rotation = rotation
    # Values is an array of arrays of width x height containing 0/1. Each inner
    # array is one rotation of the piece.
    self.FillGrid(values[self.rotation])

  def FillGrid(self, values):
    for y in xrange(self.grid.height):
      for x in xrange(self.grid.width):
        self.grid.SetValue(x, y,
                           self.color if values[x + y * self.grid.width] else 0)

  def Rotate(self):
    self.rotation = (self.rotation + 1) % len(self.values)
    self.FillGrid(self.values[self.rotation])

  def Copy(self):
    return Piece(self.grid.width, self.grid.height, self.color, self.values,
                 self.rotation)

  # Returns true/false based on whether there is a block collision between the
  # piece and the existing grid blocks, for a given offset.
  def CollidesWithGridBlocks(self, test_grid, piece_x, piece_y, border=False):
    for offset_y in xrange(self.grid.height):
      for offset_x in xrange(self.grid.width):
        piece_value = self.grid.GetValue(offset_x, offset_y)
        grid_value = test_grid.GetValue(piece_x + offset_x, piece_y + offset_y,
                                        border)
        if piece_value != 0 and grid_value != 0:
          return True
  
    return False
  
  # Returns true/false based on whether the piece collides with the border.
  def CollidesWithGridBorder(self, test_grid, piece_x, piece_y):
    # Create an empty grid.
    empty_grid = grid.Grid(test_grid.width, test_grid.height)
  
    return self.CollidesWithGridBlocks(empty_grid, piece_x, piece_y, True)

  # Adds the blocks of the piece to a grid at a particular location.
  def AddToGrid(self, dest_grid, piece_x, piece_y):
    for offset_y in xrange(self.grid.height):
      for offset_x in xrange(self.grid.width):
        piece_value = self.grid.GetValue(offset_x, offset_y)
        if piece_value != 0:
          dest_grid.SetValue(piece_x + offset_x, piece_y + offset_y,
                             piece_value)


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
