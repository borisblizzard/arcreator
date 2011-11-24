/// @file
/// @author  Boris Mikic
/// @version 2.0
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
	class Updateable;

	class xalExport Player
	{
	public:
		friend class AudioManager;
		friend class Updateable;

		Player(Sound* sound, Buffer* buffer);
		virtual ~Player();

		float getGain() { return this->gain; }
		void setGain(float value);
		float getOffset() { return this->offset; }
		Sound* getSound() { return this->sound; }
		hstr getName();
		hstr getFilename();
		hstr getRealFilename();
		float getDuration();
		int getSize();

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
		bool paused;
		bool looping;
		float fadeSpeed;
		float fadeTime;
		float offset; // TODO - should be int?
		Sound* sound;
		Buffer* buffer;
		int bufferIndex;

		virtual void _update(float k);
		
		void _play(float fadeTime = 0.0f, bool looping = false);
		void _stop(float fadeTime = 0.0f);
		void _pause(float fadeTime = 0.0f);

		float _calcGain();
		float _calcFadeGain();
		void _stopSound(float fadeTime = 0.0f);

		virtual bool _systemIsPlaying() { return false; }
		virtual float _systemGetOffset() { return 1.0f; }
		virtual void _systemSetOffset(float value) { }
		virtual bool _systemPreparePlay() { return true; }
		virtual void _systemPrepareBuffer() { }
		virtual void _systemUpdateGain() { }
		virtual void _systemUpdateFadeGain() { }
		virtual void _systemPlay() { }
		virtual void _systemStop() { }
		virtual void _systemUpdateStream() { }

	};

}
#endif
