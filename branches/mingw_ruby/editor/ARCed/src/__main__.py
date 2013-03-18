#!/usr/bin/env python
import os
import sys
import time
import types
import traceback
import inspect
import platform

import ConfigParser
import re

import ConfigParser

import wx
from wx.lib.embeddedimage import PyEmbeddedImage
import wx.lib.agw.advancedsplash as AS
import wx.lib.agw.pycollapsiblepane as PCP

if hasattr(sys, 'frozen'): 
    dirName = sys.executable
else:
    try:
        dirName = os.path.dirname(os.path.abspath(__file__))
    except:
        dirName = os.path.dirname(os.path.abspath(sys.argv[0]))
sys.path.append(dirName)

import Boot
from Boot import *

if __name__ == '__main__':

    Run(dirName)
