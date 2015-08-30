try:
    import numpy
    del numpy
except ImportError:
    raise ImportError("Numpy is required for pyxal")
try:
    from . import _pyxal as pyxal
except ImportError as err:
    pyxal = None
    print("pyxal not loaded: {0}".format(err))
