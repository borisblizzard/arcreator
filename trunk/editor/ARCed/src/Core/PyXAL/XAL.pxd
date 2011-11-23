from libcpp cimport bool
from hltypes cimport String, Array



cdef extern from "<xal/AudioManager.h>" namespace "xal":

    enum HandlingMode:
        FULL = 0
        LAZY = 1
        ON_DEMAND = 2
        STREAMED = 3

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

        Category* createCategory(String& name, HandlingMode loadMode, HandlingMode decodeMode)
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