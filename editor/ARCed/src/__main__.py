import os
import sys

if hasattr(sys, 'frozen'): 
    dirName = sys.executable
else:
    import wxversion
    wxversion.select("2.9")
    try:
        dirName = os.path.dirname(os.path.abspath(__file__))
    except:
        dirName = os.path.dirname(os.path.abspath(sys.argv[0]))
sys.path.append(dirName)

import time
import types
import traceback
import inspect
import platform

import ConfigParser
import re

import wx
from wx.lib.embeddedimage import PyEmbeddedImage
import wx.lib.agw.advancedsplash as AS
import wx.lib.agw.pycollapsiblepane as PCP

import Boot
from Boot import *

if __name__ == '__main__':

    print "Useing WxPython verison: %s" % wx.version()
    Run(dirName)