/// @file
/// @author  Boris Mikic
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
/// Provides high level thread-safe logging.

#ifndef HLTYPES_LOG_H
#define HLTYPES_LOG_H

#include "harray.h"
#include "hstring.h"
#include "hltypesExport.h"

namespace hltypes
{
	/// @brief Provides high level logging.
	/// @author Boris Mikic
	class hltypesExport Log
	{
	public:
		/// @brief Checks if log level Write is turned on.
		/// @return True if log level Write is turned on.
		static bool isLevelWrite() { return level_write; }
		/// @brief Sets the log level Write.
		/// @param[in] value Whether to turn it on or off.
		static void setLevelWrite(bool value) { level_write = value; }
		/// @brief Checks if log level Error is turned on.
		/// @return True if log level Error is turned on.
		static bool isLevelError() { return level_error; }
		/// @brief Sets the log level Error.
		/// @param[in] value Whether to turn it on or off.
		static void setLevelError(bool value) { level_error = value; }
		/// @brief Checks if log level Warn is turned on.
		/// @return True if log level Warn is turned on.
		static bool isLevelWarn() { return level_warn; }
		/// @brief Sets the log level Warn.
		/// @param[in] value Whether to turn it on or off.
		static void setLevelWarn(bool value) { level_warn = value; }
		/// @brief Checks if log level Debug is turned on.
		/// @return True if log level Debug is turned on.
		static bool isLevelDebug() { return level_debug; }
		/// @brief Sets the log level Debug.
		/// @param[in] value Whether to turn it on or off.
		static void setLevelDebug(bool value) { level_debug = value; }
		/// @brief Sets the current tag filters.
		/// @param[in] value New tag filters.
		/// @note If value is an empty Array, the no filtering will be used.
		static void setTagFilters(harray<hstr> value) { tag_filters = value; }
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
		static void setFilename(chstr filename, bool clearFile = true);
		/// @brief Sets the callback function that is called after logging.
		/// @param[in] function Callback function.
		/// @note The callback is called in a thread-safe manner.
		static void setCallbackFunction(void (*function)(chstr, chstr)) { callback_function = function; }

		/// @brief Logs a message on the log level Write.
		/// @param[in] tag The message tag.
		/// @param[in] message The message to log.
		/// @return True if level Write and tag allowed.
		static bool write(chstr tag, chstr message);
		/// @brief Logs a message on the log level Error.
		/// @param[in] tag The message tag.
		/// @param[in] message The message to log.
		/// @return True if level Error and tag allowed.
		static bool error(chstr tag, chstr message);
		/// @brief Logs a message on the log level Warn.
		/// @param[in] tag The message tag.
		/// @param[in] message The message to log.
		/// @return True if level Warn and tag allowed.
		static bool warn(chstr tag, chstr message);
		/// @brief Logs a message on the log level Debug.
		/// @param[in] tag The message tag.
		/// @param[in] message The message to log.
		/// @return True if level Debug and tag allowed.
		static bool debug(chstr tag, chstr message);
		/// @brief Same as write, except with string formatting.
		/// @see write
		static bool writef(chstr tag, const char* format, ...);
		/// @brief Same as error, except with string formatting.
		/// @see error
		static bool errorf(chstr tag, const char* format, ...);
		/// @brief Same as warn, except with string formatting.
		/// @see warn
		static bool warnf(chstr tag, const char* format, ...);
		/// @brief Same as debug, except with string formatting.
		/// @see debug
		static bool debugf(chstr tag, const char* format, ...);

	protected:
		/// @brief Flag for Write level logging.
		static bool level_write;
		/// @brief Flag for Error level logging.
		static bool level_error;
		/// @brief Flag for Warn level logging.
		static bool level_warn;
		/// @brief Flag for Debug level logging.
		static bool level_debug;
		/// @brief Filters for tags that should be logged.
		static harray<hstr> tag_filters;
		/// @brief Filename for logging to files.
		static hstr filename;
		/// @brief Callback function for logging.
		static void (*callback_function)(chstr, chstr);

		/// @brief Executes the actual message loggging.
		/// @param[in] tag The message tag.
		/// @param[in] message The message to log.
		/// @param[in] level Log level (required for Android).
		/// @return True if the message could be logged.
		static bool _system_log(chstr tag, chstr message, int level);

	};
}

/// @brief Alias for simpler code.
typedef hltypes::Log hlog;

#endif

