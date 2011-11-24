/// @file
/// @author  Kresimir Spes
/// @author  Boris Mikic
/// @author  Ivan Vucica
/// @version 2.0
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
#define STREAM_BUFFER_SIZE 32768 // number like x^2
#define STREAM_BUFFER (STREAM_BUFFER_COUNT * STREAM_BUFFER_SIZE)

namespace xal
{
	enum Format
	{
#if HAVE_M4A
		M4A,
#endif
#if HAVE_MP3
		MP3,
#endif
#if HAVE_OGG
		OGG,
#endif
#if HAVE_SPX
		SPX,
#endif
#if HAVE_WAV
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

		AudioManager(chstr systemName, unsigned long backendId, bool threaded = false, float updateTime = 0.01f, chstr deviceName = "");
		virtual ~AudioManager();
		virtual void init();
		void clear();
		
		hstr getName() { return this->name; }
		bool isEnabled() { return this->enabled; }
		bool isPaused() { return this->paused; }
		hstr getDeviceName() { return this->deviceName; }
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

	protected:
		unsigned long backendId;
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
		hthread* thread;
		hmutex mutex; // a mute ex would be nice
		
		void _update(float k);
		void _lock();
		void _unlock();

		void _destroyPlayer(Player* player);
		Player* _createManagedPlayer(chstr name);
		void _destroyManagedPlayer(Player* player);
		Buffer* _createBuffer(chstr filename, HandlingMode loadMode, HandlingMode decodeMode);

		virtual Player* _createAudioPlayer(Sound* sound, Buffer* buffer);
		virtual Source* _createSource(chstr filename, Format format);

		virtual void _convertStream(Buffer* buffer, unsigned char** stream, int *streamSize) { }

	};
	
	xalExport extern xal::AudioManager* mgr;

}

#endif
