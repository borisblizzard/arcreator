import os
import gc

import pyglet
import numpy
import PIL
from PIL import Image
import colorsys

import time

import Kernel
from Kernel import Manager as KM

#do stuff to use pygame with out a window
#os.environ["SDL_VIDEODRIVER"] = "dummy"
#if 1:
#   #some platforms might need to init the display for some parts of pygame.
#   import pygame
#   pygame.init()
#   screen = pygame.display.set_mode((1, 1))
#   from pygame import surfarray

class ImageFunctions(object):

    @staticmethod
    def Get_HSV_From_Image(image):
        a = numpy.asarray(image.convert('RGB'), int)
        R, G, B = a.T
        
        m = numpy.min(a,2).T
        M = numpy.max(a,2).T
    
        C = M-m #chroma
        Cmsk = C!=0
    
        # Hue
        H = numpy.zeros(R.shape, int)
        mask = (M==R)&Cmsk
        H[mask] = numpy.mod(60*(G[mask]-B[mask])/C[mask], 360)
        mask = (M==G)&Cmsk
        H[mask] = (60*(B[mask]-R[mask])/C[mask] + 120)
        mask = (M==B)&Cmsk
        H[mask] = (60*(R[mask]-G[mask])/C[mask] + 240)
        H *= 255
        H /= 360 # if you prefer, leave as 0-360, but don't convert to uint8
    
        # Value
        V = M
        # Saturation
        S = numpy.zeros(R.shape, int)
        S[Cmsk] = ((255*C[Cmsk])/V[Cmsk])
        
        # H, S, and V are now defined as integers 0-255
        return H, S, V
    
    @staticmethod 
    def Get_RGB_From_HSV(H, S, V):
        H = (H / 255.0) * 360.0
        S = (S / 255.0)
        V = (V / 255.0)
        
        C = V * S
        Hp = H / 60.0
        X = C * (1 - numpy.absolute(numpy.mod(Hp, 2) - 1))
        
        R = numpy.zeros(H.shape, float)
        G = numpy.zeros(H.shape, float)
        B = numpy.zeros(H.shape, float)
        
        mask = (0 <= Hp) & (Hp < 1)
        R[mask] = C[mask]
        mask = (1 <= Hp) & (Hp < 2)
        R[mask] = X[mask]
        mask = (2 <= Hp) & (Hp < 3)
        R[mask] = 0
        mask = (3 <= Hp) & (Hp < 4)
        R[mask] = 0
        mask = (4 <= Hp) & (Hp < 5)
        R[mask] = X[mask]
        mask = (5 <= Hp) & (Hp < 6)
        R[mask] = C[mask]
        
        mask = (0 <= Hp) & (Hp < 1)
        G[mask] = X[mask]
        mask = (1 <= Hp) & (Hp < 2)
        G[mask] = C[mask]
        mask = (2 <= Hp) & (Hp < 3)
        G[mask] = C[mask]
        mask = (3 <= Hp) & (Hp < 4)
        G[mask] = X[mask]
        mask = (4 <= Hp) & (Hp < 5)
        G[mask] = 0
        mask = (5 <= Hp) & (Hp < 6)
        G[mask] = 0
        
        mask = (0 <= Hp) & (Hp < 1)
        B[mask] = 0
        mask = (1 <= Hp) & (Hp < 2)
        B[mask] = 0
        mask = (2 <= Hp) & (Hp < 3)
        B[mask] = X[mask]
        mask = (3 <= Hp) & (Hp < 4)
        B[mask] = C[mask]
        mask = (4 <= Hp) & (Hp < 5)
        B[mask] = C[mask]
        mask = (5 <= Hp) & (Hp < 6)
        B[mask] = X[mask]
        
        m = V - C
        R += m
        G += m
        B += m
        
        R *= 255
        G *= 255
        B *= 255
        
        return R, G, B
                
    @staticmethod
    def change_hue_PIL(image, hue):
        Red, Green, Blue, Alpha = image.convert('RGBA').split()
        H, S, V = ImageFunctions.Get_HSV_From_Image(image)
        RH = (H + (int(255.0 * (hue / 360.0)))) % 255
        r, g, b = ImageFunctions.Get_RGB_From_HSV(RH, S, V)
        imagearray = numpy.array([r, g, b])
        newimage = Image.fromarray(imagearray.T.astype('uint8'))
        red, green, blue = newimage.split()
        finishedimage = Image.merge('RGBA', (red, green, blue, Alpha))
        return finishedimage

class RTPFunctions(Object):

    _image_ext = ["", ".png", ".gif", ".jpg", ".bmp"]

    @staticmethod
    def FindFile(name):
        rtps = Kernel.GlobalObjects.get_value("ARCed_config")["RTPs"]
        for path in rtps.values():
            for ext in PILCache._image_ext:
                path = os.path.abspath(os.path.normpath(loc + "/" + folder_name +
                                            filename + ext))
                if os.path.exists(path) and os.path.isfile(path):
                    break
            if not os.path.exists(path) or not os.path.isfile(path):
                return None


