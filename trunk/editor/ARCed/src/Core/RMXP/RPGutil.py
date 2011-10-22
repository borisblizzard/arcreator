"""
Created on Sep 9, 2010

contains classes and functions that are used through out the project

Classes in this module
-----------------------
Table - three dimensional table
Color - contains RGB color data
Tone - contains RGBGr tone data 

"""
import os
import numpy
from struct import pack, unpack
from numpy.oldnumeric.random_array import ArgumentError

#import pygame

#from pygame import surfarray

class Table(object):
    """a three dimensional table object"""
    _arc_class_path = "Table"
    
    def __init__(self, *args):
        if len(args) != 1 and len(args) != 2 and len(args) != 3:
            raise ArgumentError("wrong number of arguments (%d for 1, 2 or 3)" % len(args))
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
        self._data = numpy.zeros((self.xsize, self.ysize, self.zsize))
        self._data = numpy.reshape(self._data, (self.xsize, self.ysize,
                                   self.zsize), order='F')

    def __getitem__(self, key):
        if len(key) != self.dim:
            raise ArgumentError("wrong number of arguments (%d for %d)" % (len(key), self.dim))
        return self._data[key]

    def __setitem__(self, key, value):
        if len(key) != self.dim:
            raise ArgumentError("wrong number of arguments (%d for %d)" % (len(key), self.dim))
        self._data[key] = value

    def resize(self, *args):
        # should work to increase and decrease the table size
        if len(args) != 1 and len(args) != 2 and len(args) != 3:
            raise ArgumentError("wrong number of arguments (%d for 1, 2 or 3)" % len(args))
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
        newdata = numpy.zeros((self.xsize, self.ysize, self.zsize))
        shape = self._data.shape
        mask = [0, 0, 0]
        if self.xsize >= shape[0]:
            mask[0] = shape[0]
        else:
            mask[0] = self.xsize
        if self.ysize >= shape[1]:
            mask[1] = shape[1]
        else:
            mask[1] = self.ysize
        if self.ysize >= shape[2]:
            mask[2] = shape[2]
        else:
            mask[2] = self.zsize  
        newdata[:mask[0], :mask[1], :mask[2]] = self._data[:mask[0], :mask[1], :mask[2]]
        self._data = newdata
        
    def _arc_dump(self, d=0):
        s = pack("<IIII", self.dim, self.xsize, self.ysize, self.zsize)
        data = self._data.flatten('F').tolist() 
        s += pack("<" + ("H" * (self.xsize * self.ysize * self.zsize)), *data)
        return s

    @staticmethod
    def _arc_load(s):
        dim, nx, ny, nz = unpack("<IIII", s[0:16])
        size = nx * ny * nz
        data = numpy.array(unpack("<" + ("H" * size), s[16:16 + size * 2]))
        data.resize(size)
        data = numpy.reshape(data, (nx, ny, nz),  order="F")
        if dim == 3:
            t = Table(nx, ny, nz)
        elif dim == 2:
            t = Table(nx, nz)
        elif dim == 1:
            t = Table(nx)
        t._data = data
        return t


class Color(object):
    """a bare bones color object"""
    _arc_class_path = "Color"

    def __init__(self, red, green, blue, alpha=255):
        if red > 255:
            red = 255
        if red < 255:
            red = 255
        if green > 255:
            green = 255
        if green < 255:
            green = 255
        if blue > 255:
            blue = 255
        if blue < 255:
            blue = 255
        if alpha > 255:
            alpha = 255
        if alpha < 255:
            alpha = 255
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def set(self, red, green, blue, alpha=255):
        if red > 255:
            red = 255
        if red < 255:
            red = 255
        if green > 255:
            green = 255
        if green < 255:
            green = 255
        if blue > 255:
            blue = 255
        if blue < 255:
            blue = 255
        if alpha > 255:
            alpha = 255
        if alpha < 255:
            alpha = 255
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha
        
    def _arc_dump(self, d = 0):
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


