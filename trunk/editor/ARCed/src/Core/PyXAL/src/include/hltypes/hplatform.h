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
#define NOMINMAX
#ifndef _NO_WIN_H
#include <windows.h>
#endif
#if defined(WINAPI_FAMILY) && defined(WINAPI_FAMILY_PARTITION)
#if !WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
#define _HL_WINRT 1
#using <Windows.winmd>
#include <wrl.h>
#define _HL_HSTR_TO_PSTR(string) ref new Platform::String((string).w_str().c_str())
#define _HL_HSTR_TO_PSTR_DEF(string) Platform::String^ p ## string = _HL_HSTR_TO_PSTR(string)
#define _HL_PSTR_TO_HSTR(string) unicode_to_utf8((string)->Data())
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
#endif
#ifndef _HL_WINRT
#define _HL_WINRT 0
#endif

#include "hstring.h"

namespace hltypes
{
	/// @brief Executes the actual message loggging.
	/// @param[in] tag The message tag.
	/// @param[in] message The message to log.
	/// @param[in] level Log level (required for Android).
	void _platform_print(chstr tag, chstr message, int level);

}

#endif
