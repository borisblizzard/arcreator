import os
import re
import subprocess
import time
import traceback
from pathlib import Path
from setuptools import setup
from distutils.extension import Extension
import distutils.log
from Cython.Build import cythonize


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


def ensure_path(path):
    if path != "" and not os.path.exists(path) or not os.path.isdir(path):
        os.makedirs(path)


# scan the 'Core' directory for extension files, converting
# them to extension names in dotted notation
# "Cache.py", "Controls.py"
ingoreNames = ["__init__.py", "setup.py", "__main__.py",
               "_ext.py", "Logo.py", "Boot.py", "build", "Welder.py"]
testFiles = ["Map_Test.py", "PyXAL_Test.py", "Database_Test.py"]


class Package:

    def __init__(self, path, folder, ext, excludes=[]):
        self.path = Path(path).resolve()
        self.ext = ext
        self.excludes = excludes
        self.folder = folder

    def build(self):
        # set log verbosity to print everything
        distutils.log.set_verbosity(3)

        os.chdir(str(self.path))
        t = time.time()
        print(COLORS.OKGREEN + "Cythoning", self.path, COLORS.ENDC)
        setup(
            name='ARC Welder',
            ext_modules=cythonize(self.ext, exclude=self.excludes)
        )
        print(COLORS.OKGREEN + "Finished Compiling",
              str(self.path) + COLORS.ENDC)
        print(COLORS.OKBLUE + "Time spent Compiling %s: %s Seconds" %
              (self.path, time.time() - t) + COLORS.ENDC)


class Packager:

    def __init__(self, path, excludes):
        self.path = Path(path).resolve()
        self.excludes = excludes
        self.packages = []
        self.scanfolder(self.path)

    def scanfolder(self, path):
        if not path.is_dir():
            raise RuntimeError("Path '%s' is not a directory" % str(self.path))
        if path.name in self.excludes:
            return
        files = [f.name for f in path.iterdir() if not f.is_dir()]
        if "__init__.py" in files:
            # this is a package
            self.add_package(path)
        else:
            for f in path.iterdir():
                if f.is_dir():
                    self.scanfolder(f)

    def add_package(self, path):
        excludes = self.excludes + [
            path.name + "/__init__.py",
            path.name + "/on_enable.py",
            path.name + "/GenImages.py"]
        p = Package(
            path.parent, path.name, [path.name + "/*.py"], excludes=excludes)
        self.packages.append(p)


def builder(package):
    try:
        package.build()
        return False
    except Exception:
        return traceback.format_exc()


def _init_multiprocessing_helper():
    # KeyboardInterrupt kills workers, so don't let them get it
    global COLORS_ENABLED
    import signal
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    if COLORS_ENABLED:
        try:
            import colorama
            colorama.init()
        except ImportError:
            pass


class Cythonizer:

    def __init__(self, packages):
        self.packages = packages

    def build(self):

        ncpus = num_cpus()

        print(COLORS.OKBLUE + "Building useing ",
              ncpus, "threads" + COLORS.ENDC)

        t = time.time()

        if ncpus > 1:

            import multiprocessing
            import multiprocessing.pool

            pool = multiprocessing.Pool(
                ncpus, initializer=_init_multiprocessing_helper)

            try:
                result = pool.map_async(builder, self.packages, chunksize=1)
                pool.close()
                while not result.ready():
                    try:
                        result.get(1)  # seconds
                    except multiprocessing.TimeoutError:
                        pass
            except KeyboardInterrupt:
                pool.terminate()
                raise

            pool.terminate()
            pool.join()

            results = result.get(1)

            # fix keyboard interupt
            # from multiprocessing.pool import IMapIterator

            # def wrapper(func):
            #     def wrap(self, timeout=None):
            # Note: the timeout of 1 googol seconds introduces a rather subtle
            # bug for Python scripts intended to run many times the age of the universe.
            #         return func(self, timeout=timeout if timeout is not None else 1e100)
            #     return wrap
            # IMapIterator.next = wrapper(IMapIterator.next)

            # with multiprocessing.pool.Pool(ncpus) as pool:
            #     results = pool.map(builder, self.packages)
        else:
            results = []
            for path in self.packages:
                results.append(builder(path))

        print(COLORS.OKBLUE + "TOTAL Time spent Compiling: %s Seconds" %
              (time.time() - t) + COLORS.ENDC)
        errors = [r for r in results if r]
        if errors:
            print(COLORS.FAIL + "There were some errors:\n" + COLORS.ENDC,
                  *errors)
            return True
        else:
            print(COLORS.OKGREEN, "There were no errors", COLORS.ENDC)
        return False


def lib_name(libname):
    if os.name == 'nt':
        return "lib" + libname
    else:
        return libname


def build(path):

    plugins = Packager(os.path.join(path, "Core"), ["PyXAL", "Templates"])

    extra_plugins = [
        Package(
            os.path.join(path, "Core", "PyXAL"),
            "PyXAL",
            Extension(
                "_PyXAL",
                ["_PyXAL.pyx"],
                language="c++",
                include_dirs=["include"],
                library_dirs=["lib"],
                libraries=[lib_name("hltypes"), lib_name("xal")]
            )
        )
    ]

    packages = plugins.packages + extra_plugins

    welder_pkg = Package(
        path,
        ".",
        ["*.py"]
    )

    packages.append(welder_pkg)

    cythonizer = Cythonizer(packages)

    return cythonizer.build()


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
