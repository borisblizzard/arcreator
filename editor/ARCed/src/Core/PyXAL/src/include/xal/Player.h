/// @file
/// @author  Boris Mikic
/// @version 2.62
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://www.opensource.org/licenses/bsd-license.php
/// 
/// @section DESCRIPTION
/// 
/// Provides an interface to play and control audio data.

#ifndef XAL_PLAYER_H
#define XAL_PLAYER_H

#include <hltypes/hstring.h>

#include "xalExport.h"

namespace xal
{
	class AudioManager;
	class Buffer;
	class Category;
	class Sound;

	class xalExport Player
	{
	public:
		friend class AudioManager;

		Player(Sound* sound, Buffer* buffer);
		virtual ~Player();

		float getGain();
		void setGain(float value);
		float getPitch();
		void setPitch(float value);
		Sound* getSound() { return this->sound; }
		hstr getName();
		hstr getFilename();
		hstr getRealFilename();
		float getDuration();
		int getSize();
		float getTimePosition();
		unsigned int getSamplePosition();

		Category* getCategory();

		bool isPlaying();
		bool isPaused();
		bool isFading();
		bool isFadingIn();
		bool isFadingOut();
		bool isLooping() { return this->looping; }

		void play(float fadeTime = 0.0f, bool looping = false);
		void stop(float fadeTime = 0.0f);
		void pause(float fadeTime = 0.0f);

	protected:
		float gain;
		float pitch;
		bool paused;
		bool looping;
		float fadeSpeed;
		float fadeTime;
		float offset; // TODO - should be removed?
		Sound* sound;
		Buffer* buffer;
		int bufferIndex;
		int processedByteCount;
		float idleTime;

		float _getGain();
		void _setGain(float value);
		float _getPitch();
		void _setPitch(float value);

		virtual void _update(float k);
		
		void _play(float fadeTime = 0.0f, bool looping = false);
		void _stop(float fadeTime = 0.0f);
		void _pause(float fadeTime = 0.0f);

		float _calcGain();
		bool _tryClearMemory();

		virtual bool _systemIsPlaying() { return false; }
		virtual unsigned int _systemGetBufferPosition() { return 0; }
		virtual float _systemGetOffset() { return 0.0f; }
		virtual void _systemSetOffset(float value) { }
		virtual bool _systemPreparePlay() { return true; }
		virtual void _systemPrepareBuffer() { }
		virtual void _systemUpdateGain() { }
		virtual void _systemUpdatePitch() { }
		virtual void _systemPlay() { }
		virtual int _systemStop() { return 0; }
		virtual int _systemUpdateStream() { return 0; }

	private:
		void _stopSound(float fadeTime = 0.0f);

	};

}
#endif
