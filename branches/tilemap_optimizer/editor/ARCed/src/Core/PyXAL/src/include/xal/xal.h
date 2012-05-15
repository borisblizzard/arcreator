/// @file
/// @author  Boris Mikic
/// @version 2.4
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://www.opensource.org/licenses/bsd-license.php
/// 
/// @section DESCRIPTION
/// 
/// Provides bacic functionality for XAL.

#ifndef XAL_H
#define XAL_H

#include <hltypes/hstring.h>

#include "xalExport.h"

#define XAL_AS_ANDROID "Android"
#define XAL_AS_DIRECTSOUND "DirectSound"
#define XAL_AS_OPENAL "OpenAL"
#define XAL_AS_SDL "SDL"
#define XAL_AS_AVFOUNDATION "AVFoundation"
#define XAL_AS_COREAUDIO "CoreAudio"
#define XAL_AS_DISABLED "Disabled"
#define XAL_AS_DEFAULT ""

namespace xal
{
	xalFnExport void init(chstr systemName, void* backendId, bool threaded = true, float updateTime = 0.01f, chstr deviceName = "");
	xalFnExport void destroy();
	xalFnExport void setLogFunction(void (*function)(chstr));
	xalFnExport void log(chstr message, chstr prefix = "[xal] ");
	xalFnExport bool hasAudioSystem(chstr name);

}

#endif
