from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

XAL_ext = Extension(
                   "PyXAL",                           # name of extension
                   ["PyXAL.pyx"],                     # our Cython source "PyXAL.pyx"
                   language="c++",                    # causes Cython to create C++ source
                   include_dirs=[r"..\PyXAL\include"],                   # list of paths to search for header files
                   library_dirs=[r"..\PyXAL\bin",],                   # list of paths to search for libraries at link time
                   libraries=["xal", "hltypes"],                 # list of libraries to link to
                   runtime_library_dirs=[r"..\PyXAL\bin",],           # list of paths to search for libraries loaded at run time
                   extra_compile_args=[],
                   extra_link_args=[],
                   )


setup(
      name="PyXAL",
      ext_modules=[XAL_ext],                
      cmdclass={'build_ext': build_ext},
      )