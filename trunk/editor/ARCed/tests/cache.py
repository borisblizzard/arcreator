import os
import gc

import pyglet
import numpy
from PIL import Image
import colorsys

import time

#do stuff to use pygame with out a window
#os.environ["SDL_VIDEODRIVER"] = "dummy"
#if 1:
#   #some platforms might need to init the display for some parts of pygame.
#   import pygame
#   pygame.init()
#   screen = pygame.display.set_mode((1, 1))
#   from pygame import surfarray

class ImageFunctions(object):

#    @staticmethod
#    def change_hue_pygame(surface, hue):
#        surface.lock()
#        for x in range(surface.get_width()):
#            for y in range(surface.get_height()):
#                color = pygame.Color(*surface.get_at((x, y)))
#                hsva = list(color.hsva)
#                hsva[0] = (hsva[0] + float(hue)) % 360.0
#                color.hsva = hsva
#                surface.set_at((x, y), (color.r, color.g, color.b, color.a))
#        surface.unlock()
    
    @staticmethod
    def normalize(r, g, b, a=None):
        if a is None:
            color = (r / 255.0, g / 255.0, b / 255.0)
        else:
            color = (r / 255.0, g / 255.0, b / 255.0, a / 255.0)
        return color
    
    @staticmethod
    def de_normalize(r, g, b, a=None):
        if a is None:
            color = (int(r * 255), int(g * 255), int(b * 255))
        else:
            color = (int(r * 255), int(g * 255), int(b * 255), int(a * 255))
        return color
    
    @staticmethod
    def change_hue_PIL(image, hue):
        for x in range(image.size[0]):
            for y in range(image.size[1]):
                color = list(image.getpixel((x, y)))
                rgb = ImageFunctions.normalize(*color[:3])
                hls = list(colorsys.rgb_to_hls(*rgb))
                hls[0] = (hls[0] + float(hue / 360.0)) % 1.0
                rgb = colorsys.hls_to_rgb(*hls)
                color[:3] = ImageFunctions.de_normalize(*rgb)
                image.putpixel((x, y), tuple(color))
    
#    @staticmethod
#    def adjust_alpha_pygame(surface, alpha):
#        if alpha > 255:
#            alpha = 255
#        if alpha < 0:
#            alpha = 0
#        factor = float(alpha) / 255.0
#        alphas = surfarray.pixels_alpha(surface)
#        alphas = (alphas * factor)
#        alphas = numpy.clip(alphas, 0, 255)
#        alphas[:] = alphas.astype("uint8")
#        del alphas


