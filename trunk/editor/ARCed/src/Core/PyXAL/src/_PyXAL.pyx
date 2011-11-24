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
    ctypedef String& chstr "chstr"
    
cdef str LOG_PATH = ""
cdef bool LOG_ENABLED = False

cpdef SetLogPath(str path):
    global LOG_PATH
    cdef str blank = ""
    if not LOG_PATH == blank and not os.path.exists(path) or not os.path.isdir(path):
        os.makedirs(path)
    LOG_PATH = path
       
cpdef EnableLogging(bool state = True, str path = ""):
    global LOG_ENABLED
    LOG_ENABLED = state
    SetLogPath(path)
    
cdef void Log(chstr logMessage):
    global LOG_PATH
    global LOG_ENABLED
    if not LOG_ENABLED:
        return
    cdef const_char_ptr message
    cdef const_char_ptr line_end = "\n"
    message = logMessage.c_str()
    s = message + line_end
    message = s
    if os.path.exists(LOG_PATH):
        path = os.path.join(LOG_PATH, "XAL.log")
        file = open(path, "ab")
        file.write(message)
        file.close()
        
XAL.setLogFunction(Log)
            
    
cdef class XALManager

Mgr = None


cdef class PyAudioManager:
    
    cdef XAL.AudioManager *_pointer
    
    def __init__(self):
        raise RuntimeError("PyAudioManager Can not be initialized from python")
        
        
cdef class PySound:
    
    cdef XAL.Sound *_pointer
    
    def __init__(self):
        raise RuntimeError("PySound Can not be initialized from python")
        
    def isXALInitialized(self):
        if XAL.mgr != NULL:
            return True
        else:
            return False
        
    def getName(self):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef String hl_name = self._pointer.getName()
        cdef const_char_ptr name = hl_name.c_str()
        return name
        
    def getFilename(self):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef String hl_name = self._pointer.getFilename()
        cdef const_char_ptr name = hl_name.c_str()
        return name
    
    def getRealFilename(self):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef String hl_name = self._pointer.getRealFilename()
        cdef const_char_ptr name = hl_name.c_str()
        return name
        
        
cdef class PyPlayer:
    
    cdef XAL.Player *_pointer
    
    def __init__(self):
        raise RuntimeError("PyPlayer Can not be initialized from python")
        
    def isXALInitialized(self):
        if XAL.mgr != NULL:
            return True
        else:
            return False
        
    def getGain(self):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef float gain = self._pointer.getGain()
        return gain
        
    def setGain(self, float value):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        self._pointer.setGain(value)
        
    def getOffset(self):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef float offset = self._pointer.getOffset()
        return offset
    
    def getSound(self):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef XAL.Sound* sound = self._pointer.getSound()
        cdef PySound pysound = PySound()
        pysound._pointer = sound
        return pysound
        
    def getName(self):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef String hl_name = self._pointer.getName()
        cdef const_char_ptr name = hl_name.c_str()
        return name
        
    def getFilename(self):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef String hl_name = self._pointer.getFilename()
        cdef const_char_ptr name = hl_name.c_str()
        return name
    
    def getRealFilename(self):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef String hl_name = self._pointer.getRealFilename()
        cdef const_char_ptr name = hl_name.c_str()
        return name
        
    def getDuration(self):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef float duration = self._pointer.getDuration()
        return duration
        
    def getSize(self):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef int size = self._pointer.getSize()
        return size
        
    def isPlaying(self):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        return self._pointer.isPlaying()
        
    def isPaused(self):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        return self._pointer.isPaused()
        
    def isFading(self):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        return self._pointer.isFading()
        
    def isFadingIn(self):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        return self._pointer.isFadingIn()
    
    def isFadingOut(self):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        return self._pointer.isFadingOut()
        
    def isLooping(self):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        return self._pointer.isLooping()
        
    def play(self, float fadeTime = 0.0, bool looping = False):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        self._pointer.play(fadeTime, looping)
    
    def stop(self, float fadeTime = 0.0):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        self._pointer.stop(fadeTime)
        
    def pause(self, float fadeTime = 0.0):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        self._pointer.pause(fadeTime)
    
    
