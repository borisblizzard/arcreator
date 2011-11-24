from cython.operator cimport dereference as deref
from libcpp cimport bool
from hltypes cimport Array, String
cimport XAL

import os

cdef char* XAL_AS_DIRECTSOUND = "DirectSound"
cdef char* XAL_AS_OPENAL = "OpenAL"
cdef char* XAL_AS_SDL = "SDL"
cdef char* XAL_AS_AVFOUNDATION = "AVFoundation"
cdef char* XAL_AS_COREAUDIO = "CoreAudio"
cdef char* XAL_AS_DISABLED = "Disabled"
cdef char* XAL_AS_DEFAULT = ""

cdef XAL.HandlingMode FULL = XAL.FULL
cdef XAL.HandlingMode LAZY = XAL.LAZY
cdef XAL.HandlingMode ON_DEMAND = XAL.ON_DEMAND
cdef XAL.HandlingMode STREAMED = XAL.ON_DEMAND

cdef extern from *:
    ctypedef char* const_char_ptr "const char*"

cdef class PyAudioManager:
    
    cdef XAL.AudioManager *_pointer
    
    def __init__(self):
        pass
        
        
cdef class PySound:
    
    cdef XAL.Sound *_pointer
    
    def __init__(self):
        pass
        
    def getName(self):
        cdef String hl_name = self._pointer.getName()
        cdef const_char_ptr name = hl_name.c_str()
        return name
        
    def getFilename(self):
        cdef String hl_name = self._pointer.getFilename()
        cdef const_char_ptr name = hl_name.c_str()
        return name
    
    def getRealFilename(self):
        cdef String hl_name = self._pointer.getRealFilename()
        cdef const_char_ptr name = hl_name.c_str()
        return name
        
        
cdef class PyPlayer:
    
    cdef XAL.Player *_pointer
    
    def __init__(self):
        pass
        
    def getGain(self):
        cdef float gain = self._pointer.getGain()
        return gain
        
    def setGain(self, float value):
        self._pointer.setGain(value)
        
    def getOffset(self):
        cdef float offset = self._pointer.getOffset()
        return offset
    
    def getSound(self):
        cdef XAL.Sound* sound = self._pointer.getSound()
        cdef PySound pysound = PySound()
        pysound._pointer = sound
        return pysound
        
    def getName(self):
        cdef String hl_name = self._pointer.getName()
        cdef const_char_ptr name = hl_name.c_str()
        return name
        
    def getFilename(self):
        cdef String hl_name = self._pointer.getFilename()
        cdef const_char_ptr name = hl_name.c_str()
        return name
    
    def getRealFilename(self):
        cdef String hl_name = self._pointer.getRealFilename()
        cdef const_char_ptr name = hl_name.c_str()
        return name
        
    def getDuration(self):
        cdef float duration = self._pointer.getDuration()
        return duration
        
    def getSize(self):
        cdef int size = self._pointer.getSize()
        return size
        
    def isPlaying(self):
        return self._pointer.isPlaying()
        
    def isPaused(self):
        return self._pointer.isPaused()
        
    def isFading(self):
        return self._pointer.isFading()
        
    def isFadingIn(self):
        return self._pointer.isFadingIn()
    
    def isFadingOut(self):
        return self._pointer.isFadingOut()
        
    def isLooping(self):
        return self._pointer.isLooping()
        
    def play(self, float fadeTime = 0.0, bool looping = False):
        self._pointer.play(fadeTime, looping)
    
    def stop(self, float fadeTime = 0.0):
        self._pointer.stop(fadeTime)
        
    def pause(self, float fadeTime = 0.0):
        self._pointer.pause(fadeTime)
    
    
