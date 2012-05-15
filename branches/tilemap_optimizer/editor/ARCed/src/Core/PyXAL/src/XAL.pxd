from libcpp cimport bool
from hltypes cimport String, Array

cdef extern from "<xal/AudioManager.h>" namespace "xal":

    enum HandlingMode:
        FULL = 0
        LAZY = 1
        ON_DEMAND = 2
        STREAMED = 3
        
    enum Format:
        FLAC,
        M4A,
        MIDI,
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
        
        String getName() except +
        bool isEnabled() except +
        bool isSuspended() except +
        String getDeviceName() except +
        bool isThreaded() except +
        float getUpdateTime() except +
        float getGlobalGain() except +
        void setGlobalGain(float value) except +
        Array[Player*] getPlayers() except +

        void update() except +
        void update(float k) except +

        Category* createCategory(String& name, int loadMode, int decodeMode) except +
        Category* getCategoryByName(String& name) except +
        float getCategoryGain(String& category) except +
        void setCategoryGain(String& category, float gain) except +
        
        Sound* createSound(String& filename, String& categoryName, String& prefix) except +
        Sound* getSound(String& name) except +
        void destroySound(Sound* sound) except +
        void destroySoundsWithPrefix(String& prefix) except +
        Array[String] createSoundsFromPath(String& path, String& prefix) except +
        Array[String] createSoundsFromPath(String& path, String& category, String& prefix) except +

        Player* createPlayer(String& name) except +
        void destroyPlayer(Player* player) except +
        Player* findPlayer(String& name) except +

        void play(String& name, float fadeTime, bool looping, float gain) except +
        void stop(String& name, float fadeTime) except +
        void stopFirst(String& name, float fadeTime) except +
        void stopAll(float fadeTime) except +
        void stopCategory(String& name, float fadeTime) except +
        bool isAnyPlaying(String& name) except +
        bool isAnyFading(String& name) except +
        bool isAnyFadingIn(String& name) except +
        bool isAnyFadingOut(String& name) except +

        void suspendAudio() except +
        void resumeAudio() except +

        void queueMessage(String& message) except +

        void addAudioExtension(String& extension) except +
        String findAudioFile(String& _filename) except +
        
cdef extern from "<xal/Sound.h>" namespace "xal":

    cdef cppclass Sound:
    
        Sound(String& filename, Category* category, String& prefix)

        String getName() except +
        String getFilename() except +
        String getRealFilename() except +
        Category* getCategory() except +
        Buffer* getBuffer() except +

        int getSize() except +
        int getChannels() except +
        int getSamplingRate() except +
        int getBitsPerSample() except +
        float getDuration() except +
        Format getFormat() except +
        bool isStreamed() except +
        
        int readRawData(unsigned char** output) except +
        
cdef extern from "<xal/Category.h>" namespace "xal":

    cdef cppclass Category:
    
        Category(String& name, int loadMode, int decodeMode)
        
        String getName() except +
        float getGain() except +
        void setGain(float value) except +
        int getLoadMode() except +
        int getDecodeMode() except +
        bool isStreamed() except +
        
cdef extern from "<xal/Player.h>" namespace "xal":

    cdef cppclass Player:
    
        Player(Sound* sound, Buffer* buffer)
        
        float getGain() except +
        void setGain(float value) except +
        float getPitch() except +
        void setPitch(float value) except +
        float getOffset() except +
        Sound* getSound() except +
        String getName() except +
        String getFilename() except +
        String getRealFilename() except +
        float getDuration() except +
        int getSize() except +

        Category* getCategory() except +

        bool isPlaying() except +
        bool isPaused() except +
        bool isFading() except +
        bool isFadingIn() except +
        bool isFadingOut() except +
        bool isLooping() except +

        void play(float fadeTime, bool looping) except +
        void stop(float fadeTime) except +
        void pause(float fadeTime) except +

cdef extern from "<xal/Buffer.h>" namespace "xal":

    cdef cppclass Buffer:
    
        Buffer(String& filename, int loadMode, int decodeMode) except +
        
        String& getFilename() except +
        int getFileSize() except +
        unsigned char* getStream() except +
        Source* getSource() except +

        int getSize() except +
        int getChannels() except +
        int getSamplingRate() except +
        int getBitsPerSample() except +
        float getDuration() except +
        Format getFormat() except +
        bool isStreamed() except +
        bool setOffset(int value) except +

        void prepare() except +
        int load(bool looping, int size) except +
        void release() except +
        void free() except +
        void rewind() except +
        
cdef extern from "<xal/xal.h>" namespace "xal":
    DEF XAL_AS_ANDROID = "Android"
    DEF XAL_AS_DIRECTSOUND = "DirectSound"
    DEF XAL_AS_OPENAL = "OpenAL"
    DEF XAL_AS_SDL = "SDL"
    DEF XAL_AS_AVFOUNDATION = "AVFoundation"
    DEF XAL_AS_COREAUDIO = "CoreAudio"
    DEF XAL_AS_DISABLED = "Disabled"
    DEF XAL_AS_DEFAULT = ""
    
    void init(String& systemName, void* backendId, bool threaded, float updateTime, String& deviceName) except +
    void destroy() except +
    void setLogFunction(void (*function)(String&)) except +
    void log(String& message, String& prefix) except +
    bool hasAudioSystem(String& name) except +
    
    AudioManager* mgr