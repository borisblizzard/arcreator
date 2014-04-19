#ifndef LEGACY_EXPORT_H
#define LEGACY_EXPORT_H

	#ifdef _STATICLIB
		#define legacyExport
		#define legacyFnExport
	#else
		#ifdef _WIN32
			#ifdef LEGACY_EXPORTS
				#define legacyExport __declspec(dllexport)
				#define legacyFnExport __declspec(dllexport)
			#else
				#define legacyExport __declspec(dllimport)
				#define legacyFnExport __declspec(dllimport)
			#endif
		#else
			#define legacyExport __attribute__ ((visibility("default")))
			#define legacyFnExport
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

