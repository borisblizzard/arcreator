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
/// Provides bacic functionality for XAL.

#ifndef XAL_H
#define XAL_H

#include <hltypes/hstring.h>

#include "xalExport.h"

#define XAL_AS_DISABLED "Disabled"
#define XAL_AS_DIRECTSOUND "DirectSound"
#define XAL_AS_OPENAL "OpenAL"
#define XAL_AS_OPENSLES "OpenSLES"
#define XAL_AS_SDL "SDL"
#define XAL_AS_XAUDIO2 "XAudio2"
#define XAL_AS_AVFOUNDATION "AVFoundation"
#define XAL_AS_COREAUDIO "CoreAudio"

namespace xal
{
	extern hstr logTag;

	/// @brief Type of the audio-system.
	enum AudioSystemType
	{
		AS_DEFAULT = 0,
		AS_DISABLED = 1,
		AS_DIRECTSOUND = 2,
		AS_OPENAL = 3,
		AS_OPENSLES = 4,
		AS_SDL = 5,
		AS_XAUDIO2 = 6,
		AS_AVFOUNDATION = 7,
		AS_COREAUDIO = 8
	};

	/// @brief Initializes XAL.
	/// @param[in] type Type of the audio-system.
	/// @param[in] backendId Special ID needed by some audio systems.
	/// @param[in] threaded Whether update should be handled in a separate thread.
	/// @param[in] updateTime How much time should pass between updates when "threaded" is enabled.
	/// @param[in] deviceName Required by some audio systems.
	/// @note On Win32, backendId is the window handle. On Android, backendId is a pointer to the JavaVM.
	xalFnExport void init(AudioSystemType type, void* backendId, bool threaded = true, float updateTime = 0.01f, chstr deviceName = "");
	/// @brief Destroys XAL.
	xalFnExport void destroy();
	/// @brief Checks if XAL was compiled with a given audio-system available.
	/// @param[in] type Type of the audio-system.
	/// @return True if XAL was compiled with a given audio-system.
	xalFnExport bool hasAudioSystem(AudioSystemType type);

}

#endif
