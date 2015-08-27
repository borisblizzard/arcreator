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
/// Provides high level directory handling.

#ifndef HLTYPES_DIR_BASE_H
#define HLTYPES_DIR_BASE_H

#include "harray.h"
#include "hstring.h"
#include "hltypesExport.h"

namespace hltypes
{
	template <class T> class Array;
	/// @brief Provides high level directory handling.
	class hltypesExport DirBase
	{
	public:
		/// @brief Gets the base filename/directory without the prepended directory path.
		/// @param[in] path The path.
		/// @return Base filename/directory without the prepended directory path.
		static String baseName(const String& path);
		/// @brief Gets the base directory name of a filename/directory.
		/// @param[in] path The path.
		/// @return Base directory name of the given filename/directory.
		static String baseDir(const String& path);
		/// @brief Changes all platform-specific directory separators to / and removal of duplicate /.
		/// @param[in] path The path.
		/// @return Path with all platform-specific directory separators changed to /.
		static String systemize(const String& path);
		/// @brief Normalizes a file path by converting all platform-specific directory separators into /, removal of duplicate / and proper removal of "." and ".." where necessary.
		/// @param[in] path The path.
		/// @return Normalized path.
		/// @note Calls Dir::systemize() internally.
		static String normalize(const String& path);
		/// @brief Joins two paths taking into consideration slashes at both ends.
		/// @param[in] path1 First path.
		/// @param[in] path2 Second path.
		/// @param[in] systemizeResult Whether to systemize the resulting path as well.
		/// @return Joined path.
		static String joinPath(const String& path1, const String& path2, bool systemizeResult = false);
		/// @brief Joins an array of paths taking into consideration slashes at both ends.
		/// @param[in] paths Array of paths.
		/// @param[in] systemizeResult Whether to systemize the resulting path as well.
		/// @return Joined path.
		static String joinPaths(Array<String> paths, bool systemizeResult = false);
		/// @brief Splits a non-systemized path into its segments.
		/// @param[in] path The path.
		/// @return Split path.
		static Array<String> splitPath(const String& path);

		DEPRECATED_ATTRIBUTE static String basename(const String& path) { return DirBase::baseName(path); }
		DEPRECATED_ATTRIBUTE static String basedir(const String& path) { return DirBase::baseDir(path); }
		DEPRECATED_ATTRIBUTE static String join_path(const String& path1, const String& path2, bool systemizeResult = false) { return DirBase::joinPath(path1, path2, systemizeResult); }
		DEPRECATED_ATTRIBUTE static String join_paths(Array<String> paths, bool systemizeResult = false) { return DirBase::joinPaths(paths, systemizeResult); }
		DEPRECATED_ATTRIBUTE static Array<String> split_path(const String& path) { return DirBase::splitPath(path); }

	protected:
		/// @brief Basic constructor.
		/// @note Forces this to be a static class.
		inline DirBase() { }
		/// @brief Basic constructor.
		/// @note Forces this to be a static class.
		inline virtual ~DirBase() { }

		/// @brief Prepends the directory name to each path entry.
		/// @param[in] dirname Directory name.
		/// @param[in] entries Directory entries.
		static void _prependDirectory(const String& dirname, Array<String>& entries);
	
	};
}

/// @brief Alias for simpler code.
typedef hltypes::DirBase hdbase;

#endif

