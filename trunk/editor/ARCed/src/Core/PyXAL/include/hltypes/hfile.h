/// @file
/// @author  Kresimir Spes
/// @author  Boris Mikic
/// @author  Ivan Vucica
/// @version 1.4
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

#include "hstring.h"

#include "hltypesExport.h"

namespace hltypes
{
	template <class T> class Array;
	/// @brief Provides high level file handling.
	/// @author Kresimir Spes
	/// @author Boris Mikic
	/// @author Ivan Vucica
	/// @note When writing, \\r may be used, but \\r will be removed during read.
	class hltypesExport File
	{
	public:
		/// @brief Defines file access modes.
		/// @note Windows text read/write modes are not used because they do not work properly in multiplatform environments.
		enum AccessMode
		{
			/// @brief Read-only file mode. ("rb")
			READ,
			/// @brief Write-only file mode. ("wb")
			WRITE,
			/// @brief Write and append file mode. ("ab")
			APPEND,
			/// @brief Read and write file mode. ("r+b")
			READ_WRITE,
			/// @brief Read, write and create file mode. ("w+b")
			READ_WRITE_CREATE,
			/// @brief Read and append file mode. ("a+b")
			READ_APPEND
		};
		
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
		/// @brief Seeks to position in file.
		/// @param[in] offset Seeking offset in bytes.
		/// @param[in] seek_mode Seeking mode.
		void seek(long offset, SeekMode seek_mode = CURRENT);
		/// @brief Gets current position in file.
		/// @return Current position in file.
		long position();
		/// @brief Gets size of file in bytes.
		/// @return Size of file in bytes.
		long size();
		/// @brief Checks if file is open.
		/// @return True if file is open.
		bool is_open();
		/// @brief Checks if file has reached the end.
		/// @return True if file has reached the end.
		bool eof();
		/// @brief Closes file.
		void close();
		
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
		
		/// @brief Creates a file.
		/// @param[in] filename Name of the file.
		/// @result True if a new file was created. False if file could not be created or already exists.
		static bool create(chstr filename);
		/// @brief Creates a file or clears the file if it already exists.
		/// @param[in] filename Name of the file.
		/// @result True if a new file was created or cleared. False if file could not be created.
		static bool create_new(chstr filename);
		/// @brief Removes a file.
		/// @param[in] filename Name of the file.
		/// @result True if file exists and was removed.
		static bool remove(chstr filename);
		/// @brief Checks if a file exists.
		/// @param[in] filename Name of the file.
		/// @result True if file exists.
		static bool exists(chstr filename);
		/// @brief Clears a file recursively.
		/// @param[in] filename Name of the file.
		/// @result True if file was cleared. False if file does not exist or is already empty.
		static bool clear(chstr filename);
		/// @brief Renames a file.
		/// @param[in] old_filename Old name of the file.
		/// @param[in] new_filename New name of the file.
		/// @result True if file was renamed. False if old file does not exist or file with the new name already exists.
		/// @note If path to new file does not exist, it will be created.
		static bool rename(chstr old_filename, chstr new_filename);
		/// @brief Moves a file to another path.
		/// @param[in] filename Name of the file.
		/// @param[in] path Path where the file should be moved.
		/// @result True if file was moved. False if file does not exist or file with the same name already exists in path.
		/// @note If path does not exist, it will be created.
		static bool move(chstr filename, chstr path);
		/// @brief Copies a file recursively.
		/// @param[in] old_filename Old name of the file.
		/// @param[in] new_filename New name of the file.
		/// @result True if file was copied. False if old file does not exist or file with the new name already exists.
		/// @note If path does not exist, it will be created.
		static bool copy(chstr old_filename, chstr new_filename);
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
		
		/// @brief Defines the number of repeated attempts to access a file.
		static int repeats;
		/// @brief Defines the timeout in miliseconds between repeated attempts to access a file.
		static float timeout;

		/// @brief Sets the number of repeated attempts to access a file.
		/// @param[in] value New value.
		static void setRepeats(int value) { repeats = value; }
		/// @brief Sets the timeout in miliseconds between repeated attempts to access a file.
		/// @param[in] value New value.
		static void setTimeout(float value) { timeout = value; }

	protected:
		/// @brief Current filename.
		hstr filename;
		/// @brief OS file handle.
		FILE* cfile;
		/// @brief Byte value offset while reading/writing that serves as simple binary encryption.
		unsigned char encryption_offset;
		
	};
}

/// @brief Alias for simpler code.
typedef hltypes::File hfile;

#endif

