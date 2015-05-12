import os
import sys
import traceback

from . import log

from wx.tools.img2py import img2py as img2py

try:
    dirName = os.path.dirname(os.path.abspath(__file__))
except:
    dirName = os.path.dirname(os.path.abspath(sys.argv[0]))


def convert(folder):

    try:
        ouputFile = os.path.abspath(os.path.join(folder, "GenImages.py"))

        iconFolder = os.path.abspath(os.path.join(folder, "Icons"))
        entries = os.listdir(iconFolder)
        imgFileExts = ["png", "gif", "jpg", "bmp"]
        i = 0
        log.log(
            "Converting " + str(len(entries)) + " Images",
            log.WARN
        )
        for entry in entries:
            filepath = os.path.abspath(os.path.join(iconFolder, entry))
            if os.path.exists(filepath) and os.path.isfile(filepath):
                split_name = os.path.basename(entry).split(".")
                img_name = "".join(split_name[0:-1])
                if split_name[-1] in imgFileExts:
                    log.log("Converting " + filepath, log.GREEN)
                    if i > 0:
                        img2py(filepath, ouputFile, append=True,
                               imgName=img_name, icon=True, catalog=True,
                               functionCompatible=False)
                    else:
                        img2py(filepath, ouputFile, append=False,
                               imgName=img_name, icon=True, catalog=True,
                               functionCompatible=False)
                    i += 1
        return False

    except Exception:
        return traceback.format_exc()


if __name__ == '__main__':

    try:
        import colorama
        COLORS_ENABLED = True
        colorama.init()
    except ImportError:
        pass

    convert()
