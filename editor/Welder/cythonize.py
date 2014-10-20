import sys
import os
import re
import subprocess
import stat
import shutil
import time
from pathlib import Path
from setuptools import setup
from distutils.extension import Extension
from Cython.Build import cythonize


def available_cpu_count():
    """ Number of available virtual or physical CPUs on this system, i.e.
    user/real as output by time(1) when called with an optimally scaling
    userspace-only program"""

    # cpuset
    # cpuset may restrict the number of *available* processors
    try:
        m = re.search(r'(?m)^Cpus_allowed:\s*(.*)$',
                      open('/proc/self/status').read())
        if m:
            res = bin(int(m.group(1).replace(',', ''), 16)).count('1')
            if res > 0:
                return res
    except IOError:
        pass

    # Python 2.6+
    try:
        import multiprocessing
        return multiprocessing.cpu_count()
    except (ImportError, NotImplementedError):
        pass

    # http://code.google.com/p/psutil/
    try:
        import psutil
        return psutil.NUM_CPUS
    except (ImportError, AttributeError):
        pass

    # POSIX
    try:
        res = int(os.sysconf('SC_NPROCESSORS_ONLN'))

        if res > 0:
            return res
    except (AttributeError, ValueError):
        pass

    # Windows
    try:
        res = int(os.environ['NUMBER_OF_PROCESSORS'])

        if res > 0:
            return res
    except (KeyError, ValueError):
        pass

    # jython
    try:
        from java.lang import Runtime
        runtime = Runtime.getRuntime()
        res = runtime.availableProcessors()
        if res > 0:
            return res
    except ImportError:
        pass

    # BSD
    try:
        sysctl = subprocess.Popen(['sysctl', '-n', 'hw.ncpu'],
                                  stdout=subprocess.PIPE)
        scStdout = sysctl.communicate()[0]
        res = int(scStdout)

        if res > 0:
            return res
    except (OSError, ValueError):
        pass

    # Linux
    try:
        res = open('/proc/cpuinfo').read().count('processor\t:')

        if res > 0:
            return res
    except IOError:
        pass

    # Solaris
    try:
        pseudoDevices = os.listdir('/devices/pseudo/')
        res = 0
        for pd in pseudoDevices:
            if re.match(r'^cpuid@[0-9]+$', pd):
                res += 1

        if res > 0:
            return res
    except OSError:
        pass

    # Other UNIXes (heuristic)
    try:
        try:
            dmesg = open('/var/run/dmesg.boot').read()
        except IOError:
            dmesgProcess = subprocess.Popen(['dmesg'], stdout=subprocess.PIPE)
            dmesg = dmesgProcess.communicate()[0]

        res = 0
        while '\ncpu' + str(res) + ':' in dmesg:
            res += 1

        if res > 0:
            return res
    except OSError:
        pass

    raise Exception('Can not determine number of CPUs on this system')


def num_cpus():
    try:
        return available_cpu_count()
    except Exception:
        return 1

start_time = time.time()

# scan the 'Core' directory for extension files, converting
# them to extension names in dotted notation
# "Cache.py", "Controls.py"
ingoreNames = ["__init__.py", "setup.py", "__main__.py", "_ext.py", "Logo.py", "Boot.py", "build", "Welder.py"]
testFiles = ["Map_Test.py", "PyXAL_Test.py", "Database_Test.py"]


def builder(path):
    os.chdir(path)
    print("Building %s" % path)
    if Path(path).name == "PyXAL":
        ext = Extension(
            "_PyXal",
            ["_PyXal.pyx"],
            language="c++",
            include_dirs=["src/include"],
            library_dirs=["src/lib"],
            libraries=["libhltypes", "libxal"]
        ),
    else:
        ext = ["*.py"]
    setup(
        name='ARC Welder',
        ext_modules=cythonize(ext, exclude=["__init__.py"])
    )


class PackageCythonizer:

    def __init__(self, path):
        self.path = Path(path).resolve()
        self.packages = []
        self.scanfolder(self.path)

    def scanfolder(self, path):
        if not path.is_dir():
            raise RuntimeError("Path '%s' is not a directory" % str(self.path))
        files = [f.name for f in path.iterdir() if not f.is_dir()]
        if "__init__.py" in files:
            # this is a package
            self.add_package(str(path))
        else:
            for f in path.iterdir():
                if f.is_dir():
                    self.scanfolder(f)

    def add_package(self, path):
        self.packages.append(path)

    def build(self):

        ncpus = num_cpus()

        if ncpus > 1:
            import multiprocessing.pool
            # fix keyboard interupt
            from multiprocessing.pool import IMapIterator

            def wrapper(func):
                def wrap(self, timeout=None):
                    # Note: the timeout of 1 googol seconds introduces a rather subtle
                    # bug for Python scripts intended to run many times the age of the universe.
                    return func(self, timeout=timeout if timeout is not None else 1e100)
                return wrap
            IMapIterator.next = wrapper(IMapIterator.next)

            with multiprocessing.pool.Pool(ncpus) as pool:
                list(pool.imap(builder, self.packages))
        else:
            for path in self.packages:
                builder(path)

# def ensure_path(path):
#     if path != "" and not os.path.exists(path) or not os.path.isdir(path):
#         os.makedirs(path)

# #"Cache.pyd", "Controls.pyd"
# copyIngoreNames = ["setup.py", "setup.pyd", "src", "bin", "build", "dist", "log", "RTP", "plugins"]
# #  "Cache.py", "Controls.py"
# copyIncludeNames = ["__init__.py", "__main__.py", "_ext.py", "Logo.py", "Welder.cfg", "Boot.py"]
# copyIncludeNames.extend(testFiles)


# def copy_compiled_dir(dir, dest_dir):
#     ensure_path(os.path.abspath(dest_dir))
#     for file in os.listdir(dir):
#         path = os.path.join(dir, file)
#         if file in copyIngoreNames:
#             continue
#         if os.path.isfile(path) and ((file in copyIncludeNames) or path.endswith(".pyd") or path.endswith(".dll")):
#             to_copy = os.path.abspath(path)
#             copy_to = os.path.abspath(os.path.join(dest_dir, file))
#             print("Copying %s   to => %s" % (to_copy, copy_to))
#             shutil.copyfile(to_copy, copy_to)
#         elif os.path.isdir(path):
#             if (file == "Core") and not ("Compiled" in dir):
#                 file = os.path.join("Compiled", file)
#             copy_compiled_dir(path, os.path.join(dest_dir, file))
# print("")
# print("=============================================")
# print("Copying files to Core_Compiled")
# print("=============================================")
# print("")
# shutil.rmtree(os.path.abspath(r"..\compiled"), ignore_errors=True)
# copy_compiled_dir("./", os.path.abspath(r"..\compiled"))
# print("")
# print("=============================================")
# print("Done with Compileation")
# print("%s Seconds" % (time.time() - start_time))
# print("=============================================")

if __name__ == '__main__':

    plugins = PackageCythonizer("src/Core")

    plugins.build()

    # setup(
    #     name='ARC Welder',
    #     ext_modules=exts
    # )
