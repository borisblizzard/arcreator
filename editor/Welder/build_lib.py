import sys, os
import shutil
import site
import platform
import sysconfig
import zipfile

compiled_dir = None

version = sys.version_info

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

if sys.platform == 'win32':
    version_str = str(version.major) + str(version.minor)
    lib_dir = "C:\\Python" + version_str + "\\Lib"
    compiled_dir = "C:\\Python" + version_str + "\\DLLs"
elif sys.platform == 'linux':
    version_str = str(version.major) + "." + str(version.minor)
    lib_dir = "/usr/lib/python" + version_str + "/"
    compiled_dir = lib_dir + "lib-dynload/"
else:
    lib_dir = ""

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
    'Cython',
    'wx',
    'PIL',
    'numpy',
    'pyximport',
    'setuptools',
    'sure',
    'cython.py',
    'rabbyt'

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
    shutil.copyfile(path, to)
    shutil.copystat(path, to)



def add_dep(path, files, prefix=""):
    fil = os.path.basename(path)
    root, ext = os.path.splitext(fil)
    if (ext in dep_exts) or (ext in source_exts) or (not ext in exclud_ext):
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


def scan_needed_location(folder, files):
    for fil in os.listdir(folder):
        path = os.path.join(folder, fil)
        if not fil in site_needed:
            continue
        prefix = ""
        if os.path.isdir(path):
            prefix = fil
        scan_dep(path, files, prefix)


def copy_needed_site():
    dest_folder = os.path.abspath(os.path.join(".", "lib"))
    prefix_mapping = {}
    locations = site.getsitepackages()
    locations.append(site.getusersitepackages())

    for path in locations:
        if os.path.exists(path):
            files = {}
            scan_needed_location(path, files)
            prefix_mapping.update(files)

    for fil, path in prefix_mapping.items():
        to = os.path.join(dest_folder, fil)
        print("copying %s ==> %s" % (path, to))
        copy_file(path, to)

def zip_std_lib():
    f = zipfile.PyZipFile("python.zip", mode="w", compression=zipfile.ZIP_DEFLATED, optimize=1)
    for fil in os.listdir(lib_dir):
        if fil not in std_exclude_files:
            root, ext = os.path.splitext(fil)
            path = os.path.join(lib_dir, fil)
            if ext in source_exts:
                print(path)
                f.writepy(path)

    f.close()

    dest_folder = os.path.abspath(os.path.join(".", "lib"))
    print("scanning %s" % compiled_dir)
    for fil in os.listdir(compiled_dir):
        path = os.path.join(compiled_dir, fil)
        print("scanning %s" % path)
        if os.path.isfile(path):
            root, ext = os.path.splitext(fil)
            if ext in dep_exts:
                to = os.path.join(dest_folder, fil)
                path = os.path.join(compiled_dir, fil)
                print("copying %s ==> %s" % (path, to))
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
        linkname = RemoveVersionNumbers(libname)
        libdir = sysconfig.get_config_var('LIBDIR')
        files.append(os.path.join(libdir, libname))
        files.append(os.path.join(libdir, linkname))
    else:
        #osx
        pass
        
    dest_folder = os.path.abspath(".")
    for path in files:
        if os.path.exists(path):
            fil = os.path.basename(path)
            root, ext = os.path.splitext(fil)
            to = os.path.join(dest_folder, fil)
            print("copying %s ==> %s" % (path, to))
            copy_file(path, to)

print("========================================")
print("Ziping Python Standard Library")
print("========================================")
zip_std_lib()

print("")
print("========================================")
print("Copying Python site-packages")
print("========================================")
copy_needed_site()

print("")
print("========================================")
print("Copying Python shared libary")
print("========================================")
copy_pyhton_lib()