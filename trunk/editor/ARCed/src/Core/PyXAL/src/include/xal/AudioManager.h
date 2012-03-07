/// @file
/// @author  Kresimir Spes
/// @author  Boris Mikic
/// @author  Ivan Vucica
/// @version 2.2
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
#ifdef HAVE_FLAC
		FLAC,
#endif
#ifdef HAVE_M4A
		M4A,
#endif
#ifdef HAVE_MIDI
		MIDI,
#endif
#ifdef HAVE_OGG
		OGG,
#endif
#ifdef HAVE_SPX
		SPX,
#endif
#ifdef HAVE_WAV
		WAV,
#endif
		UNKNOWN
	};

	enum HandlingMode
	{
		/// @brief Handles on Sound creation, keeps results in memory.
		FULL = 0,
		/// @brief Handles when first need arises, keeps results in memory.
		LAZY = 1,
		/// @brief Handles when first need arises, removes from memory when not needed anymore.
		ON_DEMAND = 2,
		/// @brief Handles streamed.
		STREAMED = 3
	};

	class Buffer;
	class Category;
	class ExternalComponent;
	class Player;
	class Sound;
	class Source;

	class xalExport AudioManager
	{
	public:
		friend class Buffer;
		friend class ExternalComponent;
		friend class Player;
		friend class Sound;

		virtual ~AudioManager();
		virtual void init();
		void clear();
		
		hstr getName() { return this->name; }
		bool isEnabled() { return this->enabled; }
		bool isPaused() { return this->paused; }
		hstr getDeviceName() { return this->deviceName; }
		bool isThreaded() { return (this->thread != NULL); }
		float getUpdateTime() { return this->updateTime; }
		float getGlobalGain() { return this->gain; }
		void setGlobalGain(float value);
		harray<Player*> getPlayers();

		static void update();
		void update(float k);

		Category* createCategory(chstr name, HandlingMode loadMode = FULL, HandlingMode decodeMode = FULL);
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

		void play(chstr name, float fadeTime = 0.0f, bool looping = false, float gain = 1.0f);
		void stop(chstr name, float fadeTime = 0.0f);
		void stopFirst(chstr name, float fadeTime = 0.0f);
		void stopAll(float fadeTime = 0.0f);
		void pauseAll(float fadeTime = 0.0f);
		void resumeAll(float fadeTime = 0.0f);
		void stopCategory(chstr name, float fadeTime = 0.0f);
		bool isAnyPlaying(chstr name);
		bool isAnyFading(chstr name);
		bool isAnyFadingIn(chstr name);
		bool isAnyFadingOut(chstr name);

		void queueMessage(chstr message);

		void addAudioExtension(chstr extension);
		hstr findAudioFile(chstr _filename);

	protected:
		// protected constructor to ensure that this class has to be subclassed
		AudioManager(chstr systemName, void* backendId, bool threaded = false, float updateTime = 0.01f, chstr deviceName = "");

		void* backendId;
		hstr name;
		bool enabled;
		bool paused;
		bool threaded;
		hstr deviceName;
		float updateTime;
		float gain;
		hmap<hstr, Category*> categories;
		harray<Player*> players;
		harray<Player*> managedPlayers;
		harray<Player*> pausedPlayers;
		hmap<hstr, Sound*> sounds;
		harray<hstr> extensions;
		hthread* thread;
		hmutex mutex; // a mute ex would be nice

		void _setGlobalGain(float value);
		harray<Player*> _getPlayers();

		void _startThreading();
		void _clear();
		
		void _update(float k);
		virtual void _lock();
		virtual void _unlock();

		Category* _createCategory(chstr name, HandlingMode loadMod, HandlingMode decodeMode);
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
		virtual Source* _createSource(chstr filename, Format format);

		void _play(chstr name, float fadeTime, bool looping, float gain);
		void _stop(chstr name, float fadeTime);
		void _stopFirst(chstr name, float fadeTime);
		void _stopAll(float fadeTime);
		void _pauseAll(float fadeTime);
		void _resumeAll(float fadeTime);
		void _stopCategory(chstr name, float fadeTime);
		bool _isAnyPlaying(chstr name);
		bool _isAnyFading(chstr name);
		bool _isAnyFadingIn(chstr name);
		bool _isAnyFadingOut(chstr name);

		virtual void _convertStream(Buffer* buffer, unsigned char** stream, int *streamSize) { }

	private:
		harray<hstr> _queuedMessages;

		void _flushQueuedMessages();

	};
	
	xalExport extern xal::AudioManager* mgr;

}

#endif
