from libcpp cimport bool
from hltypes cimport String, Array

cdef extern from *:
    ctypedef char* const_char_ptr "const char*"
    ctypedef unsigned char* const_unsigned_char_ptr "const unsigned char*"
    ctypedef String& chstr "chstr"

cdef extern from "<xal/AudioManager.h>" namespace "xal":

    
        
    enum Format:
        FLAC,
        M4A,
        OGG,
        SPX,
        WAV,
        UNKNOWN
    
    enum BufferMode:
        FULL = 0
        MANAGED = 1
        LAZY = 2
        LAZY_MANAGED = 3
        ON_DEMAND = 4
        STREAMED = 5
        
    enum SourceMode:
        DISK = 0
        RAM = 1

    cdef cppclass Player
    cdef cppclass Category
    cdef cppclass Buffer
    cdef cppclass ExternalComponent
    cdef cppclass Sound
    cdef cppclass Source

    cdef cppclass AudioManager:
        AudioManager(chstr systemName, int backendId, bool threaded, float updateTime, chstr deviceName)
        void init()
        void clear()
        
        void* getBackendId() except +
        String getName() except +
        int getSamplingRate() except +
        int getChannels() except +
        int getBitsPerSample() except +
        bool isEnabled() except +
        float getIdlePlayerUnloadTime() except +
        void setIdlePlayerUnloadTime(float value) except +
        bool isSuspended() except +
        String getDeviceName() except +
        bool isThreaded() except +
        float getUpdateTime() except +
        float getGlobalGain() except +
        void setGlobalGain(float value) except +
        Array[Player*] getPlayers() except +

        void update() except +
        void update(float k) except +

        Category* createCategory(chstr name, BufferMode bufferMode, SourceMode sourceMode) except +
        Category* getCategoryByName(chstr name) except +
        float getCategoryGain(chstr category) except +
        void setCategoryGain(chstr category, float gain) except +
        
        Sound* createSound(chstr filename, chstr categoryName, chstr prefix) except +
        Sound* getSound(chstr name) except +
        void destroySound(Sound* sound) except +
        void destroySoundsWithPrefix(chstr prefix) except +
        Array[String] createSoundsFromPath(chstr path, chstr prefix) except +
        Array[String] createSoundsFromPath(chstr path, chstr category, chstr prefix) except +

        Player* createPlayer(chstr name) except +
        void destroyPlayer(Player* player) except +
        Player* findPlayer(chstr name) except +
        bool hasSound(chstr name) except +

        void play(chstr name, float fadeTime, bool looping, float gain) except +
        void stop(chstr name, float fadeTime) except +
        void stopFirst(chstr name, float fadeTime) except +
        void stopAll(float fadeTime) except +
        void stopCategory(chstr name, float fadeTime) except +
        bool isAnyPlaying(chstr name) except +
        bool isAnyFading(chstr name) except +
        bool isAnyFadingIn(chstr name) except +
        bool isAnyFadingOut(chstr name) except +
        
        void clearMemory() except +

        void suspendAudio() except +
        void resumeAudio() except +

        void queueMessage(chstr message) except +

        void addAudioExtension(chstr extension) except +
        String findAudioFile(chstr _filename) except +
        
cdef extern from "<xal/Sound.h>" namespace "xal":

    cdef cppclass Sound:
    
        Sound(chstr filename, Category* category, chstr prefix)

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
    
        Category(chstr name, int bufferMode, int sourceMode)
        
        String getName() except +
        float getGain() except +
        void setGain(float value) except +
        int getBufferMode() except +
        int getSourceMode() except +
        bool isStreamed() except +
        bool isMemoryManaged() except +
        
cdef extern from "<xal/Player.h>" namespace "xal":

    cdef cppclass Player:
    
        Player(Sound* sound, Buffer* buffer)
        
        float getGain() except +
        void setGain(float value) except +
        float getPitch() except +
        void setPitch(float value) except +
        Sound* getSound() except +
        String getName() except +
        String getFilename() except +
        String getRealFilename() except +
        float getDuration() except +
        int getSize() except +
        float getTimePosition() except +
        unsigned int getSamplePosition() except +
        

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
    
        Buffer(chstr filename, Category* category) except +
        
        chstr getFilename() except +
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
        void release(bool playerPaused) except +
        void free() except +
        void rewind() except +
        
        int convertToOutputSize(int size) except +
        int convertToInputSize(int size) except +
        
cdef extern from "<xal/xal.h>" namespace "xal":
    DEF XAL_AS_ANDROID = "Android"
    DEF XAL_AS_DIRECTSOUND = "DirectSound"
    DEF XAL_AS_OPENAL = "OpenAL"
    DEF XAL_AS_SDL = "SDL"
    DEF XAL_AS_AVFOUNDATION = "AVFoundation"
    DEF XAL_AS_COREAUDIO = "CoreAudio"
    DEF XAL_AS_DISABLED = "Disabled"
    DEF XAL_AS_DEFAULT = ""
    
    void init(chstr systemName, void* backendId, bool threaded, float updateTime, chstr deviceName) except +
    void destroy() except +
    void setLogFunction(void (*function)(chstr)) except +
    void log(chstr message, chstr prefix) except +
    bool hasAudioSystem(chstr name) except +
    
    AudioManager* mgr