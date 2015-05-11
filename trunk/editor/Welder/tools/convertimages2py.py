import os
import sys
from wx.tools.img2py import img2py as img2py

try:
    dirName = os.path.dirname(os.path.abspath(__file__))
except:
    dirName = os.path.dirname(os.path.abspath(sys.argv[0]))


class bcolors:

    def __init__(self):
        self.enable()

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

    def enable(self):
        self.HEADER = '\033[35m'
        self.OKBLUE = '\033[34m'
        self.OKGREEN = '\033[32m'
        self.WARNING = '\033[33m'
        self.FAIL = '\033[31m'
        self.ENDC = '\033[0m'


COLORS = bcolors()
COLORS.disable()
COLORS_ENABLED = False


def enable_colors(colors=False):
    global COLORS_ENABLED
    global COLORS
    if colors:
        COLORS.enable()
        COLORS_ENABLED = True
    else:
        COLORS.disable()
        COLORS_ENABLED = False


def main(folder):

    try:
        ouputFile = os.path.join(folder, "GenImages.py")

        iconFolder = os.path.join(folder, "Icons")
        entries = os.listdir(iconFolder)
        imgFileExts = ["png", "gif", "jpg", "bmp"]
        i = 0
        print(COLORS.WARNING, "Converting", len(
            entries), "Images", COLORS.ENDC)
        for entry in entries:
            filepath = os.path.join(iconFolder, entry)
            if os.path.exists(filepath) and os.path.isfile(filepath):
                split_name = os.path.basename(entry).split(".")
                img_name = "".join(split_name[0:-1])
                if split_name[-1] in imgFileExts:
                    if i > 0:
                        img2py(filepath, ouputFile, append=True,
                               imgName=img_name, icon=True, catalog=True,
                               functionCompatible=False)
                    else:
                        img2py(filepath, ouputFile, append=False,
                               imgName=img_name, icon=True, catalog=True,
                               functionCompatible=False)
                    i += 1

    except Exception as err:
        print(COLORS.FAIL, err, COLORS.ENDC)


if __name__ == '__main__':

    try:
        import colorama
        COLORS_ENABLED = True
        colorama.init()
    except ImportError:
        pass

    main()
