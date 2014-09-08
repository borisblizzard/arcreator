/// @file
/// @version 3.2
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://opensource.org/licenses/BSD-3-Clause
/// 
/// @section DESCRIPTION
/// 
/// Provides an interface for the audio manager.

#ifndef XAL_AUDIO_MANAGER_H
#define XAL_AUDIO_MANAGER_H

#include <hltypes/harray.h>
#include <hltypes/hltypesUtil.h>
#include <hltypes/hmap.h>
#include <hltypes/hmutex.h>
#include <hltypes/hstring.h>
#include <hltypes/hthread.h>

#include "xalExport.h"

#define STREAM_BUFFER_COUNT 8 // greater or equal to 2
#define STREAM_BUFFER_SIZE 32768 // equal to any power of 2
#define STREAM_BUFFER (STREAM_BUFFER_COUNT * STREAM_BUFFER_SIZE)

namespace xal
{
	enum Format
	{
		FLAC,
		M4A,
		OGG,
		SPX, // not supported yet
		WAV,
		UNKNOWN
	};

	enum BufferMode
	{
		/// @brief Buffers data upon player creation, keeps results in memory.
		FULL = 0,
		/// @brief Buffers when first need arises, keeps results in memory.
		LAZY = 1,
		/// @brief Buffers when first need arises, clears memory after a timeout.
		MANAGED = 2,
		/// @brief Buffers when first need arises, clears memory after usage.
		ON_DEMAND = 3,
		/// @brief Buffers in streamed mode.
		STREAMED = 4
	};

	enum SourceMode
	{
		/// @brief Leaves data on permanent storage device.
		DISK = 0,
		/// @brief Copies data to RAM buffer and accesses it from there.
		RAM = 1
	};

	class Buffer;
	class Category;
	class Player;
	class Sound;
	class Source;

	/// @brief Provides generic functionality regarding audio management.
	class xalExport AudioManager
	{
	public:
		friend class Buffer;
		friend class Category;
		friend class Player;
		friend class Sound;

		/// @brief Destructor.
		virtual ~AudioManager();
		/// @brief Initializes implementation-specific functionality.
		virtual void init();
		/// @brief Uninitializes implementation-specific functionality.
		void clear();
		
		inline void* getBackendId() { return this->backendId; }
		HL_DEFINE_GET(hstr, name, Name);
		HL_DEFINE_GET(int, samplingRate, SamplingRate);
		HL_DEFINE_GET(int, channels, Channels);
		HL_DEFINE_GET(int, bitsPerSample, BitsPerSample);
		HL_DEFINE_IS(enabled, Enabled);
		HL_DEFINE_IS(suspended, Suspended);
		HL_DEFINE_GETSET(float, idlePlayerUnloadTime, IdlePlayerUnloadTime);
		HL_DEFINE_GET(hstr, deviceName, DeviceName);
		inline bool isThreaded() { return (this->thread != NULL); }
		HL_DEFINE_GET(float, updateTime, UpdateTime);
		HL_DEFINE_GET(float, globalGain, GlobalGain);
		void setGlobalGain(float value);
		harray<Player*> getPlayers();

		/// @brief Threaded update call.
		/// @param[in] thread The Thread instance calling.
		/// @note This is used for threaded update only and should never be called from the outside.
		static void update(hthread* thread);
		/// @brief Updates all audio processing.
		/// @param[in] timeDelta Time since the call of this method in seconds.
		/// @note timeDelta is usually the time since the last frame in games. You don't have to call this if threaded update is enabled.
		void update(float timeDelta);

		/// @brief Creates a new audio Category.
		/// @param[in] name Name of the Category.
		/// @param[in] bufferMode How to handle the intermediate Buffer of the Sound in this category.
		/// @param[in] sourceMode How to handle the Source of the Sound in this category.
		/// @return The newly created Category.
		/// @note If the Category exists already, this call will have no effect.
		Category* createCategory(chstr name, BufferMode bufferMode, SourceMode sourceMode);
		/// @brief Gets the audio Category with the given name.
		/// @param[in] name Name of the Category.
		/// @return The Category with the given name.
		Category* getCategory(chstr name);
		/// @brief Checks whether a Category exists.
		/// @param[in] name Name of the Category.
		/// @return True if the Category exists.
		bool hasCategory(chstr name);
		
