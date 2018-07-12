from sdl2 import *


def rgb_to_color_value(windowsurface, r_int, g_int, b_int):
    return SDL_MapRGB(windowsurface.contents.format, r_int, g_int, b_int)

