import os
import shutil
import time
import traceback
from pathlib import Path


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


def ensure_path(path):
    if path != "" and not os.path.exists(path) or not os.path.isdir(path):
        os.makedirs(path)


class Distributer:

    excludes = ["lib", "build", "__pycache__",
                "src", "Makefile", "temp"]
    exclude_suffixes = [".c", ".cpp"]

    def __init__(self, path):
        self.path = Path(path).resolve()
        self.files = []
        self.dirs = []

    def add_file(self, fil, sub=None):
        self.files.append((fil, sub))

    def add_dir(self, d, sub=None):
        self.dirs.append((d, sub))

    def make_dist(self, dest):
        print(COLORS.OKBLUE + "Removing old dist folder")
        if os.path.exists(dest):
            shutil.rmtree(dest, True)
            time.sleep(0.1)
        ensure_path(dest)
        dest = Path(dest).resolve()
        print(COLORS.WARNING + "Scanning..." + COLORS.ENDC)
        self.scanfolder(self.path, "Editor")
        self.scanfolder(self.path, "Launcher")
        lib = self.path / "Launcher" / "lib"
        if lib.exists():
            self.add_dir(lib, "Launcher")
        print(COLORS.WARNING + "Copying files..." + COLORS.ENDC)
        self.copyfiles(dest)
        self.copydirs(dest)
        print(COLORS.OKGREEN + "Dist built at:", str(dest) + COLORS.ENDC)

    def scanfolder(self, path, sub=None, depth=0):
        if depth < 1 and sub is not None:
            path = path / sub
        print(COLORS.OKBLUE + "Scanning " + str(path) + COLORS.ENDC)
        if not path.is_dir():
            raise RuntimeError("Path '%s' is not a directory" % str(self.path))
        files = [
            f
            for f
            in path.iterdir()
            if f.name not in self.excludes
            and f.suffix not in self.exclude_suffixes
        ]
        for f in files:
            if f.is_dir():
                self.scanfolder(f, sub, depth + 1)
                continue
            if f.suffix == ".py":
                if (f.with_suffix(".so") in files
                        or f.with_suffix(".pyd") in files):
                    continue
            self.add_file(f, sub)

    def copyfiles(self, dest):
        for f_info in self.files:
            f, sub = f_info
            dpath = Path(self.get_dest(dest, f, sub))
            ensure_path(str(dpath.parent))
            print(COLORS.WARNING +
                  "Copying:",
                  str(f.relative_to(Path.cwd())),
                  COLORS.ENDC,
                  "->",
                  COLORS.OKGREEN +
                  str(dpath.relative_to(Path.cwd()))
                  + COLORS.ENDC)
            shutil.copy2(str(f), str(dpath))

    def copydirs(self, dest):
        for d_info in self.dirs:
            d, sub = d_info
            dpath = Path(self.get_dest(dest, d, sub))
            ensure_path(str(dpath.parent))
            print(COLORS.WARNING +
                  "Copying:",
                  str(d.relative_to(Path.cwd()))
                  + COLORS.ENDC,
                  "->",
                  COLORS.OKGREEN +
                  str(dpath.relative_to(Path.cwd()))
                  + COLORS.ENDC)
            recursive_overwrite(str(d), str(dpath))

    def get_dest(self, dest, path, sub=None):
        if sub is not None:
            path_part = str(self.path / sub)
        else:
            path_part = str(self.path)
        return dest / str(path).replace(path_part + os.path.sep, "")


def make_dist(folder, dest):

    try:
        Distributer(folder).make_dist(dest)
    except Exception:
        return traceback.format_exc()

    # there was no error
    return False


def enable_colors(colors=False):
    global COLORS_ENABLED
    global COLORS
    if colors:
        COLORS.enable()
        COLORS_ENABLED = True
    else:
        COLORS.disable()
        COLORS_ENABLED = False

if __name__ == '__main__':

    try:
        import colorama
        COLORS_ENABLED = True
        colorama.init()
    except ImportError:
        pass

    make_dist()
