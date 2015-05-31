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
/// Provides high level resource directory handling.

#ifndef HLTYPES_RESOURCE_DIR_H
#define HLTYPES_RESOURCE_DIR_H

#include "harray.h"
#include "hdbase.h"
#include "hltypesExport.h"
#include "hmap.h"
#include "hresource.h"
#include "hstring.h"

namespace hltypes
{
	template <class T> class Array;
	/// @brief Provides high level directory handling.
	class hltypesExport ResourceDir : public DirBase
	{
	public:
		friend class Resource;

		/// @brief Checks if a resource directory exists.
		/// @param[in] dirName Name of the resource directory.
		/// @param[in] caseSensitive Whether to check case sensitive files if file was not found.
		/// @return True if resource directory exists.
		/// @note Disabling caseSensitive is somewhat costly if the given file is not found at first.
		static bool exists(const String& dirName, bool caseSensitive = true);
		/// @brief Gets all resource directory entries in the given resource directory.
		/// @param[in] dirName Name of the resource directory.
		/// @param[in] prependDir Whether the same parent path should be appended to the resource entries.
		/// @return Array of all resource directory entries.
		/// @note Entries include "." and "..".
		static Array<String> entries(const String& dirName, bool prependDir = false);
		/// @brief Gets all physical resource directory contents in the given resource directory.
		/// @param[in] dirName Name of the resource directory.
		/// @param[in] prependDir Whether the same parent path should be appended to the resource contents.
		/// @return Array of all resource directory contents.
		/// @note Contents do not include "." and "..".
		static Array<String> contents(const String& dirName, bool prependDir = false);
		/// @brief Gets all resource directories in the given directory.
		/// @param[in] dirName Name of the resource directory.
		/// @param[in] prependDir Whether the same parent path should be appended to the resource directory paths.
		/// @return Array of all resource directories.
		static Array<String> directories(const String& dirName, bool prependDir = false);
		/// @brief Gets all resource files in the given directory.
		/// @param[in] dirName Name of the directory.
		/// @param[in] prependDir Whether the same parent path should be appended to the file paths.
		/// @return Array of all files.
		static Array<String> files(const String& dirName, bool prependDir = false);

	protected:
		/// @brief Cache for directory entries.
		/// @note This is usually only used when ZIP resources are being used.
		static Map<String, Array<String> > cacheDirectories;
		/// @brief Cache for file entries.
		/// @note This is usually only used when ZIP resources are being used.
		static Map<String, Array<String> > cacheFiles;

		/// @brief Basic constructor.
		/// @note Forces this to be a static class.
		inline ResourceDir() : DirBase() { }
		/// @brief Basic constructor.
		/// @note Forces this to be a static class.
		inline ~ResourceDir() { }

		/// @brief Checks if the prefix matches the resource path and removes it.
		/// @param[in,out] path The resource path which gets modified.
		/// @param[in] prefix Prefix to check.
		/// @return True if prefix matches.
		static bool _checkDirPrefix(String& path, const String& prefix);
		/// @brief Gets the file listing within the resource archive.
		/// @return True File listing within the resource archive.
		/// @note This is usually only used when ZIP resources are being used.
		static Array<String> _getInternalFiles();
		/// @brief Removes CWD from resource paths.
		/// @param[in] paths The resource paths.
		/// @return Resource paths without the CWD.
		static Array<String> _removeCwd(Array<String> paths);

	};
}

/// @brief Alias for simpler code.
typedef hltypes::ResourceDir hrdir;

#endif

