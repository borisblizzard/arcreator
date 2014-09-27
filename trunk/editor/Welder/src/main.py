#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    if hasattr(sys, 'frozen'):
        dirName = sys.executable
    else:
        try:
            dirName = os.path.dirname(os.path.abspath(__file__))
        except:
            dirName = os.path.dirname(os.path.abspath(sys.argv[0]))
    sys.path.append(dirName)

    from Boot import Run

    Run(dirName, sys.argv)
