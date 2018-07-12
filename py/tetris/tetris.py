import sys
import ctypes
from sdl2 import *


def main():
    SDL_Init(SDL_INIT_VIDEO)
    window = SDL_CreateWindow(hello_world.HELLO_WORLD_STR,
                              SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
                              512, 256, SDL_WINDOW_SHOWN)
    windowsurface = SDL_GetWindowSurface(window)
    test_rect = SDL_Rect(25, 25, 50, 50)
    SDL_FillRect(windowsurface, test_rect, SDL_MapRGB(windowsurface.contents.format, 0, 255, 0))

    #image = SDL_LoadBMP(b"pysdl.bmp")
    #SDL_BlitSurface(image, None, windowsurface, None)

    SDL_UpdateWindowSurface(window)
    #SDL_FreeSurface(image)

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
