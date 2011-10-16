'''
Created on Dec 20, 2010

contains the cache modules 

Classes in this module
-----------------------
WxCache - graphics cache for the WxPython drawing methods
'''

import wx
import os
import gc

#if we ever need pygame
#===============================================================================
# os.environ["SDL_VIDEODRIVER"] = "dummy"
# if 1:
#    #some platforms might need to init the display for some parts of pygame.
#    import pygame
#    pygame.init()
#    screen = pygame.display.set_mode((1, 1))
#===============================================================================

import Kernel
from Kernel import Manager as KM

import RPGutil
#ChangeHue = RPGutil.PySurfaceFunctions.change_hue

class WxCache(object):

    _Cache = {}
    _image_ext = ["", ".png", ".gif", ".jpg", ".bmp"]

    @staticmethod
    def Load_bitmap(folder_name, filename, hue=0, loc=""):
        key = (folder_name, filename, loc, hue)
        if not WxCache._Cache.has_key(key) or not WxCache._Cache[key].Ok:
            for ext in WxCache._image_ext:
                path = os.path.abspath(os.path.normpath(loc + "/" + folder_name +
                                           filename + ext))
                if os.path.exists(path) and os.path.isfile(path):
                    break
            if not os.path.exists(path) and not os.path.isfile(path):
                return None
            try:
                if filename != "":
                    image = wx.Image(path)
                    if hue != 0:
                        image.RotateHue(hue / 360.0)
                    WxCache._Cache[key] = image.ConvertToBitmap()
                else:
                    return None
                return WxCache._Cache[key]
            except:
                wx.MessageBox("Warning: loading of file %s failed." % path)
        else:
            return WxCache._Cache[key]

    @staticmethod
    def Animation(filename, hue, loc=""):
        return WxCache.Load_bitmap("Graphics/Animations/", filename, hue, loc)

    @staticmethod
    def Autotile(filename, loc=""):
        return WxCache.Load_bitmap("Graphics/Autotiles/", filename, 0, loc)

    @staticmethod
    def Battleback(filename, loc=""):
        return WxCache.Load_bitmap("Graphics/Battlebacks/", filename, 0, loc)

    @staticmethod
    def Battler(filename, hue, loc=""):
        return WxCache.Load_bitmap("Graphics/Battlers/", filename, hue, loc)

    @staticmethod
    def Character(filename, hue, loc=""):
        return WxCache.Load_bitmap("Graphics/Characters/", filename, hue, loc)

    @staticmethod
    def Fog(filename, hue, loc=""):
        return WxCache.Load_bitmap("Graphics/Fogs/", filename, hue, loc)

    @staticmethod
    def Gameover(filename, loc=""):
        return WxCache.Load_bitmap("Graphics/Gameovers/", filename, 0, loc)

    @staticmethod
    def Icon(filename, loc=""):
        return WxCache.Load_bitmap("Graphics/Icons/", filename, 0, loc)

    @staticmethod
    def Panorama(filename, hue, loc=""):
        return WxCache.Load_bitmap("Graphics/Panoramas/", filename, hue, loc)

    @staticmethod
    def Picture(filename, loc=""):
        return WxCache.Load_bitmap("Graphics/Pictures/", filename, 0, loc)

    @staticmethod
    def Tileset(filename, loc=""):
        return WxCache.Load_bitmap("Graphics/Tilesets/", filename, 0, loc)

    @staticmethod
    def Title(filename, loc=""):
        return WxCache.Load_bitmap("Graphics/Titles/", filename, 0, loc)

    @staticmethod
    def Windowskin(filename, loc=""):
        return WxCache.Load_bitmap("Graphics/Windowskins/", filename, 0, loc)

    @staticmethod
    def Tile(filename, tile_id, hue, loc=""):
        try:
            key = [loc + filename, tile_id, hue]
            if not WxCache._Cache.has_key(key) or not WxCache._Cache[key].Ok:
                x = (tile_id - 384) % 8 * 32
                y = (tile_id - 384) / 8 * 32
                rect = wx.Rect(x, y, 32, 32)
                tileset = WxCache.Tileset(filename, loc)
                WxCache._Cache[key] = tileset.GetSubImage(rect)
                WxCache._Cache[key].RotateHue(hue / 360.0)
            return WxCache._Cache[key]
        except:
            wx.MessageBox("Warning: loading of file %s failed" % filename)
            return wx.EmptyImage(1, 1)

    @staticmethod
    def Clear():
        WxCache._Cache = {}
        gc.collect()

