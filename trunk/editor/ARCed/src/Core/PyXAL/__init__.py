try:
    import numpy
    del numpy
except ImportError:
    raise ImportError("Numpy is required for PyXAL")
import _PyXAL
