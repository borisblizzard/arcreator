/// @file
/// @author  Boris Mikic
/// @version 2.0
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://www.opensource.org/licenses/bsd-license.php
/// 
/// @section DESCRIPTION
/// 
/// Provides high level file streaming from RAM.

#ifndef HLTYPES_FILE_STREAM_H
#define HLTYPES_FILE_STREAM_H

#include "hsbase.h"
#include "hltypesExport.h"

namespace hltypes
{
	template <class T> class Array;
	/// @brief Provides high level data streaming.
	/// @author Boris Mikic
	class hltypesExport Stream : public StreamBase
	{
	public:
		/// @brief Basic constructor.
		Stream(unsigned char encryption_offset = 0);
		/// @brief Destructor.
		~Stream();
		/// @brief Clears the stream.
		void clear();

	protected:
		/// @brief Data stream container.
		unsigned char* stream;
		/// @brief Data stream container.
		long stream_size;
		/// @brief Data stream container.
		long current_size;
		/// @brief writing position;
		long stream_position;

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
		/// @brief Checks if stream is open.
		/// @return True if stream is open.
		bool _is_open();
		/// @brief Gets current position in stream.
		/// @return Current position in stream.
		long _position();
		/// @brief Seeks to position in stream.
		/// @param[in] offset Seeking offset in bytes.
		/// @param[in] seek_mode Seeking mode.
		void _seek(long offset, SeekMode seek_mode = CURRENT);

	};
}

/// @brief Alias for simpler code.
typedef hltypes::Stream hstream;

#endif

