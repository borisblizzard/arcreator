/// @file
/// @author  Kresimir Spes
/// @author  Boris Mikic
/// @author  Ivan Vucica
/// @version 2.61
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://www.opensource.org/licenses/bsd-license.php
/// 
/// @section DESCRIPTION
/// 
/// Provides an interface for audio managers.

#ifndef XAL_AUDIO_MANAGER_H
#define XAL_AUDIO_MANAGER_H

#include <hltypes/harray.h>
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
		SPX,
		WAV,
		UNKNOWN
	};

	enum BufferMode
	{
		/// @brief Buffers data upon player creation, keeps results in memory.
		FULL = 0,
		/// @brief Buffers data upon player creation, clears memory after a timeout.
		MANAGED = 1,
		/// @brief Buffers when first need arises, keeps results in memory.
		LAZY = 2,
		/// @brief Buffers when first need arises, clears memory after a timeout.
		LAZY_MANAGED = 3,
		/// @brief Buffers when first need arises, clears memory after usage.
		ON_DEMAND = 4,
		/// @brief Buffers in streamed mode.
		STREAMED = 5
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

	class xalExport AudioManager
	{
	public:
		friend class Buffer;
		friend class Player;
		friend class Sound;

		virtual ~AudioManager();
		virtual void init();
		void clear();
		
		void* getBackendId() { return this->backendId; }
		hstr getName() { return this->name; }
		int getSamplingRate() { return this->samplingRate; }
		int getChannels() { return this->channels; }
		int getBitsPerSample() { return this->bitsPerSample; }
		bool isEnabled() { return this->enabled; }
		bool isSuspended() { return this->suspended; }
		float getIdlePlayerUnloadTime() { return this->idlePlayerUnloadTime; }
		void setIdlePlayerUnloadTime(float value) { this->idlePlayerUnloadTime = value; }
		hstr getDeviceName() { return this->deviceName; }
		bool isThreaded() { return (this->thread != NULL); }
		float getUpdateTime() { return this->updateTime; }
		float getGlobalGain() { return this->gain; }
		void setGlobalGain(float value);
		harray<Player*> getPlayers();

		static void update(); // used for threaded update only
		void update(float k);

		Category* createCategory(chstr name, BufferMode bufferMode, SourceMode sourceMode);
		Category* getCategoryByName(chstr name);
		float getCategoryGain(chstr category);
		void setCategoryGain(chstr category, float gain);
		
		Sound* createSound(chstr filename, chstr categoryName, chstr prefix = "");
		Sound* getSound(chstr name);
		void destroySound(Sound* sound);
		void destroySoundsWithPrefix(chstr prefix);
		harray<hstr> createSoundsFromPath(chstr path, chstr prefix = "");
		harray<hstr> createSoundsFromPath(chstr path, chstr category, chstr prefix);

		Player* createPlayer(chstr name);
		void destroyPlayer(Player* player);
		Player* findPlayer(chstr name);
		bool hasSound(chstr name);

		void play(chstr name, float fadeTime = 0.0f, bool looping = false, float gain = 1.0f);
		void stop(chstr name, float fadeTime = 0.0f);
		void stopFirst(chstr name, float fadeTime = 0.0f);
		void stopAll(float fadeTime = 0.0f);
		void stopCategory(chstr name, float fadeTime = 0.0f);
		bool isAnyPlaying(chstr name);
		bool isAnyFading(chstr name);
		bool isAnyFadingIn(chstr name);
		bool isAnyFadingOut(chstr name);

		void clearMemory();

		void suspendAudio();
		void resumeAudio();

		void queueMessage(chstr message);

		void addAudioExtension(chstr extension);
		hstr findAudioFile(chstr _filename);

	protected:
		// protected constructor to ensure that this class has to be subclassed
		AudioManager(chstr systemName, void* backendId, bool threaded = false, float updateTime = 0.01f, chstr deviceName = "");

		void* backendId;
		hstr name;
		int samplingRate;
		int channels;
		int bitsPerSample;
		bool enabled;
		bool suspended;
		bool threaded;
		float idlePlayerUnloadTime;
		hstr deviceName;
		float updateTime;
		float gain;
		hmap<hstr, Category*> categories;
		harray<Player*> players;
		harray<Player*> managedPlayers;
		harray<Player*> suspendedPlayers;
		hmap<hstr, Sound*> sounds;
		harray<hstr> extensions;
		hthread* thread;
		bool threadRunning;
		hmutex mutex; // a mute ex would be nice

		void _setGlobalGain(float value);
		harray<Player*> _getPlayers();

		void _startThreading();
		void _clear();
		
		void _update(float k);
		virtual void _lock();
		virtual void _unlock();

		Category* _createCategory(chstr name, BufferMode bufferMode, SourceMode sourceMode);
		Category* _getCategoryByName(chstr name);
		float _getCategoryGain(chstr category);
		void _setCategoryGain(chstr category, float gain);

		Sound* _createSound(chstr filename, chstr categoryName, chstr prefix);
		Sound* _getSound(chstr name);
		void _destroySound(Sound* sound);
		void _destroySoundsWithPrefix(chstr prefix);
		harray<hstr> _createSoundsFromPath(chstr path, chstr prefix);
		harray<hstr> _createSoundsFromPath(chstr path, chstr category, chstr prefix);

		Player* _createPlayer(chstr name);
		void _destroyPlayer(Player* player);
		Player* _findPlayer(chstr name);
		Player* _createManagedPlayer(chstr name);
		void _destroyManagedPlayer(Player* player);

		virtual Player* _createSystemPlayer(Sound* sound, Buffer* buffer);
		virtual Source* _createSource(chstr filename, Category* category, Format format);

		void _play(chstr name, float fadeTime, bool looping, float gain);
		void _stop(chstr name, float fadeTime);
		void _stopFirst(chstr name, float fadeTime);
		void _stopAll(float fadeTime);
		void _stopCategory(chstr name, float fadeTime);
		bool _isAnyPlaying(chstr name);
		bool _isAnyFading(chstr name);
		bool _isAnyFadingIn(chstr name);
		bool _isAnyFadingOut(chstr name);

		void _clearMemory();

		void _suspendAudio();
		void _resumeAudio();

		virtual void _convertStream(Buffer* buffer, unsigned char** stream, int *streamSize) { }

		virtual void _suspendSystem() { }
		virtual void _resumeSystem() { }

	private:
		harray<hstr> _queuedMessages;

		void _flushQueuedMessages();

	};
	
	xalExport extern xal::AudioManager* mgr;

}

#endif
