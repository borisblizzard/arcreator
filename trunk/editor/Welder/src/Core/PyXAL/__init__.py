try:
    import numpy
    del numpy
except ImportError:
    raise ImportError("Numpy is required for PyXAL")
try:
    from . import _PyXAL as PyXAL
except ImportError as err:
    PyXAL = None
    print("PyXAL not loaded: {0}".format(err))
