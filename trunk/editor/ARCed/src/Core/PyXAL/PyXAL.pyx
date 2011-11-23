from hltypes cimport Array, String
from XAL cimport AudioManager

class PyAudioManager(object):

	def __init__(self, char* systemname, int backendId, bint threaded = False, float updateTime = 0.01, char* deviceName = ""):
		cdef String* name = new String(systemname)
		cdef String* dname = new String(deviceName)
		cdef AudioManager *mgr = new AudioManager(name[0], backendId, threaded, updateTime, dname[0])