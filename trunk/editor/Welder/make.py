#!/usr/bin/python
import sys
import os
import sysconfig
import shutil
import distutils.log

from tools import cythonize
from tools import convertimages2py
from tools import buildlauncher
from tools import buildlib
from tools import makedist


def recursive_overwrite(src, dest, ignore=None):
    if os.path.isdir(src):
        if not os.path.isdir(dest):
            os.makedirs(dest)
        shutil.copystat(src, dest)
        files = os.listdir(src)
        if ignore is not None:
            ignored = ignore(src, files)
        else:
            ignored = set()
        for f in files:
            if f not in ignored:
                recursive_overwrite(os.path.join(src, f),
                                    os.path.join(dest, f),
                                    ignore)
    else:
        destdir = os.path.dirname(dest)
        if not os.path.isdir(destdir):
            os.makedirs(destdir)
        shutil.copy2(src, dest)


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


if __name__ == "__main__":

    # set log verbosity to print everything
    distutils.log.set_verbosity(3)

    # get some color in here
    COLORS_ENABLED = False
    try:
        import colorama
        COLORS_ENABLED = True
        colorama.init()
    except ImportError:
        pass

    COLORS = bcolors()
    if not COLORS_ENABLED:
        COLORS.disable()

    # one stop shop for building welder runnign this file will ensure
    # everything is in it's place before building

    try:
        dirName = os.path.dirname(os.path.abspath(__file__))
    except:
        dirName = os.path.dirname(os.path.abspath(sys.argv[0]))

    # ==========================================================================
    # Icon Conversion
    # ==========================================================================
    print(
        COLORS.HEADER +
        "===================================================================\n"
        "  Converting Icons\n"
        "==================================================================="
        + COLORS.ENDC
    )
    filepath = os.path.join(dirName, "EditorIcons")

    convertimages2py.enable_colors(COLORS_ENABLED)

    error = convertimages2py.main(filepath)

    if error:
        print(
            COLORS.FAIL + "There was an error converting images" + COLORS.ENDC)
        exit()

    # move the images.py into place
    filepath = os.path.join(dirName, "EditorIcons", "GenImages.py")
    topath = os.path.join(
        dirName, "Editor", "Core", "Editor", "Icons", "GenImages.py")
    shutil.copy2(filepath, topath)

    # =========================================================================
    # Clone Source Tree
    # =========================================================================
    destfolder = sysconfig.get_platform() + "-" + \
        sysconfig.get_python_version()
    destpath = os.path.join(dirName, "build", destfolder, "Editor")

    srcpath = os.path.join(dirName, "Editor")

    print(COLORS.WARNING + "Copying source tree to:", destpath + COLORS.ENDC)
    recursive_overwrite(srcpath, destpath,
                        ignore=shutil.ignore_patterns(
                            '*.pyc',
                            '*.pyo',
                            "__pycache__",
                            "build",
                            "src",
                            "*.c",
                            "*.pyd"
                        ))

    # =========================================================================
    # Cython Run
    # =========================================================================
    print(
        COLORS.HEADER +
        "===================================================================\n"
        "  Cythoning Modules\n"
        "==================================================================="
        + COLORS.ENDC
    )

    cythonize.enable_colors(COLORS_ENABLED)

    sys.argv.extend(["build_ext", "--inplace"])
    error = cythonize.build(destpath)

    if error:
        print(COLORS.FAIL + "There was an error Cythoning files" + COLORS.ENDC)
        exit()

    sys.argv = sys.argv[:-2]

    # =========================================================================
    # Build Launcher
    # =========================================================================
    print(
        COLORS.HEADER +
        "===================================================================\n"
        "  Building Launcher\n"
        "==================================================================="
        + COLORS.ENDC
    )

    buildlauncher.enable_colors(COLORS_ENABLED)

    destpath = os.path.join(dirName, "build", destfolder, "Launcher")
    srcpath = os.path.join(dirName, "Launcher")

    error = buildlauncher.build(srcpath, destpath)

    if error:
        print(COLORS.FAIL +
              "There was an error Building the launcher"
              + COLORS.ENDC + "\n",
              error)
        exit()

    # =========================================================================
    # Build Lib
    # =========================================================================
    print(
        COLORS.HEADER +
        "===================================================================\n"
        "  Building Python Library\n"
        "==================================================================="
        + COLORS.ENDC
    )

    buildlib.enable_colors(COLORS_ENABLED)

    destpath = os.path.join(dirName, "build", destfolder, "Launcher")

    error = buildlib.build(destpath)

    if error:
        print(COLORS.FAIL +
              "There was an error Building the Python library"
              + COLORS.ENDC + "\n",
              error)
        exit()

    # =========================================================================
    # make dist
    # =========================================================================
    print(
        COLORS.HEADER +
        "===================================================================\n"
        "  Making Welder Distrabution\n"
        "==================================================================="
        + COLORS.ENDC
    )

    makedist.enable_colors(COLORS_ENABLED)

    frompath = os.path.join(dirName, "build", destfolder)
    distpath = os.path.join(dirName, "dist", destfolder)

    error = makedist.make_dist(frompath, distpath)

    if error:
        print(COLORS.FAIL +
              "There was an error Building Welder Distrabution"
              + COLORS.ENDC + "\n",
              error)
        exit()

    print(
        COLORS.OKGREEN +
        "===================================================================\n"
        "  Build Compleate: check the dist directory for compleate build\n"
        "==================================================================="
        + COLORS.ENDC
    )
