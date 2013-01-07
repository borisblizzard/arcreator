from cython.operator cimport dereference as deref
from libc.stdlib cimport free
from libcpp cimport bool
from hltypes cimport Array, String

cimport XAL

import os

cdef char* XAL_AS_ANDROID = "Android"
cdef char* XAL_AS_DIRECTSOUND = "DirectSound"
cdef char* XAL_AS_OPENAL = "OpenAL"
cdef char* XAL_AS_SDL = "SDL"
cdef char* XAL_AS_AVFOUNDATION = "AVFoundation"
cdef char* XAL_AS_COREAUDIO = "CoreAudio"
cdef char* XAL_AS_DISABLED = "Disabled"
cdef char* XAL_AS_DEFAULT = ""

cdef XAL.BufferMode FULL = XAL.FULL
cdef XAL.BufferMode LAZY = XAL.LAZY
cdef XAL.BufferMode MANAGED = XAL.MANAGED
cdef XAL.BufferMode ON_DEMAND = XAL.ON_DEMAND
cdef XAL.BufferMode STREAMED = XAL.STREAMED

cdef XAL.SourceMode DISK = XAL.DISK
cdef XAL.SourceMode RAM = XAL.RAM

cdef XAL.Format FLAC = XAL.FLAC
cdef XAL.Format M4A = XAL.M4A
cdef XAL.Format OGG = XAL.OGG
cdef XAL.Format SPX = XAL.SPX
cdef XAL.Format WAV = XAL.WAV
cdef XAL.Format UNKNOWN = XAL.UNKNOWN

cdef extern from *:
    ctypedef char* const_char_ptr "const char*"
    ctypedef unsigned char* const_unsigned_char_ptr "const unsigned char*"
    ctypedef String& chstr "chstr"
    ctypedef String hstr "hstr"
    ctypedef Array harray "harray"
    
# cdef str LOG_PATH = ""
# cdef bool LOG_ENABLED = False

# cpdef SetLogPath(str path):
    # '''
    # Sets the path where XAL should create a log file. 
    # the path should not include the file
    # PyXAL will try to create a folder at the path if the path doesn't exist and will save it's log in that folder as a file named XAL.log
    
    # @param path: string path to the folder where the log should be made
    # @return: returns True or False if the path was set
    # '''
    # global LOG_PATH
    # cdef str blank = ""
    # cdef bint result = False
    # if not LOG_PATH == blank and not os.path.exists(path) or not os.path.isdir(path):
        # try:
            # os.makedirs(path)
        # except Exception:
            # return result
    # LOG_PATH = path
    # result = True
    # return result
       
# cpdef EnableLogging(bool state = True, str path = ""):
    # '''
    # sets the logging state of PyXAL by default it is off
    
    # @param state: bool True or False if XAL should be logging data default is True so calling
        # PyXAL.EnableLogging will turn logging on (by default PyXAL does not log)
    # @param path: string path to the folder where PyXAL should create the log 
        # it is an empty string by default so that should mean the log will be made in the 
        # current working directory. calling PyXAL.EnableLogging will set the path to an empty string if the paramater is not included
    # @return: returns True or False if the path was set
    # '''
    # global LOG_ENABLED
    # LOG_ENABLED = state
    # cdef bint result = False
    # result = SetLogPath(path)
    # return result
    
# cdef void Log(chstr logMessage):
    # global LOG_PATH
    # global LOG_ENABLED
    # if not LOG_ENABLED:
        # return
    # cdef const_char_ptr message
    # cdef const_char_ptr line_end = "\n"
    # message = logMessage.c_str()
    # pymessage = message + line_end
    # if os.path.exists(LOG_PATH):
        # try:
            # path = os.path.join(LOG_PATH, "XAL.log")
            # file = open(path, "ab")
            # file.write(pymessage)
            # file.close()
        # except Exception:
            # pass
            
# XAL.setLogFunction(Log)

Mgr = None

cdef hstr Py_to_Hstr (string):
    py_byte_string = string.encode('UTF-8')
    cdef char* c_str = py_byte_string
    cdef hstr hstring = hstr(c_str)
    return hstring
    
