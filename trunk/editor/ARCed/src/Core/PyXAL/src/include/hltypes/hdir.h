/// @file
/// @author  Boris Mikic
/// @author  Kresimir Spes
/// @version 1.4
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://www.opensource.org/licenses/bsd-license.php
/// 
/// @section DESCRIPTION
/// 
/// Provides high level directory handling.

#ifndef HLTYPES_DIR_H
#define HLTYPES_DIR_H

#include "hstring.h"
#include "hltypesExport.h"

namespace hltypes
{
	template <class T> class Array;
	/// @brief Provides high level directory handling.
	/// @author Boris Mikic
	/// @author Kresimir Spes
	class hltypesExport Dir
	{
	public:
		/// @brief 2DO
		/// @param[in] filepath of the file.
		/// @result 2DO
		static hstr convert_to_native_path(hstr path);
		/// @brief Creates a directory.
		/// @param[in] dirname Name of the directory.
		/// @result True if a new directory was created. False if directory could not be created or already exists.
		static bool create(chstr dirname);
		/// @brief Creates a directory or clears the directory if it already exists.
		/// @param[in] dirname Name of the directory.
		/// @result True if a new directory was created or cleared. False if directory could not be created.
		static bool create_new(chstr dirname);
		/// @brief Removes a directory.
		/// @param[in] dirname Name of the directory.
		/// @result True if directory exists and was removed.
		static bool remove(chstr dirname);
		/// @brief Checks if a directory exists.
		/// @param[in] dirname Name of the directory.
		/// @result True if directory exists.
		static bool exists(chstr dirname);
		/// @brief Clears a directory recursively.
		/// @param[in] dirname Name of the directory.
		/// @result True if directory was cleared. False if directory does not exist or is already empty.
		static bool clear(chstr dirname);
		/// @brief Renames a directory.
		/// @param[in] old_dirname Old name of the directory.
		/// @param[in] new_dirname New name of the directory.
		/// @result True if directory was renamed. False if old directory does not exist or directory with the new name already exists.
		/// @note If path to new directory does not exist, it will be created.
		static bool rename(chstr old_dirname, chstr new_dirname);
		/// @brief Moves a directory to another path.
		/// @param[in] dirname Name of the directory.
		/// @param[in] path Path where the directory should be moved.
		/// @result True if directory was moved. False if directory does not exist or directory with the same name already exists in path.
		/// @note If path does not exist, it will be created.
		static bool move(chstr dirname, chstr path);
		/// @brief Copies a directory recursively.
		/// @param[in] old_dirname Old name of the directory.
		/// @param[in] new_dirname New name of the directory.
		/// @result True if directory was copied. False if old directory does not exist or directory with the new name already exists.
		/// @note If path does not exist, it will be created.
		static bool copy(chstr old_dirname, chstr new_dirname);
		/// @brief Creates the parent path of the given directory or file.
		/// @param[in] path Path of a directory or file.
		/// @result True if parent path was created.
		/// @note This method is used to create the parent path structure for a directory or file without haivng to manually split the path string.
		static bool create_path(chstr path);
		/// @brief Gets all directory entries in the given directory.
		/// @param[in] dirname Name of the directory.
		/// @param[in] prepend_dir Whether the same parent path should be appended to the entries.
		/// @result Array of all directory entries.
		/// @note Entries include "." and "..".
		static Array<hstr> entries(chstr dirname, bool prepend_dir = false);
		/// @brief Gets all physical directory contents in the given directory.
		/// @param[in] dirname Name of the directory.
		/// @param[in] prepend_dir Whether the same parent path should be appended to the contents.
		/// @result Array of all directory contents.
		/// @note Contents do not include "." and "..".
		static Array<hstr> contents(chstr dirname, bool prepend_dir = false);
		/// @brief Gets all directories in the given directory.
		/// @param[in] dirname Name of the directory.
		/// @param[in] prepend_dir Whether the same parent path should be appended to the directory paths.
		/// @result Array of all directories.
		static Array<hstr> directories(chstr dirname, bool prepend_dir = false);
		/// @brief Gets all files in the given directory.
		/// @param[in] dirname Name of the directory.
		/// @param[in] prepend_dir Whether the same parent path should be appended to the file paths.
		/// @result Array of all files.
		static Array<hstr> files(chstr dirname, bool prepend_dir = false);
		/// @brief Changes current working directory to given parameter
		/// @param[in] dirname Name of the directory
		static void chdir(chstr dirname);
	};
}

/// @brief Alias for simpler code.
typedef hltypes::Dir hdir;

#endif

