import os
import shutil
import time
import traceback
from pathlib import Path

from . import log
from . import fileutil


def ensure_path(path):
    if path != "" and not os.path.exists(path) or not os.path.isdir(path):
        os.makedirs(path)


class Distributer:

    excludes = ["lib", "build", "__pycache__",
                "src", "Makefile", "temp"]
    exclude_suffixes = [".c", ".cpp", ".h"]

    def __init__(self, path):
        self.path = Path(path).resolve()
        self.files = []
        self.dirs = []

    def add_file(self, fil, sub=None):
        self.files.append((fil, sub))

    def add_dir(self, d, sub=None):
        self.dirs.append((d, sub))

    def make_dist(self, dest):
        log.log("Removing old dist folder", log.BLUE)
        if os.path.exists(dest):
            shutil.rmtree(dest, True)
            time.sleep(0.1)
        ensure_path(dest)
        dest = Path(dest).resolve()
        log.log("Scanning...", log.WARN)
        self.scanfolder(self.path, "Editor")
        self.scanfolder(self.path, "Launcher")
        lib = self.path / "Launcher" / "lib"
        if lib.exists():
            self.add_dir(lib, "Launcher")
        log.log("Copying files...", log.WARN)
        self.copyfiles(dest)
        self.copydirs(dest)
        log.log("Dist built at: " + str(dest), log.GREEN)

    def scanfolder(self, path, sub=None, depth=0):
        if depth < 1 and sub is not None:
            path = path / sub
        log.log("Scanning " + str(path), log.BLUE)
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
            log.log(
                "Copying: " +
                str(f.relative_to(Path.cwd())) +
                " ->",
                log.WARN
            )
            log.log("\t" + str(dpath.relative_to(Path.cwd())), log.GREEN)
            shutil.copy2(str(f), str(dpath))

    def copydirs(self, dest):
        for d_info in self.dirs:
            d, sub = d_info
            dpath = Path(self.get_dest(dest, d, sub))
            ensure_path(str(dpath.parent))
            log.log(
                "Copying: " +
                str(d.relative_to(Path.cwd())) +
                " ->",
                log.WARN
            )
            log.log("\t" + str(dpath.relative_to(Path.cwd())), log.GREEN)
            fileutil.copy_overwrite(str(d), str(dpath))

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


if __name__ == '__main__':

    try:
        import colorama
        COLORS_ENABLED = True
        colorama.init()
    except ImportError:
        pass

    make_dist()
