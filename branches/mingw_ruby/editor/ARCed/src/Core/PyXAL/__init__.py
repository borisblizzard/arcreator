try:
    import numpy
    del numpy
except ImportError:
    raise ImportError("Numpy is required for PyXAL")
try :
    import _PyXAL
except ImportError:
    _PyXAL = None
    print "PyXAL not loaded"