		/// @brief Creates a new Sound within a Category.
		/// @param[in] filename Filename of the Sound.
		/// @param[in] categoryName Name of the Category where to register the new Sound.
		/// @param[in] prefix Used to differentiate between Sounds that have the same filename (e.g. by using a directory path as prefix).
		/// @return The newly created Sound.
		Sound* createSound(chstr filename, chstr categoryName, chstr prefix = "");
		/// @brief Gets the Sound with the given name.
		/// @param[in] name Name of the Sound.
		/// @return The Sound with the given name.
		Sound* getSound(chstr name);
		/// @brief Destroys a Sound.
		/// @param[in] name Name of the Sound.
		void destroySound(Sound* sound);
		/// @brief Destroys all Sounds that have the given prefix in their name.
		/// @param[in] prefix Prefix for Sound names to destroy.
		void destroySoundsWithPrefix(chstr prefix);
		/// @brief Creates Sounds from a path and creates a Category for each directory.
		/// @param[in] path Path where the directories are located.
		/// @param[in] prefix Used to differentiate between Sounds that have the same filename (e.g. by using a directory path as prefix).
		/// @return A list of all Sound names that were created.
		/// @note The base-name of each directory located in path is used as Category name and all Sounds within are assigned to that Category.
		harray<hstr> createSoundsFromPath(chstr path, chstr prefix = "");
		/// @brief Creates Sounds from a path and assigns them to a Category.
		/// @param[in] path Path where the audio files are located.
		/// @param[in] categoryName Name for the Category.
		/// @param[in] prefix Used to differentiate between Sounds that have the same filename (e.g. by using a directory path as prefix).
		/// @return A list of all Sound names that were created.
		/// @note If the Category does not exist, it will be created.
		harray<hstr> createSoundsFromPath(chstr path, chstr categoryName, chstr prefix);

		/// @brief Creates a Player for a Sound.
		/// @param[in] soundName Name of the Sound for which the player will be used.
		/// @return The newly created player.
		Player* createPlayer(chstr soundName);
		/// @brief Destroys a Player.
		/// @param[in] player The player to destroy.
		void destroyPlayer(Player* player);
		/// @brief Checks whether a Sound exists.
		/// @param[in] name Name of the Sound.
		/// @brief True if a Sound exists.
		bool hasSound(chstr name);

		/// @brief Plays a Sound in a fire-and-forget fashion.
		/// @param[in] soundName Name of the Sound.
		/// @param[in] fadeTime Time how long to fade in the Sound.
		/// @param[in] looping Whether the Sound should be looped.
		/// @param[in] gain The gain of the Sound.
		/// @note If the audio manager is suspended, this does nothing.
		void play(chstr soundName, float fadeTime = 0.0f, bool looping = false, float gain = 1.0f);
		/// @brief Stops all Sound instances that were played in a fire-and-forget fashion.
		/// @param[in] soundName Name of the Sound.
		/// @param[in] fadeTime Time how long to fade out the Sounds.
		void stop(chstr soundName, float fadeTime = 0.0f);
		/// @brief Stops only the first Sound instance that was played in a fire-and-forget fashion.
		/// @param[in] soundName Name of the Sound.
		/// @param[in] fadeTime Time how long to fade out the Sound.
		void stopFirst(chstr soundName, float fadeTime = 0.0f);
		/// @brief Stops all Sounds that are currently playing.
		/// @param[in] fadeTime Time how long to fade out the Sounds.
		/// @note This method also stops manually created Players.
		void stopAll(float fadeTime = 0.0f);
		/// @brief Stops all Sounds that belong to a certain Category.
		/// @param[in] categoryName Name of the Category.
		/// @param[in] fadeTime Time how long to fade out the Sounds.
		/// @note This method also stops manually created Players.
		void stopCategory(chstr categoryName, float fadeTime = 0.0f);
		/// @brief Checks if a Sound is playing.
		/// @param[in] soundName Name of the Sound.
		/// @return True if there is any Sound playing.
		/// @note This method only checks managed Sounds that were played in a fire-and-forget fashion.
		bool isAnyPlaying(chstr soundName);
		/// @brief Checks if a Sound is fading.
		/// @param[in] soundName Name of the Sound.
		/// @return True if there is any Sound fading.
		/// @note This method only checks managed Sounds that were played in a fire-and-forget fashion.
		bool isAnyFading(chstr soundName);
		/// @brief Checks if a Sound is fading in.
		/// @param[in] soundName Name of the Sound.
		/// @return True if there is any Sound fading in.
		/// @note This method only checks managed Sounds that were played in a fire-and-forget fashion.
		bool isAnyFadingIn(chstr soundName);
		/// @brief Checks if a Sound is fading out.
		/// @param[in] soundName Name of the Sound.
		/// @return True if there is any Sound fading out.
		/// @note This method only checks managed Sounds that were played in a fire-and-forget fashion.
		bool isAnyFadingOut(chstr soundName);

