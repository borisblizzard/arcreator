# -*- coding: iso-8859-1 -*-
from distutils.core import setup
import py2exe
import glob
import os
import zlib
import shutil


# Remove the build folder
shutil.rmtree("build", ignore_errors=True)

# do the same for dist folder
shutil.rmtree("dist", ignore_errors=True)

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



data_files = []

includes = []
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
            'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
            'Tkconstants', 'Tkinter']
packages = []
dll_excludes = ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll', 'tcl84.dll',
                'tk84.dll',
                'MSVCP90.dll', 'mswsock.dll', 'powrprof.dll']
icon_resources = [(0, 'icon.ico')]
bitmap_resources = []
other_resources = []
other_resources = [(24, 1, MANIFEST_TEMPLATE % dict(prog="ARCed", version="0.0.0.1"))]


ARCedTarget = Target(
    # what to build
    script = "Main.py",
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
    script = "Mapeditor.py",
    icon_resources = icon_resources,
    bitmap_resources = bitmap_resources,
    other_resources = other_resources,
    dest_base = "maptest",
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
    windows = [ARCedTarget, maptestTargert]
    )
