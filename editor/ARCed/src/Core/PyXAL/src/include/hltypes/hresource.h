/// @file
/// @author  Boris Mikic
/// @version 1.55
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://www.opensource.org/licenses/bsd-license.php
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
	/// @author Kresimir Spes
	/// @author Boris Mikic
	/// @author Ivan Vucica
	/// @note When writing, \\r may be used, but \\r will be removed during read.
	class hltypesExport Resource : public FileBase
	{
	public:
		/// @brief Constructor that immediately opens a resource file.
		/// @param[in] filename Name of the resource file (may include path).
		Resource(chstr filename);
		/// @brief Basic constructor.
		Resource();
		/// @brief Destructor.
		~Resource();
		/// @brief Opens a resource file.
		/// @param[in] filename Name of the resource file (may include path).
		/// @note If this instance is already working with an opened resource file handle, that resource file handle will be closed.
		void open(chstr filename);
		/// @brief Closes resource file.
		void close();
		
		/// @brief Checks if a resource file exists.
		/// @param[in] filename Name of the resource file.
		/// @result True if resource file exists.
		static bool exists(chstr filename);
		/// @brief Opens file, gets size and closes file.
		/// @see size
		static long hsize(chstr filename);
		/// @brief Opens file, reads data and closes file.
		/// @see read(int count)
		static hstr hread(chstr filename, int count);
		/// @brief Opens file, reads data and closes file.
		/// @see read(chstr delimiter = "")
		static hstr hread(chstr filename, chstr delimiter = "");
		/// @brief Create a full filename.
		/// @params[in] filename Original filename.
		/// @returns Full filename.
		static hstr make_full_path(chstr filename);
		
		/// @brief Gets the interal current working directory within a possible archive.
		/// @return Interal current working directory.
		static hstr getCwd() { return cwd; }
		/// @brief Sets the interal current working directory within a possible archive.
		/// @param[in] value New value.
		static void setCwd(chstr value) { cwd = value; }
		/// @brief Gets the resource archive's filename.
		/// @return Resource archive's filename.
		static hstr getArchive() { return archive; }
		/// @brief Sets the resource archive's filename.
		/// @param[in] value New value.
		static void setArchive(chstr value) { archive = value; }
		/// @brief Gets the resource archive's filename.
		/// @return Resource archive's filename.
		static bool hasZip();

	protected:
		/// @brief Data position;
		int data_position;
		/// @brief OS archive file handle.
		void* archivefile;

		/// @brief Defines the internal current working directory of a possible resource archive.
		static hstr cwd;
		/// @brief Defines the resource archive's filename.
		static hstr archive;

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
