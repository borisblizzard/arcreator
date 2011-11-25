import os
import gc

import pyglet
import numpy
import PIL
from PIL import Image
import colorsys

import time

import collections

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

    @staticmethod
    def PilImageToWxImage(pilImage, copyAlpha=True):

        hasAlpha = pilImage.mode[-1] == 'A'
        if copyAlpha and hasAlpha:  # Make sure there is an alpha layer copy.
            wxImage = wx.EmptyImage(*pilImage.size)
            pilImageCopyRGBA = pilImage.copy()
            pilImageCopyRGB = pilImageCopyRGBA.convert('RGB')    # RGBA --> RGB
            pilImageRgbData = pilImageCopyRGB.tostring()
            wxImage.SetData(pilImageRgbData)
            wxImage.SetAlphaData(pilImageCopyRGBA.tostring()[3::4])  # Create layer and insert alpha values.
        else:    # The resulting image will not have alpha.
            wxImage = wx.EmptyImage(*pilImage.size)
            pilImageCopy = pilImage.copy()
            pilImageCopyRGB = pilImageCopy.convert('RGB')    # Discard any alpha from the PIL image.
            pilImageRgbData = pilImageCopyRGB.tostring()
            wxImage.SetData(pilImageRgbData)

        return wxImage

class RTPFunctions(object):

    _image_ext = ["", ".png", ".gif", ".jpg", ".bmp"]
    _audio_ext = ['', '.wav', '.ogg'] # No .mid for now

    @staticmethod
    def FindFile(folder_name, name):
        flag = False
        flag, testpath = RTPFunctions.TestFiles(Kernel.GlobalObjects.get_value("CurrentProjectDir"), folder_name, name)
        if flag:
            return testpath
        else:
            rtps = Kernel.GlobalObjects.get_value("ARCed_config").get_section("RTPs")
            for rtp_name, path in rtps.iteritems():
                flag, testpath = RTPFunctions.TestFiles(path, folder_name, name)
            if flag:
                return testpath
            else:
                return ""
            
    @staticmethod
    def TestFiles(path, folder_name, name):
        for ext in RTPFunctions._image_ext:
            testpath = os.path.normpath(os.path.expandvars(os.path.join(path, folder_name, name + ext)))
            if os.path.exists(testpath) and os.path.isfile(testpath):
                return True, testpath
        return False, ""

    @staticmethod
    def GetFileList(folder, type='image'):
        files, entries = [], []
        if type == 'image': extensions = RTPFunctions._image_ext
        elif type == 'audio': extensions = RTPFunctions._audio_ext
        else: return files
        directories = [Kernel.GlobalObjects.get_value('CurrentProjectDir')]
        rtps = Kernel.GlobalObjects.get_value("ARCed_config").get_section("RTPs")
        directories.extend([os.path.expandvars(path[1]) for path in rtps.iteritems()])
        for dir in directories:
            entries.extend(os.listdir(os.path.join(dir, folder)))
        for entry in entries:
            file, ext = os.path.splitext(entry)
            if ext in extensions:
                files.append(file)
        return files

    @staticmethod
    def FindAudioFile(folder_name, name):
        flag = False
        flag, testpath = RTPFunctions.TestAudioFiles(Kernel.GlobalObjects.get_value("CurrentProjectDir"), folder_name, name)
        if flag:
            return testpath
        else:
            rtps = Kernel.GlobalObjects.get_value("ARCed_config").get_section("RTPs")
            for rtp_name, path in rtps.iteritems():
                flag, testpath = RTPFunctions.TestAudioFiles(path, folder_name, name)
            if flag:
                return testpath
            else:
                return ""

    @staticmethod
    def TestAudioFiles(path, folder_name, name):
        for ext in RTPFunctions._audio_ext:
            testpath = os.path.normpath(os.path.expandvars(os.path.join(path, folder_name, name + ext)))
            if os.path.exists(testpath) and os.path.isfile(testpath):
                return True, testpath
        return False, ""

