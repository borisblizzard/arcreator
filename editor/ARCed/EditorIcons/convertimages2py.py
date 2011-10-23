import os
import sys
from wx.tools.img2py import img2py as img2py

try:
    dirName = os.path.dirname(os.path.abspath(__file__))
except:
    dirName = os.path.dirname(os.path.abspath(sys.argv[0]))
    
ouputFile = os.path.join(dirName, "images.py")
    
entries = os.listdir(dirName)
imgFileExts = ["png", "gif", "jpg", "bmp"]
for entry in entries:
    if os.path.exists(entry) and os.path.isfile(entry):
        split_name = os.path.basename(entry).split(".")
        img_name = "".join(split_name[0:-1])
        if split_name[-1] in imgFileExts:
            img2py(entry, ouputFile, True, True, None, img_name, True, True)