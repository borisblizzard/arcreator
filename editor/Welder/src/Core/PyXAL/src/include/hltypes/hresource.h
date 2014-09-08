/// @file
/// @version 2.32
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://opensource.org/licenses/BSD-3-Clause
/// 
/// @section DESCRIPTION
/// 
/// Provides high level resource file handling.

#ifndef HLTYPES_RESOURCE_H
#define HLTYPES_RESOURCE_H

#include <stdio.h>

#include "hfbase.h"
#include "hstring.h"

#include "hltypesExport.h"

namespace hltypes
{
	template <class T> class Array;
	/// @brief Provides high level resource file handling.
	/// @note When writing, \\r may be used, but \\r will be removed during read.
	class hltypesExport Resource : public FileBase
	{
	public:
		/// @brief Constructor that immediately opens a resource file.
		/// @param[in] filename Name of the resource file (may include path).
		Resource(const String& filename);
		/// @brief Basic constructor.
		Resource();
		/// @brief Destructor.
		~Resource();
		/// @brief Opens a resource file.
		/// @param[in] filename Name of the resource file (may include path).
		/// @note If this instance is already working with an opened resource file handle, that resource file handle will be closed.
		void open(const String& filename);
		/// @brief Closes resource file.
		void close();
		
		/// @brief Checks if a resource file exists.
		/// @param[in] filename Name of the resource file.
		/// @param[in] case_sensitive Whether to check case sensitive files if file was not found.
		/// @return True if resource file exists.
		/// @note Disabling case_sensitive is somewhat costly if the given file is not found at first.
		static bool exists(const String& filename, bool case_sensitive = true);
		/// @brief Opens file, gets size and closes file.
		/// @see size
		static long hsize(const String& filename);
		/// @brief Opens file, reads data and closes file.
		/// @see read(int count)
		static String hread(const String& filename, int count);
		/// @brief Opens file, reads data and closes file.
		/// @see read
		static String hread(const String& filename, const String& delimiter = "");
		/// @brief Gets the file information provided by the implementation.
		/// @param[in] filename The filename of the file.
		/// @return File information provided by the implementation.
		static FileInfo get_info(const String& filename);
		/// @brief Create a full filename.
		/// @params[in] filename Original filename.
		/// @return Full filename.
		static String make_full_path(const String& filename);
		
		/// @brief Gets the interal current working directory within a possible archive.
		/// @return Interal current working directory.
		static inline String getCwd() { return cwd; }
		/// @brief Sets the interal current working directory within a possible archive.
		/// @param[in] value New value.
		static inline void setCwd(const String& value) { cwd = value; }
		/// @brief Gets the resource archive's filename.
		/// @return Resource archive's filename.
		static inline String getArchive() { return archive; }
		/// @brief Sets the resource archive's filename.
		/// @param[in] value New value.
		static void setArchive(const String& value);
		/// @brief Checks if the archive is an actual ZIP archive.
		/// @return True if the archive is an actual ZIP archive.
		static inline bool isZipArchive() { return zipArchive; }
		/// @brief Checks if compiled with ZIP support.
		/// @return True if compiled with ZIP support.
		static bool hasZip();

	protected:
		/// @brief Data position;
		int data_position;
		/// @brief OS archive file handle.
		void* archivefile;

		/// @brief Defines the internal current working directory of a possible resource archive.
		static String cwd;
		/// @brief Defines the resource archive's filename.
		static String archive;
		/// @brief Defines whether the archive is set to an actual file.
		static bool zipArchive;

		/// @brief Updates internal data size.
		void _update_data_size();

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
typedef hltypes::Resource hresource;

#endif
