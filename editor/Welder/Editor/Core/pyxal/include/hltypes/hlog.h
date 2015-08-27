/// @file
/// @version 3.0
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://opensource.org/licenses/BSD-3-Clause
/// 
/// @section DESCRIPTION
/// 
/// Provides high level thread-safe logging.

#ifndef HLTYPES_LOG_H
#define HLTYPES_LOG_H

#include "harray.h"
#include "hltypesExport.h"
#include "hstring.h"
#include "hmutex.h"

namespace hltypes
{
	/// @brief Provides high level logging.
	class hltypesExport Log
	{
	public:
		/// @brief Level Write value.
		/// @note Usually only used internally.
		static int LevelWrite;
		/// @brief Level Error value.
		/// @note Usually only used internally.
		static int LevelError;
		/// @brief Level Warn value.
		/// @note Usually only used internally.
		static int LevelWarn;
		/// @brief Level Debug value.
		/// @note Usually only used internally.
		static int LevelDebug;

		/// @brief Checks if log level Write is turned on.
		/// @return True if log level Write is turned on.
		static inline bool isLevelWrite() { return levelWrite; }
		/// @brief Sets the log level Write.
		/// @param[in] value Whether to turn it on or off.
		static inline void setLevelWrite(bool value) { levelWrite = value; }
		/// @brief Checks if log level Error is turned on.
		/// @return True if log level Error is turned on.
		static inline bool isLevelError() { return levelError; }
		/// @brief Sets the log level Error.
		/// @param[in] value Whether to turn it on or off.
		static inline void setLevelError(bool value) { levelError = value; }
		/// @brief Checks if log level Warn is turned on.
		/// @return True if log level Warn is turned on.
		static inline bool isLevelWarn() { return levelWarn; }
		/// @brief Sets the log level Warn.
		/// @param[in] value Whether to turn it on or off.
		static inline void setLevelWarn(bool value) { levelWarn = value; }
		/// @brief Checks if log level Debug is turned on.
		/// @return True if log level Debug is turned on.
		static inline bool isLevelDebug() { return levelDebug; }
		/// @brief Sets the log level Debug.
		/// @param[in] value Whether to turn it on or off.
		static inline void setLevelDebug(bool value) { levelDebug = value; }
		/// @brief Sets the current tag filters.
		/// @param[in] value New tag filters.
		/// @note If value is an empty Array, the no filtering will be used.
		static inline void setTagFilters(Array<String> value) { tagFilters = value; }
		/// @brief Sets all logging levels at once.
		/// @param[in] write Value for Log level Write.
		/// @param[in] write Value for Log level Error.
		/// @param[in] write Value for Log level Warn.
		/// @param[in] write Value for Log level Debug.
		static void setLevels(bool write, bool error, bool warn, bool debug);
		/// @brief Sets the filename for log dump.
		/// @param[in] filename Filename for log dump.
		/// @param[in] clearFile Set to true if file should be cleared.
		/// @note If filename is an empty String, the no dumping will be used.
		static void setFilename(const String& filename, bool clearFile = true);
		/// @brief Sets the callback function that is called after logging.
		/// @param[in] function Callback function.
		/// @note The callback is called in a thread-safe manner.
		static inline void setCallbackFunction(void (*function)(const String&, const String&)) { callbackFunction = function; }

		/// @brief Logs a message on the log level Write.
		/// @param[in] tag The message tag.
		/// @param[in] message The message to log.
		/// @return True if level Write and tag allowed.
		static bool write(const String& tag, const String& message);
		/// @brief Logs a message on the log level Error.
		/// @param[in] tag The message tag.
		/// @param[in] message The message to log.
		/// @return True if level Error and tag allowed.
		static bool error(const String& tag, const String& message);
		/// @brief Logs a message on the log level Warn.
		/// @param[in] tag The message tag.
		/// @param[in] message The message to log.
		/// @return True if level Warn and tag allowed.
		static bool warn(const String& tag, const String& message);
		/// @brief Logs a message on the log level Debug.
		/// @param[in] tag The message tag.
		/// @param[in] message The message to log.
		/// @return True if level Debug and tag allowed.
		static bool debug(const String& tag, const String& message);
		/// @brief Same as write, except with string formatting.
		/// @see write
		static bool writef(const String& tag, const char* format, ...);
		/// @brief Same as error, except with string formatting.
		/// @see error
		static bool errorf(const String& tag, const char* format, ...);
		/// @brief Same as warn, except with string formatting.
		/// @see warn
		static bool warnf(const String& tag, const char* format, ...);
		/// @brief Same as debug, except with string formatting.
		/// @see debug
		static bool debugf(const String& tag, const char* format, ...);
		/// @brief Merges all log files into one.
		/// @param[in] clearFile Set to true if file should be cleared.
		/// @note Call this at application exit or before changing logging files.
		static void finalize(bool clearFile = true);

	protected:
		/// @brief Flag for Write level logging.
		static bool levelWrite;
		/// @brief Flag for Error level logging.
		static bool levelError;
		/// @brief Flag for Warn level logging.
		static bool levelWarn;
		/// @brief Flag for Debug level logging.
		static bool levelDebug;
		/// @brief Filters for tags that should be logged.
		static Array<String> tagFilters;
		/// @brief Filename for logging to files.
		static String filename;
		/// @brief Callback function for logging.
		static void(*callbackFunction)(const String&, const String&);
		/// @brief Mutex to ensure thread-safe handling
		static Mutex mutex;
		/// @brief Used for segmented Win32 log files.
		static int fileIndex;
		/// @brief Used for segmented Win32 log files.
		static String fileExtension;

		/// @brief Basic constructor.
		/// @note Forces this to be a static class.
		inline Log() { }
		/// @brief Basic constructor.
		/// @note Forces this to be a static class.
		inline ~Log() { }

		/// @brief Executes the actual message loggging.
		/// @param[in] tag The message tag.
		/// @param[in] message The message to log.
		/// @param[in] level Log level (required for Android).
		/// @return True if the message could be logged.
		static bool _systemLog(const String& tag, const String& message, int level);
		/// @brief Used for segmented Win32 log files.
		static String _makeFilename(const String& filename, int index);
		/// @brief Used for segmented Win32 log files.
		static String _makeCurrentFilename(const String& filename);

	};
}

/// @brief Alias for simpler code.
typedef hltypes::Log hlog;

#endif

