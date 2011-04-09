import os
import gc

import pyglet

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
                self._Cache[key]= tileset.get_region(x, tileset.height - y - 32, 32, 32)
            else:
                return None
        return self._Cache[key]

    def Clear(self):
        self._Cache = {}
        gc.collect()