class PygletCache(object):

    
    _image_ext = ["", ".png", ".gif", ".jpg", ".bmp"]

    Autotiles = [
               [[27, 28, 33, 34], [5, 28, 33, 34], [27, 6, 33, 34],
                [5, 6, 33, 34], [27, 28, 33, 12], [5, 28, 33, 12],
                [27, 6, 33, 12], [5, 6, 33, 12] ],
               [[27, 28, 11, 34], [5, 28, 11, 34], [27, 6, 11, 34],
                [5, 6, 11, 34], [27, 28, 11, 12], [5, 28, 11, 12],
                [27, 6, 11, 12], [5, 6, 11, 12] ],
               [[25, 26, 31, 32], [25, 6, 31, 32], [25, 26, 31, 12],
                [25, 6, 31, 12], [15, 16, 21, 22], [15, 16, 21, 12],
                [15, 16, 11, 22], [15, 16, 11, 12] ],
               [[29, 30, 35, 36], [29, 30, 11, 36], [5, 30, 35, 36],
                [5, 30, 11, 36], [39, 40, 45, 46], [5, 40, 45, 46],
                [39, 6, 45, 46], [5, 6, 45, 46] ],
               [[25, 30, 31, 36], [15, 16, 45, 46], [13, 14, 19, 20],
                [13, 14, 19, 12], [17, 18, 23, 24], [17, 18, 11, 24],
                [41, 42, 47, 48], [5, 42, 47, 48] ],
               [[37, 38, 43, 44], [37, 6, 43, 44], [13, 18, 19, 24],
                [13, 14, 43, 44], [37, 42, 43, 48], [17, 18, 47, 48],
                [13, 18, 43, 48], [1, 2, 7, 8] ]
               ]


    def __init__(self):
        self._Cache = {}
        
    def changeHue(self, image, hue):
        pitch = len('RGBA') * image.width
        data = image.get_data('RGBA', pitch)
        
        #t = time.time()
        
        #surface = pygame.image.frombuffer(data, (image.width, image.height), 'RGBA')
        #ImageFunctions.change_hue_pygame(surface, hue)
        
        im = Image.fromstring('RGBA', (image.width, image.height), data)
        ImageFunctions.change_hue_PIL(im, hue)
        
        #newdata = pygame.image.tostring(surface, 'RGBA')
        newdata = im.tostring()
        
        image.set_data('RGBA', pitch, newdata)
        
        #print time.time() - t
        
        return image
        
    def Load_bitmap(self, folder_name, filename, hue=0, loc=""):
        key = (folder_name, filename, loc, hue)
        if not self._Cache.has_key(key) or not self._Cache[key]:
            for ext in self._image_ext:
                path = os.path.abspath(os.path.normpath(loc + "/" + folder_name +
                                            filename + ext))
                if os.path.exists(path) and os.path.isfile(path):
                    break
            if not os.path.exists(path) and not os.path.isfile(path):
                return None
            try:
                if filename != "":
                    image = pyglet.image.load(path)
                    if hue != 0:
                        image = self.changeHue(image.get_image_data(), hue)
                    self._Cache[key] = image
                else:
                    return None
                return self._Cache[key]
            except AttributeError:
               return None
        else:
            return self._Cache[key]


    def Animation(self, filename, hue, loc=""):
        return self.Load_bitmap("Graphics/Animations/", filename, hue, loc)

    def Autotile(self, filename, loc=""):
        return self.Load_bitmap("Graphics/Autotiles/", filename, 0, loc)

    def AutotilePattern(self, filename, pattern, loc=""):
        key = (loc + filename, pattern, 0)
        if not self._Cache.has_key(key) or not self._Cache[key]:
            autotile = self.Autotile(filename, loc)
            if autotile:
                # Collects Auto-Tile Tile Layout
                tiles = self.Autotiles[int(pattern) / 8][int(pattern) % 8]
                self._Cache[key] = pyglet.image.create(32, 32).get_texture()
                for i in range(4):
                    tile_position = tiles[i] - 1
                    x = tile_position % 6 * 16
                    y = tile_position / 6 * 16
                    autotile_part = autotile.get_region(x, autotile.height - y - 16, 16, 16)
                    tile_x = (i % 2 * 16)
                    tile_y = 16 - (i / 2 * 16)
                    self._Cache[key].blit_into(autotile_part, tile_x, tile_y, 0)
            else:
                return None
        return self._Cache[key]

    def Battleback(self, filename, loc=""):
        return self.Load_bitmap("Graphics/Battlebacks/", filename, 0, loc)

    def Battler(self, filename, hue, loc=""):
        return self.Load_bitmap("Graphics/Battlers/", filename, hue, loc)

    def Character(self, filename, hue, loc=""):
        return self.Load_bitmap("Graphics/Characters/", filename, hue, loc)

    def Fog(self, filename, hue, loc=""):
        return self.Load_bitmap("Graphics/Fogs/", filename, hue, loc)

    def Gameover(self, filename, loc=""):
        return self.Load_bitmap("Graphics/Gameovers/", filename, 0, loc)

    def Icon(self, filename, loc=""):
        return self.Load_bitmap("Graphics/Icons/", filename, 0, loc)

    def Panorama(self, filename, hue, loc=""):
        return self.Load_bitmap("Graphics/Panoramas/", filename, hue, loc)

    def Picture(self, filename, loc=""):
        return self.Load_bitmap("Graphics/Pictures/", filename, 0, loc)

    def Tileset(self, filename, loc=""):
        return self.Load_bitmap("Graphics/Tilesets/", filename, 0, loc)

    def Title(self, filename, loc=""):
        return self.Load_bitmap("Graphics/Titles/", filename, 0, loc)

    def Windowskin(self, filename, loc=""):
        return self.Load_bitmap("Graphics/Windowskins/", filename, 0, loc)

    def Tile(self, filename, tile_id, hue, loc=""):
        key = (loc + filename, int(tile_id), hue)
        if not self._Cache.has_key(key) or not self._Cache[key]:
            tileset = self.Tileset(filename, loc)
            if tileset:
                id = int(tile_id) - 384
                x = id % 8 * 32
                y = id / 8 * 32
                self._Cache[key] = tileset.get_region(x, tileset.height - y - 32, 32, 32)
            else:
                return None
        return self._Cache[key]

    def Clear(self):
        self._Cache = {}
        gc.collect()