cdef Hstr_to_Py (hstr string):
    cdef const_char_ptr c_str = string.c_str()
    py_byte_string = c_str
    pystring = py_byte_string.decode('UTF-8')
    return pystring
    

cdef class PyAudioManager:
    '''
    A wrapper for the C++ xal::AudioManager class. it is currently not used
    '''
    
    cdef XAL.AudioManager *_pointer
    cdef bool destroyed
    
    def __init__(self):
        '''
        this is a wapper class for a C++ class . it should not be initialied outside of the PyXAL module as proper set up would be impossible.
        as such calling the __init__ method will raise a Runtime Error
        '''
        raise RuntimeError("PyAudioManager Can not be initialized from python")
        
        
cdef class SoundWrapper:
    '''
    A wrapper class for the C++ xal::Sound class. it is returned by the XALManager.createSound and PyPlayer.getSound methods
    '''
    
    cdef XAL.Sound *_pointer
    cdef bool destroyed
    
    def __init__(self):
        '''
        this is a wapper class for a C++ class . it should not be initialied outside of the PyXAL module as proper set up would be impossible.
        as such calling the __init__ method will raise a Runtime Error
        '''
        raise RuntimeError("PySound Can not be initialized from python")
        
    def _destroy(self):
        if self.isXALInitialized() and not self.destroyed :
            XAL.mgr.destroySound(self._pointer)
            self.destroyed = True
            
    def __dealloc__(self):
        if (XAL.mgr != NULL) and (not self.destroyed):
            XAL.mgr.destroySound(self._pointer)
            self.destroyed = True
        
    def isXALInitialized(self):
        '''
        returns true if the C++ side of the interface to XAL exists
        '''
        if XAL.mgr != NULL:
            return True
        else:
            return False
        
    def getName(self):
        '''
        @return: returns the string name of the sound. it is normal the full path of teh sound file with out the file extention
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        cdef hstr hl_name = self._pointer.getName()
        name = Hstr_to_Py(hl_name)
        return name
        
    def getFilename(self):
        '''
        @return: returns a string containing the file name the sound was loaded from
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        cdef hstr hl_name = self._pointer.getFilename()
        name = Hstr_to_Py(hl_name)
        return name
    
    def getRealFilename(self):
        '''
        @return: returns a string with the full path to the file the string was loaded from
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        cdef hstr hl_name = self._pointer.getRealFilename()
        name = Hstr_to_Py(hl_name)
        return name
        
    def getSize(self):
        '''
        @return: int the size of the sound data in bits not bytes
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        cdef int size = self._pointer.getSize()
        return size
        
    def getChannels(self):
        '''
        @return: int number of channels the sound has. 1 for mono or 2 for stereo 
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        cdef int channels = self._pointer.getChannels()
        return channels
        
    def getSamplingRate(self):
        '''
        @return: int the sampeling rate for the sound in samples per second
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        cdef int rate = self._pointer.getSamplingRate()
        return rate
        
    def getBitsPerSample(self):
        '''
        @return: int the bits per sample of data in the sound. usualy 8, 16, or 24, possibly 32 not sure
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        cdef int rate = self._pointer.getBitsPerSample()
        return rate
    
    def getDuration(self):
        '''
        @return: float duration of the sound in seconds. it is a floating point number to acound for fractions of a second
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        cdef float duration = self._pointer.getDuration()
        return duration
    
    def getFormat(self):
        '''
        @return: int the intrnal designation of the sound format. coresponds to a file type but as of now there is no way to tell for certin which is which 
            as the nubers will change depending on what formats are currently suported by XAL
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        cdef int format = <int>self._pointer.getFormat()
        return format
        
    def isStreamed(self):
        '''
        @return: bool is the sound being streamed from it's file to the player? or is it comleatly loaded into memory. 
            should always return false in PyXAL as PyXAL uses full decoding mode
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        cdef bint streamed = self._pointer.isStreamed()
        return streamed
        
    def readPcmData(self):
        '''
        read the pcm data of the sound and return it the format of said data can be determined from the size, chanels, bits per sample and sampleling rate of the sound
        @return: a 2 tuple of (number of bits read, string of bytes read)
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        cdef unsigned char* pcm_data
        cdef int pcm_size
        cdef char* c_data
        data = ""
        try:
            pcm_size = self._pointer.readPcmData(&pcm_data)
            if pcm_size > 0:
                c_data = <char*>pcm_data
                data = c_data[:pcm_size]
        finally:
            free(pcm_data)
            pcm_data = NULL
        return (pcm_size, data)
                
                
cdef class PlayerWrapper:
    '''
    a wraper for the C++ class xal::Player. it is retuned by the XALManager.createPlayer method
    '''
    
    cdef XAL.Player *_pointer
    cdef bool destroyed
    
    def __init__(self):
        '''
        this is a wapper class for a C++ class . it should not be initialied outside of the PyXAL module as proper set up would be impossible.
        as such calling the __init__ method will raise a Runtime Error
        '''
        raise RuntimeError("PyPlayer Can not be initialized from python")
        
    def _destroy(self):
        if self.isXALInitialized() and not self.destroyed:
            XAL.mgr.destroyPlayer(self._pointer)
            self.destroyed = True
            
    def __dealloc__(self):
        if (XAL.mgr != NULL) and (not self.destroyed):
            XAL.mgr.destroyPlayer(self._pointer)
            self.destroyed = True      
        
    def isXALInitialized(self):
        '''
        returns true if the C++ side of the interface to XAL exists
        '''
        if XAL.mgr != NULL:
            return True
        else:
            return False
        
    def getGain(self):
        '''
        @return: float the current gain of the player (also knows as volume)
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        cdef float gain = self._pointer.getGain()
        return gain
        
    def setGain(self, float value):
        '''
        set the gain of the player (also knows as volume)
        @param value: float the value of the volume to set 1.0 is normal 2.0 is twice as loud 0.5 is half volume ect.
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        self._pointer.setGain(value)
        
    def getPitch(self):
        '''
        @return: float the current pitch of the player
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        cdef float offset = self._pointer.getPitch()
        return offset
        
    def setPitch(self, float value):
        '''
        set the current pitch of the player
        @param value: float the value of the pitch to set to set 1.0 is normal 2.0 is a 200% shift 0.5 is a 50% shift
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        self._pointer.setPitch(value)
        
    def getName(self):
        '''
        @return: returns the string name of the sound. it is normal the full path of teh sound file with out the file extention
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        cdef hstr hl_name = self._pointer.getName()
        name = Hstr_to_Py(hl_name)
        return name
        
    def getFilename(self):
        '''
        @return: returns a string containing the file name the sound was loaded from
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        cdef hstr hl_name = self._pointer.getFilename()
        name = Hstr_to_Py(hl_name)
        return name
    
    def getRealFilename(self):
        '''
        @return: returns a string with the full path to the file the string was loaded from
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        cdef hstr hl_name = self._pointer.getRealFilename()
        name = Hstr_to_Py(hl_name)
        return name
        
    def getDuration(self):
        '''
        @return: float duration of the sound in seconds. it is a floating point number to acound for fractions of a second
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        cdef float duration = self._pointer.getDuration()
        return duration
        
    def getSize(self):
        '''
        @return: int the size of the sound data in bits not bytes
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        cdef int size = self._pointer.getSize()
        return size
        
    def getTimePosition(self):
        '''
        @return: float the time position in seconds
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        cdef float size = self._pointer.getTimePosition()
        return size
        
    def getSamplePosition(self):
        '''
        @return: unsigned int the position in the buffer
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        cdef unsigned int size = self._pointer.getSamplePosition()
        return size
        
    def isPlaying(self):
        '''
        @return: bool True of the sound is playing
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._pointer.isPlaying()
        
    def isPaused(self):
        '''
        @return: bool True if the sound is paused
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._pointer.isPaused()
        
    def isFading(self):
        '''
        @return: bool True if the sound is fading in or out
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._pointer.isFading()
        
    def isFadingIn(self):
        '''
        @return: bool True if the sound is fading in
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._pointer.isFadingIn()
    
    def isFadingOut(self):
        '''
        @return: bool True if teh sound is fading out
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._pointer.isFadingOut()
        
    def isLooping(self):
        '''
        @return: bool True of the sound is looping
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._pointer.isLooping()
        
    def play(self, float fadeTime = 0.0, bool looping = False):
        '''
        start the sound playing at it's current offset, the offset starts at 0.0 when teh sound is first loaded
        
        @param fadeTime: float the time in seconds for the sound to fade in (0.0 by default)
        @param looping: bool should the sound loop (False by default)
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        self._pointer.play(fadeTime, looping)
    
    def stop(self, float fadeTime = 0.0):
        '''
        stop the sound playing and rest set it's offset to 0.0
        
        @param fadeTime: float the time in seconds for the sound to fade out (0.0 by default)
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        self._pointer.stop(fadeTime)
        
    def pause(self, float fadeTime = 0.0):
        '''
        stop the sound playing keeping the current offset of the sound
        
        @param fadeTime: float the time in seconds for the sound to fade out (0.0 by default)
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        self._pointer.pause(fadeTime)
 
 
class PySound(object):
    '''
    a interface for the wrapper of the xal::Sound class
    '''
    
    CATEGORY_STR = "default" 
    _wrapper = None
    destroyed = False
    
    def __init__(self, filename):
        '''
        this creates a sound object from a file name
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        path = os.path.split(filename)[0]
        cdef hstr file_str = Py_to_Hstr(filename)
        cdef hstr path_str = Py_to_Hstr(path)
        cdef hstr category = Py_to_Hstr(self.CATEGORY_STR)
        cdef XAL.Sound* sound 
        sound = XAL.mgr.createSound(file_str, category, path_str)
        if sound == NULL:
            raise RuntimeError("XAL Failed to load file %s" % filename)
        cdef SoundWrapper wrapper = SoundWrapper.__new__(SoundWrapper)
        wrapper._pointer = sound
        wrapper.destroyed = False
        self._wrapper = wrapper
        
    def _destroy(self):
        if self.isXALInitialized() and not self.destroyed:
            self._wrapper._destroy()
            self.destroyed = True
            
    def __del__(self):
        if self.isXALInitialized():
            self._destroy()
        del self._wrapper
        
    def isXALInitialized(self):
        '''
        returns true if the C++ side of the interface to XAL exists
        '''
        if XAL.mgr != NULL:
            return True
        else:
            return False
        
    def getName(self):
        '''
        @return: returns the string name of the sound. it is normal the full path of teh sound file with out the file extention
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._wrapper.getName()
        
    def getFilename(self):
        '''
        @return: returns a string containing the file name the sound was loaded from
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._wrapper.getFilename()
    
    def getRealFilename(self):
        '''
        @return: returns a string with the full path to the file the string was loaded from
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._wrapper.getRealFilename()
        
    def getSize(self):
        '''
        @return: int the size of the sound data in bits not bytes
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._wrapper.getSize()
        
    def getChannels(self):
        '''
        @return: int number of channels the sound has. 1 for mono or 2 for stereo 
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._wrapper.getChannels()
        
    def getSamplingRate(self):
        '''
        @return: int the sampeling rate for the sound in samples per second
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._wrapper.getSamplingRate()
        
    def getBitsPerSample(self):
        '''
        @return: int the bits per sample of data in the sound. usualy 8, 16, or 24, possibly 32 not sure
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._wrapper.getBitsPerSample()
    
    def getDuration(self):
        '''
        @return: float duration of the sound in seconds. it is a floating point number to acound for fractions of a second
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._wrapper.getDuration()
    
    def getFormat(self):
        '''
        @return: int the intrnal designation of the sound format. coresponds to a file type but as of now there is no way to tell for certin which is which 
            as the nubers will change depending on what formats are currently suported by XAL
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._wrapper.getFormat()
        
    def isStreamed(self):
        '''
        @return: bool is the sound being streamed from it's file to the player? or is it comleatly loaded into memory. 
            should always return false in PyXAL as PyXAL uses full decoding mode
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._wrapper.isStreamed()
        
    def readPcmData(self):
        '''
        read the raw data of the sound and return it the format of said data can be determined from the size, chanels, bits per sample and sampleling rate of the sound
        @return: a 2 tuple of (number of bits read, string of bytes read)
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._wrapper.readPcmData()       
        
class PyPlayer(object):
    '''
    a interface for the C++ wrapper
    '''
    
    _wrapper = None
    _sound = None
    destroyed = False
    
    def __init__(self, sound):
        '''
        a PyPlayer object created by bassing a PySound to the __init__ method
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if not isinstance(sound, PySound):
            raise TypeError("Expected argument 1 to be of type PySound got %s" % type(sound))
        sound_name = sound.getName()
        cdef hstr hl_name = Py_to_Hstr(sound_name)
        cdef XAL.Player* player 
        player = XAL.mgr.createPlayer(hl_name)
        if player == NULL:
            raise RuntimeError("XAL Failed to create a player for %s" % sound_name)
        cdef PlayerWrapper wrapper = PlayerWrapper.__new__(PlayerWrapper)
        wrapper._pointer = player
        wrapper.destroyed = False
        self._wrapper = wrapper
        self._sound = sound
              
    def _destroy(self):
        if self.isXALInitialized() and not self.destroyed:
            self._wrapper._destroy()
            self.destroyed = True
        
    def __del__(self):
        global Mgr
        if not self.destroyed:
            if Mgr is not None:
                if hasattr(Mgr, "_players"):
                    if Mgr._players.has_key(self.getName()):
                        if self in Mgr._player[self.getName()]:
                            Mgr.players[self.getName()].remove(self)
            if self.isXALInitialized():
                self._destroy()
        del self._wrapper
        del self._sound
             
        
    def isXALInitialized(self):
        '''
        returns true if the C++ side of the interface to XAL exists
        '''
        if XAL.mgr != NULL:
            return True
        else:
            return False
        
    def getGain(self):
        '''
        @return: float the current gain of the player (also knows as volume)
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._wrapper.getGain()
        
    def setGain(self, float value):
        '''
        set the gain of the player (also knows as volume)
        @param value: float the value of the volume to set 1.0 is normal 2.0 is twice as loud 0.5 is half volume ect.
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        self._wrapper.setGain(value)
        
    def getPitch(self):
        '''
        @return: float the current pitch of the player
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._wrapper.getPitch()
        
    def setPitch(self, float value):
        '''
        set the current pitch of the player
        @param value: float the value of the pitch to set to set 1.0 is normal 2.0 is a 200% shift 0.5 is a 50% shift
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        self._wrapper.setPitch(value)
    
    def getSound(self):
        '''
        return a PySound class wrapper for the sound object of the player
        '''
        return self._sound
        
    def getName(self):
        '''
        @return: returns the string name of the sound. it is normal the full path of teh sound file with out the file extention
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._wrapper.getName()
        
    def getFilename(self):
        '''
        @return: returns a string containing the file name the sound was loaded from
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._wrapper.getFilename()
    
    def getRealFilename(self):
        '''
        @return: returns a string with the full path to the file the string was loaded from
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._wrapper.getRealFilename()
        
    def getDuration(self):
        '''
        @return: float duration of the sound in seconds. it is a floating point number to acound for fractions of a second
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._wrapper.getDuration()
        
    def getSize(self):
        '''
        @return: int the size of the sound data in bits not bytes
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._wrapper.getSize()
        
    def getTimePosition(self):
        '''
        @return: float the time position in seconds
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._wrapper.getTimePosition()
        
    def getSamplePosition(self):
        '''
        @return: unsigned int the position in the buffer
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._wrapper.getSamplePosition()
        
    def isPlaying(self):
        '''
        @return: bool True of the sound is playing
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._wrapper.isPlaying()
        
    def isPaused(self):
        '''
        @return: bool True if the sound is paused
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._wrapper.isPaused()
        
    def isFading(self):
        '''
        @return: bool True if the sound is fading in or out
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._wrapper.isFading()
        
    def isFadingIn(self):
        '''
        @return: bool True if the sound is fading in
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._wrapper.isFadingIn()
    
    def isFadingOut(self):
        '''
        @return: bool True if teh sound is fading out
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._wrapper.isFadingOut()
        
    def isLooping(self):
        '''
        @return: bool True of the sound is looping
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        return self._wrapper.isLooping()
        
    def play(self, float fadeTime = 0.0, bool looping = False):
        '''
        start the sound playing at it's current offset, the offset starts at 0.0 when teh sound is first loaded
        
        @param fadeTime: float the time in seconds for the sound to fade in (0.0 by default)
        @param looping: bool should the sound loop (False by default)
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        self._wrapper.play(fadeTime, looping)
    
    def stop(self, float fadeTime = 0.0):
        '''
        stop the sound playing and rest set it's offset to 0.0
        
        @param fadeTime: float the time in seconds for the sound to fade out (0.0 by default)
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        self._wrapper.stop(fadeTime)
        
    def pause(self, float fadeTime = 0.0):
        '''
        stop the sound playing keeping the current offset of the sound
        
        @param fadeTime: float the time in seconds for the sound to fade out (0.0 by default)
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self.destroyed:
            raise RuntimeError("the C++ interface for this object has been destroyed")
        self._wrapper.pause(fadeTime)
    

