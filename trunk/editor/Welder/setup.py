import sys, os, stat, commands, shutil, time
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

start_time = time.time()

#pop down to the source folder
os.chdir("src")

# scan the 'Core' directory for extension files, converting
# them to extension names in dotted notation
# "Cache.py", "Controls.py"
ingoreNames = ["__init__.py", "setup.py", "__main__.py", "_ext.py", "Logo.py", "Boot.py", "build", "Welder.py"]
testFiles = ["Map_Test.py", "PyXAL_Test.py", "Database_Test.py"]


def scandir(dir):
    files = []
    for file in os.listdir(dir):
        path = os.path.join(dir, file)
        if file in ingoreNames or "setup" in file or file in testFiles:
            continue
        if os.path.isfile(path) and path.endswith(".py"):
            files.append(path.replace(os.path.sep, ".")[:-3])
        elif os.path.isdir(path):
            files.extend(scandir(path))
    return files


# generate an Extension object from its dotted name
def makeExtension(extName):
    extPath = extName.replace(".", os.path.sep)+".py"
    return Extension(
        "Compiled." + extName,
        [extPath],
        language="c++",
        include_dirs=["."]   # adding the '.' to include_dirs is CRUCIAL!!
    )


# get the list of extensions
extNames = scandir("./")
new_names = []
for name in extNames:
    new_names.append(name.replace("./", ""))
extNames = new_names
print "============================================="
print "Cython Compileing Core"
print "============================================="
print "Compileing these modules:"

for name in extNames:
    print "\t" + name
print "\tWelder"
print "\tCore.PyXAL._PyXAL"
print ""
# and build up the set of Extension objects
extensions = [makeExtension(name) for name in extNames]

#============================================
#Extentions we want to handel special
#============================================
XAL_ext = Extension(
    "Compiled.Core.PyXAL._PyXAL",                                                                               # name of extension
    ["Core\PyXAL\src\_PyXAL.pyx"],                                                                              # our Cython source "PyXAL.pyx"
    language="c++",                                                                                             # causes Cython to create C++ source
    include_dirs=[r"Core\PyXAL\src\include", r"C:\Python27\include", r"C:\Python27\PC"],                        # list of paths to search for header files
    library_dirs=[r"Core\PyXAL\src\bin", r"Core\PyXAL\src\lib", r"C:\Python27\libs", 'C:\Python27\PCbuild', ],  # list of paths to search for libraries at link time
    libraries=["libhltypes",  "libxal"],                                                                        # list of libraries to link to
    extra_compile_args=[],
    extra_link_args=[],
)

Welder_ext = Extension(
    "Welder",                         # name of extension
    ["Welder.py"],                    # our source file
    language="c++"                    # causes Cython to create C++ source
)

extensions.extend([XAL_ext, Welder_ext])


#============================================
#Call the Setup function and start the compilation
#============================================
print "============================================="
print "Starting Compilation"
print "============================================="
setup(
    name="ARCed",
    ext_modules=extensions,
    cmdclass={'build_ext': build_ext}
)


def ensure_path(path):
    if path != "" and not os.path.exists(path) or not os.path.isdir(path):
        os.makedirs(path)

#"Cache.pyd", "Controls.pyd"
copyIngoreNames = ["setup.py", "setup.pyd", "src", "bin", "build", "dist", "log", "RTP", "plugins"]
#  "Cache.py", "Controls.py"
copyIncludeNames = ["__init__.py", "__main__.py", "_ext.py", "Logo.py", "Welder.cfg", "Boot.py"]
copyIncludeNames.extend(testFiles)


def copy_compiled_dir(dir, dest_dir):
    ensure_path(os.path.abspath(dest_dir))
    for file in os.listdir(dir):
        path = os.path.join(dir, file)
        if file in copyIngoreNames:
            continue
        if os.path.isfile(path) and ((file in copyIncludeNames) or path.endswith(".pyd") or path.endswith(".dll")):
            to_copy = os.path.abspath(path)
            copy_to = os.path.abspath(os.path.join(dest_dir, file))
            print "Copying %s   to => %s" % (to_copy, copy_to)
            shutil.copyfile(to_copy, copy_to)
        elif os.path.isdir(path):
            if (file == "Core") and not ("Compiled" in dir):
                file = os.path.join("Compiled", file)
            copy_compiled_dir(path, os.path.join(dest_dir, file))
print ""
print "============================================="
print "Copying files to Core_Compiled"
print "============================================="
print ""
shutil.rmtree(os.path.abspath(r"..\compiled"), ignore_errors=True)
copy_compiled_dir("./", os.path.abspath(r"..\compiled"))
print ""
print "============================================="
print "Done with Compileation"
print "%s Seconds" % (time.time() - start_time)
print "============================================="
