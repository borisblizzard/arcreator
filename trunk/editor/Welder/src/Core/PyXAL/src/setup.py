from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

XAL_ext = Extension(
      "_PyXAL",                           # name of extension
      ["_PyXAL.pyx"],                     # our Cython source "PyXAL.pyx"
      language="c++",                    # causes Cython to create C++ source
      include_dirs=[r".\include", r"C:\Python34\include", r"C:\Python34\PC"],                   # list of paths to search for header files
      library_dirs=[r".\bin", r".\lib", r"C:\Python34\libs", 'C:\Python34\PCbuild', ],                   # list of paths to search for libraries at link time
      libraries=["libhltypes",  "libxal"],                 # list of libraries to link to
      extra_compile_args=[],
      extra_link_args=[],
 )


setup(
      name="_PyXAL",
      ext_modules=[XAL_ext],                
      cmdclass={'build_ext': build_ext},
)