		/// @brief Frees up unused memory.
		/// @note This can be useful if the operating system is low on memory.
		void clearMemory();

		/// @brief Suspends the entire audio processing.
		/// @note This is useful when the app goes out of focus. It does nothing if the system has already been suspended.
		void suspendAudio();
		/// @brief Resumes the previously suspended audio processing.
		/// @note This is useful when the app goes out of focus. It does nothing if the system hasn't been suspended previously.
		void resumeAudio();

		/// @brief Adds a custom audio file extension.
		/// @param[in] extension File extension to add.
		void addAudioExtension(chstr extension);
		/// @brief Finds an actual audio filename.
		/// @param[in] filename Reference filename for the audio file.
		/// @return The actual audio filename.
		virtual hstr findAudioFile(chstr filename);

	protected:
		/// @brief Constructor.
		/// @param[in] backendId Special ID needed by some audio systems.
		/// @param[in] threaded Whether update should be handled in a separate thread.
		/// @param[in] updateTime How much time should pass between updates when "threaded" is enabled.
		/// @param[in] deviceName Required by some audio systems.
		/// @note On Win32, backendId is the window handle. On Android, backendId is a pointer to the JavaVM.
		AudioManager(void* backendId, bool threaded = false, float updateTime = 0.01f, chstr deviceName = "");

		/// @brief Name of the audio system.
		hstr name;
		/// @brief Back-end ID.
		void* backendId;
		/// @brief Sampling rate of the audio device.
		int samplingRate;
		/// @brief Number of channels of the audio device.
		int channels;
		/// @brief Bites per sample of the audio device.
		int bitsPerSample;
		/// @brief Whether any audio system is present.
		bool enabled;
		/// @brief Whether the audio system is suspended temporarily.
		/// @note Usually should be true when the app is suspended or out of focus.
		bool suspended;
		/// @brief Whether the audio system uses threaded updating.
		bool threaded;
		/// @brief How long a Player needs to remain inactive for its data to be cleared.
		float idlePlayerUnloadTime;
		/// @brief Device name which is required for some audio systems.
		hstr deviceName;
		/// @brief How much time should pass between updates when "threaded" is enabled.
		float updateTime;
		/// @brief Global gain.
		float globalGain;
		/// @brief List of registered audio categories.
		hmap<hstr, Category*> categories;
		/// @brief Currently existing Player instances.
		harray<Player*> players;
		/// @brief List of Player instances that are managed solely by the audio system.
		/// @note Managed players are usually created when a Sound is played through a call to the AudioManager instance and destroyed when they aren't needed anymore (using a fire-and-forget mechanism).
		harray<Player*> managedPlayers;
		/// @brief List of Player instances that need to resume once the audio system exits suspension.
		harray<Player*> suspendedPlayers;
		/// @brief List of loaded Sounds.
		hmap<hstr, Sound*> sounds;
		/// @brief List Buffer instances.
		harray<Buffer*> buffers;
		/// @brief List of file extensions supported.
		harray<hstr> extensions;
		/// @brief Thread instance handling the threaded update.
		hthread* thread;
		/// @brief Whether the threaded update is running.
		bool threadRunning;
		/// @brief Mutex for data access when threaded updating is used.
		hmutex mutex; // a mute ex would be nice

		/// @note This method is not thread-safe and is for internal usage only.
		void _setGlobalGain(float value);
		/// @note This method is not thread-safe and is for internal usage only.
		harray<Player*> _getPlayers();

		/// @note Starts the thread for threaded update.
		void _startThreading();
		/// @note This method is not thread-safe and is for internal usage only.
		void _clear();
		
		/// @note This method is not thread-safe and is for internal usage only.
		virtual void _update(float timeDelta);
		/// @brief Locks the mutex for thread synchronization.
		virtual void _lock();
		/// @brief Unlocks the mutex for thread synchronization.
		virtual void _unlock();

