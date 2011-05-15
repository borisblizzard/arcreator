#ifndef RGSS_EXPORT_H
#define RGSS_EXPORT_H

	#ifdef _STATICLIB
		#define rgssExport
		#define rgssFnExport
	#else
		#ifdef _WIN32
			#ifdef RGSS_EXPORTS
				#define rgssExport __declspec(dllexport)
				#define rgssFnExport __declspec(dllexport)
			#else
				#define rgssExport __declspec(dllimport)
				#define rgssFnExport __declspec(dllimport)
			#endif
		#else
			#define rgssExport __attribute__ ((visibility("default")))
			#define rgssFnExport
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