cdef class XALManager:

    cdef bint destroyed, inited
    cdef char* CATEGORY_STR
    cdef XAL.Category *_category

    def __init__(self, char* systemname, int backendId, bint threaded = False, float updateTime = 0.01, char* deviceName = ""):
        self.CATEGORY_STR = "default"
        cdef String* name = new String(systemname)
        cdef String* dname = new String(deviceName)
        XAL.init(name[0], backendId, threaded, updateTime, dname[0])
        self.inited = True
        self.destroyed = False
        self.SetupXAL()
        del name
        del dname
        
    def SetupXAL(self):
        cdef String* category = new String(self.CATEGORY_STR)
        self._category = XAL.mgr.createCategory(category[0], FULL, FULL)
    
    def __del__(self):
        XAL.destroy()
        self.destroyed = True
        
    def DestroyXAL(self):
        XAL.destroy()
        self.destroyed = True
        
    def get_manager(self):
        cdef PyAudioManager wraper
        if self.inited and not self.destroyed:
            wraper = PyAudioManager()
            wraper._pointer = XAL.mgr
            return wraper
            
    def createSound(self, bytes filename):
        cdef char* file = filename
        s = os.path.split(filename)[0]
        cdef char* path = s
        cdef String* file_str = new String(file)
        cdef String* path_str = new String(path)
        cdef String* category = new String(self.CATEGORY_STR)
        cdef XAL.Sound* sound = XAL.mgr.createSound(file_str[0], category[0], path_str[0])
        cdef PySound pysound = PySound()
        pysound._pointer = sound
        del file_str
        del path_str
        del category
        return pysound
        
    def createPlayer(self, PySound sound):
        s = sound.getName()
        cdef char* name = s
        cdef String* hl_name = new String(name)
        cdef XAL.Player* player = XAL.mgr.createPlayer(hl_name[0])
        cdef PyPlayer pyplayer = PyPlayer()
        pyplayer._pointer = player
        del hl_name
        return pyplayer
        
    def destroyPlayer(self, PyPlayer pyplayer):
        XAL.mgr.destroyPlayer(pyplayer._pointer)
        
    def findPlayer(self, bytes name):
        cdef char* name_str = name
        cdef String* hl_name = new String(name_str)
        cdef XAL.Player* player = XAL.mgr.findPlayer(hl_name[0])
        cdef PyPlayer pyplayer = PyPlayer()
        pyplayer._pointer = player
        del hl_name
        return pyplayer
        
    def play(self, bytes name, float fadeTime = 0.0, bool looping = False, float gain = 1.0):
        cdef char* name_str = name
        cdef String* hl_name = new String(name_str)
        XAL.mgr.play(hl_name[0], fadeTime, looping, gain)
        del hl_name
        
    def stop(self, bytes name, float fadeTime = 0.0):
        cdef char* name_str = name
        cdef String* hl_name = new String(name_str)
        XAL.mgr.stop(hl_name[0], fadeTime)
        del hl_name
    
    def stopFirst(self, bytes name, float fadeTime = 0.0):
        cdef char* name_str = name
        cdef String* hl_name = new String(name_str)
        XAL.mgr.stopFirst(hl_name[0], fadeTime)
        del hl_name
    
    def stopAll(self, float fadeTime = 0.0):
        XAL.mgr.stopAll(fadeTime)
        
    def pauseAll(self, float fadeTime = 0.0):
        XAL.mgr.pauseAll(fadeTime)
    
    def resumeAll(self, float fadeTime = 0.0):
        XAL.mgr.resumeAll(fadeTime)
    
    def isAnyPlaying(self, bytes name):
        cdef char* name_str = name
        cdef String* hl_name = new String(name_str)
        cdef bint result = XAL.mgr.isAnyPlaying(hl_name[0])
        del hl_name
        return result
        
    def isAnyFading(self, bytes name):
        cdef char* name_str = name
        cdef String* hl_name = new String(name_str)
        cdef bint result = XAL.mgr.isAnyFading(hl_name[0])
        del hl_name
        return result
    
    def isAnyFadingIn(self, bytes name):
        cdef char* name_str = name
        cdef String* hl_name = new String(name_str)
        cdef bint result = XAL.mgr.isAnyFadingIn(hl_name[0])
        del hl_name
        return result
    
    def isAnyFadingOut(self, bytes name):
        cdef char* name_str = name
        cdef String* hl_name = new String(name_str)
        cdef bint result = XAL.mgr.isAnyFadingOut(hl_name[0])
        del hl_name
        return result