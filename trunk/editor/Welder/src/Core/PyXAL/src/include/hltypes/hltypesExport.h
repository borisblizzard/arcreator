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
/// Defines macros for DLL exports/imports.

#ifndef HLTYPES_EXPORT_H
#define HLTYPES_EXPORT_H

	/// @def hltypesExport
	/// @brief Macro for DLL exports/imports.
	/// @def hltypesFnExport
	/// @brief Macro for function DLL exports/imports.
	#ifdef _LIB
		#define hltypesExport
		#define hltypesFnExport
	#else
		#ifdef _WIN32
			#ifdef HLTYPES_EXPORTS
				#define hltypesExport __declspec(dllexport)
				#define hltypesFnExport __declspec(dllexport)
			#else
				#define hltypesExport __declspec(dllimport)
				#define hltypesFnExport __declspec(dllimport)
			#endif
			#ifdef _WINRT
				#define hltypesSpecialExport
				#define hltypesMemberExport hltypesExport
			#endif
		#else
			#define hltypesExport __attribute__ ((visibility("default")))
			#define hltypesFnExport __attribute__ ((visibility("default")))
		#endif
	#endif
	#ifndef DEPRECATED_ATTRIBUTE
		#ifdef _MSC_VER
			#define DEPRECATED_ATTRIBUTE __declspec(deprecated("function is deprecated"))
		#else
			#define DEPRECATED_ATTRIBUTE __attribute__((deprecated))
		#endif
	#endif
	#ifndef hltypesSpecialExport
		#define hltypesSpecialExport hltypesExport
		#define hltypesMemberExport
	#endif

#endif

