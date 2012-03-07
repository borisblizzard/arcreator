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
/// Provides a base class for streaming.

#ifndef HLTYPES_STREAM_BASE_H
#define HLTYPES_STREAM_BASE_H

#include <stdio.h>

#include "harray.h"
#include "hltypesExport.h"
#include "hstring.h"

namespace hltypes
{
	template <class T> class Array;
	/// @brief Provides a base class for streaming.
	/// @author Boris Mikic
	class hltypesExport StreamBase
	{
	public:
		/// @brief Defines file seek modes.
		enum SeekMode
		{
			/// @brief Seek from current position. (SEEK_CUR)
			CURRENT,
			/// @brief Seek from start position. (SEEK_SET)
			START,
			/// @brief Seek from current position. (SEEK_END)
			END
		};
		
		/// @brief Basic constructor.
		StreamBase(unsigned char encryption_offset = 0);
		/// @brief Destructor.
		virtual ~StreamBase();

		/// @brief Checks if data is "open".
		/// @return True if data is "open".
		bool is_open();
		/// @brief Seeks to position in data.
		/// @param[in] offset Seeking offset in bytes.
		/// @param[in] seek_mode Seeking mode.
		void seek(long offset, SeekMode seek_mode = CURRENT);
		/// @brief Seeks to position 0.
		void rewind();
		/// @brief Gets current position in data.
		/// @return Current position in data.
		long position();
		/// @brief Gets size of the data in bytes.
		/// @return Size of the data in bytes.
		long size();
		/// @brief Checks if data has reached the end.
		/// @return True if data has reached the end.
		bool eof();

		/// @brief Reads from the file until delimiter character is read.
		/// @param[in] delimiter String where to stop reading.
		/// @return The read string.
		/// @note Delimiter String is not included in return result.
		/// @note When delimiter is omitted, the file will be read until EOF.
		hstr read(chstr delimiter = "");
		/// @brief Reads n bytes from the file.
		/// @param[in] count Number of bytes to read.
		/// @return The read string.
		hstr read(int count);
		/// @brief Reads one line from the file.
		/// @return The read line.
		/// @note \\n is not included in the returned String.
		hstr read_line();
		/// @brief Reads all lines from the file.
		/// @return Array with read lines.
		/// @note \\n is not included in the read lines.
		Array<hstr> read_lines();
		/// @brief Writes string to the file.
		/// @param[in] text String to write.
		void write(chstr text);
		/// @brief Writes string to the file.
		/// @param[in] text C-type string to write.
		void write(const char* text);
		/// @brief Writes string to the file and appends \\n at the end.
		/// @param[in] text String to write.
		void write_line(chstr text);
		/// @brief Writes string to the file and appends \\n at the end.
		/// @param[in] text C-type string to write.
		void write_line(const char* text);
		/// @brief Writes formatted string to the file.
		/// @param[in] format C-type string containing format.
		/// @param[in] ... Formatting arguments.
		void writef(const char* format, ...);
		/// @brief Reads raw data from the file.
		/// @param[in] buffer Pointer to raw data buffer.
		/// @param[in] count Number of bytes to read.
		/// @return Number of bytes read.
		/// @note If return value differs from parameter count, it can indicate a reading error or that end of file has been reached.
		int read_raw(void* buffer, int count);
		/// @brief Writes raw data to the file.
		/// @param[out] buffer Pointer to raw data buffer.
		/// @param[in] count Number of bytes to write.
		/// @return Number of bytes written.
		/// @note If return value differs from parameter count, it can indicate a writing error.
		int write_raw(void* buffer, int count);

