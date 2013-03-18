/// @file
/// @author  Kresimir Spes
/// @author  Boris Mikic
/// @author  Ivan Vucica
/// @version 2.0
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://www.opensource.org/licenses/bsd-license.php
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
	template <class T> class Array;
	/// @brief Provides high level file handling.
	/// @author Kresimir Spes
	/// @author Boris Mikic
	/// @author Ivan Vucica
	class hltypesExport File : public FileBase
	{
	public:
		/// @brief Constructor that immediately opens a file.
		/// @param[in] filename Name of the file (may include path).
		/// @param[in] access_mode File access mode.
		/// @param[in] encryption_offset Byte value offset while reading/writing that serves as simple binary encryption.
		File(chstr filename, AccessMode access_mode = READ, unsigned char encryption_offset = 0);
		/// @brief Basic constructor.
		File();
		/// @brief Destructor.
		~File();
		/// @brief Opens a file.
		/// @param[in] filename Name of the file (may include path).
		/// @param[in] access_mode File access mode.
		/// @param[in] encryption_offset Byte value offset while reading/writing that serves as simple binary encryption.
		/// @note If this instance is already working with an opened file handle, that file handle will be closed.
		void open(chstr filename, AccessMode access_mode = READ, unsigned char encryption_offset = 0);
		/// @brief Closes file.
		void close();
		
		/// @brief Creates a file.
		/// @param[in] filename Name of the file.
		/// @return True if a new file was created. False if file could not be created or already exists.
		static bool create(chstr filename);
		/// @brief Creates a file or clears the file if it already exists.
		/// @param[in] filename Name of the file.
		/// @return True if a new file was created or cleared. False if file could not be created.
		static bool create_new(chstr filename);
		/// @brief Removes a file.
		/// @param[in] filename Name of the file.
		/// @return True if file exists and was removed.
		static bool remove(chstr filename);
		/// @brief Checks if a file exists.
		/// @param[in] filename Name of the file.
		/// @return True if file exists.
		static bool exists(chstr filename);
		/// @brief Clears a file recursively.
		/// @param[in] filename Name of the file.
		/// @return True if file was cleared. False if file does not exist or is already empty.
		static bool clear(chstr filename);
		/// @brief Renames a file.
		/// @param[in] old_filename Old name of the file.
		/// @param[in] new_filename New name of the file.
		/// @param[in] overwrite Whether to overwrite an already existing file.
		/// @return True if file was renamed. False if old file does not exist or file with the new name already exists.
		/// @note If path to new file does not exist, it will be created.
		static bool rename(chstr old_filename, chstr new_filename, bool overwrite = false);
		/// @brief Moves a file to another path.
		/// @param[in] filename Name of the file.
		/// @param[in] path Path where the file should be moved.
		/// @param[in] overwrite Whether to overwrite an already existing file.
		/// @return True if file was moved. False if file does not exist or file with the same name already exists in path.
		/// @note If path does not exist, it will be created.
		static bool move(chstr filename, chstr path, bool overwrite = false);
		/// @brief Copies a file recursively.
		/// @param[in] old_filename Old name of the file.
		/// @param[in] new_filename New name of the file.
		/// @param[in] overwrite Whether to overwrite an already existing file.
		/// @return True if file was copied. False if old file does not exist or file with the new name already exists.
		/// @note If path does not exist, it will be created.
		static bool copy(chstr old_filename, chstr new_filename, bool overwrite = false);
		/// @brief Opens file, gets size and closes file.
		/// @see size
		static long hsize(chstr filename);
		/// @brief Opens file, reads data and closes file.
		/// @see read(int count)
		static hstr hread(chstr filename, int count);
		/// @brief Opens file, reads data and closes file.
		/// @see read(chstr delimiter = "")
		static hstr hread(chstr filename, chstr delimiter = "");
		/// @brief Opens file, writes data and closes file.
		/// @see write
		static void hwrite(chstr filename, chstr text);
		/// @brief Opens file, appends data and closes file.
		/// @see write
		static void happend(chstr filename, chstr text);
		
	protected:
		/// @brief Reads data from the stream.
		/// @param[in] src Destination data buffer.
		/// @param[in] size Size in bytes of a single buffer element.
		/// @param[in] sound Number of elements to read.
		/// @return Number of bytes read.
		long _read(void* buffer, int size, int count);
		/// @brief Writes data to the stream.
		/// @param[in] src Source data buffer.
		/// @param[in] size Size in bytes of a single buffer element.
		/// @param[in] sound Number of elements contained in buffer.
		/// @return Number of bytes written.
		long _write(const void* buffer, int size, int count);
		/// @brief Checks if file is open.
		/// @return True if file is open.
		bool _is_open();
		/// @brief Gets current position in file.
		/// @return Current position in file.
		long _position();
		/// @brief Seeks to position in file.
		/// @param[in] offset Seeking offset in bytes.
		/// @param[in] seek_mode Seeking mode.
		void _seek(long offset, SeekMode seek_mode = CURRENT);

	};
}

/// @brief Alias for simpler code.
typedef hltypes::File hfile;

#endif