		/// @note This method is not thread-safe and is for internal usage only.
		Category* _createCategory(chstr name, BufferMode bufferMode, SourceMode sourceMode);
		/// @note This method is not thread-safe and is for internal usage only.
		Category* _getCategory(chstr name);

		/// @note This method is not thread-safe and is for internal usage only.
		virtual Sound* _createSound(chstr filename, chstr categoryName, chstr prefix);
		/// @note This method is not thread-safe and is for internal usage only.
		Sound* _getSound(chstr name);
		/// @note This method is not thread-safe and is for internal usage only.
		void _destroySound(Sound* sound);
		/// @note This method is not thread-safe and is for internal usage only.
		void _destroySoundsWithPrefix(chstr prefix);
		/// @note This method is not thread-safe and is for internal usage only.
		harray<hstr> _createSoundsFromPath(chstr path, chstr prefix);
		/// @note This method is not thread-safe and is for internal usage only.
		harray<hstr> _createSoundsFromPath(chstr path, chstr category, chstr prefix);

		/// @note This method is not thread-safe and is for internal usage only.
		Player* _createPlayer(chstr name);
		/// @note This method is not thread-safe and is for internal usage only.
		void _destroyPlayer(Player* player);

		/// @brief Creates an internally managed Player.
		/// @param[in] soundName Name of the Sound.
		/// @return The newly created Player.
		Player* _createManagedPlayer(chstr name);
		/// @brief Destroys an internally managed Player.
		/// @param[in] player The Player to destroy.
		void _destroyManagedPlayer(Player* player);

		/// @note This method is not thread-safe and is for internal usage only.
		Buffer* _createBuffer(Sound* sound);
		/// @note This method is not thread-safe and is for internal usage only.
		void _destroyBuffer(Buffer* buffer);

		/// @note This method is not thread-safe and is for internal usage only.
		virtual Player* _createSystemPlayer(Sound* sound) = 0;
		/// @note This method is not thread-safe and is for internal usage only.
		virtual Source* _createSource(chstr filename, Category* category, Format format);

		/// @note This method is not thread-safe and is for internal usage only.
		void _play(chstr soundName, float fadeTime, bool looping, float gain);
		/// @note This method is not thread-safe and is for internal usage only.
		void _stop(chstr soundName, float fadeTime);
		/// @note This method is not thread-safe and is for internal usage only.
		void _stopFirst(chstr soundName, float fadeTime);
		/// @note This method is not thread-safe and is for internal usage only.
		void _stopAll(float fadeTime);
		/// @note This method is not thread-safe and is for internal usage only.
		void _stopCategory(chstr categoryName, float fadeTime);
		/// @note This method is not thread-safe and is for internal usage only.
		bool _isAnyPlaying(chstr soundName);
		/// @note This method is not thread-safe and is for internal usage only.
		bool _isAnyFading(chstr soundName);
		/// @note This method is not thread-safe and is for internal usage only.
		bool _isAnyFadingIn(chstr soundName);
		/// @note This method is not thread-safe and is for internal usage only.
		bool _isAnyFadingOut(chstr soundName);

		/// @note This method is not thread-safe and is for internal usage only.
		void _clearMemory();

		/// @note This method is not thread-safe and is for internal usage only.
		virtual void _suspendAudio();
		/// @note This method is not thread-safe and is for internal usage only.
		virtual void _resumeAudio();

		/// @brief Depending on the audio manager implementation, this method may convert audio data to the appropriate format (bit rate, channel number, sampling rate).
		/// @param[in] buffer Buffer object that describes the data.
		/// @param[in,out] stream The data stream buffer.
		/// @param[in,out] streamSize The size of the stream itself.
		/// @param[in] dataSize The size of the data within the stream.
		/// @return dataSize if no conversion was done or a positive integer for the size of the new data.
		virtual int _convertStream(Buffer* buffer, unsigned char** stream, int *streamSize, int dataSize) { return dataSize; }

		/// @brief Special additional processing for suspension, required for some implementations.
		/// @note This method is not thread-safe and is for internal usage only.
		inline virtual void _suspendSystem() { }
		/// @brief Special additional processing for suspension, required for some implementations.
		/// @note This method is not thread-safe and is for internal usage only.
		inline virtual void _resumeSystem() { }

	};
	
	xalExport extern xal::AudioManager* mgr;

}

#endif
