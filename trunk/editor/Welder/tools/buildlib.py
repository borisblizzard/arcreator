import sys
import os
import shutil
import platform
import sysconfig
import zipfile
import traceback
from pathlib import Path

compiled_dir = None

version = sys.version_info

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


def RemoveVersionNumbers(libName):
    tweaked = False
    parts = libName.split(".")
    while parts:
        if not parts[-1].isdigit():
            break
        parts.pop(-1)
        tweaked = True
    if tweaked:
        libName = ".".join(parts)
    return libName

virenv_dir = os.path.join(dirName, ".venv", "Lib")

if sys.platform == 'win32':
    version_str = str(version.major) + str(version.minor)
    lib_dir = "C:\\Python" + version_str + "\\Lib"
    binary_folder = "DLLs"
    binary_dir = "C:\\Python" + version_str + "\\" + binary_folder

elif sys.platform == 'linux':
    version_str = str(version.major) + "." + str(version.minor)
    lib_dir = "/usr/lib/python" + version_str + "/"
    binary_folder = "lib-dynload"
    binary_dir = lib_dir + binary_folder + "/"
else:
    lib_dir = ""


# if os.path.exists(virenv_dir):
#     lib_dir = virenv_dir

std_exclude_files = [
    "test",
    "__pycache__",
    "idlelib",
    "tkinter",
    "turtledemo",
    "antigravity.py",
    "turtle.py",
    "site-packages"
]

binary_excludes = [
    "_tkinter",
    "tcl86t",
    "tk86t"
]

site_needed = [
    'pyitect',
    'wx',
    'PIL',
    'numpy',
    'setuptools',
    'pyglet',
    'rabbyt',
    'pkg_resources',
    'pkg_resources.py',
    'win32',
    'pywin32.pth'
]

dep_exts = [".dll", ".pyd", ".so"]
source_exts = ["", ".py"]
exclud_ext = [".pyc", ".pyo", ".egg-info", '.dist-info']


def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)


def copy_file(path, to):
    ensure_dir(to)
    print(
        COLORS.WARNING + "Copying:",
        path + COLORS.ENDC,
        " -> ",
        COLORS.OKGREEN +
        str(Path(to).relative_to(Path.cwd()))
        + COLORS.ENDC
    )
    shutil.copyfile(path, to)
    shutil.copystat(path, to)


def add_dep(path, files, prefix=""):
    fil = os.path.basename(path)
    root, ext = os.path.splitext(fil)
    if (ext in dep_exts) or (ext in source_exts) or (ext not in exclud_ext):
        files[os.path.join(prefix, fil)] = path


def scan_dep(path, files, prefix=""):
    if os.path.isdir(path):
        print(COLORS.OKBLUE + "Scanning", path + COLORS.ENDC)
        for fil in os.listdir(path):
            fil_path = os.path.join(path, fil)
            if os.path.isdir(fil_path):
                new_prefix = os.path.join(prefix, fil)
                scan_dep(fil_path, files, new_prefix)
            elif os.path.isfile(fil_path):
                add_dep(fil_path, files, prefix)
    elif os.path.isfile(path):
        add_dep(path, files, prefix)


def scan_library(folder, files):
    for fil in os.listdir(folder):
        path = os.path.join(folder, fil)
        if fil in std_exclude_files:
            continue
        prefix = ""
        if os.path.isdir(path):
            prefix = fil
        scan_dep(path, files, prefix)


def scan_needed_location(folder, files):
    for fil in os.listdir(folder):
        path = os.path.join(folder, fil)
        if fil not in site_needed:
            continue
        prefix = ""
        if os.path.isdir(path):
            prefix = fil
        scan_dep(path, files, prefix)


def copy_needed_site(dest):
    dest_folder = os.path.abspath(os.path.join(dest, "lib", "site-packages"))
    prefix_mapping = {}
    locations = sys.path

    for path in locations:
        if os.path.exists(path) and os.path.isdir(path):
            files = {}
            print(COLORS.OKBLUE + "Scanning", path + COLORS.ENDC)
            scan_needed_location(path, files)
            prefix_mapping.update(files)

    for fil, path in prefix_mapping.items():
        to = os.path.join(dest_folder, fil)
        copy_file(path, to)


def copy_std_lib(dest):
    dest_folder = os.path.abspath(os.path.join(dest, "lib"))
    files = {}
    scan_library(lib_dir, files)
    for fil, path in files.items():
        to = os.path.join(dest_folder, fil)
        copy_file(path, to)


def zip_std_lib(dest):
    dest_file = os.path.abspath(os.path.join(dest, "python.zip"))
    f = zipfile.ZipFile(dest_file, mode="w", compression=zipfile.ZIP_DEFLATED)
    files = {}
    scan_library(lib_dir, files)
    for fil, path in files.items():
        print(COLORS.OKGREEN + "/" + fil + COLORS.ENDC)
        f.write(path, fil)

    f.close()


def copy_binaries(dest):

    dest_folder = os.path.abspath(os.path.join(dest, "lib", binary_folder))
    print(COLORS.OKBLUE + ("scanning %s" % binary_dir) + COLORS.ENDC)
    for fil in os.listdir(binary_dir):
        path = os.path.join(binary_dir, fil)
        if os.path.isfile(path):
            root, ext = os.path.splitext(fil)
            if ext in dep_exts and root not in binary_excludes:
                to = os.path.join(dest_folder, fil)
                path = os.path.join(binary_dir, fil)
                copy_file(path, to)


def copy_python_lib(dest):
    files = []
    if sys.platform == 'win32':
        dllname = "python%s%s.dll" % sys.version_info[:2]
        # two location to try
        system32path = os.path.join("C:\\", "Windows", "System32")
        syswow64path = os.path.join("C:\\", "Windows", "SysWOW64")
        files.append(os.path.join(system32path, dllname))
        if "64" in platform.machine() and "64" in platform.architecture()[0]:
            files.append(os.path.join(syswow64path, dllname))
    elif sys.platform == 'linux':
        libname = sysconfig.get_config_var("INSTSONAME")
        libdir = sysconfig.get_config_var(
            'LIBDIR') + (sysconfig.get_config_var("multiarchsubdir") or "")
        files.append(os.path.join(libdir, libname))
    else:
        # osx
        pass

    dest_folder = os.path.abspath(dest)
    for path in files:
        if os.path.exists(path):
            fil = os.path.basename(path)
            root, ext = os.path.splitext(fil)
            to = os.path.join(dest_folder, fil)
            copy_file(path, to)


def build(dest):

    try:
        print(
            COLORS.HEADER +
            "========================================\n"
            "Ziping Python Standard Library\n"
            "========================================"
            + COLORS.ENDC)
        zip_std_lib(dest)

        print(
            COLORS.HEADER +
            "========================================\n"
            "Copying Python Binaries\n"
            "========================================"
            + COLORS.ENDC)
        copy_binaries(dest)

        print(
            COLORS.HEADER +
            "========================================\n"
            "Copying Python Needed site-packages\n"
            "========================================"
            + COLORS.ENDC)
        copy_needed_site(dest)

        print(
            COLORS.HEADER +
            "========================================\n"
            "Copying Python Shared libary\n"
            "========================================"
            + COLORS.ENDC)
        copy_python_lib(dest)
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

    build()
