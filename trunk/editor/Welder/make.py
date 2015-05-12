#!/usr/bin/python
import sys
import os
import sysconfig
import shutil
import distutils.log

from tools import log
from tools import cythonize
from tools import convertimages2py
from tools import buildlauncher
from tools import buildlib
from tools import makedist
from tools import fileutil


def fail():
    log.log(
        "===================================================================\n"
        "  Build FAILED: check build/build.log for full details\n"
        "===================================================================",
        log.FAIL
    )
    sys.exit()


if __name__ == "__main__":
    # one stop shop for building welder
    # running this file will ensure
    # everything is in it's place before building

    # get the local dir
    try:
        dirName = os.path.dirname(os.path.abspath(__file__))
    except:
        dirName = os.path.dirname(os.path.abspath(sys.argv[0]))

    # set up paths
    destfolder = (sysconfig.get_platform() + "-" +
                  sysconfig.get_python_version())
    destpath = os.path.join(dirName, "build", destfolder)
    distpath = os.path.join(dirName, "dist", destfolder)

    editorsrcpath = os.path.join(dirName, "Editor")
    launchersrcpath = os.path.join(dirName, "Launcher")

    editorbuildpath = os.path.join(destpath, "Editor")
    launcherbuildpath = os.path.join(dirName, "build", destfolder, "Launcher")

    logpath = os.path.join(destpath, "build.log")

    # init loging
    log.init_log_file(logpath)

    log.replace_distutils_Log_log()
    # set log verbosity to print everything
    distutils.log.set_verbosity(3)

    # ==========================================================================
    # Icon Conversion
    # ==========================================================================
    log.log(
        "===================================================================\n"
        "  Converting Icons\n"
        "===================================================================",
        log.HEAD
    )
    iconpath = os.path.join(dirName, "EditorIcons")

    error = convertimages2py.convert(iconpath)

    if error:
        log.log("There was an error converting images", log.FAIL)
        log.log(error)
        fail()

    # move the images.py into place
    filepath = os.path.join(dirName, "EditorIcons", "GenImages.py")
    topath = os.path.join(
        dirName, "Editor", "Core", "Editor", "Icons", "GenImages.py")
    shutil.copy2(filepath, topath)

    # =========================================================================
    # Clone Source Tree
    # =========================================================================

    log.log(
        "===================================================================\n"
        "  Cythoning Modules\n"
        "===================================================================",
        log.HEAD
    )

    log.log("Copying source tree to: " + editorbuildpath, log.WARN)
    fileutil.copy_overwrite(
        editorsrcpath,
        editorbuildpath,
        ignore=shutil.ignore_patterns(
            '*.pyc',
            '*.pyo',
            "__pycache__",
            "build",
            "src",
            "*.c",
            "*.pyd"
        )
    )

    # =========================================================================
    # Cython Run
    # =========================================================================

    error = cythonize.build(editorbuildpath)

    if error:
        log.log("There was an error Cythoning files", log.FAIL)
        log.log(error)
        fail()

    # =========================================================================
    # Build Launcher
    # =========================================================================
    log.log(
        "===================================================================\n"
        "  Building Launcher\n"
        "===================================================================",
        log.HEAD
    )

    error = buildlauncher.build(launchersrcpath, launcherbuildpath)

    if error:
        log.log("There was an error Building the launcher", log.FAIL)
        log.log(error)
        fail()

    # =========================================================================
    # Build Lib
    # =========================================================================
    log.log(
        "===================================================================\n"
        "  Building Python Library\n"
        "===================================================================",
        log.HEAD
    )

    error = buildlib.build(launcherbuildpath)

    if error:
        log.log("There was an error Building the Python library", log.FAIL)
        log.log(error)
        fail()

    # =========================================================================
    # make dist
    # =========================================================================
    log.log(
        "===================================================================\n"
        "  Making Welder Distrabution\n"
        "===================================================================",
        log.HEAD
    )

    error = makedist.make_dist(destpath, distpath)

    if error:
        log.log("There was an error Building Welder Distrabution", log.FAIL)
        log.log(error)
        fail()

    log.log(
        "===================================================================\n"
        "  Build SUCEEDED: check the dist directory for compleate build\n"
        "===================================================================",
        log.GREEN
    )