class PILCache(object):

    _NormalCache = collections.OrderedDict()
    _TileCache = collections.OrderedDict()
    _AutoTileCache = collections.OrderedDict()

    _normal_limit = 200
    _tile_limit = 100
    _hue_limit = 5
    _autotile_limit = 250
    

    try:
        config = Kernel.GlobalObjects.get_value("ARCed_config")
        if config.has_section("Cache"):
            section = config.get_section("Cache")
            if section.has_item("normal_limit"):
                _normal_limit = config.getint("Cache", "normal_limit")
                if _normal_limit <= 1: _normal_limit = 2
            if section.has_item("tile_limit"):
                _tile_limit = config.getint("Cache", "tile_limit")
                if _tile_limit <= 1: _tile_limit = 2
            if section.has_item("autotile_limit"):
                _autotile_limit = config.getint("Cache", "autotile_limit")
                if _autotile_limit <= 1: _autotile_limit = 2
            if section.has_item("hue_limit"):
                _hue_limit = config.getint("Cache", "hue_limit")
                if _hue_limit <= 1: _hue_limit = 2
            del section

        del config
    except:
        Kernel.Log("Error setting PIL Cache Config", "[Cache]", error=True)
    
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
    def NormalCacheLimit():
        if len(PILCache._NormalCache) > PILCache._normal_limit:
            for i in xrange(len(PILCache._NormalCache) - PILCache._normal_limit):
                item = PILCache._NormalCache.popitem(False)
                del item
            gc.collect()

    @staticmethod
    def TileCacheLimit():
        if len(PILCache._TileCache) > PILCache._tile_limit:
            for i in xrange(len(PILCache._TileCache) - PILCache._tile_limit):
                item = PILCache._TileCache.popitem(False)
                del item
            gc.collect()

    @staticmethod
    def AutotileCacheLimit():
        if len(PILCache._AutoTileCache) > PILCache._autotile_limit:
            for i in xrange(len(PILCache._AutoTileCache) - PILCache._autotile_limit):
                item = PILCache._AutoTileCache.popitem(False)
                del item
            gc.collect()

    @staticmethod
    def HueCacheLimit(cache, key):
        if cache.has_key(key):
            if len(cache[key]) > PILCache._hue_limit:
                for i in xrange(len(cache[key]) - PILCache._hue_limit):
                    item = cache[key].popitem(False)
                    del item

    @staticmethod
    def CacheLimit():
        PILCache.NormalCacheLimit()
        PILCache.TileCacheLimit()
        PILCache.AutotileCacheLimit()

    @staticmethod  
    def Load_bitmap(folder_name, filename, hue=0):
        key = (folder_name, filename)
        if not PILCache._NormalCache.has_key(key):
            PILCache._NormalCache[key] = collections.OrderedDict()
        try:
            return PILCache._NormalCache[key][hue]
        except KeyError:
            path = RTPFunctions.FindFile(folder_name, filename)
            if path != "":
                image = Image.open(path).convert('RGBA')
                if hue != 0:
                    image = PILCache.changeHue(image, hue)
            
                PILCache._NormalCache[key][hue] = image
                PILCache.HueCacheLimit(PILCache._NormalCache, key)
                del image
                return PILCache._NormalCache[key][hue]
            else:
                return None          

    @staticmethod
    def Animation(filename, hue):
        return PILCache.Load_bitmap("Graphics/Animations/", filename, hue)
    
    @staticmethod
    def Autotile(filename):
        return PILCache.Load_bitmap("Graphics/Autotiles/", filename, 0)

    @staticmethod
    def AutotilePattern(filename, pattern):
        key = (filename, pattern, 0)
        try:
            return PILCache._AutoTileCache[key]
        except KeyError:
            autotile = PILCache.Autotile(filename)
            if autotile:
                # Collects Auto-Tile Tile Layout
                tiles = PILCache.Autotiles[int(pattern) / 8][int(pattern) % 8]
                PILCache._AutoTileCache[key] = Image.new('RGBA', (32, 32), (0, 0, 0, 0))
                for i in xrange(4):
                    tile_position = tiles[i] - 1
                    x = tile_position % 6 * 16
                    y = tile_position / 6 * 16
                    autotile_part = autotile.crop((x, y, x + 16, y + 16))
                    tile_x = (i % 2 * 16)
                    tile_y = (i / 2 * 16)
                    PILCache._AutoTileCache[key].paste(autotile_part, (tile_x, tile_y))
                    del autotile_part
                del tiles
                del autotile
                return PILCache._AutoTileCache[key]
            else:
                del autotile
                return None
        

    @staticmethod
    def Battleback(filename):
        return PILCache.Load_bitmap("Graphics/Battlebacks/", filename, 0)

    @staticmethod
    def Battler(filename, hue):
        return PILCache.Load_bitmap("Graphics/Battlers/", filename, hue)

    @staticmethod
    def Character(filename, hue):
        return PILCache.Load_bitmap("Graphics/Characters/", filename, hue)

    @staticmethod
    def Fog(filename, hue):
        return PILCache.Load_bitmap("Graphics/Fogs/", filename, hue)

    @staticmethod
    def Gameover(filename):
        return PILCache.Load_bitmap("Graphics/Gameovers/", filename, 0)

    @staticmethod
    def Icon(filename):
        return PILCache.Load_bitmap("Graphics/Icons/", filename, 0)

    @staticmethod
    def Panorama(filename, hue):
        return PILCache.Load_bitmap("Graphics/Panoramas/", filename, hue)

    @staticmethod
    def Picture(filename):
        return PILCache.Load_bitmap("Graphics/Pictures/", filename, 0)

    @staticmethod
    def Tileset(filename):
        return PILCache.Load_bitmap("Graphics/Tilesets/", filename, 0)

    @staticmethod
    def Title(filename):
        return PILCache.Load_bitmap("Graphics/Titles/", filename, 0)

    @staticmethod
    def Windowskin(filename):
        return PILCache.Load_bitmap("Graphics/Windowskins/", filename, 0)

    @staticmethod
    def Tile(filename, tile_id, hue):
        key = (filename, int(tile_id))
        if not PILCache._TileCache.has_key(key):
            PILCache._TileCache[key] = collections.OrderedDict()
        try:
            return PILCache._TileCache[key][hue]
        except KeyError:
            tileset = PILCache.Tileset(filename)
            if tileset:
                id = int(tile_id) - 384
                x = id % 8 * 32
                y = id / 8 * 32
                PILCache._TileCache[key][hue] = tileset.crop((x, y, x + 32, y + 32))
                PILCache.HueCacheLimit(PILCache._TileCache, key)
                del tileset
                return PILCache._TileCache[key][hue]
                
            else:
                del tileset
                return None
        

    @staticmethod
    def Clear():
        PILCache._NormalCache = collections.OrderedDict()
        PILCache._TileCache = collections.OrderedDict()
        PILCache._AutoTileCache = collections.OrderedDict()
        gc.collect()