#pygame version
#===============================================================================
#class PyGameCache(object):
#    
#    _Cache = {}
#    _image_ext = ["", ".png", ".gif", ".jpg", ".bmp"]
#    _formatsurf = pygame.Surface((1, 1), pygame.SRCALPHA, 32)
#
#    Autotiles = [
#               [[27, 28, 33, 34], [5, 28, 33, 34], [27, 6, 33, 34],
#                [5, 6, 33, 34], [27, 28, 33, 12], [5, 28, 33, 12],
#                [27, 6, 33, 12], [5, 6, 33, 12] ],
#               [[27, 28, 11, 34], [5, 28, 11, 34], [27, 6, 11, 34],
#                [5, 6, 11, 34], [27, 28, 11, 12], [5, 28, 11, 12],
#                [27, 6, 11, 12], [5, 6, 11, 12] ],
#               [[25, 26, 31, 32], [25, 6, 31, 32], [25, 26, 31, 12],
#                [25, 6, 31, 12], [15, 16, 21, 22], [15, 16, 21, 12],
#                [15, 16, 11, 22], [15, 16, 11, 12] ],
#               [[29, 30, 35, 36], [29, 30, 11, 36], [5, 30, 35, 36],
#                [5, 30, 11, 36], [39, 40, 45, 46], [5, 40, 45, 46],
#                [39, 6, 45, 46], [5, 6, 45, 46] ],
#               [[25, 30, 31, 36], [15, 16, 45, 46], [13, 14, 19, 20],
#                [13, 14, 19, 12], [17, 18, 23, 24], [17, 18, 11, 24],
#                [41, 42, 47, 48], [5, 42, 47, 48] ],
#               [[37, 38, 43, 44], [37, 6, 43, 44], [13, 18, 19, 24],
#                [13, 14, 43, 44], [37, 42, 43, 48], [17, 18, 47, 48],
#                [13, 18, 43, 48], [1, 2, 7, 8] ]
#               ]
#
#    @staticmethod
#    def Load_bitmap(folder_name, filename, hue=0, loc=""):
#        key = (folder_name, filename, loc, hue)
#        if not PyGameCache._Cache.has_key(key) or not PyGameCache._Cache[key]:
#            for ext in PyGameCache._image_ext:
#                path = os.path.abspath(os.path.normpath(loc + "/" + folder_name +
#                                       filename + ext))
#                if os.path.exists(path) and os.path.isfile(path):
#                    break
#            if not os.path.exists(path) and not os.path.isfile(path):
#                return None
#            try:
#                if filename != "":
#                    image = pygame.image.load(path).convert_alpha()
#                    if hue != 0:
#                        ChangeHue(image, hue)
#                    PyGameCache._Cache[key] = image
#                else:
#                    return None
#                return PyGameCache._Cache[key]
#            except AttributeError:
#                return None
#        else:
#            return PyGameCache._Cache[key]
#
#    @staticmethod
#    def Animation(filename, hue, loc=""):
#        return PyGameCache.Load_bitmap("Graphics/Animations/", filename, hue, loc)
#
#    @staticmethod
#    def Autotile(filename, loc=""):
#        return PyGameCache.Load_bitmap("Graphics/Autotiles/", filename, 0, loc)
#
#    @staticmethod
#    def AutotilePattern(filename, pattern, loc=""):
#        key = (loc + filename, pattern, 0)
#        if not PyGameCache._Cache.has_key(key) or not PyGameCache._Cache[key]:
#            autotile = PyGameCache.Autotile(filename, loc)
#            if autotile:
#                # Collects Auto-Tile Tile Layout
#                tiles = PyGameCache.Autotiles[int(pattern) / 8][int(pattern) % 8]
#                PyGameCache._Cache[key] = pygame.Surface((32, 32),
#                                                        pygame.SRCALPHA, 32)
#                for i in xrange(4):
#                    tile_position = tiles[i] - 1
#                    rect = (tile_position % 6 * 16, tile_position / 6 * 16, 16, 16)
#                    PyGameCache._Cache[key].blit(autotile, (i % 2 * 16, i / 2 * 16), rect)
#            else:
#                return None
#        return PyGameCache._Cache[key]
#
#    @staticmethod
#    def Battleback(filename, loc=""):
#        return PyGameCache.Load_bitmap("Graphics/Battlebacks/", filename, 0, loc)
#    
#    @staticmethod
#    def Battler(filename, hue, loc=""):
#        return PyGameCache.Load_bitmap("Graphics/Battlers/", filename, hue, loc)
#    
#    @staticmethod
#    def Character(filename, hue, loc=""):
#        return PyGameCache.Load_bitmap("Graphics/Characters/", filename, hue, loc)
#    
#    @staticmethod
#    def Fog(filename, hue, loc=""):
#        return PyGameCache.Load_bitmap("Graphics/Fogs/", filename, hue, loc)
#    
#    @staticmethod
#    def Gameover(filename, loc=""):
#        return PyGameCache.Load_bitmap("Graphics/Gameovers/", filename, 0, loc)
#    
#    @staticmethod
#    def Icon(filename, loc=""):
#        return PyGameCache.Load_bitmap("Graphics/Icons/", filename, 0, loc)
#    
#    @staticmethod
#    def Panorama(filename, hue, loc=""):
#        return PyGameCache.Load_bitmap("Graphics/Panoramas/", filename, hue, loc)
#    
#    @staticmethod
#    def Picture(filename, loc=""):
#        return PyGameCache.Load_bitmap("Graphics/Pictures/", filename, 0, loc)
#    
#    @staticmethod
#    def Tileset(filename, loc=""):
#        return PyGameCache.Load_bitmap("Graphics/Tilesets/", filename, 0, loc)
#    
#    @staticmethod
#    def Title(filename, loc=""):
#        return PyGameCache.Load_bitmap("Graphics/Titles/", filename, 0, loc)
#    
#    @staticmethod
#    def Windowskin(filename, loc=""):
#        return PyGameCache.Load_bitmap("Graphics/Windowskins/", filename, 0, loc)
#    
#    @staticmethod
#    def Tile(filename, tile_id, hue, loc=""):
#        key = (loc + filename, int(tile_id), hue)
#        if not PyGameCache._Cache.has_key(key) or not PyGameCache._Cache[key]:
#            PyGameCache._Cache[key] = pygame.Surface((32, 32),
#                                                     pygame.SRCALPHA, 32)
#            x = (int(tile_id) - 384) % 8 * 32
#            y = (int(tile_id) - 384) / 8 * 32
#            rect = (x, y, 32, 32)
#            tileset = PyGameCache.Tileset(filename, loc)
#            if tileset:
#                PyGameCache._Cache[key].blit(tileset, (0, 0), rect)
#                if hue != 0:
#                    ChangeHue(PyGameCache._Cache[key], hue)
#            else:
#                return None
#        return PyGameCache._Cache[key]
#    
#    @staticmethod
#    def Clear():
#        PyGameCache._Cache = {}
#        gc.collect()
##===============================================================================
