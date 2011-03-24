#ifndef ZER0_EXPORT_H
#define ZER0_EXPORT_H

	#ifdef _STATICLIB
		#define zer0Export
		#define zer0FnExport
	#else
		#ifdef _WIN32
			#ifdef ZER0_EXPORTS
				#define zer0Export __declspec(dllexport)
				#define zer0FnExport __declspec(dllexport)
			#else
				#define zer0Export __declspec(dllimport)
				#define zer0FnExport __declspec(dllimport)
			#endif
		#else
			#define zer0Export __attribute__ ((visibility("default")))
			#define zer0FnExport
		#endif
	#endif
	#ifndef DEPRECATED_ATTRIBUTE
		#ifdef _MSC_VER
			#define DEPRECATED_ATTRIBUTE
		#else
			#define DEPRECATED_ATTRIBUTE __attribute__((deprecated))
		#endif
	#endif

#endif

