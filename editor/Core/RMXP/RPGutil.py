"""
Created on Sep 9, 2010

contains classes and functions that are used through out the project

Classes in this module
-----------------------
Table - three dimensional table
Color - contains RGB color data
Tone - contains RGBGr tone data 

functions in this module
------------------------
opj - Convert paths to the platform-specific separator

"""
import os
import numpy
import pygame

from pygame import surfarray

def opj(path):
    """Convert paths to the platform-specific separator"""
    path.replace("\\", "/")
    st = apply(os.path.join, tuple(path.split('/')))
    # HACK: on Linux, a leading / gets lost...
    if path.startswith('/'):
        st = '/' + st
    return st

class Table(object):
    """a three dimensional table object"""
    __class_path__ = "Table"
    __instance_variables__ = ['xsize', 'ysize', 'zsize', 'data']
    def __init__(self, xsize=1, ysize=1, zsize=1):
        self.xsize = xsize
        self.ysize = ysize
        self.zsize = zsize
        self.data = [0] * (xsize * ysize * zsize)
        self._data = numpy.zeros((xsize, ysize, zsize))
        self._data = numpy.reshape(self._data, (self.xsize, self.ysize,
                                   self.zsize), order='F')

    def _prep_rmpy_dump(self):
        self.data = self._data.ravel(order='F').tolist()

    def _post_rmpy_load(self):
        self._data = numpy.array(self.data)
        self._data.resize(self.xsize * self.ysize * self.zsize)
        self._data = numpy.reshape(self._data, (self.xsize, self.ysize,
                                   self.zsize), order='F')


    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value

    def resize(self, xsize=1, ysize=1, zsize=1):
        # This only works for increasing the size of the data,
        # but is easy do adapt to other cases
        newdata = numpy.zeros((xsize, ysize, zsize))
        shape = self._data.shape
        newdata[:shape[0], :shape[1], :shape[2]] = self._data
        self._data = newdata

class Color(object):
    """a bare bones color object"""
    __class_path__ = "Color"
    __instance_variables__ = ['red', 'green', 'blue', 'alpha']
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

class Tone(object):
    """a bare bones tone class"""
    __class_path__ = "Tone"
    __instance_variables__ = ['red', 'green', 'blue', 'gray']
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

class PySurfaceFunctions(object):

    @staticmethod
    def change_hue(surface, hue):
        surface.lock()
        for x in range(surface.get_width()):
            for y in range(surface.get_height()):
                color = pygame.Color(*surface.get_at((x, y)))
                hsva = list(color.hsva)
                hsva[0] = (hsva[0] + float(hue)) % 360.0
                color.hsva = hsva
                surface.set_at((x, y), (color.r, color.g, color.b, color.a))
        surface.unlock()

    @staticmethod
    def adjust_alpha(surface, alpha):
        if alpha > 255:
            alpha = 255
        if alpha < 0:
            alpha = 0
        factor = float(alpha) / 255.0
        alphas = surfarray.pixels_alpha(surface)
        alphas = (alphas * factor)
        alphas = numpy.clip(alphas, 0, 255)
        alphas[:] = alphas.astype("uint8")
        del alphas



