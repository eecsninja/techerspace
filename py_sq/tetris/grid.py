class Grid:
  def __init__(self, width, height):
    self.width = width
    self.height = height

    self.array = [0] * width * height

  def SetValue(self, x, y, value):
    # TODO: Check bounds.
    self.array[x + self.width * y] = value

  def GetValue(self, x, y):
    # TODO: Check bounds.
    return self.array[x + self.width * y]
