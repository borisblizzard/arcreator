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
/// Provides high level file streaming from RAM.

#ifndef HLTYPES_FILE_STREAM_H
#define HLTYPES_FILE_STREAM_H

#include "hsbase.h"
#include "hltypesExport.h"

namespace hltypes
{
	/// @brief Provides high level data streaming.
	class hltypesExport Stream : public StreamBase
	{
	public:
		/// @brief Constructor.
		/// @param[in] initialCapacity Initial capacity of the internal buffer.
		/// @note initialCapacity is used to prevent unnecessary calls to realloc() internally if it's not needed. This is NOT the Stream's initial size.
		Stream(int initialCapacity = 16);
		/// @brief Constructor.
		/// @param[in] initialData Initial data in the Stream.
		/// @param[in] initialDataSize Initial data's size.
		/// @note initialData is copied into the Stream.
		Stream(unsigned char* initialData, int initialDataSize);
		/// @brief Constructor.
		/// @param[in] initialData Initial data in the Stream.
		/// @param[in] initialDataSize Initial data's size.
		/// @param[in] initialCapacity Initial capacity of the internal buffer.
		/// @note initialData is copied into the Stream. initialCapacity will be corrected to initialDataSize if less than initialDataSize.
		Stream(unsigned char* initialData, int initialDataSize, int initialCapacity);
		/// @brief Copy constructor.
		/// @param[in] other Other Stream.
		Stream(const Stream& other);
		/// @brief Destructor.
		~Stream();
		/// @brief Clears the Stream.
		/// @param[in] newCapacity New capacity of the internal buffer.
		/// @note newCapacity is used to prevent unnecessary calls to realloc() internally if it's not needed. This is NOT the Stream's initial size.
		void clear(int newCapacity = 16LL);
		/// @brief Resizes internal buffer.
		/// @param[in] newCapacity New capacity of the internal buffer.
		/// @return True if internal buffer was resized or already the same size that was requested.
		/// @note This does not change the data stream size. Use this to avoid allocation of too much data if not needed.
		/// @note If newCapacity is smaller than the stream size, data will be lost and the Stream will be resized.
		bool setCapacity(int newCapacity);
		/// @brief Writes raw data to the Stream.
		/// @param[in] buffer Pointer to raw data buffer.
		/// @param[in] count Number of bytes to write.
		/// @return Number of bytes written.
		/// @note If return value differs from parameter count, it can indicate a writing error.
		int writeRaw(void* buffer, int count);
		/// @brief Writes raw data to the Stream from another Stream.
		/// @param[in] stream Another Stream.
		/// @param[in] count Number of bytes to write.
		/// @return Number of bytes written.
		int writeRaw(StreamBase& stream, int count);
		/// @brief Writes raw data to the Stream from another Stream.
		/// @param[in] stream Another Stream.
		/// @return Number of bytes written.
		int writeRaw(StreamBase& stream);
		/// @brief Writes raw data to the Stream from another Stream.
		/// @param[in] stream Another Stream.
		/// @param[in] count Number of bytes to write.
		/// @return Number of bytes written.
		int writeRaw(Stream& stream, int count);
		/// @brief Writes raw data to the Stream from another Stream.
		/// @param[in] stream Another Stream.
		/// @return Number of bytes written.
		int writeRaw(Stream& stream);
		/// @brief Prepares Stream for manual writing without using write_raw() directly.
		/// @param[in] count Number of bytes to prepare. Stream size is increased if necessary, but contains garbage data.
		/// @return Number of bytes ready to be written.
		/// @note Use this when you intend to manually write data. This does not change the current position and seeking has to be done manually as well.
		/// @see write_raw()
		int prepareManualWriteRaw(int count);
		/// @brief Writes a certain value into the buffer.
		/// @param[in] value The value.
		/// @param[in] count Number of bytes to write.
		/// @return Number of bytes written.
		/// @note If return value differs from parameter count, it can indicate a writing error.
		int fill(unsigned char value, int count);
		/// @brief Truncates the Stream and removes data.
		/// @param[in] targetSize The size the Stream should be truncated to.
		/// @return True if Stream was truncated/reduced.
		/// @note If size is greater or equal than the current size, the stream size will stay unchanged.
		bool truncate(int64_t targetSize);
		/// @brief Gets a direct reference to the internal steam.
		/// @param[in] index Reference to a specific element.
		/// @return Direct reference to the internal steam.
		const unsigned char& operator[](int index);
		/// @brief Copies the other Stream into this one.
		/// @param[in] other Other Stream.
		/// @return This modified Stream.
		Stream& operator=(Stream& other);
		/// @brief Casts this Array into a C-array.
		/// @return The C-array.
		operator char*() const;
		/// @brief Casts this Array into a C-array.
		/// @return The C-array.
		operator const char*() const;
		/// @brief Casts this Array into a C-array.
		/// @return The C-array.
		operator unsigned char*() const;
		/// @brief Casts this Array into a C-array.
		/// @return The C-array.
		operator const unsigned char*() const;

	protected:
		/// @brief Data stream container.
		unsigned char* stream;
		/// @brief Data stream size.
		int64_t streamSize;
		/// @brief writing position;
		int64_t streamPosition;
		/// @brief Capacity data of stream container.
		int64_t capacity;

		/// @brief Updates internal data size.
		void _updateDataSize();

		/// @brief Reads data from the Stream.
		/// @param[in] buffer Destination data buffer.
		/// @param[in] count Number of elements to read.
		/// @return Number of bytes read.
		int _read(void* buffer, int count);
		/// @brief Writes data to the Stream.
		/// @param[in] buffer Source data buffer.
		/// @param[in] count Number of elements contained in buffer.
		/// @return Number of bytes written.
		int _write(const void* buffer, int count);
		/// @brief Checks if Stream is open.
		/// @return True if Stream is open.
		bool _isOpen();
		/// @brief Gets current position in Stream.
		/// @return Current position in Stream.
		int64_t _position();
		/// @brief Seeks to position in Stream.
		/// @param[in] offset Seeking offset in bytes.
		/// @param[in] seekMode Seeking mode.
		bool _seek(int64_t offset, SeekMode seekMode = CURRENT);
		/// @brief Resizes internal buffer if necessary.
		/// @param[in,out] write_size Number of bytes that is needed for the next write.
		/// @note This does not change the data stream size. Use this to avoid allocation of too much data if not needed.
		bool _tryIncreaseCapacity(int& write_size);

	};
}

/// @brief Alias for simpler code.
typedef hltypes::Stream hstream;

#endif

