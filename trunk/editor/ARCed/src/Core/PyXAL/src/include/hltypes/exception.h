/// @file
/// @author  Kresimir Spes
/// @author  Boris Mikic
/// @version 1.5
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://www.opensource.org/licenses/bsd-license.php
/// 
/// @section DESCRIPTION
/// 
/// Provides high level exceptions.

#ifndef HLTYPES_EXCEPTION_H
#define HLTYPES_EXCEPTION_H

#include "hstring.h"

#include "hltypesExport.h"

namespace hltypes
{
	/// @brief Provides functionality of a basic exception.
	class hltypesExport exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] message Exception message.
		/// @param[in] source_file Name of the source file.
		/// @param[in] line Number of the line.
		exception(chstr message, const char* source_file, int line);
		/// @brief Destructor.
		virtual ~exception();
		/// @brief Gets the exception message.
		/// @return The exception message.
		virtual hstr message() { return this->msg; }
		/// @brief Same as message.
		/// @see message
		virtual hstr getErrorText() { return message(); }
		
	protected:
		/// @brief Exception message.
		hstr msg;
		
	};
	/// @brief Alias for simpler code.
	#define hl_exception(msg) hltypes::exception(msg, __FILE__, __LINE__)
	
	/// @brief Defines a file-not-found exception.
	class hltypesExport _file_not_found : public exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] filename Name of the file.
		/// @param[in] source_file Name of the source file.
		/// @param[in] line Number of the line.
		_file_not_found(chstr filename, const char* source_file, int line);
		~_file_not_found();
		
	};
	/// @brief Alias for simpler code.
	#define file_not_found(filename) hltypes::_file_not_found(filename, __FILE__, __LINE__)
	
	/// @brief Defines a file-not-open exception.
	class hltypesExport _file_not_open : public exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] filename Name of the file.
		/// @param[in] source_file Name of the source file.
		/// @param[in] line Number of the line.
		_file_not_open(chstr filename, const char* source_file, int line);
		~_file_not_open();
		
	};
	/// @brief Alias for simpler code.
	#define file_not_open(filename) hltypes::_file_not_open(filename, __FILE__, __LINE__)
	
	/// @brief Defines a file-long-error exception.
	class hltypesExport _file_long_error : public exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] filename Name of the file.
		/// @param[in] source_file Name of the source file.
		/// @param[in] line Number of the line.
		_file_long_error(chstr filename, const char* source_file, int line);
		~_file_long_error();
		
	};
	/// @brief Alias for simpler code.
	#define file_long_error(filename) hltypes::_file_long_error(filename, __FILE__, __LINE__)
	
	/// @brief Defines a resource-not-writeable exception.
	class hltypesExport _resource_not_writeable : public exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] filename Name of the resource file.
		/// @param[in] source_file Name of the source file.
		/// @param[in] line Number of the line.
		_resource_not_writeable(chstr filename, const char* source_file, int line);
		~_resource_not_writeable();
		
	};
	/// @brief Alias for simpler code.
	#define resource_not_writeable(filename) hltypes::_resource_not_writeable(filename, __FILE__, __LINE__)

	/// @brief Defines a resource-not-seekable exception.
	class hltypesExport _resource_not_seekable : public exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] filename Name of the resource file.
		/// @param[in] source_file Name of the source file.
		/// @param[in] line Number of the line.
		_resource_not_seekable(chstr filename, const char* source_file, int line);
		~_resource_not_seekable();
		
	};
	/// @brief Alias for simpler code.
	#define resource_not_seekable(filename) hltypes::_resource_not_seekable(filename, __FILE__, __LINE__)

	/// @brief Defines an index-error exception.
	class hltypesExport _index_error : public exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] index Index of the entry.
		/// @param[in] source_file Name of the source file.
		/// @param[in] line Number of the line.
		_index_error(int index, const char* source_file, int line);
		~_index_error();
		
	};
	/// @brief Alias for simpler code.
	#define index_error(index) hltypes::_index_error(index, __FILE__, __LINE__)
	
	/// @brief Defines a random-error exception.
	class hltypesExport _size_error : public exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] function_name Name of the function.
		/// @param[in] source_file Name of the source file.
		/// @param[in] line Number of the line.
		_size_error(chstr function_name, const char* source_file, int line);
		~_size_error();
		
	};
	/// @brief Alias for simpler code.
	#define size_error(function_name) hltypes::_size_error(function_name, __FILE__, __LINE__)
	
	/// @brief Defines an element-error exception.
	class hltypesExport _element_not_found_error : public exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] source_file Name of the source file.
		/// @param[in] line Number of the line.
		_element_not_found_error(const char* source_file, int line);
		~_element_not_found_error();
		
	};
	/// @brief Alias for simpler code.
	#define element_not_found_error() hltypes::_element_not_found_error(__FILE__, __LINE__)
	
	/// @brief Defines a range-error exception.
	class hltypesExport _range_error : public exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] start Start of the range.
		/// @param[in] count Number of elements in the range.
		/// @param[in] source_file Name of the source file.
		/// @param[in] line Number of the line.
		_range_error(int start, int count, const char* source_file, int line);
		~_range_error();
		
	};
	/// @brief Alias for simpler code.
	#define range_error(start, count) hltypes::_range_error(start, count, __FILE__, __LINE__)
	
	/// @brief Defines a key-error exception.
	class hltypesExport _key_error : public exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] key Name of the key.
		/// @param[in] container Name of the container.
		/// @param[in] source_file Name of the source file.
		/// @param[in] line Number of the line.
		_key_error(chstr key, chstr container, const char* source_file, int line);
		~_key_error();
		
	};
	/// @brief Alias for simpler code.
	#define key_error(key, container) hltypes::_key_error(key, container, __FILE__, __LINE__)
	
	/// @brief Defines a resource-error exception.
	class hltypesExport _resource_error : public exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] type Type of the resource.
		/// @param[in] name Name of the resource.
		/// @param[in] container Name of the container.
		/// @param[in] source_file Name of the source file.
		/// @param[in] line Number of the line.
		_resource_error(chstr type, chstr name, chstr container, const char* source_file, int line);
		~_resource_error();
		
	};
	/// @brief Alias for simpler code.
	#define resource_error(type, name, container) hltypes::_resource_error(type, name, container, __FILE__, __LINE__)
	
}

#endif
