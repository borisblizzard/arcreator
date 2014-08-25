#!/usr/bin/env python
import os
import sys
import time
import types
import traceback
import inspect
import platform

import configparser
import re

import wx

if __name__ == '__main__':
    if hasattr(sys, 'frozen'): 
        dirName = sys.executable
    else:
        try:
            dirName = os.path.dirname(os.path.abspath(__file__))
        except:
            dirName = os.path.dirname(os.path.abspath(sys.argv[0]))
    sys.path.append(dirName)

    import Welder

    import Boot
    from Boot import *

    Run(dirName)
