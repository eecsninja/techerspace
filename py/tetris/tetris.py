import sys
import ctypes
import common.hello_world as hello_world
import common.color as color
import common.grid as grid
from sdl2 import *


def main():
    # initialize a tetris grid data object
    tgrid_row_n = 20
    tgrid_col_n = 10
    tgrid_block_pixel = 20
    tgrid = grid.TetrisGrid(tgrid_row_n, tgrid_col_n, tgrid_block_pixel)
    SDL_Init(SDL_INIT_VIDEO)
    window = SDL_CreateWindow(hello_world.HELLO_WORLD_STR,
                              SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
                              tgrid.get_window_w(), tgrid.get_window_h(), SDL_WINDOW_SHOWN)
    print(tgrid.get_window_w())
    print(tgrid.get_window_h())
    windowsurface = SDL_GetWindowSurface(window)
    RED = color.rgb_to_color_value(windowsurface, 255, 0, 0)
    GREEN = color.rgb_to_color_value(windowsurface, 0, 255, 0)
    BLUE = color.rgb_to_color_value(windowsurface, 0, 0, 255)
    BLACK = color.rgb_to_color_value(windowsurface, 0, 0, 0)

    # inititalize the screen to be entirely black
    for ii in range(tgrid_row_n):
        for jj in range(tgrid_col_n):
            tgrid.set_value(ii, jj, BLACK)

    # test some tgrid functions
    tgrid.set_value(0, 9, BLUE)
    tgrid.set_value(10, 0, RED)
    tgrid.set_value(19, 4, GREEN)
    print(tgrid.get_value(10,0))
    print(tgrid.get_grid())
    # test loop to draw every element of the mapped screen
    for ii in range(tgrid_row_n):
        for jj in range(tgrid_col_n):
            SDL_FillRect(windowsurface, tgrid.get_sdl_rect(ii, jj), tgrid.get_value(ii, jj))

    # test_rect = SDL_Rect(0, 480, 32, 32)
    # SDL_FillRect(windowsurface, test_rect, GREEN)
    # SDL_FillRect(windowsurface, SDL_Rect(0, 0, 32, 32), RED)
    # SDL_FillRect(windowsurface, SDL_Rect(0, 32, 32, 32), BLUE)

    SDL_UpdateWindowSurface(window)

    running = True
    event = SDL_Event()
    while running:
        while SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == SDL_QUIT:
                running = False
                break

    SDL_DestroyWindow(window)
    SDL_Quit()
    return 0


if __name__ == "__main__":
    sys.exit(main())