class PILCache(object):

    _Cache = {}
    
    

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

    @staticmethod
    def changeHue(image, hue):
        roatedImage = ImageFunctions.change_hue_PIL(image, hue)
        return roatedImage
      
    @staticmethod  
    def Load_bitmap(folder_name, filename, hue=0, loc=""):
        key = (folder_name, filename, loc, hue)
        if not PILCache._Cache.has_key(key) or not PILCache._Cache[key]:
            for ext in PILCache._image_ext:
                path = os.path.abspath(os.path.normpath(loc + "/" + folder_name +
                                            filename + ext))
                if os.path.exists(path) and os.path.isfile(path):
                    break
            if not os.path.exists(path) or not os.path.isfile(path):
                return None
            if filename != "":
                image = Image.open(path).convert('RGBA')
                if hue != 0:
                    image = PILCache.changeHue(image, hue)
                PILCache._Cache[key] = image
            else:
                return None
            return PILCache._Cache[key]
        else:
            return PILCache._Cache[key]

    @staticmethod
    def Animation(filename, hue, loc=""):
        return PILCache.Load_bitmap("Graphics/Animations/", filename, hue, loc)
    
    @staticmethod
    def Autotile(filename, loc=""):
        return PILCache.Load_bitmap("Graphics/Autotiles/", filename, 0, loc)

    @staticmethod
    def AutotilePattern(filename, pattern, loc=""):
        key = (loc + filename, pattern, 0)
        if not PILCache._Cache.has_key(key) or not PILCache._Cache[key]:
            autotile = PILCache.Autotile(filename, loc)
            if autotile:
                # Collects Auto-Tile Tile Layout
                tiles = PILCache.Autotiles[int(pattern) / 8][int(pattern) % 8]
                PILCache._Cache[key] = Image.new('RGBA', (32, 32), (0, 0, 0, 0))
                for i in xrange(4):
                    tile_position = tiles[i] - 1
                    x = tile_position % 6 * 16
                    y = tile_position / 6 * 16
                    autotile_part = autotile.crop((x, y, x + 16, y + 16))
                    tile_x = (i % 2 * 16)
                    tile_y = (i / 2 * 16)
                    PILCache._Cache[key].paste(autotile_part, (tile_x, tile_y))
            else:
                return None
        return PILCache._Cache[key]

    @staticmethod
    def Battleback(filename, loc=""):
        return PILCache.Load_bitmap("Graphics/Battlebacks/", filename, 0, loc)

    @staticmethod
    def Battler(filename, hue, loc=""):
        return PILCache.Load_bitmap("Graphics/Battlers/", filename, hue, loc)

    @staticmethod
    def Character(filename, hue, loc=""):
        return PILCache.Load_bitmap("Graphics/Characters/", filename, hue, loc)

    @staticmethod
    def Fog(filename, hue, loc=""):
        return PILCache.Load_bitmap("Graphics/Fogs/", filename, hue, loc)

    @staticmethod
    def Gameover(filename, loc=""):
        return PILCache.Load_bitmap("Graphics/Gameovers/", filename, 0, loc)

    @staticmethod
    def Icon(filename, loc=""):
        return PILCache.Load_bitmap("Graphics/Icons/", filename, 0, loc)

    @staticmethod
    def Panorama(filename, hue, loc=""):
        return PILCache.Load_bitmap("Graphics/Panoramas/", filename, hue, loc)

    @staticmethod
    def Picture(filename, loc=""):
        return PILCache.Load_bitmap("Graphics/Pictures/", filename, 0, loc)

    @staticmethod
    def Tileset(filename, loc=""):
        return PILCache.Load_bitmap("Graphics/Tilesets/", filename, 0, loc)

    @staticmethod
    def Title(filename, loc=""):
        return PILCache.Load_bitmap("Graphics/Titles/", filename, 0, loc)

    @staticmethod
    def Windowskin(filename, loc=""):
        return PILCache.Load_bitmap("Graphics/Windowskins/", filename, 0, loc)

    @staticmethod
    def Tile(filename, tile_id, hue, loc=""):
        key = (loc + filename, int(tile_id), hue)
        if not PILCache._Cache.has_key(key) or not PILCache._Cache[key]:
            tileset = PILCache.Tileset(filename, loc)
            if tileset:
                id = int(tile_id) - 384
                x = id % 8 * 32
                y = id / 8 * 32
                PILCache._Cache[key] = tileset.crop((x, y, x + 32, y + 32))
            else:
                return None
        return PILCache._Cache[key]

    @staticmethod
    def Clear():
        PILCache._Cache = {}
        gc.collect()

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
        
    def Load_bitmap(self, folder_name, filename, hue=0, loc=""):
        key = (folder_name, filename, loc, hue)
        if not self._Cache.has_key(key) or not self._Cache[key]:
            image = PILCache.Load_bitmap(folder_name, filename, hue, loc)
            if image != None:
                pygletimage = pyglet.image.create(*image.size).get_image_data()
                pitch = -len('RGBA') * pygletimage.width
                data = image.tostring()
                pygletimage.set_data('RGBA', pitch, data)
                self._Cache[key] = pygletimage
                return self._Cache[key]
            else:
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
            image = PILCache.AutotilePattern(filename, pattern, loc)
            if image != None:
                pygletimage = pyglet.image.create(*image.size).get_image_data()
                pitch = -len('RGBA') * pygletimage.width
                data = image.tostring()
                pygletimage.set_data('RGBA', pitch, data)
                self._Cache[key] = pygletimage
                return self._Cache[key]
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
            image = PILCache.Tile(filename, tile_id, hue, loc)
            if image != None:
                pygletimage = pyglet.image.create(*image.size).get_image_data()
                pitch = -len('RGBA') * pygletimage.width
                data = image.tostring()
                pygletimage.set_data('RGBA', pitch, data)
                self._Cache[key] = pygletimage
                return self._Cache[key]
            else:
                return None
        return self._Cache[key]

    def Clear(self):
        self._Cache = {}
        gc.collect()