class PygletCache(object):

    def __init__(self):
        self._Cache = collections.OrderedDict()
        self.limit = 200
        try:
            config = Kernel.GlobalObjects.get_value("ARCed_config")
            if config.has_section("Cache"):
                section = config.get_section("Cache")
                if section.has_item("pyglet_limit"):
                    self.limit = config.getint("Cache", "pyglet_limit")
        except:
            Kernel.Log("Error setting pyglet Cache Config", "[Cache]", error=True)

    def CacheLimit(self):
        if len(self._Cache) > self.limit:
            for i in xrange(len(self._Cache) - self.limit):
                item = self._Cache.popitem(False)
                del item
        
    def Load_bitmap(self, folder_name, filename, hue=0):
        key = (folder_name, filename, hue)
        try:
            return self._Cache[key]
        except KeyError:
            image = PILCache.Load_bitmap(folder_name, filename, hue)
            if image != None:
                pygletimage = pyglet.image.create(*image.size).get_image_data()
                pitch = -len('RGBA') * pygletimage.width
                data = image.tostring()
                pygletimage.set_data('RGBA', pitch, data)
                self._Cache[key] = pygletimage
                del pygletimage
                del data
                del image
                return self._Cache[key]
            else:
                del image
                return None
            
    def Animation(self, filename, hue):
        return self.Load_bitmap("Graphics/Animations/", filename, hue)

    def Autotile(self, filename):
        return self.Load_bitmap("Graphics/Autotiles/", filename, 0)

    def AutotilePattern(self, filename, pattern):
        key = (filename, pattern, 0)
        try:
            return self._Cache[key]
        except KeyError:
            image = PILCache.AutotilePattern(filename, pattern)
            if image != None:
                pygletimage = pyglet.image.create(*image.size).get_image_data()
                pitch = -len('RGBA') * pygletimage.width
                data = image.tostring()
                pygletimage.set_data('RGBA', pitch, data)
                self._Cache[key] = pygletimage
                del image
                del data
                del pygletimage
                return self._Cache[key]
            else:
                del image
                return None

    def Battleback(self, filename):
        return self.Load_bitmap("Graphics/Battlebacks/", filename, 0)

    def Battler(self, filename, hue):
        return self.Load_bitmap("Graphics/Battlers/", filename, hue)

    def Character(self, filename, hue):
        return self.Load_bitmap("Graphics/Characters/", filename, hue)

    def Fog(self, filename, hue):
        return self.Load_bitmap("Graphics/Fogs/", filename, hue)

    def Gameover(self, filename):
        return self.Load_bitmap("Graphics/Gameovers/", filename, 0)

    def Icon(self, filename):
        return self.Load_bitmap("Graphics/Icons/", filename, 0)

    def Panorama(self, filename, hue):
        return self.Load_bitmap("Graphics/Panoramas/", filename, hue)

    def Picture(self, filename):
        return self.Load_bitmap("Graphics/Pictures/", filename, 0)

    def Tileset(self, filename):
        return self.Load_bitmap("Graphics/Tilesets/", filename, 0)

    def Title(self, filename):
        return self.Load_bitmap("Graphics/Titles/", filename, 0)

    def Windowskin(self, filename):
        return self.Load_bitmap("Graphics/Windowskins/", filename, 0)

    def Tile(self, filename, tile_id, hue):
        key = (filename, int(tile_id), hue)
        try:
            return self._Cache[key]
        except KeyError:
            image = PILCache.Tile(filename, tile_id, hue)
            if image != None:
                pygletimage = pyglet.image.create(*image.size).get_image_data()
                pitch = -len('RGBA') * pygletimage.width
                data = image.tostring()
                pygletimage.set_data('RGBA', pitch, data)
                self._Cache[key] = pygletimage
                del image
                del data
                del pygletimage
                return self._Cache[key]
            else:
                del image
                return None

    def Clear(self):
        self._Cache = {}
        gc.collect()