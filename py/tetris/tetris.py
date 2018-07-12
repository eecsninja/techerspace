import sys
import ctypes
import common.hello_world as hello_world
import common.color as color
from sdl2 import *


def main():
    SDL_Init(SDL_INIT_VIDEO)
    window = SDL_CreateWindow(hello_world.HELLO_WORLD_STR,
                              SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
                              256, 512, SDL_WINDOW_SHOWN)
    windowsurface = SDL_GetWindowSurface(window)
    RED = color.rgb_to_color_value(windowsurface, 255, 0, 0)
    GREEN = color.rgb_to_color_value(windowsurface, 0, 255, 0)
    BLUE = color.rgb_to_color_value(windowsurface, 0, 0, 255)

    test_rect = SDL_Rect(0, 480, 32, 32)
    SDL_FillRect(windowsurface, test_rect, GREEN)
    SDL_FillRect(windowsurface, SDL_Rect(0, 0, 32, 32), RED)
    SDL_FillRect(windowsurface, SDL_Rect(0, 32, 32, 32), BLUE)

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
