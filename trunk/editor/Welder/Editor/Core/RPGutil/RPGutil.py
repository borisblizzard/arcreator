"""
Created on Sep 9, 2010

contains classes and functions that are used through out the project

Classes in this module
-----------------------
Table - three dimensional table
Color - contains RGB color data
Tone - contains RGBGr tone data
"""
import numpy
from struct import pack, unpack


class Table(object):
    """a three dimensional table object"""
    _arc_class_path = "Table"
    
    def __init__(self, *args):
        if len(args) != 1 and len(args) != 2 and len(args) != 3:
            raise TypeError("wrong number of arguments (%d for 1, 2 or 3)" % len(args))
        self.dim = len(args)
        self.xsize = args[0]
        if len(args) >= 2:
            self.ysize = args[1]
        else:
            self.ysize = 1
        if len(args) == 3:
            self.zsize = args[2] 
        else:
            self.zsize = 1
        if self.dim == 3:
            shape = (self.xsize, self.ysize, self.zsize)
        elif self.dim == 2:
            shape = (self.xsize, self.ysize)
        else:
            shape = (self.xsize,)
        self._data = numpy.zeros(shape, dtype=numpy.int16)
        self._data = numpy.reshape(self._data, shape, order='F')

    def __getitem__(self, key):
        if isinstance(key, int):
            if self.dim > 1:
                raise TypeError("wrong number of arguments (%d for %d)" % (1, self.dim))
        elif len(key) != self.dim:
            raise TypeError("wrong number of arguments (%d for %d)" % (len(key), self.dim))
        return self._data[key]

    def __setitem__(self, key, value):
        if isinstance(key, int):
            if self.dim > 1:
                raise TypeError("wrong number of arguments (%d for %d)" % (1, self.dim))
        elif len(key) != self.dim:
            raise TypeError("wrong number of arguments (%d for %d)" % (len(key), self.dim))
        try:
            self._data[key] = value
        except:
            print('__SETITEM__ THREW EXCEPTION')

    def resize(self, *args):
        # should work to increase and decrease the table size
        if len(args) != self.dim:
            raise TypeError("wrong number of arguments (%d for %d)" % (len(args), self.dim))
        self.xsize = args[0]
        if len(args) >= 2:
            self.ysize = args[1]
        else:
            self.ysize = 1
        if len(args) == 3:
            self.zsize = args[2] 
        else:
            self.zsize = 1
        newdata = numpy.zeros(self.getShape(), dtype=numpy.int16)
        shape = self._data.shape
        mask = [0, 0, 0]
        if self.dim == 1:
            if self.xsize >= shape[0]:
                mask[0] = shape[0]
            else:
                mask[0] = self.xsize
            newdata[:mask[0]] = self._data[:mask[0]]
        elif self.dim == 2:
            if self.xsize >= shape[0]:
                mask[0] = shape[0]
            else:
                mask[0] = self.xsize
            if self.ysize >= shape[1]:
                mask[1] = shape[1]
            else:
                mask[1] = self.ysize
            newdata[:mask[0], :mask[1]] = self._data[:mask[0], :mask[1]]
        elif self.dim == 3:
            if self.xsize >= shape[0]:
                mask[0] = shape[0]
            else:
                mask[0] = self.xsize
            if self.ysize >= shape[1]:
                mask[1] = shape[1]
            else:
                mask[1] = self.ysize
            if self.zsize >= shape[2]:
                mask[2] = shape[2]
            else:
                mask[2] = self.zsize  
            newdata[:mask[0], :mask[1], :mask[2]] = self._data[:mask[0], :mask[1], :mask[2]]
        self._data = newdata
        
    def _arc_dump(self, d=0):
        s = pack("<IIII", self.dim, self.xsize, self.ysize, self.zsize)
        data = self._data.flatten('F').tolist() 
        s += pack("<" + ("h" * (self.xsize * self.ysize * self.zsize)), *data)
        return s

    @staticmethod
    def _arc_load(s):
        dim, nx, ny, nz = unpack("<IIII", s[0:16])
        size = nx * ny * nz
        data = numpy.array(unpack("<" + ("h" * size), s[16:16 + size * 2]), dtype=numpy.int16)
        if dim == 3:
            t = Table(nx, ny, nz)
            shape = (nx, ny, nz)
        elif dim == 2:
            t = Table(nx, ny)
            shape = (nx, ny)
        elif dim == 1:
            t = Table(nx)
            shape = (nx,)
        data = numpy.reshape(data, shape,  order="F")
        t._data = data
        return t

    def getShape(self):
        if self.dim == 3:
            shape = (self.xsize, self.ysize, self.zsize)
        elif self.dim == 2:
            shape = (self.xsize, self.ysize)
        else:
            shape = (self.xsize,)
        return shape


class Color(object):
    """a bare bones color object"""
    _arc_class_path = "Color"

    def __init__(self, red, green, blue, alpha=255):
        if red > 255:
            red = 255
        if red < 0:
            red = 0
        if green > 255:
            green = 255
        if green < 0:
            green = 0
        if blue > 255:
            blue = 255
        if blue < 0:
            blue = 0
        if alpha > 255:
            alpha = 255
        if alpha < 0:
            alpha = 0
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def set(self, red, green, blue, alpha=255):
        if red > 255:
            red = 255
        if red < 0:
            red = 0
        if green > 255:
            green = 255
        if green < 0:
            green = 0
        if blue > 255:
            blue = 255
        if blue < 0:
            blue = 0
        if alpha > 255:
            alpha = 255
        if alpha < 0:
            alpha = 0
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def _arc_dump(self, d=0):
        return pack("<ffff", self.red, self.green, self.blue, self.alpha)

    @staticmethod
    def _arc_load(s):
        return Color(*unpack("<ffff", s))


class Tone(object):
    """a bare bones tone class"""
    _arc_class_path = "Tone"

    def __init__(self, red, green, blue, gray=0):
        if red > 255:
            red = 255
        if red < -255:
            red = -255
        if green > 255:
            green = 255
        if green < -255:
            green = -255
        if blue > 255:
            blue = 255
        if blue < -255:
            blue = -255
        if gray > 255:
            gray = 255
        if gray < -255:
            gray = -255
        self.red = red
        self.green = green
        self.blue = blue
        self.gray = gray

    def set(self, red, green, blue, gray=0):
        if red > 255:
            red = 255
        if red < -255:
            red = -255
        if green > 255:
            green = 255
        if green < -255:
            green = -255
        if blue > 255:
            blue = 255
        if blue < -255:
            blue = -255
        if gray > 255:
            gray = 255
        if gray < -255:
            gray = -255
        self.red = red
        self.green = green
        self.blue = blue
        self.gray = gray

    def _arc_dump(self, d = 0):
        return pack("<ffff", self.red, self.green, self.blue, self.gray)

    @staticmethod
    def _arc_load(s):
        return Tone(*unpack("<ffff", s))


