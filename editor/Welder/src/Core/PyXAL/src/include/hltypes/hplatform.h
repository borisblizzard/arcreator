/// @file
/// @version 2.3
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://opensource.org/licenses/BSD-3-Clause
/// 
/// @section DESCRIPTION
/// 
/// Provides special preprocessor macros for platform definitions and special platform specific functions.

#ifndef HLTYPES_PLATFORM_H
#define HLTYPES_PLATFORM_H

#if defined(_WIN32) && defined(_MSC_VER)
#ifdef max
#undef max
#endif
#ifdef min
#undef min
#endif
#ifndef NOMINMAX
#define NOMINMAX
#endif
#ifndef _NO_WIN_H
#include <windows.h>
#endif

// define _WINRT for external projects just in case
#if !defined(_WINRT) && defined(WINAPI_FAMILY) && defined(WINAPI_FAMILY_PARTITION)
#if !WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
#define _WINRT
#endif
#endif

#ifdef _WINRT
#if !defined(_WINP8) && !defined(_OPENKODE)
#using <Windows.winmd>
#endif
#include <wrl.h>
#define _HL_HSTR_TO_PSTR(string) ref new Platform::String((string).w_str().c_str())
#define _HL_HSTR_TO_PSTR_DEF(string) Platform::String^ p ## string = _HL_HSTR_TO_PSTR(string)
#define _HL_PSTR_TO_HSTR(string) hstr::from_unicode((string)->Data())
#define _HL_TRY_DELETE(name) \
	if (name != NULL) \
	{ \
		delete name; \
		name = NULL; \
	}
#define _HL_TRY_DELETE_ARRAY(name) \
	if (name != NULL) \
	{ \
		delete [] name; \
		name = NULL; \
	}
#define _HL_TRY_RELEASE(name) \
	if (name != NULL) \
	{ \
		name->Release(); \
		name = NULL; \
	}
#endif
#endif

#include "hstring.h"

namespace hltypes
{
	/// @brief Executes the actual message loggging.
	/// @param[in] tag The message tag.
	/// @param[in] message The message to log.
	/// @param[in] level Log level (required for Android).
	void _platform_print(const String& tag, const String& message, int level);

}

#endif