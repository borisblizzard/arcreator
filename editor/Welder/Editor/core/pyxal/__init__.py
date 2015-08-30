try:
    import numpy
    del numpy
except ImportError:
    raise ImportError("Numpy is required for PyXAL")
try:
    from . import _pyxal as PyXAL
except ImportError as err:
    PyXAL = None
    print("PyXAL not loaded: {0}".format(err))