cdef class XALManagerWrapper(object):
    '''
    a wrapper for the xal::mgr object which is a xal::AudioManager. in other words this is the main interface to XAL you SHOLD NOT create an instance of the class yourself.
    call PyXAL.Init to set up XAL. an instance of this class will be made avalable at PyXAL.Mgr
    '''

    cdef bint destroyed, inited
    cdef XAL.Category *_category
    cdef char* CATEGORY_STR

    def __init__(self, char* systemname, int backendId, bint threaded = False, float updateTime = 0.01, char* deviceName = ""):
        '''
        sets up the interface and initializes XAL you SHOULD NOT BE CREATING THIS CLASS YOUR SELF call PyXAL.Init and use the object created at PyXAL.Mgr
        if PyXAL.Mgr is None call PyXAL.Destroy and then PyXAL.Init to set up the interface again
        
        @param systemname: string name of the back end system to use
        @param backendId: int window handle of the calling aplication
        @param threaded: bool should the system use a threaded interface? (False by defaut)
        @param updateTime: float how offten should XAL update (0.01 by default)
        @param deviceName: string arbatrary device name ("" by default)
        '''
        global Mgr
        if Mgr is not None:
            raise RuntimeError("Only one XALManager interface allowed at a time, use the one at PyXAL.Mgr")
        self.CATEGORY_STR = "default"
        cdef hstr name = hstr(systemname)
        cdef hstr dname = hstr(deviceName)
        self._destroyXAL()
        XAL.init(name, <void*>backendId, threaded, updateTime, dname)
        self.inited = True
        self.destroyed = False
        self.SetupXAL()
        
    def __dealloc__(self):
        if XAL.mgr != NULL:
            fade = 0.0
            XAL.mgr.stopAll(fade)
            XAL.destroy()
                  
    def isXALInitialized(self):
        '''
        returns true if the C++ side of the interface to XAL exists
        '''
        if XAL.mgr != NULL:
            return True
        else:
            return False
            
    def SetupXAL(self):
        '''
        set up XAL and create the default sound catagory
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef hstr category = hstr(self.CATEGORY_STR)
        self._category = XAL.mgr.createCategory(category, FULL, DISK)
    
    def _destroyXAL(self):
        if XAL.mgr != NULL:
            fade = 0.0
            XAL.mgr.stopAll(fade)
            XAL.destroy()
    
class XALManager(object):
    '''
    a wrapper for the xal::mgr object which is a xal::AudioManager. in other words this is the main interface to XAL you SHOLD NOT create an instance of the class yourself.
    call PyXAL.Init to set up XAL. an instance of this class will be made avalable at PyXAL.Mgr
    '''

    destroyed = False
    inited = False
    
    CATEGORY_STR = "default"
    
    _players = {}
    _wrapper = None

    def __init__(self, int backendId, bint threaded = False):
        '''
        sets up the interface and initializes XAL you SHOULD NOT BE CREATING THIS CLASS YOUR SELF call PyXAL.Init and use the object created at PyXAL.Mgr
        if PyXAL.Mgr is None call PyXAL.Destroy and then PyXAL.Init to set up the interface again
        
        @param backendId: int window handle of the calling aplication
        @param threaded: bool should the system use a threaded interface? (False by defaut)
        '''
        global Mgr
        if Mgr is not None:
            raise RuntimeError("Only one XALManager interface allowed at a time, use the one at PyXAL.Mgr")
        cdef XALManagerWrapper wrapper = XALManagerWrapper(XAL_AS_DEFAULT, backendId, threaded)
        self._wrapper = wrapper
        self._players = {}
        
    def isXALInitialized(self):
        '''
        returns true if the C++ side of the interface to XAL exists
        '''
        if XAL.mgr != NULL:
            return True
        else:
            return False
    
    def __del__(self):
        '''
        make sure XAL is destroyed if the interface is destroyed
        '''
        del self._players
        del self._wrapper
            
    def clear(self):
        '''
        clear the XAL interface and reset it to be like it was freshly initialized all current sounds and players become invalid
        '''
        self._players = {}
        if self.isXALInitialized():
            fade = 0.0
            XAL.mgr.stopAll(fade)
            XAL.mgr.clear()
            
    def createSound(self, filename):
        '''
        create a sound object
        raises a runtime error if the sound fails to load so be sure to put this call in a try except block
        
        @param filename: string full path to a sound file to load
        @return: a PySound wraper to the sound object
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        pysound = PySound(filename)
        return pysound
        
    def createPlayer(self, sound):
        '''
        create a player from a sound object
        raises a runtime error if XAL fails to create a player so be sure to put this call in a try except block
        
        @param sound: a PySound wrapper to a sound object
        @return: a PyPlayer wraper to the player object
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if not isinstance(sound, PySound):
            raise TypeError("Expected argument 1 to be of type PySound got %s" % type(sound))
        sound_name = sound.getName()
        if not self._players.has_key(sound_name):
            self._players[sound_name] = []
        pyplayer = PyPlayer(sound)
        self._players[sound_name].append(pyplayer)
        return pyplayer
        
    def destroyPlayer(self, player):
        '''
        destroy a player object
        destroyes the C++ interface. the object is unusable after this
        
        @param pyplayer: the PyPlayer wrapper for the player to destory
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if not isinstance(player, PyPlayer):
            raise TypeError("Expected argument 1 to be of type PyPlayer got %s" % type(player))
        name = player.getName()
        if self._players.has_key(name):
            if player in self._players[name]:
                self._players[name].remove(player)
        player._destroy()
        
    def destroySound(self, sound):
        '''
        destroy a sound object
        destroyes the C++ interface. the object is unusable after this and so is any player that uses the sound
        
        @param pyplayer: the Pysound wrapper for the sound to destory
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if not isinstance(sound, PySound):
            raise TypeError("Expected argument 1 to be of type PySound got %s" % type(sound))
        sound._destroy()
        
    def findPlayer(self, str name):
        '''
        tries to find a player for the sound whos name is passed. it find the player useing the intrealy kept list of wrpaed player instances. returns the first player in the list
        
        @param name: string the name of the soudn to find a player for
        @return: a PyPlayer wraper to the player object or None if no player is found
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        if self._players.has_key(name):
            if len(self._players[name]) > 0:
                return self._players[name][0]
        return None
        
    def play(self, name, float fadeTime = 0.0, bool looping = False, float gain = 1.0):
        '''
        play the sound identified by the name passed (it must of alrady been created)
        
        @param name: string the name of the sound to play. it must alrady of been created
        @param fadeTime: float time is seconds for teh sound to fade in (0.0 by default)
        @param looping: bool should the sound loop? (False by default)
        @param gain: float the volume to play the sound at. 1.0 is normal 0.5 is half 2.0 is twice the volume ect. (1.0 by default)
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef hstr hl_name = Py_to_Hstr(name)
        XAL.mgr.play(hl_name, fadeTime, looping, gain)
        
    def stop(self, name, float fadeTime = 0.0):
        '''
        stop playing the sound identifed by the name passed
        
        @param name: string the name of the sound to stop
        @param fadeTime: float the time is second for the sound to fade out (0.0 by default)
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef hstr hl_name = Py_to_Hstr(name)
        XAL.mgr.stop(hl_name, fadeTime)
    
    def stopFirst(self, name, float fadeTime = 0.0):
        '''
        stop playing the first player of the sound identifed by the name passed
        
        @param name: string the name of the sound to stop
        @param fadeTime: float the time is second for the sound to fade out (0.0 by default)
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef hstr hl_name = Py_to_Hstr(name)
        XAL.mgr.stopFirst(hl_name, fadeTime)
    
    def stopAll(self, float fadeTime = 0.0):
        '''
        stop playing the all players of the sound identifed by the name passed
        
        @param name: string the name of the sound to stop
        @param fadeTime: float the time is second for the sound to fade out (0.0 by default)
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        XAL.mgr.stopAll(fadeTime)
    
    def isAnyPlaying(self, name):
        '''
        @param name: sting name of sound to check
        @return: bool True if there is a sound by this name playing
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef hstr hl_name = Py_to_Hstr(name)
        cdef bint result = XAL.mgr.isAnyPlaying(hl_name)
        return result
        
    def isAnyFading(self, name):
        '''
        @param name: sting name of sound to check
        @return: bool True if there is a sound by this name fading in or out
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef hstr hl_name = Py_to_Hstr(name)
        cdef bint result = XAL.mgr.isAnyFading(hl_name)
        return result
    
    def isAnyFadingIn(self, name):
        '''
        @param name: sting name of sound to check
        @return: bool True if there is a sound by this name fading in
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef hstr hl_name = Py_to_Hstr(name)
        cdef bint result = XAL.mgr.isAnyFadingIn(hl_name)
        return result
    
    def isAnyFadingOut(self, name):
        '''
        @param name: sting name of sound to check
        @return: bool True if there is a sound by this name fading out
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        cdef hstr hl_name = Py_to_Hstr(name)
        cdef bint result = XAL.mgr.isAnyFadingOut(hl_name)
        return result

    def suspendAudio(self):
        '''
        pause all sounds and players
        
        @param fadeTime: float the time is second for the sound to fade out (0.0 by default)
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        XAL.mgr.suspendAudio()
    
    def resumeAudio(self):
        '''
        resume all sounds and players
        
        @param fadeTime: float the time is second for the sound to fade in (0.0 by default)
        '''
        if not self.isXALInitialized():
            raise RuntimeError("XAL is not Initialized")
        XAL.mgr.resumeAudio()
        
def Init(int backendId, bint threaded = True):
    '''
    Setup XAL and create an XALManager interface at PyXAL.Mgr
    
    @param backendId: int window handel in the calling aplication
    @param threaded: bool should XAL use a threaded interface? (True by default)
    '''
    global Mgr
    if Mgr is None:
        if XAL.mgr != NULL:
            fade = 0.0
            XAL.mgr.stopAll(fade)
            XAL.destroy()
        Mgr = XALManager(backendId, threaded)
        
def Destroy():
    '''
    Destroy XAL and remove the interface at PyXAL setting it to None
    '''
    global Mgr
    if XAL.mgr != NULL:
        fade = 0.0
        XAL.mgr.stopAll(fade)
        XAL.destroy()
    Mgr = None