		/// @brief Dumps data to file in a platform-aware format.
		/// @param c Character to dump.
		void dump(char c);
		/// @brief Dumps data to file in a platform-aware format.
		/// @param c Unsigned character to dump.
		void dump(unsigned char c);
		/// @brief Dumps data to file in a platform-aware format.
		/// @param i Int to dump.
		void dump(int i);
		/// @brief Dumps data to file in a platform-aware format.
		/// @param i Unsigned int to dump.
		void dump(unsigned int i);
		/// @brief Dumps data to file in a platform-aware format.
		/// @param l Long to dump.
		void dump(long l);
		/// @brief Dumps data to file in a platform-aware format.
		/// @param l Unsigned long to dump.
		void dump(unsigned long l);
		/// @brief Dumps data to file in a platform-aware format.
		/// @param s Short int to dump.
		void dump(short s);
		/// @brief Dumps data to file in a platform-aware format.
		/// @param s Unsigned short int to dump.
		void dump(unsigned short s);
		/// @brief Dumps data to file in a platform-aware format.
		/// @param f Float to dump.
		void dump(float f);
		/// @brief Dumps data to file in a platform-aware format.
		/// @param d Double to dump.
		void dump(double d);
		/// @brief Dumps data to file in a platform-aware format.
		/// @param b Bool to dump.
		void dump(bool b);
		/// @brief Dumps data to file in a platform-aware format.
		/// @param str String to dump.
		void dump(chstr str);
		/// @brief Dumps data to file in a platform-aware format.
		/// @param c C-type string to dump.
		void dump(const char* c);

		/// @brief Loads data from file in a platform-aware format.
		/// @return Loaded character.
		char load_char();
		/// @brief Loads data from file in a platform-aware format.
		/// @return Loaded unsigned character.
		unsigned char load_uchar();
		/// @brief Loads data from file in a platform-aware format.
		/// @return Loaded int.
		int load_int();
		/// @brief Loads data from file in a platform-aware format.
		/// @return Loaded unsigned int.
		unsigned int load_uint();
		/// @brief Loads data from file in a platform-aware format.
		/// @return Loaded long.
		long load_long();
		/// @brief Loads data from file in a platform-aware format.
		/// @return Loaded unsigned long.
		unsigned long load_ulong();
		/// @brief Loads data from file in a platform-aware format.
		/// @return Loaded short int.
		short load_short();
		/// @brief Loads data from file in a platform-aware format.
		/// @return Loaded unsigned short int.
		unsigned short load_ushort();
		/// @brief Loads data from file in a platform-aware format.
		/// @return Loaded float.
		float load_float();
		/// @brief Loads data from file in a platform-aware format.
		/// @return Loaded double.
		double load_double();
		/// @brief Loads data from file in a platform-aware format.
		/// @return Loaded bool.
		bool load_bool();
		/// @brief Loads data from file in a platform-aware format.
		/// @return Loaded String.
		hstr load_hstr();
		/// @brief Loads data from file in a platform-aware format.
		/// @return Loaded String.
		hstr load_string();
		
	protected:
		/// @brief Data size, mostly used for optimization and faster "eof" detection.
		long data_size;
		/// @brief Byte value offset while reading/writing that serves as simple binary encryption.
		unsigned char encryption_offset;

		/// @brief Updates internal data size.
		virtual void _update_data_size();
		/// @brief Checks if object can be used.
		virtual void _check_availability();

		/// @brief Gets special descriptor.
		/// @returns Special descriptor.
		virtual hstr _descriptor() { return "stream"; }
		/// @brief Reads data from the stream.
		/// @param[in] src Destination data buffer.
		/// @param[in] size Size in bytes of a single buffer element.
		/// @param[in] sound Number of elements to read.
		/// @return Number of bytes read.
		virtual long _read(void* buffer, int size, int count) = 0;
		/// @brief Writes data to the stream.
		/// @param[in] src Source data buffer.
		/// @param[in] size Size in bytes of a single buffer element.
		/// @param[in] sound Number of elements contained in buffer.
		/// @return Number of bytes written.
		virtual long _write(const void* buffer, int size, int count) = 0;
		/// @brief Checks if data is "open".
		/// @return True if data is "open".
		virtual bool _is_open() = 0;
		/// @brief Gets current position in data.
		/// @return Current position in data.
		virtual long _position() = 0;
		/// @brief Seeks to position in data.
		/// @param[in] offset Seeking offset in bytes.
		/// @param[in] seek_mode Seeking mode.
		virtual void _seek(long offset, SeekMode seek_mode = CURRENT) = 0;

	};
}

/// @brief Alias for simpler code.
typedef hltypes::StreamBase hsbase;

#endif

