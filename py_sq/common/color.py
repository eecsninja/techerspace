from sdl2 import *

def RGBToColorValue(surface, r, g, b):
    return SDL_MapRGB(surface.contents.format, r, g, b)