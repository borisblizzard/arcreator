# -*- coding: iso-8859-1 -*-
from distutils.core import setup
import py2exe
import glob
import sys
import os
import zlib
import shutil

if hasattr(sys, 'frozen'): 
    dirName = sys.executable
else:
    try:
        dirName = os.path.dirname(os.path.abspath(__file__))
    except:
        dirName = os.path.dirname(os.path.abspath(sys.argv[0]))
sys.path.append(os.path.join(dirName, "compiled"))

# Remove the dist folder
shutil.rmtree("dist", ignore_errors=True)

#change into the build folder
os.chdir("compiled")

# Remove the build folder
shutil.rmtree("build", ignore_errors=True)



MANIFEST_TEMPLATE = """
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
  <assemblyIdentity
    version="%(version)s"
    processorArchitecture="x86"
    name="%(prog)s"
    type="win32"
  />
  <description>%(prog)s</description>
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
    <security>
      <requestedPrivileges>
        <requestedExecutionLevel
            level="asInvoker"
            uiAccess="false">
        </requestedExecutionLevel>
      </requestedPrivileges>
    </security>
  </trustInfo>
  <dependency>
    <dependentAssembly>
      <assemblyIdentity
            type="win32"
            name="Microsoft.VC90.CRT"
            version="9.0.21022.8"
            processorArchitecture="x86"
            publicKeyToken="1fc8b3b9a1e18e3b">
      </assemblyIdentity>
    </dependentAssembly>
  </dependency>
  <dependency>
    <dependentAssembly>
        <assemblyIdentity
            type="win32"
            name="Microsoft.Windows.Common-Controls"
            version="6.0.0.0"
            processorArchitecture="X86"
            publicKeyToken="6595b64144ccf1df"
            language="*"
        />
    </dependentAssembly>
  </dependency>
</assembly>
"""

class Target(object):
    """ A simple class that holds information on our executable file. """
    def __init__(self, **kw):
        """ Default class constructor. Update as you need. """
        self.__dict__.update(kw)


def scandirfordll(dir, files=[], paths=[]):
    for file in os.listdir(dir):
        path = os.path.join(dir, file)
        if os.path.isfile(path) and path.endswith(".dll"):
            paths.append(os.path.abspath(path))
            files.append(file)
        elif os.path.isdir(path):
            scandirfordll(path, files, paths)
    return files, paths

data_files = []

includes = []
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
            'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
            'Tkconstants', 'Tkinter']
packages = []
dll_excludes = ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll', 'tcl84.dll',
                'tk84.dll',
                'MSVCP90.dll', 'mswsock.dll', 'powrprof.dll',]
extra_dlls, extra_dll_paths = scandirfordll(".")
print extra_dlls
dll_excludes.extend(extra_dlls)

icon_resources = [(0, '..\icon.ico')]
bitmap_resources = []
other_resources = []
other_resources = [(24, 1, MANIFEST_TEMPLATE % dict(prog="ARCed", version="0.0.0.1"))]


ARCedTarget = Target(
    # what to build
    script = "__main__.py",
    icon_resources = icon_resources,
    bitmap_resources = bitmap_resources,
    other_resources = other_resources,
    dest_base = "ARCed",
    version = "0.6.1.469",
    company_name = "ARC Developers",
    copyright = "© 2011 ARC Developers arc@chaos-project.com",
    name = "ARCed (Advanced RPG Creator Editor)"
    )

maptestTargert = Target(
    # what to build
    script = "Map_Test.py",
    icon_resources = icon_resources,
    bitmap_resources = bitmap_resources,
    other_resources = other_resources,
    dest_base = "maptest",
    version = "0.6.1.469",
    company_name = "ARC Developers",
    copyright = "© 2011 ARC Developers arc@chaos-project.com",
    name = "ARCed (Advanced RPG Creator Editor)"
    )
	
DatabaseTestTargert = Target(
    # what to build
    script = "Database_Test.py",
    icon_resources = icon_resources,
    bitmap_resources = bitmap_resources,
    other_resources = other_resources,
    dest_base = "maptest",
    version = "0.6.1.469",
    company_name = "ARC Developers",
    copyright = "© 2011 ARC Developers arc@chaos-project.com",
    name = "ARCed (Advanced RPG Creator Editor)"
    )
    
PyXALTargert = Target(
    # what to build
    script = "PyXAL_Test.py",
    icon_resources = icon_resources,
    bitmap_resources = bitmap_resources,
    other_resources = other_resources,
    dest_base = "PyXAL Test",
    version = "0.6.1.469",
    company_name = "ARC Developers",
    copyright = "© 2011 ARC Developers arc@chaos-project.com",
    name = "ARCed (Advanced RPG Creator Editor)"
    )

setup(

    data_files = data_files,

    options = {"py2exe": {"compressed": 1,
                          "optimize": 2,
                          "includes": includes,
                          "excludes": excludes,
                          "packages": packages,
                          "dll_excludes": dll_excludes,
                          "bundle_files": 2,
                          "dist_dir": "dist",
                          "xref": False,
                          "skip_archive": False,
                          "ascii": False,
                          "custom_boot_script": '',
                         }
              },

    zipfile = None,
    console = [],
    windows = [ARCedTarget, maptestTargert, DatabaseTestTargert, PyXALTargert]
    )
    

def movePaths(paths, dest):
    for path in paths:
        name = os.path.split(path)[1]
        to = os.path.abspath(os.path.join(dest, name))
        print "Moving %s  to => %s" % (path, to)
        shutil.copyfile(path, to)

print "======Moving extra dlls and cfg=========="
paths_to_move = ["ARCed.cfg"]
paths_to_move.extend(extra_dll_paths) 
movePaths(paths_to_move, "dist")

#pop back to our dir
os.chdir("..")
#move the dist folder
shutil.move(r"compiled\dist", "dist")
