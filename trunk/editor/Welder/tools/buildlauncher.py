#!/usr/bin/python
import sys
import os
import sysconfig
import distutils.ccompiler
import distutils.sysconfig
import distutils.dep_util
import distutils.log
import traceback


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


def enable_colors(colors=False):
    global COLORS_ENABLED
    global COLORS
    if colors:
        COLORS.enable()
        COLORS_ENABLED = True
    else:
        COLORS.disable()
        COLORS_ENABLED = False


# pulled form distutils and modified a bit
def get_libraries(extralibs=[], debug=False):
    """Return the list of libraries to link against when building a
    shared extension.  On most platforms, this is just 'ext.libraries';
    on Windows, we add the Python library (eg. python20.dll).
    """
    # The python library is always needed on Windows.  For MSVC, this
    # is redundant, since the library is mentioned in a pragma in
    # pyconfig.h that MSVC groks.  The other Windows compilers all seem
    # to need it mentioned explicitly, though, so that's what we do.
    # Append '_d' to the python import library on debug builds.
    if sys.platform == "win32":
        template = "python%d%d"
        if debug:
            template = template + '_d'
        pythonlib = (template %
                     (sys.hexversion >> 24, (sys.hexversion >> 16) & 0xff))
        # don't extend ext.libraries, it may be shared with other
        # extensions, it is a reference to the original list
        return extralibs + [pythonlib]
    elif sys.platform[:6] == "cygwin":
        template = "python%d.%d"
        pythonlib = (template %
                     (sys.hexversion >> 24, (sys.hexversion >> 16) & 0xff))
        # don't extend ext.libraries, it may be shared with other
        # extensions, it is a reference to the original list
        return extralibs + [pythonlib]
    elif sys.platform[:6] == "atheos":
        from distutils import sysconfig

        template = "python%d.%d"
        pythonlib = (template %
                     (sys.hexversion >> 24, (sys.hexversion >> 16) & 0xff))
        # Get SHLIBS from Makefile
        extra = []
        for lib in sysconfig.get_config_var('SHLIBS').split():
            if lib.startswith('-l'):
                extra.append(lib[2:])
            else:
                extra.append(lib)
        # don't extend ext.libraries, it may be shared with other
        # extensions, it is a reference to the original list
        return extralibs + [pythonlib, "m"] + extra
    elif sys.platform == 'darwin':
        # Don't use the default code below
        return extralibs
    elif sys.platform[:3] == 'aix':
        # Don't use the default code below
        return extralibs
    else:
        from distutils import sysconfig
        if sysconfig.get_config_var('Py_ENABLE_SHARED'):
            pythonlib = 'python{}.{}{}'.format(
                sys.hexversion >> 24, (sys.hexversion >> 16) & 0xff,
                sys.abiflags)
            return extralibs + [pythonlib]
        else:
            return extralibs


def build(folder, out_dir, debug=False, force=False):

    # set log verbosity to print everything
    distutils.log.set_verbosity(3)

    sources = []
    include_dirs = []
    lib_dirs = []

    cc = distutils.ccompiler.new_compiler(verbose=1)
    distutils.sysconfig.customize_compiler(cc)

    out_temp_path = os.path.abspath(os.path.join(out_dir, "temp"))
    out_path = os.path.abspath(out_dir)
    target = "welder"
    target_exe = cc.executable_filename(target)
    target_path = os.path.abspath(os.path.join(out_path, target_exe))

    # for welder
    sources.append(os.path.abspath(os.path.join(folder, "welder.c")))
    if sys.platform == "win32":
        sources.append(os.path.abspath(os.path.join(folder, "welder.rc")))

    include_dirs.append(os.path.abspath(os.path.join(folder, "include")))

    lib_dirs.append(os.path.abspath(os.path.join(folder, "libs")))

    # for python
    py_include = distutils.sysconfig.get_python_inc()
    plat_py_include = distutils.sysconfig.get_python_inc(plat_specific=1)
    include_dirs.append(os.path.abspath(sysconfig.get_path('include')))
    include_dirs.append(os.path.abspath(py_include))
    if plat_py_include != py_include:
        include_dirs.append(os.path.abspath(plat_py_include))

    lib_dirs.append(os.path.abspath(os.path.join(sys.exec_prefix, 'libs')))
    lib_dirs.append(os.path.abspath(os.path.join(sys.base_exec_prefix,
                                                 'libs')))

    # define Macros
    if sys.platform == "win32":
        cc.define_macro("_CONSOLE")
        cc.define_macro("_MBCS")
    else:
        pass

    # collect link libs
    if sys.platform == "win32":
        extralibs = [
            "kernel32",
            "user32",
            "gdi32",
            "winspool",
            "comdlg32",
            "advapi32",
            "shell32",
            "ole32",
            "oleaut32",
            "uuid",
            "odbc32",
            "odbccp32",
            "shlwapi"
        ]
    else:
        extralibs = []

    libraries = get_libraries(extralibs, debug)

    # extra compile arguments?
    extra_cc_args = []
    if sys.platform == "win32":
        extra_link_args = [
            "/MANIFEST",
            "/MANIFESTUAC:level='asInvoker' uiAccess='false'",
            "/SUBSYSTEM:CONSOLE"
        ]
    else:
        extra_link_args = [
            "-Wl,-R,'$ORIGIN'"
        ]

    language = cc.detect_language(sources)

    # no need to compile if we are up-to-date
    if not (force or
            distutils.dep_util.newer_group(sources, target_path, 'newer')):
        print(
            COLORS.OKGREEN +
            "Skipping Launcher build, " + str(target_path)
            + " is up-to-date"
            + COLORS.ENDC
        )
        # there was no error
        return False
    else:
        print(
            COLORS.OKBLUE + "Starting Launcher build: "
            + str(target_path)
            + COLORS.ENDC
        )
    # ensure paths exist
    if not os.path.isdir(out_path):
        os.makedirs(out_path)

    if not os.path.isdir(out_temp_path):
        os.makedirs(out_temp_path)

    try:
        # compile sources to objects
        objects = cc.compile(
            sources,
            output_dir=out_temp_path,
            macros=[],
            include_dirs=include_dirs,
            debug=debug,
            extra_postargs=extra_cc_args,
            depends=[]
        )

        # link objects and libraries into an exacutable
        cc.link_executable(
            objects,
            target,
            output_dir=out_path,
            libraries=libraries,
            library_dirs=lib_dirs,
            extra_postargs=extra_link_args,
            debug=debug,
            target_lang=language
        )
    except Exception:
        return traceback.format_exc()

    print(COLORS.OKGREEN + "Build of launcher compleated" +
          COLORS.ENDC)
    # there was no error
    return False

if __name__ == '__main__':

    try:
        import colorama
        COLORS_ENABLED = True
        colorama.init()
    except ImportError:
        pass

    build()
