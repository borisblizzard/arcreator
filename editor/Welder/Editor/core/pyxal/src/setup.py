from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

XAL_ext = Extension(
      "_pyxal",                           # name of extension
      ["_pyxal.pyx"],                     # our Cython source "pyxal.pyx"
      language="c++",                    # causes Cython to create C++ source
      include_dirs=[r".\include"],                   # list of paths to search for header files
      library_dirs=[r".\bin", r".\lib"],                   # list of paths to search for libraries at link time
      libraries=["libhltypes",  "libxal"],                 # list of libraries to link to
      extra_compile_args=[],
      extra_link_args=[],
 )


setup(
      name="_pyxal",
      ext_modules=[XAL_ext],                
      cmdclass={'build_ext': build_ext},
)