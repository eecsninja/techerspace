from sdl2 import SDL_Rect
# this file defines the grid classes that implement the grid logic as well as the grid drawing


# class Thingy:
#     """This class stores an arbistrary object"""
#     # constructor
#     def __init__(self, value):
#         self.value = value
#
#     # method
#     def showme(self):
#         """Print this object to stdout."""
#         print("value = %s", self.value)
#
#     # an alternative versoin of showme
#     def __repr__(self):
#         return str(self.value)

# now we define a class tetrisgrid which defines and initializes a grid of predetermined size

class TetrisGrid:
    # constructor to initialize the grid
    def __init__(self, num_blocks_w, num_blocks_h, num_block_pixels):
        self.num_blocks_w = num_blocks_w
        self.num_blocks_h = num_blocks_h
        self.num_block_pixels = num_block_pixels

        # inititalize our grid
        tetrisgrid = {}
        for ii in range(self.num_blocks_h):
            tetrisgrid[ii] = {}
            for jj in range(self.num_blocks_w):
                tetrisgrid[ii][jj] = 0

        self.grid_dict = tetrisgrid

    # return the entire grid
    def get_grid(self):
        return self.grid_dict

    # set the entire grid
    def set_grid(self, new_grid):
        # insert checking to make sure the types and sizes of the old and new grid are the same
        self.grid_dict = new_grid

    # get a grid value
    def get_value(self, row_ii, col_jj):
        return self.grid_dict[row_ii][col_jj]

    # set a grid value
    def set_value(self, row_ii, col_jj, new_value):
        self.grid_dict[row_ii][col_jj] = new_value

    # return an SDL_Rect object corresponding to the specified window block
    def get_sdl_rect(self, row_ii, col_jj):
        x_coord = self.num_block_pixels * row_ii
        y_coord = self.num_block_pixels * col_jj
        return SDL_Rect(x_coord, y_coord, self.num_block_pixels, self.num_block_pixels)

    # get the window width in pixels
    def get_window_w(self):
        return self.num_blocks_w * self.num_block_pixels

    # get the window height in pixels
    def get_window_h(self):
        return self.num_blocks_h * self.num_block_pixels



