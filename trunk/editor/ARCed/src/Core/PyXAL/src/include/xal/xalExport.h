/// @file
/// @author  Kresimir Spes
/// @version 2.0
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://www.opensource.org/licenses/bsd-license.php
/// 
/// @section DESCRIPTION
/// 
/// Defines macros for DLL exports/imports.

#ifndef XAL_EXPORT_H
#define XAL_EXPORT_H

	/// @def xalExport
	/// @brief Macro for DLL exports/imports.
	/// @def xalFnExport
	/// @brief Macro for function DLL exports/imports.
	#ifdef _STATICLIB
		#define xalExport
		#define xalFnExport
	#else
		#ifdef _WIN32
			#ifdef XAL_EXPORTS
				#define xalExport __declspec(dllexport)
				#define xalFnExport __declspec(dllexport)
			#else
				#define xalExport __declspec(dllimport)
				#define xalFnExport __declspec(dllimport)
			#endif
		#else
			#define xalExport __attribute__ ((visibility("default")))
			#define xalFnExport
		#endif
	#endif
	#ifndef DEPRECATED_ATTRIBUTE
		#ifdef _MSC_VER
			#define DEPRECATED_ATTRIBUTE __declspec(deprecated("function is deprecated"))
		#else
			#define DEPRECATED_ATTRIBUTE __attribute__((deprecated))
		#endif
	#endif

#endif

