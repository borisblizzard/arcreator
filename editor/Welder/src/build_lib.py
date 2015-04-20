import sys
import os
import shutil
import platform
import sysconfig
import zipfile
from pathlib import Path

compiled_dir = None

version = sys.version_info

try:
    dirName = os.path.dirname(os.path.abspath(__file__))
except:
    dirName = os.path.dirname(os.path.abspath(sys.argv[0]))


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
    compiled_folder = "DLLs"
    compiled_dir = "C:\\Python" + version_str + "\\" + compiled_folder

elif sys.platform == 'linux':
    version_str = str(version.major) + "." + str(version.minor)
    lib_dir = "/usr/lib/python" + version_str + "/"
    compiled_folder = "lib-dynload"
    compiled_dir = lib_dir + compiled_folder + "/"
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

site_needed = [
    'pyitect',
    'wx',
    'PIL',
    'numpy',
    'setuptools',
    'pyglet',
    'rabbyt',
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
    print("Copying: ", path, " -> ", str(Path(to).relative_to(Path.cwd())))
    shutil.copyfile(path, to)
    shutil.copystat(path, to)


def add_dep(path, files, prefix=""):
    fil = os.path.basename(path)
    root, ext = os.path.splitext(fil)
    if (ext in dep_exts) or (ext in source_exts) or (ext not in exclud_ext):
        files[os.path.join(prefix, fil)] = path


def scan_dep(path, files, prefix=""):
    if os.path.isdir(path):
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


def copy_needed_site():
    dest_folder = os.path.abspath(os.path.join(dirName, "lib", "site-packages"))
    prefix_mapping = {}
    locations = sys.path

    for path in locations:
        if os.path.exists(path) and os.path.isdir(path):
            files = {}
            scan_needed_location(path, files)
            prefix_mapping.update(files)

    for fil, path in prefix_mapping.items():
        to = os.path.join(dest_folder, fil)
        copy_file(path, to)


def copy_std_lib():
    dest_folder = os.path.abspath(os.path.join(dirName, "lib"))
    files = {}
    scan_library(lib_dir, files)
    for fil, path in files.items():
        to = os.path.join(dest_folder, fil)
        copy_file(path, to)


def zip_std_lib():
    f = zipfile.ZipFile("python.zip", mode="w", compression=zipfile.ZIP_DEFLATED)
    files = {}
    scan_library(lib_dir, files)
    for fil, path in files.items():
        print(path)
        f.write(path, fil)

    f.close()


def copy_compiled():

    dest_folder = os.path.abspath(os.path.join(dirName, "lib", compiled_folder))
    print("scanning %s" % compiled_dir)
    for fil in os.listdir(compiled_dir):
        path = os.path.join(compiled_dir, fil)
        print("scanning %s" % path)
        if os.path.isfile(path):
            root, ext = os.path.splitext(fil)
            if ext in dep_exts:
                to = os.path.join(dest_folder, fil)
                path = os.path.join(compiled_dir, fil)
                copy_file(path, to)


def copy_pyhton_lib():
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
        libdir = sysconfig.get_config_var('LIBDIR') + (sysconfig.get_config_var("multiarchsubdir") or "")
        files.append(os.path.join(libdir, libname))
    else:
        # osx
        pass

    dest_folder = os.path.abspath(dirName)
    for path in files:
        if os.path.exists(path):
            fil = os.path.basename(path)
            root, ext = os.path.splitext(fil)
            to = os.path.join(dest_folder, fil)
            copy_file(path, to)

print("========================================")
print("Ziping Python Standard Library")
print("========================================")
zip_std_lib()

print("========================================")
print("Copying Compiled Python Extentions")
print("========================================")
copy_compiled()

print("")
print("========================================")
print("Copying Python Needed site-packages")
print("========================================")
copy_needed_site()

print("")
print("========================================")
print("Copying Python Shared libary")
print("========================================")
copy_pyhton_lib()
