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

#ifndef HLTYPES_DIR_H
#define HLTYPES_DIR_H

#include "hdbase.h"
#include "hstring.h"
#include "hltypesExport.h"

namespace hltypes
{
	template <class T> class Array;
	/// @brief Provides high level directory handling.
	class hltypesExport Dir : public DirBase
	{
	public:
		/// @brief Sets flag for creating directories with full access permissions on Win32 (Vista and later).
		/// @return Flag for creating directories with full access permissions on Win32 (Vista and later).
		static inline bool getWin32FullDirectoryPermissions() { return win32FullDirectoryPermissions; }
		/// @brief Sets flag for creating directories with full access permissions on Win32 (Vista and later).
		/// @param[in] value New value.
		static inline void setWin32FullDirectoryPermissions(bool value) { win32FullDirectoryPermissions = value; }

		/// @brief Creates a directory.
		/// @param[in] dirName Name of the directory.
		/// @return True if a new directory was created. False if directory could not be created or already exists.
		static bool create(const String& dirName);
		/// @brief Creates a directory or clears the directory if it already exists.
		/// @param[in] dirName Name of the directory.
		/// @return True if a new directory was created or cleared. False if directory could not be created.
		static bool createNew(const String& dirName);
		/// @brief Removes a directory.
		/// @param[in] dirName Name of the directory.
		/// @return True if directory exists and was removed.
		static bool remove(const String& dirName);
		/// @brief Checks if a directory exists.
		/// @param[in] dirName Name of the directory.
		/// @param[in] caseSensitive Whether to check case sensitive files if file was not found.
		/// @return True if directory exists.
		/// @note Disabling caseSensitive is somewhat costly if the given file is not found at first.
		static bool exists(const String& dirName, bool caseSensitive = true);
		/// @brief Clears a directory recursively.
		/// @param[in] dirName Name of the directory.
		/// @return True if directory was cleared. False if directory does not exist or is already empty.
		static bool clear(const String& dirName);
		/// @brief Renames a directory.
		/// @param[in] oldDirName Old name of the directory.
		/// @param[in] newDirName New name of the directory.
		/// @return True if directory was renamed. False if old directory does not exist or directory with the new name already exists.
		/// @note If path to new directory does not exist, it will be created.
		static bool rename(const String& oldDirName, const String& newDirName);
		/// @brief Moves a directory to another path.
		/// @param[in] dirName Name of the directory.
		/// @param[in] path Path where the directory should be moved.
		/// @return True if directory was moved. False if directory does not exist or directory with the same name already exists in path.
		/// @note If path does not exist, it will be created.
		static bool move(const String& dirName, const String& path);
		/// @brief Copies a directory recursively.
		/// @param[in] oldDirName Old name of the directory.
		/// @param[in] newDirName New name of the directory.
		/// @return True if directory was copied. False if old directory does not exist or directory with the new name already exists.
		/// @note If path does not exist, it will be created.
		static bool copy(const String& oldDirName, const String& newDirName);
		/// @brief Gets all directory entries in the given directory.
		/// @param[in] dirName Name of the directory.
		/// @param[in] prependDir Whether the same parent path should be appended to the entries.
		/// @return Array of all directory entries.
		/// @note Entries include "." and "..".
		static Array<String> entries(const String& dirName, bool prependDir = false);
		/// @brief Gets all physical directory contents in the given directory.
		/// @param[in] dirName Name of the directory.
		/// @param[in] prependDir Whether the same parent path should be appended to the contents.
		/// @return Array of all directory contents.
		/// @note Contents do not include "." and "..".
		static Array<String> contents(const String& dirName, bool prependDir = false);
		/// @brief Gets all directories in the given directory.
		/// @param[in] dirName Name of the directory.
		/// @param[in] prependDir Whether the same parent path should be appended to the directory paths.
		/// @return Array of all directories.
		static Array<String> directories(const String& dirName, bool prependDir = false);
		/// @brief Gets all files in the given directory.
		/// @param[in] dirName Name of the directory.
		/// @param[in] prependDir Whether the same parent path should be appended to the file paths.
		/// @return Array of all files.
		static Array<String> files(const String& dirName, bool prependDir = false);
		/// @brief Changes current working directory to given parameter.
		/// @param[in] dirName Name of the directory.
		static void chdir(const String& dirName);
		/// @brief Gets the current working directory.
		/// @return Current working directory.
		static String cwd();

		DEPRECATED_ATTRIBUTE static bool create_new(const String& dirName) { return Dir::createNew(dirName); }

	protected:
		/// @brief Basic constructor.
		/// @note Forces this to be a static class.
		inline Dir() : DirBase() { }
		/// @brief Basic constructor.
		/// @note Forces this to be a static class.
		inline ~Dir() { }

		/// @brief Flag for creating directories with full access permissions on Win32 (Vista and later).
		static bool win32FullDirectoryPermissions;

	};
}

/// @brief Alias for simpler code.
typedef hltypes::Dir hdir;

#endif

