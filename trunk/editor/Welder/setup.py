
import os
import re
import subprocess
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


def ensure_path(path):
    if path != "" and not os.path.exists(path) or not os.path.isdir(path):
        os.makedirs(path)


# scan the 'Core' directory for extension files, converting
# them to extension names in dotted notation
# "Cache.py", "Controls.py"
ingoreNames = ["__init__.py", "setup.py", "__main__.py", "_ext.py", "Logo.py", "Boot.py", "build", "Welder.py"]
testFiles = ["Map_Test.py", "PyXAL_Test.py", "Database_Test.py"]


class Package:

    def __init__(self, path, folder, ext, excludes=[]):
        self.path = Path(path).resolve()
        self.ext = ext
        self.excludes = excludes
        self.folder = folder

    def build(self):
        os.chdir(str(self.path))
        t = time.time()
        exclude = self.excludes + [self.folder + "/__init__.py", self.folder + "/on_enable.py"]
        setup(
            name='ARC Welder',
            ext_modules=cythonize(self.ext, exclude=exclude)
        )
        print("Time spent Compiling %s: %s Seconds" % (self.path, time.time() - t))


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
        p = Package(path.parent, path.name, [path.name + "/*.py"])
        self.packages.append(p)


def builder(package):
    try:
        package.build()
        return False
    except Exception as e:
        return e


class Cythonizer:

    def __init__(self, packages):
        self.packages = packages

    def build(self):

        ncpus = num_cpus()

        t = time.time()

        if ncpus > 1:
            import multiprocessing.pool
            # fix keyboard interupt
            # from multiprocessing.pool import IMapIterator

            # def wrapper(func):
            #     def wrap(self, timeout=None):
            #         # Note: the timeout of 1 googol seconds introduces a rather subtle
            #         # bug for Python scripts intended to run many times the age of the universe.
            #         return func(self, timeout=timeout if timeout is not None else 1e100)
            #     return wrap
            # IMapIterator.next = wrapper(IMapIterator.next)

            with multiprocessing.pool.Pool(ncpus) as pool:
                results = pool.map(builder, self.packages)
        else:
            results = []
            for path in self.packages:
                results.append(builder(path))

        print("TOTAL Time spent Compiling: %s Seconds" % (time.time() - t))
        errors = [r for r in results if r]
        if errors:
            print("There were some errors:\n", errors)
            return False
        else:
            print("There were no errors")
        return True


class Distributer:

    excludes = ["lib", "build", "__pycache__", "src", "Makefile", "build_lib.py"]
    exclude_suffixes = [".c", ".cpp"]

    def __init__(self, path):
        self.path = Path(path).resolve()
        self.files = []
        self.dirs = []
        lib = self.path / "lib"
        if lib.exists():
            self.dirs.append(lib)

    def make_dist(self, dest):
        print("Removing old dist folder")
        if os.path.exists(dest):
            shutil.rmtree(dest, True)
            time.sleep(0.1)
        ensure_path(dest)
        dest = Path(dest).resolve()
        print("Scanning...")
        self.scanfolder(self.path)
        print("Copying files...")
        self.copyfiles(dest)
        self.copydirs(dest)
        print("Dist built at:", str(dest))

    def scanfolder(self, path):
        if not path.is_dir():
            raise RuntimeError("Path '%s' is not a directory" % str(self.path))
        files = [f for f in path.iterdir() if f.name not in self.excludes and f.suffix not in self.exclude_suffixes]
        for f in files:
            if f.is_dir():
                self.scanfolder(f)
                continue
            if f.suffix == ".py":
                if f.with_suffix(".so") in files or f.with_suffix(".pyd") in files:
                    continue
            self.files.append(f)

    def copyfiles(self, dest):
        for f in self.files:
            dpath = Path(self.get_dest(dest, f))
            ensure_path(str(dpath.parent))
            print("Copying: ", str(f.relative_to(Path.cwd())), "->", str(dpath.relative_to(Path.cwd())))
            shutil.copyfile(str(f), str(dpath))

    def copydirs(self, dest):
        for d in self.dirs:
            dpath = Path(self.get_dest(dest, d))
            ensure_path(str(dpath.parent))
            print("Copying: ", str(d.relative_to(Path.cwd())), "->", str(dpath.relative_to(Path.cwd())))
            shutil.copytree(str(d), str(dpath))

    def get_dest(self, dest, path):
        return dest / str(path).replace(str(self.path) + os.path.sep, "")


if __name__ == '__main__':

    plugins = Packager("src/Core", ["PyXAL"])

    extra_plugins = [
        Package(
            "src/Core/PyXAL",
            "PyXAL",
            Extension(
                "_PyXAL",
                ["_PyXAL.pyx"],
                language="c++",
                include_dirs=["src/include"],
                library_dirs=["src/lib"],
                libraries=["libhltypes", "libxal"]
            )
        )
    ]

    packages = plugins.packages + extra_plugins

    welder_pkg = Package(
        "src",
        "src",
        ["*.py"],
        ["build_lib.py"]
    )

    packages.append(welder_pkg)

    cythonizer = Cythonizer(packages)

    if cythonizer.build():
        Distributer("src").make_dist("dist")
