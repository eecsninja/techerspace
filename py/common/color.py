from sdl2 import *


def rgb_to_color_value(surface, r_int, g_int, b_int):
    return SDL_MapRGB(surface.contents.format, r_int, g_int, b_int)

