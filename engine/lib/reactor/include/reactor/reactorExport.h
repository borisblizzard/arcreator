#ifndef REACTOR_EXPORT_H
#define REACTOR_EXPORT_H

	#ifdef _STATICLIB
		#define reactorExport
		#define reactorFnExport
	#else
		#ifdef _WIN32
			#ifdef REACTOR_EXPORTS
				#define reactorExport __declspec(dllexport)
				#define reactorFnExport __declspec(dllexport)
			#else
				#define reactorExport __declspec(dllimport)
				#define reactorFnExport __declspec(dllimport)
			#endif
		#else
			#define reactorExport __attribute__ ((visibility("default")))
			#define reactorFnExport
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

