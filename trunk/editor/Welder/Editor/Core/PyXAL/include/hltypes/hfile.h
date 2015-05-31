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
/// Provides high level file handling.

#ifndef HLTYPES_FILE_H
#define HLTYPES_FILE_H

#include <stdio.h>

#include "hfbase.h"
#include "hstring.h"

#include "hltypesExport.h"

namespace hltypes
{
	/// @brief Provides high level file handling.
	/// @note When writing, \\r may be used, but \\r will be removed during read.
	class hltypesExport File : public FileBase
	{
	public:
		/// @brief Constructor that immediately opens a file.
		/// @param[in] filename Name of the file (may include path).
		/// @param[in] access_mode File access mode.
		DEPRECATED_ATTRIBUTE File(const String& filename, AccessMode access_mode = READ);
		/// @brief Basic constructor.
		File();
		/// @brief Destructor.
		~File();
		/// @brief Opens a file.
		/// @param[in] filename Name of the file (may include path).
		/// @param[in] access_mode File access mode.
		/// @note If this instance is already working with an opened file handle, that file handle will be closed.
		void open(const String& filename, AccessMode access_mode = READ);
		/// @brief Closes file.
		void close();
		
		/// @brief Creates a file.
		/// @param[in] filename Name of the file.
		/// @return True if a new file was created. False if file could not be created or already exists.
		static bool create(const String& filename);
		/// @brief Creates a file or clears the file if it already exists.
		/// @param[in] filename Name of the file.
		/// @return True if a new file was created or cleared. False if file could not be created.
		static bool createNew(const String& filename);
		/// @brief Removes a file.
		/// @param[in] filename Name of the file.
		/// @return True if file exists and was removed.
		static bool remove(const String& filename);
		/// @brief Checks if a file exists.
		/// @param[in] filename Name of the file.
		/// @param[in] caseSensitive Whether to check case sensitive files if file was not found (costly).
		/// @return True if file exists.
		/// @note Disabling caseSensitive is somewhat costly if the given file is not found at first.
		static bool exists(const String& filename, bool caseSensitive = true);
		/// @brief Clears a file recursively.
		/// @param[in] filename Name of the file.
		/// @return True if file was cleared. False if file does not exist or is already empty.
		static bool clear(const String& filename);
		/// @brief Renames a file.
		/// @param[in] old_filename Old name of the file.
		/// @param[in] new_filename New name of the file.
		/// @param[in] overwrite Whether to overwrite an already existing file.
		/// @return True if file was renamed. False if old file does not exist or file with the new name already exists.
		/// @note If path to new file does not exist, it will be created.
		static bool rename(const String& old_filename, const String& new_filename, bool overwrite = false);
		/// @brief Moves a file to another path.
		/// @param[in] filename Name of the file.
		/// @param[in] path Path where the file should be moved.
		/// @param[in] overwrite Whether to overwrite an already existing file.
		/// @return True if file was moved. False if file does not exist or file with the same name already exists in path.
		/// @note If path does not exist, it will be created.
		static bool move(const String& filename, const String& path, bool overwrite = false);
		/// @brief Copies a file recursively.
		/// @param[in] old_filename Old name of the file.
		/// @param[in] new_filename New name of the file.
		/// @param[in] overwrite Whether to overwrite an already existing file.
		/// @return True if file was copied. False if old file does not exist or file with the new name already exists.
		/// @note If path does not exist, it will be created.
		static bool copy(const String& old_filename, const String& new_filename, bool overwrite = false);
		/// @brief Opens file, reads data and closes file.
		/// @see read(int count)
		static String hread(const String& filename, int count);
		/// @brief Opens file, reads data and closes file.
		/// @see read(const String& delimiter = "")
		static String hread(const String& filename, const String& delimiter = "");
		/// @brief Opens file, writes data and closes file.
		/// @see write
		static void hwrite(const String& filename, const String& text);
		/// @brief Opens file, appends data and closes file.
		/// @see write
		static void happend(const String& filename, const String& text);
		/// @brief Gets the file information provided by the OS.
		/// @param[in] filename The filename of the file.
		/// @return File information provided by the OS.
		static FileInfo hinfo(const String& filename);

		DEPRECATED_ATTRIBUTE static bool create_new(const String& filename) { return File::createNew(filename); }
		DEPRECATED_ATTRIBUTE static FileInfo get_info(const String& filename) { return File::hinfo(filename); }
		DEPRECATED_ATTRIBUTE static int64_t hsize(const String& filename) { return File::hinfo(filename).size; } // use hinfo like this to get the size

	protected:
		/// @brief Reads data from the stream.
		/// @param[in] src Destination data buffer.
		/// @param[in] count Number of elements to read.
		/// @return Number of bytes read.
		int _read(void* buffer, int count);
		/// @brief Writes data to the stream.
		/// @param[in] src Source data buffer.
		/// @param[in] count Number of elements contained in buffer.
		/// @return Number of bytes written.
		int _write(const void* buffer, int count);
		/// @brief Checks if file is open.
		/// @return True if file is open.
		bool _isOpen();
		/// @brief Gets current position in file.
		/// @return Current position in file.
		int64_t _position();
		/// @brief Seeks to position in file.
		/// @param[in] offset Seeking offset in bytes.
		/// @param[in] seekMode Seeking mode.
		bool _seek(int64_t offset, SeekMode seekMode = CURRENT);

	private:
		/// @brief Copy constructor.
		/// @note Usage is not allowed and it will throw an exception.
		File(const File& other);
		/// @brief Assignment operator.
		/// @note Usage is not allowed and it will throw an exception.
		File& operator=(File& other);

	};
}

/// @brief Alias for simpler code.
typedef hltypes::File hfile;

#endif