cdef class XALManager:

    cdef bint destroyed, inited
    cdef char* CATEGORY_STR
    cdef XAL.Category *_category

    def __init__(self, char* systemname, int backendId, bint threaded = False, float updateTime = 0.01, char* deviceName = ""):
        global Mgr
        if Mgr is not None:
            raise RuntimeError("Only one XALManager interface allowed at a time, use the one at PyXAL.Mgr")
        self.CATEGORY_STR = "default"
        cdef String* name = new String(systemname)
        cdef String* dname = new String(deviceName)
        self.DestroyXAL()
        XAL.init(name[0], backendId, threaded, updateTime, dname[0])
        self.inited = True
        self.destroyed = False
        self.SetupXAL()
        del name
        del dname
        
    def isXALInitialized(self):
        if XAL.mgr != NULL:
            return True
        else:
            return False
            
    def SetupXAL(self):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef String* category = new String(self.CATEGORY_STR)
        self._category = XAL.mgr.createCategory(category[0], FULL, FULL)
    
    def __del__(self):
        if XAL.mgr != NULL:
            print "del XALManger"
            fade = 0.0
            XAL.mgr.stopAll(fade)
            XAL.destroy()
    
    def __dealloc__(self):
        if XAL.mgr != NULL:
            print "dealloc XALManger"
            fade = 0.0
            XAL.mgr.stopAll(fade)
            XAL.destroy()		
        
    def DestroyXAL(self):
        if self.isXALInitialized():
            print "DestroyXAL XALManger"
            fade = 0.0
            XAL.mgr.stopAll(fade)
            XAL.destroy()
            
    def clear(self):
        if self.isXALInitialized():
            print "clear XALManager"
            fade = 0.0
            XAL.mgr.stopAll(fade)
            XAL.mgr.clear()
            
    def createSound(self, bytes filename):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef char* file = filename
        s = os.path.split(filename)[0]
        cdef char* path = s
        cdef String* file_str = new String(file)
        cdef String* path_str = new String(path)
        cdef String* category = new String(self.CATEGORY_STR)
        cdef XAL.Sound* sound 
        sound = XAL.mgr.createSound(file_str[0], category[0], path_str[0])
        if sound == NULL:
            raise RuntimeError("XAL Failed to load file %s" % filename)
        cdef PySound pysound = PySound.__new__(PySound)
        pysound._pointer = sound
        del file_str
        del path_str
        del category
        return pysound
        
    def createPlayer(self, PySound sound):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        sound_name = sound.getName()
        cdef char* name = sound_name
        cdef String* hl_name = new String(name)
        cdef XAL.Player* player 
        player = XAL.mgr.createPlayer(hl_name[0])
        if player == NULL:
            raise RuntimeError("XAL Failed to create a player for %s" % sound_name)
        cdef PyPlayer pyplayer = PyPlayer.__new__(PyPlayer)
        pyplayer._pointer = player
        del hl_name
        return pyplayer
        
    def destroyPlayer(self, PyPlayer pyplayer):
        if pyplayer is None:
            raise RuntimeError("destroyPlayer Passed a None object")
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        XAL.mgr.destroyPlayer(pyplayer._pointer)
        
    def destroySound(self, PySound pysound):
        if pysound is None:
            raise RuntimeError("destroySound Passed a None object")
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        XAL.mgr.destroySound(pysound._pointer)
        
    def findPlayer(self, bytes name):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef char* name_str = name
        cdef String* hl_name = new String(name_str)
        cdef XAL.Player* player 
        player = XAL.mgr.findPlayer(hl_name[0])
        if player == NULL:
            raise RuntimeError("XAL Failed to find a player for %s" % name)
        cdef PyPlayer pyplayer = PyPlayer.__new__(PyPlayer)
        pyplayer._pointer = player
        del hl_name
        return pyplayer
        
    def play(self, bytes name, float fadeTime = 0.0, bool looping = False, float gain = 1.0):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef char* name_str = name
        cdef String* hl_name = new String(name_str)
        XAL.mgr.play(hl_name[0], fadeTime, looping, gain)
        del hl_name
        
    def stop(self, bytes name, float fadeTime = 0.0):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef char* name_str = name
        cdef String* hl_name = new String(name_str)
        XAL.mgr.stop(hl_name[0], fadeTime)
        del hl_name
    
    def stopFirst(self, bytes name, float fadeTime = 0.0):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef char* name_str = name
        cdef String* hl_name = new String(name_str)
        XAL.mgr.stopFirst(hl_name[0], fadeTime)
        del hl_name
    
    def stopAll(self, float fadeTime = 0.0):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        XAL.mgr.stopAll(fadeTime)
        
    def pauseAll(self, float fadeTime = 0.0):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        XAL.mgr.pauseAll(fadeTime)
    
    def resumeAll(self, float fadeTime = 0.0):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        XAL.mgr.resumeAll(fadeTime)
    
    def isAnyPlaying(self, bytes name):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef char* name_str = name
        cdef String* hl_name = new String(name_str)
        cdef bint result = XAL.mgr.isAnyPlaying(hl_name[0])
        del hl_name
        return result
        
    def isAnyFading(self, bytes name):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef char* name_str = name
        cdef String* hl_name = new String(name_str)
        cdef bint result = XAL.mgr.isAnyFading(hl_name[0])
        del hl_name
        return result
    
    def isAnyFadingIn(self, bytes name):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef char* name_str = name
        cdef String* hl_name = new String(name_str)
        cdef bint result = XAL.mgr.isAnyFadingIn(hl_name[0])
        del hl_name
        return result
    
    def isAnyFadingOut(self, bytes name):
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef char* name_str = name
        cdef String* hl_name = new String(name_str)
        cdef bint result = XAL.mgr.isAnyFadingOut(hl_name[0])
        del hl_name
        return result
        
def Init(int backendId, bint threaded = True):
    global Mgr
    if Mgr is None:
        if XAL.mgr != NULL:
            print "Init XAL"
            fade = 0.0
            XAL.mgr.stopAll(fade)
            XAL.destroy()
        Mgr = XALManager(XAL_AS_DEFAULT, backendId, threaded)
        
def Destroy():
    global Mgr
    if XAL.mgr != NULL:
        print "XAL Destroy"
        fade = 0.0
        XAL.mgr.stopAll(fade)
        XAL.destroy()
    Mgr = None