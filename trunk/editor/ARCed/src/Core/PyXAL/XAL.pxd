from libcpp cimport bool
from hltypes cimport String, Array

cdef extern from "<xal/AudioManager.h>" namespace "xal":

    enum HandlingMode:
        FULL = 0
        LAZY = 1
        ON_DEMAND = 2
        STREAMED = 3
        
    enum Format:
        M4A,
        MP3,
        OGG,
        SPX,
        WAV,
        UNKNOWN

    cdef cppclass Player
    cdef cppclass Category
    cdef cppclass Buffer
    cdef cppclass ExternalComponent
    cdef cppclass Sound
    cdef cppclass Source

    cdef cppclass AudioManager:
        AudioManager(String& systemName, int backendId, bool threaded, float updateTime, String& deviceName)
        void init()
        void clear()
        
        String getName()
        bool isEnabled()
        bool isPaused()
        String getDeviceName()
        float getUpdateTime()
        float getGlobalGain()
        void setGlobalGain(float value)
        Array[Player*] getPlayers()

        void update()
        void update(float k)

        Category* createCategory(String& name, int loadMode, int decodeMode)
        Category* getCategoryByName(String& name)
        float getCategoryGain(String& category)
        void setCategoryGain(String& category, float gain)
        
        Sound* createSound(String& filename, String& categoryName, String& prefix)
        Sound* getSound(String& name)
        void destroySound(Sound* sound)
        void destroySoundsWithPrefix(String& prefix)
        Array[String] createSoundsFromPath(String& path, String& prefix)
        Array[String] createSoundsFromPath(String& path, String& category, String& prefix)

        Player* createPlayer(String& name)
        void destroyPlayer(Player* player)
        Player* findPlayer(String& name)

        void play(String& name, float fadeTime, bool looping, float gain)
        void stop(String& name, float fadeTime)
        void stopFirst(String& name, float fadeTime)
        void stopAll(float fadeTime)
        void pauseAll(float fadeTime)
        void resumeAll(float fadeTime)
        void stopCategory(String& name, float fadeTime)
        bool isAnyPlaying(String& name)
        bool isAnyFading(String& name)
        bool isAnyFadingIn(String& name)
        bool isAnyFadingOut(String& name)
        
cdef extern from "<xal/Sound.h>" namespace "xal":

    cdef cppclass Sound:
    
        Sound(String& filename, Category* category, String& prefix)

        String getName()
        String getFilename()
        String getRealFilename()
        Category* getCategory()
        Buffer* getBuffer()

        int getSize()
        int getChannels()
        int getSamplingRate()
        int getBitsPerSample()
        float getDuration()
        Format getFormat()
        bool isStreamed()
        
cdef extern from "<xal/Category.h>" namespace "xal":

    cdef cppclass Category:
    
        Category(String& name, int loadMode, int decodeMode)
        
        String getName()
        float getGain()
        void setGain(float value)
        int getLoadMode()
        int getDecodeMode()
        bool isStreamed()
        
cdef extern from "<xal/Player.h>" namespace "xal":

    cdef cppclass Player:
    
        Player(Sound* sound, Buffer* buffer)
        
        float getGain()
        void setGain(float value)
        float getOffset()
        Sound* getSound()
        String getName()
        String getFilename()
        String getRealFilename()
        float getDuration()
        int getSize()

        Category* getCategory()

        bool isPlaying()
        bool isPaused()
        bool isFading()
        bool isFadingIn()
        bool isFadingOut()
        bool isLooping()

        void play(float fadeTime, bool looping)
        void stop(float fadeTime)
        void pause(float fadeTime)

cdef extern from "<xal/Buffer.h>" namespace "xal":

    cdef cppclass Buffer:
    
        Buffer(String& filename, int loadMode, int decodeMode)
        
        String& getFilename()
        int getFileSize()
        unsigned char* getStream()
        Source* getSource()

        int getSize()
        int getChannels()
        int getSamplingRate()
        int getBitsPerSample()
        float getDuration()
        Format getFormat()
        bool isStreamed()
        bool setOffset(int value)

        void prepare()
        int load(bool looping, int size)
        void release()
        void free()
        void rewind()
        
cdef extern from "<xal/xal.h>" namespace "xal":
    DEF XAL_AS_DIRECTSOUND = "DirectSound"
    DEF XAL_AS_OPENAL = "OpenAL"
    DEF XAL_AS_SDL = "SDL"
    DEF XAL_AS_AVFOUNDATION = "AVFoundation"
    DEF XAL_AS_COREAUDIO = "CoreAudio"
    DEF XAL_AS_DISABLED = "Disabled"
    DEF XAL_AS_DEFAULT = ""
    
    void init(String& systemName, int backendId, bool threaded, float updateTime, String& deviceName)
    void destroy()
    void setLogFunction(void (*function)(String&))
    void log(String& message, String& prefix)
    bool hasAudioSystem(String& name)
    
    AudioManager* mgr